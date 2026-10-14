"""Apply the declared v2 signatory correction. No inference calls or new generations."""
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent
base = json.loads((ROOT / 'reviews/assistant-v51/grades.json').read_text())
rows = copy.deepcopy(base['rows'])
changes = json.loads((OUT / 'corrections.json').read_text())
by_path = {c['path']: c for c in changes}
assert len(by_path) == len(changes) == 19
historical_boundary = ('For the legacy v2 vendor brief only, do not score the identity of the contract '
                      'signatory or an implied assignment of that role: the source did not specify it '
                      'and adjudication was inconsistent. Continue scoring other unsupported facts, '
                      'deadlines, approvals and commitments. C05 still requires Priya procurement '
                      'ownership and CFO approval before signing. This exception does not validate '
                      'a guessed signatory and does not apply to v3.')
changed_verdicts = 0
for old, row in zip(base['rows'], rows):
    text = (ROOT / row['path']).read_text()
    assert hashlib.sha256(text.encode()).hexdigest() == row['outputSha256']
    if row['task'] != 'vendor-decision-memo':
        assert row == old
        continue
    g = next(g for g in row['grades'] if g['id'] == 'grounding')
    g['criterion'] += ' ' + historical_boundary
    if row['path'] in by_path:
        c = by_path[row['path']]
        previous = next(g for g in old['grades'] if g['id'] == 'grounding')
        assert previous == c['previous'] and c['outputSha256'] == row['outputSha256']
        assert c['previous']['evidence']['quote'] in text
        changed_verdicts += g['verdict'] != c['verdict']
        g['verdict'], g['reason'] = c['verdict'], c['reason']
        # Keep the exact historical quotation, including on a retired finding.
    row['gradeOrigin'] += '; assistant-v52 legacy signatory boundary correction'
    row['counts'] = {v: sum(g['verdict'] == v for g in row['grades']) for v in ('pass', 'fail', 'review')}
    row['contentReady'] = (not row['counts']['fail'] and not row['counts']['review']
                           and row['words'] <= row['maxWords'] and not row['placeholderFindings'])
    row['readyWithoutEdits'] = bool(row['contentReady'] and row['styleGatePass'] and not row['editorialFindings'])
assert changed_verdicts == 17
assert sum(r['task'] == 'vendor-decision-memo' for r in rows) == 66
method = copy.deepcopy(base['method'])
method['revision'] = 'October 13: retire the under-specified v2 vendor signatory inference uniformly across all 33 models. Seventeen verdicts change, two mixed reasons retain their verdicts. No draft, price, other content check or style finding changes. New v3 authority facts require a separate future cohort.'
method['legacyVendorBoundary'] = historical_boundary
(OUT / 'grades.json').write_text(json.dumps({'method': method, 'rows': rows, 'ungraded': base['ungraded']}, indent=2) + '\n')
summary = []
for model in dict.fromkeys(r['model'] for r in rows):
    for cond in ('default', 'house'):
        rs = [r for r in rows if r['model'] == model and r['condition'] == cond]
        c = {v: sum(r['counts'][v] for r in rs) for v in ('pass', 'fail', 'review')}
        summary.append({'model': model, 'condition': cond, 'completed': len(rs), 'expected': 8,
                        **c, 'total': sum(c.values()), 'contentReady': sum(r['contentReady'] for r in rs),
                        'readyWithoutEdits': sum(r['readyWithoutEdits'] for r in rs),
                        'generationCostUsd': sum(r['originalGenerationCostUsd'] for r in rs),
                        'benchEligible': True})
(OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
lines = ['# Corrected legacy comparison: explicit authority required for future tests', '',
         'October 13, 2026. Provisional, unblinded assistant grades. 33 models, 528 primary drafts; 56 repeat drafts remain separate.', '',
         '## What was wrong', '',
         'The v2 source says Priya owns procurement and CFO approval is needed before signing. It never names the signatory. Some drafts lost credit for proceeding to signing, while similar Astra and Sol wording passed. This was an inconsistent grading boundary, not evidence that one model understood authority better.', '',
         '## Historical correction', '', historical_boundary, '',
         'The six existing vendor checks remain, including grounding against all other source facts. Seventeen grounding verdicts change to pass because the sole recorded finding was retired. This means no remaining scored grounding defect, not confirmation of signing authority. Two mixed findings retain their original verdict after removing the signatory allegation. The correction applies to all 66 primary vendor memos. Astra and Luna full repeats and the Sol/Astra comparison have no signatory deductions, so their numerical results do not change.', '',
         'The raw outputs, frozen v2 inputs and earlier reviews remain untouched. This is a revised scoring edition of the same drafts, not a new generation or a pass on the new authority task. No other content judgment, style finding or cost changed.', '',
         '| Model | Condition | Grounding before | Grounding now | Checks now | Content ready | Ready without edits |',
         '|---|---|---|---|---:|---:|---:|']
for c in changes:
    s = next(s for s in summary if s['model'] == c['model'] and s['condition'] == c['condition'])
    lines.append(f"| {c['model']} | {c['condition']} | {c['previous']['verdict']} | {c['verdict']} | {s['pass']}/54 | {s['contentReady']}/8 | {s['readyWithoutEdits']}/8 |")
lines += ['', '## Replacement for future runs', '',
          '`data/tasks-v3.json` replaces only the vendor ownership fact and C05. Priya coordinates procurement and cannot sign; Alex, the commercial director, is the sole signatory; CFO approval precedes Alex signing and does not delegate authority. C05 requires all three roles and the order explicitly. Wrong or omitted roles fail. Saying only "proceed with signing" cannot substitute for identifying Alex. The eight-brief total remains 54 checks.', '',
          'The collector targets unused pilot-v33, protocol 0.33.0, with v3 tasks. No model has run v3 yet. Never compare a new v3 panel directly with these v2 scores or import a v2 vendor answer as a v3 success. The unrelated proposed readout revision remains inactive. The authored [boundary examples](../../data/vendor-authority-controls-v3.json) illustrate pass/fail decisions; they are not independent human calibration.', '',
          '## Evidence and reproduction', '',
          '- [Exact before/after decisions and retained quotes](corrections.json)',
          '- [Cumulative grades](grades.json), [summary](summary.json), [ranking and prices](RANKING.md)',
          '- [Muse Wonder versus Astra and other new models](MUSE-COMPARISON.md)',
          '- [Argon original review](../assistant-v50/REPORT.md), [Nemotron and Muse original review](../assistant-v51/REPORT.md)', '',
          'Run `python3 reviews/assistant-v52/build.py` and `python3 scripts/ranking.py reviews/assistant-v52 runs/pilot-v32`. These read saved files and make no API calls.', '']
(OUT / 'REPORT.md').write_text('\n'.join(lines))
print(json.dumps([s for s in summary if s['model'] in ['Astra', 'Muse Wonder 1.0', 'Gemini 4 Argon', 'Mistral Large 4']], indent=2))
