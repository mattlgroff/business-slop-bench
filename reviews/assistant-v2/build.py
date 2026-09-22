"""Apply explicit assistant decisions to corrected and newly collected drafts.
Carry forward a prior grade only when the exact output and its task are unchanged.
"""
import json,hashlib,copy,re
from pathlib import Path
root=Path(__file__).resolve().parents[2]; out=Path(__file__).parent
old=json.loads((root/'reviews/assistant-v1/grades.json').read_text())
tasks=json.loads((root/'data/tasks-v2.json').read_text())
old_tasks={t['id']:t for t in json.loads((root/'data/tasks.json').read_text())}
prior={(r['model'],r['task'],r['condition']):r for r in old['rows']}
models=[('Qwen Flash','alibaba--qwen3.8-flash'),('Kimi K3','moonshotai--kimi-k3'),('Opus 5','anthropic--claude-opus-5')]
updates={
('Qwen Flash','ai-strategy-slides','default'):[('grounding','fail','Low risk; no external dependencies','Invents absence of external dependencies, legal clearance, and a specific Q3 quarter not given in the brief.')],
('Qwen Flash','ai-strategy-slides','house'):[('C01','fail','Slide 4: Evaluation & Next Steps','No specific recommendation between the two pilots.'),('grounding','fail','Risk of budget overrun is high.','Invents budget-overrun risk and states that no legal barriers exist for Option A without evidence.')],
('Kimi K3','ai-strategy-slides','default'):[],
('Kimi K3','ai-strategy-slides','house'):[('grounding','fail','no path to use','Overstates pending authorization as no path to use; also rules out use for a whole quarter without an approval date.')],
('Opus 5','pilot-client-email','default'):[('grounding','fail','No variable costs, no overrun exposure.','A fixed pilot fee does not establish no variable costs or overrun exposure for the client. Also invents prior discussions.')],
('Opus 5','pilot-client-email','house'):[('grounding','review',"I'd rather hold the team's availability than release it and rebook later.",'Creates staffing-pressure implications absent from the source. Wording may describe a proposed scheduling preference rather than a definite existing hold.')],
('Opus 5','launch-delay-email','default'):[('grounding','fail','not a gap in execution','Rules out execution problems without supplied evidence; claims review thoroughness and team control.')],
}
editorial={
('Opus 5','pilot-client-email','default'):[('16','This pilot exists to produce that evidence','The lengthy rationale repeats the evidence gap and scope boundary; the email exceeds the explicit word limit.')],
('Opus 5','pilot-client-email','house'):[('16','That measurement gives you a defensible number either way','Long hypothetical outcomes delay the approval request; the email exceeds the explicit word limit.')],
('Opus 5','launch-delay-email','default'):[('2','An update on the launch position and one decision I need from you.','Throat clearing delays the material date change; the email exceeds the word limit.')],
}
def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def anchor(text,quote):
 assert quote in text,quote
 i=text.index(quote);return {'quote':quote,'offset':i,'line':text[:i].count('\n')+1}
rows=[];missing=[]
for model,slug in models:
 for task in tasks:
  for cond in ['default','house']:
   key=(model,task['id'],cond);stem=f'{slug}--{task["id"]}--{cond}'
   path=root/'runs/pilot-v10'/f'{stem}.json'
   if not path.exists():missing.append({'model':model,'task':task['id'],'condition':cond,'status':'not generated'});continue
   record=json.loads(path.read_text())
   if record['status']!='ok':missing.append({'model':model,'task':task['id'],'condition':cond,'status':'generation failed','error':record['error']});continue
   text=(path.with_suffix('.md')).read_text();assert record['text']==text
   if key not in updates:
    assert key in prior and prior[key]['outputSha256']==digest(text) and old_tasks[task['id']]==task
    r=copy.deepcopy(prior[key]);r['gradeOrigin']='assistant-v1, unchanged input task and exact output'
    r['path']=str(path.with_suffix('.md').relative_to(root));rows.append(r);continue
   overs={x[0]:x for x in updates[key]};assert set(overs)<=set(c['id'] for c in task['checks'])
   grades=[]
   for c in task['checks']:
    o=overs.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
   findings=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in editorial.get(key,[])]
   words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']}
   ready=counts['fail']==0 and counts['review']==0 and words<=task['maxWords']
   rows.append({'model':model,'task':task['id'],'condition':cond,'path':str(path.with_suffix('.md').relative_to(root)),'outputSha256':digest(text),'writerInputHash':record['inputHash'],'gradeOrigin':'assistant-v2, reviewed against corrected task set','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':[],'editorialFindings':findings,'contentReady':ready,'styleGatePass':not ems,'readyWithoutEdits':ready and not ems and not findings,'originalGenerationCostUsd':record['billing']['totalCost']})
assert len([r for r in rows if r['model']!='Opus 5'])==32
method=copy.deepcopy(old['method']);method['tasksSha256']=hashlib.sha256((root/'data/tasks-v2.json').read_bytes()).hexdigest();method['exceptions']=[x for x in method['exceptions'] if 'quarter' not in x];method['revision']='Only the capacity statement in the AI strategy brief changed to next quarter. Four affected Qwen/Kimi drafts regenerated once each. Prior grades carried only across byte-identical outputs and identical tasks. Opus remains partial due to Gateway 429 failures.'
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':missing},indent=2)+'\n')
summary=[]
for model,_ in models:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];cs={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**cs,'total':sum(cs.values()),'contentReady':sum(r['contentReady'] for r in rs),'styleGatePass':sum(r['styleGatePass'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'wordLimitFailures':sum(r['words']>r['maxWords'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant grades: corrected task set','',method['status']+'. Model identities were visible. No Jev judgments were used.','',method['revision'],'','## Complete eight-brief comparison','','| Model | Condition | Content checks passed | Failed | Unresolved | Ready without edits |','|---|---|---:|---:|---:|---:|']
for s in summary:
 if s['completed']==8:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["readyWithoutEdits"]}/8 |')
lines+=['','Unresolved checks earn no credit. Ready without edits requires all task-content checks to pass, the word limit, no placeholders, the style gate, and no supported editorial findings. Default style results describe house-style fit without supplying those instructions. These overlapping checks are not independent observations.','', '## Opus: incomplete, not a comparable model total','', '| Condition | Generated and graded | Content checks passed | Failed | Unresolved | Word-limit failures | Ready without edits |','|---|---:|---:|---:|---:|---:|---:|']
for s in summary:
 if s['model']=='Opus 5':lines.append(f'| {s["condition"]} | {s["completed"]}/8 | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["wordLimitFailures"]} | {s["readyWithoutEdits"]}/{s["completed"]} |')
lines+=['','Missing outputs are ungraded, not failures or zero-quality scores. The 429 message does not establish whether the cause is provider capacity, model access, or account rate restriction.','', '## Newly reviewed evidence','']
for r in rows:
 if not r['gradeOrigin'].startswith('assistant-v2'):continue
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}), {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+ [('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 for label,reason,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {reason}')
 if not fs:lines.append('No content or editorial defect found in this review; any em dash violations remain separate.')
 lines.append('')
lines+=['Unchanged draft decisions and explanations are retained in [grades.json](grades.json), with their original grade provenance. [Previous full evidence report](../assistant-v1/REPORT.md). The correction and new generation are not a causal experiment: output differences may reflect sampling variation.','']
(out/'REPORT.md').write_text('\n'.join(lines))
print(json.dumps(summary,indent=2))
