"""Append five explicitly reviewed partial-sample drafts; no judge API calls."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v3/grades.json').read_text());rows=copy.deepcopy(base['rows'])
tasks={t['id']:t for t in json.loads((root/'data/tasks-v2.json').read_text())}
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
# Enumerated reviewed outputs only. Missing requests are never converted to grades.
decisions=[
 ('Fable 5.1','anthropic--claude-fable-5.1','pilot-client-email','default', [('grounding','fail','Thank you for the productive discussions so far.','Invents productive prior discussions not supplied in the source.')], []),
 ('Fable 5.1','anthropic--claude-fable-5.1','pilot-client-email','house', [], []),
 ('DeepSeek Flash','deepseek--deepseek-v4.1-flash','pilot-client-email','default', [('grounding','fail','Following our discussions','Invents prior discussions not supplied in the source.')], [('29','I want to be transparent:','Candor preamble adds no information to the necessary baseline caveat that follows.')]),
 ('DeepSeek Flash','deepseek--deepseek-v4.1-flash','pilot-client-email','house', [('grounding','review','I will secure it before work begins.','May imply a guarantee of granted security approval, or may describe a plan to satisfy the prerequisite. The source authorizes the prerequisite, not a guaranteed approval outcome.')], [('16','Approving the scope and fee, subject to security clearance, lets us set that date and begin.','Repeats the approval-to-start logic immediately before another conditional approval request and scheduling promise.')]),
 ('DeepSeek Flash','deepseek--deepseek-v4.1-flash','launch-delay-email','default', [('grounding','fail','The team has responded well.','Invents an objective team-performance assessment absent from the source.')], [('2','I want to give you a clear update on our launch position.','Throat clearing before the actual date update.')]),
]
manifest=out/'reviewed-output-hashes.json';expected=json.loads(manifest.read_text()) if manifest.exists() else {};hashes={}
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for model,slug,taskid,cond,overrides,editorial in decisions:
 stem=f'{slug}--{taskid}--{cond}';p=root/'runs/pilot-v11'/f'{stem}.json';record=json.loads(p.read_text());text=p.with_suffix('.md').read_text();assert record['status']=='ok' and text==record['text']
 h=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=h
 if expected:assert expected[stem]==h,'Output changed; new review required'
 task=tasks[taskid];os={x[0]:x for x in overrides};grades=[]
 for c in task['checks']:
  o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
 es=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in editorial]
 counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
 ready=not counts['fail'] and not counts['review'] and words<=task['maxWords']
 rows.append({'model':model,'task':taskid,'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':record['inputHash'],'gradeOrigin':'assistant-v4, reviewed saved partial sample','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':[],'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems,'readyWithoutEdits':bool(ready and not ems and not es),'originalGenerationCostUsd':record['billing']['totalCost']})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
method=copy.deepcopy(base['method']);method['revision']='Adds two Fable 5.1 and three DeepSeek Flash drafts. Other outputs remain missing due to API failures or not yet attempted. Fable uses a declared non-ZDR route because the model rejects ZDR; all briefs are synthetic.'
method['exceptions']+=['Fable default: the claim of productive discussions is the confirmed grounding failure. The no-open-ended-costs phrase occurs in the fixed-fee bullet and is not separately penalized as a broad guarantee. This narrows the initial editorial concern.','DeepSeek house: the explicit security prerequisite passes C04. The separate statement that the author will secure approval remains unresolved under grounding.']
ungraded=[]
slugs={'Qwen Flash':'alibaba--qwen3.8-flash','Kimi K3':'moonshotai--kimi-k3','Astra':'openai--gpt-6-astra','Opus 5':'anthropic--claude-opus-5','Fable 5.1':'anthropic--claude-fable-5.1','DeepSeek Flash':'deepseek--deepseek-v4.1-flash'}
for model,slug in slugs.items():
 for taskid in tasks:
  for cond in ['default','house']:
   if any(r['model']==model and r['task']==taskid and r['condition']==cond for r in rows):continue
   paths=[root/'runs'/run/f'{slug}--{taskid}--{cond}.json' for run in ['pilot-v11','pilot-v10']]
   records=[json.loads(p.read_text()) for p in paths if p.exists()]
   status='not generated' if not records else 'generation failed' if records[0]['status']=='error' else 'awaiting review'
   ungraded.append({'model':model,'task':taskid,'condition':cond,'status':status})
assert len(ungraded)==40
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':ungraded},indent=2)+'\n')
summary=[]
for model in ['Qwen Flash','Kimi K3','Astra','Opus 5','Fable 5.1','DeepSeek Flash']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant comparison: first-email coverage across six models','',method['status']+'. Model identities were visible; no Jev judgments were used.','', '## Same pilot-client email, both conditions','', '| Model | Default content checks | House content checks | Ready default / house |','|---|---:|---:|---|']
for model in ['Qwen Flash','Kimi K3','Astra','Opus 5','Fable 5.1','DeepSeek Flash']:
 rs={r['condition']:r for r in rows if r['model']==model and r['task']=='pilot-client-email'}
 assert set(rs)=={'default','house'}
 d,h=rs['default'],rs['house']
 lines.append(f'| {model} | {d["counts"]["pass"]}/7 | {h["counts"]["pass"]}/7 | {"Yes" if d["readyWithoutEdits"] else "No"} / {"Yes" if h["readyWithoutEdits"] else "No"} |')
lines+=['','Ready requires all critical checks, word limit, no placeholders, clean style gate, and no supported editorial edits. A content pass alone does not mean ready. Unresolved checks earn no credit. Opus house and DeepSeek house each have one unresolved grounding check, not a confirmed grounding failure.','', 'This single brief is a matched comparison, not a general model ranking. Fable house is usable on this review. Fable default invents prior discussions. DeepSeek repeats that mistake in its default draft; its house draft has an ambiguous approval promise and redundant wording.','', '## New evidence','']
for r in rows[-5:]:
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not fs:lines.append('No supported content or editorial finding in this review.')
 lines.append('')
lines+=['## Coverage and operational limits','','Fable 5.1 has two completed drafts. DeepSeek Flash has three. Their incomplete eight-brief samples are not compared as full model totals. A cooled Fable retry completed the house email, then the next default email returned 429. DeepSeek launch-house timed out twice at 90 seconds. No missing output receives a zero quality score.','', 'Fable 5 and 5.1 lack ZDR support in the catalog. The runner declares their non-ZDR exception for these synthetic tasks. This changes data-retention routing, not prompts, reasoning effort, output limits or grading criteria. The rejected initial ZDR request and failed attempts remain in the budget ledger.','', '[Complete eight-brief samples and earlier evidence](../assistant-v3/REPORT.md). [All current decisions](grades.json). Run `python3 scripts/coverage.py` for current generation coverage without quality inference.','']
(out/'REPORT.md').write_text('\n'.join(lines))
print('Verified',len(rows),'reviewed drafts; added',len(decisions),'partial-sample reviews')
