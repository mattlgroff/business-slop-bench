"""Sensitivity analysis only. Does not rewrite grades, tasks, or live configuration."""
import copy,hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths=['data/tasks-v2.json','reviews/assistant-v16/grades.json','reviews/repeatability-v1/grades.json']
before={p:sha(root/p) for p in paths}
tasks=read(root/'data/tasks-v2.json');proposal=read(root/'data/proposed-tasks-v3.json')
assert len(tasks)==len(proposal)==8
for original,candidate in zip(tasks,proposal):
 if original['id']=='pilot-results-memo':
  assert candidate['brief']==original['brief']+' Quantify the change in mean handling time in minutes or percent, and distinguish that observation from a causal claim.'
  assert {k:v for k,v in original.items() if k!='brief'}=={k:v for k,v in candidate.items() if k!='brief'}
 else:assert original==candidate
assert "const taskFile = 'data/tasks-v2.json'" in (root/'src/cli.ts').read_text(),'Proposal must remain inactive during this audit'
base=read(root/'reviews/assistant-v16/grades.json');cases=read(out/'cases.json')
keys={(c['model'],c['condition'],c['path']) for c in cases};assert len(keys)==len(cases)==6
for c in cases:
 assert sha(root/c['path'])==c['outputSha256']
 text=(root/c['path']).read_text();e=c['evidence'];assert text[e['offset']:e['offset']+len(e['quote'])]==e['quote']
assert keys=={(r['model'],r['condition'],r['path']) for r in base['rows'] if r['task']=='pilot-results-memo'}
summary=[]
for model in ['Muse','Gemini Flash','Luna']:
 for condition in ['default','house']:
  rs=[r for r in base['rows'] if r['model']==model and r['condition']==condition];assert len(rs)==8
  adjusted=copy.deepcopy(rs)
  for r in adjusted:
   if (r['model'],r['condition'],r['path']) not in keys:continue
   assert r['counts']=={'pass':6,'fail':1,'review':0}
   assert [(g['id'],g['verdict']) for g in r['grades'] if g['verdict']!='pass']==[('C01','fail')]
   case=next(c for c in cases if (c['model'],c['condition'],c['path'])==(r['model'],r['condition'],r['path']))
   assert case['outputSha256']==r['outputSha256']
   r['contentReady']=r['words']<=r['maxWords'] and not r['placeholderFindings']
   r['readyWithoutEdits']=r['contentReady'] and r['styleGatePass'] and not r['editorialFindings']
  summary.append({'model':model,'condition':condition,'officialContentReady':sum(r['contentReady'] for r in rs),'hypotheticalContentReady':sum(r['contentReady'] for r in adjusted),'officialReadyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'hypotheticalReadyWithoutEdits':sum(r['readyWithoutEdits'] for r in adjusted)})
after={p:sha(root/p) for p in paths};assert before==after
(out/'integrity.json').write_text(json.dumps({'officialInputsUnchanged':True,'before':before,'after':after},indent=2)+'\n')
(out/'sensitivity.json').write_text(json.dumps(summary,indent=2)+'\n')
task=next(t for t in tasks if t['id']=='pilot-results-memo');criterion=next(c for c in task['checks'] if c['id']=='C01')
lines=['# Readout criterion audit','', 'This is an audit of benchmark design, not a replacement leaderboard. The live brief, rubric, outputs and official grades remain unchanged. No model calls were made.','', '## Prompt and criterion','',f'Writer brief: {task["brief"]}','',f'Critical C01: {criterion["statement"]}','', 'The brief asks for a scaling recommendation, supporting results and a next decision. It does not directly request the derived handling-time reduction. The rubric makes that derivation a mandatory content gate. That can measure analytical completeness, but an omission must not be described as incorrect arithmetic or inability to calculate.','', 'The supplied original rubric describes numbers integrity through arithmetic, units, baselines and forecast-versus-actual distinctions. It does not mandate this particular derived figure. C01 is a task-specific benchmark design choice.','', '## Effect on current uncapped comparisons','', 'All six primary readouts from Muse, Gemini Flash and Luna give the correct endpoints and pass their other content checks. Each has C01 as its only content blocker. The following sensitivity view removes only that reviewed omission from the gate; it leaves every other finding and style decision unchanged. It is not an adopted score.','', '| Model | Condition | Official content ready | Hypothetical content ready | Official ready without edits | Hypothetical ready without edits |','|---|---|---:|---:|---:|---:|']
for s in summary:lines.append(f'| {s["model"]} | {s["condition"]} | {s["officialContentReady"]}/8 | {s["hypotheticalContentReady"]}/8 | {s["officialReadyWithoutEdits"]}/8 | {s["hypotheticalReadyWithoutEdits"]}/8 |')
lines+=['','The repeatability study shows this gate is sample-sensitive: Muse explicitly gave the reduction on one of three attempts and Luna on two of three. All those readouts retained the correct no-scale decision under the other frozen checks. That is a variation in completeness, not evidence of variable subtraction ability.','', '## Prospective repair','', 'A proposed task-v3 file adds one sentence to the readout brief:','', '> Quantify the change in mean handling time in minutes or percent, and distinguish that observation from a causal claim.','', 'The proposed file preserves every fact, check, severity, word limit and other brief. It is inactive. Validate it on fresh samples before adopting it, keep its results separate, and retain historical grades. If the intended construct is spontaneous inclusion of useful calculations, retain the natural brief and report this omission as its own completeness measure instead of presenting it as wrong arithmetic.','', 'Readiness also includes editorial preferences. A draft blocked only on this omission can still be substantively useful; a content pass does not certify polished writing or production reliability.','', '## Audited evidence','']
for c in cases:
 e=c['evidence'];lines.append(f'- **{c["model"]}, {c["condition"]}:** [{e["quote"]}](../../{c["path"]}:{e["line"]}). Correct endpoints; no explicit derived reduction.')
lines+=['','[Inactive proposed task set](../../data/proposed-tasks-v3.json), [machine-readable sensitivity](sensitivity.json), [unchanged official-file hashes](integrity.json), [repeatability study](../repeatability-v1/REPORT.md).','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps(summary,indent=2))
