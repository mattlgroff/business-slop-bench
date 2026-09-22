"""Apply four explicit exception corrections; never infer semantic verdicts."""
import copy
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
out = Path(__file__).parent
read = lambda path: json.loads(path.read_text())
base = read(root / 'reviews/assistant-v33/grades.json')
result = copy.deepcopy(base)
corrections = read(out / 'corrections.json')
assert len(corrections) == 4
changes = []
for correction in corrections:
    matches = [r for r in result['rows'] if r['path'] == correction['path']]
    assert len(matches) == 1
    row = matches[0]
    text = (root / row['path']).read_text()
    assert hashlib.sha256(text.encode()).hexdigest() == row['outputSha256'] == correction['outputSha256']
    assert row['negativeParallelismFindings'] == correction['previousFindings']
    for finding in row['negativeParallelismFindings']:
        assert text[finding['offset']:finding['offset'] + len(finding['quote'])] == finding['quote']
    previous_gate = row['styleGatePass']
    row['negativeParallelismFindings'] = []
    row['styleGatePass'] = not row['emDashes']
    row['readyWithoutEdits'] = bool(row['contentReady'] and row['styleGatePass'] and not row['editorialFindings'])
    changes.append({'path': row['path'], 'previousStyleGatePass': previous_gate, 'styleGatePass': row['styleGatePass']})
# Only the named style fields may change. Existing numeric/readiness results stay intact.
for previous, current in zip(base['rows'], result['rows']):
    mutable = {'negativeParallelismFindings', 'styleGatePass', 'readyWithoutEdits'}
    assert {k:v for k,v in previous.items() if k not in mutable} == {k:v for k,v in current.items() if k not in mutable}
    assert previous['readyWithoutEdits'] == current['readyWithoutEdits']
result['method']['revision'] = 'Corrects four negative-parallelism findings under the frozen lens factual and decision-boundary exceptions. All content grades, em dashes, other editorial findings and readiness counts are unchanged. This remains an unblinded assistant correction, not independent validation.'
(out / 'grades.json').write_text(json.dumps(result, indent=2) + '\n')
summary = read(root / 'reviews/assistant-v33/summary.json')
(out / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
(out / 'changes.json').write_text(json.dumps(changes, indent=2) + '\n')
lines = ['# Negative-parallelism exception correction', '', result['method']['status'] + '.', '',
         'Four confirmed style findings were overbroad: the previous rationale treated a removable negative clause as sufficient evidence of empty rhetoric. The frozen lens explicitly permits factual corrections, scope boundaries and mutually exclusive conditions. The following corrections apply that exception; they do not relax the rubric.', '',
         'All content grades, em dash counts, other editorial findings, eligibility and ready-without-edits totals remain unchanged. Three corrected drafts still contain em dashes; the Opus 5 house handoff now passes the style gate but remains blocked on content. [Unchanged comparison table](../assistant-v33/REPORT.md) and [corrected cumulative grades](grades.json).', '']
for c in corrections:
    lines += ['## ' + c['model'] + ' / ' + c['task'] + ' / ' + c['condition'], '', c['reason'], '']
    for f in c['previousFindings']:
        lines += [f'Previous finding at [line {f["line"]}](../../{c["path"]}:{f["line"]}):', '', '> ' + f['quote'], '']
lines += ['No model calls were made. Exact source hashes and quote offsets were verified. Historical reports retain the original findings for traceability. Scanner matches still require contextual judgment, and this correction does not validate the rest of the rubric independently.', '']
(out / 'REPORT.md').write_text('\n'.join(lines))
print(json.dumps({'correctedFindings': len(corrections), 'styleGateChanges': sum(c['previousStyleGatePass'] != c['styleGatePass'] for c in changes), 'readinessChanges': 0}))
