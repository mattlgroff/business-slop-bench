"""Apply the recorded sample-adequacy grounding correction only."""
import copy,json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
base=read(root/'reviews/assistant-v34/grades.json');result=copy.deepcopy(base)
c=read(out/'correction.json');row=next(r for r in result['rows'] if r['path']==c['path'])
text=(root/row['path']).read_text();assert hashlib.sha256(text.encode()).hexdigest()==c['outputSha256']==row['outputSha256']
e=c['evidence'];assert text[e['offset']:e['offset']+len(e['quote'])]==e['quote']
g=next(g for g in row['grades'] if g['id']==c['check']);assert g['verdict']==c['previousVerdict']
g.update(verdict=c['verdict'],reason=c['reason'],evidence=e)
row['counts']={v:sum(g['verdict']==v for g in row['grades']) for v in ['pass','fail','review']}
row['contentReady']=False;row['readyWithoutEdits']=False
for old,new in zip(base['rows'],result['rows']):
 if old['path']!=c['path']:assert old==new
 else:
  assert {k:v for k,v in old.items() if k not in ['grades','counts','contentReady','readyWithoutEdits']}=={k:v for k,v in new.items() if k not in ['grades','counts','contentReady','readyWithoutEdits']}
  assert [g for g in old['grades'] if g['id']!='grounding']==[g for g in new['grades'] if g['id']!='grounding']
result['method']['revision']='Corrects one unsupported sample-adequacy claim in Fable 5 default readout. All other rows and the v34 factual-contrast corrections are preserved. Unblinded assistant review, not independent validation.'
summary=read(root/'reviews/assistant-v34/summary.json')
for s in summary:
 rs=[r for r in result['rows'] if r['model']==s['model'] and r['condition']==s['condition']]
 for v in ['pass','fail','review']:s[v]=sum(r['counts'][v] for r in rs)
 for k in ['contentReady','readyWithoutEdits']:s[k]=sum(r[k] for r in rs)
(out/'grades.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
s=next(s for s in summary if s['model']=='Fable 5' and s['condition']=='default')
lines=['# Readout grounding correction','',result['method']['status']+'.','',
'Fable 5 labels the pilot sample "Adequate for a pilot." The source supplies ticket counts but no sample-adequacy criterion or evidence. This is an unsupported factual assessment under the existing grounding rule.', '',
f'[Exact passage, line {e["line"]}](../../{c["path"]}:{e["line"]}). The output hash and quote location were verified.', '',
f'Fable 5 default changes from 50/54 to {s["pass"]}/54 content checks and from 4/8 to {s["contentReady"]}/8 content-ready drafts. Ready without edits remains 0/8. Fable remains non-ZDR and disqualified regardless of these writing scores. No other model score changes.', '',
'## Follow-up-study language reviewed','',
'Claims that a matched follow-up will isolate the true effect deserve closer review, but an objective for a proposed study is different from a promise of conclusive results. No blanket keyword rule was applied. The MiniMax default and Fable 5 house readouts remain candidates for reviewer calibration; their grades are unchanged in this correction.', '',
'Opus 5 house refers to isolating the handling-time difference rather than expressly promising the true causal effect. Fable 5.1 default describes what the proposed study should test. Conditional rules that permit scaling only if results meet criteria do not guarantee that those results will occur. These cases were left unchanged.', '',
'For methodological background, [Austin (2011)](https://pubmed.ncbi.nlm.nih.gov/21818162/) discusses matching methods for reducing confounding in observational studies. This benchmark does not specify a propensity-score design, and that reference is not an additional requirement imposed on writers. The correction above follows solely from the supplied source pack.', '',
'[Corrected cumulative grades](grades.json), [summary](summary.json), and [explicit correction](correction.json). All 303 other rows are unchanged; earlier style-exception corrections remain applied. No paid request was made for this audit.', '']
lines += ['## Current reviewed comparison', '', '| Model | Condition | Checks passed | Content ready | Ready without edits |', '|---|---|---:|---:|---:|']
for item in summary:
 label=item['model']+(' (non-ZDR, disqualified)' if not item['benchEligible'] else '')
 lines.append(f"| {label} | {item['condition']} | {item['pass']}/{item['total']} | {item['contentReady']}/{item['completed']} | {item['readyWithoutEdits']}/{item['completed']} |")
lines += ['', 'This table covers the 304 reviewed drafts in assistant-v34 plus the correction above. Concurrent collections are not included until reviewed.', '']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps(s,indent=2))
