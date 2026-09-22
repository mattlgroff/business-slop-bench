"""Append the successful Opus 5 retry and separate Opus 4.6 paired sample."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v6/grades.json').read_text());rows=copy.deepcopy(base['rows'])
tasks={t['id']:t for t in json.loads((root/'data/tasks-v2.json').read_text())}
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
cases=[
 ('Opus 5','anthropic/claude-opus-5','pilot-v14','launch-delay-email','house',[('grounding','fail',"Nia's team has kept the review on a clear schedule and has flagged each step early",'Invents a record of team performance and early warnings not provided in the source.')],[]),
 ('Opus 4.6','anthropic/claude-opus-4.6','pilot-v15','pilot-client-email','default',[('C04','fail','We initiate security clearance for client data access.','Initiating clearance does not explicitly require granted approval before data access.'),('grounding','fail','every week of delay is unquantified cost','Asserts a cost of delay without supplied evidence; also invents prior discussions.')],[('2',"I'm writing to formally propose",'Delays the proposal with an unnecessary announcement of writing it.')]),
 ('Opus 4.6','anthropic/claude-opus-4.6','pilot-v15','pilot-client-email','house',[('grounding','review','measure actual improvement against it','May imply improvement will exist or an intervention beyond assessment, but could mean measuring whether improvement occurs. The source does not resolve that reading.')],[('2','Below is the summary.','Unnecessary preamble inside the requested finished email.')]),
]
manifest=out/'reviewed-output-hashes.json';expected=json.loads(manifest.read_text()) if manifest.exists() else {};hashes={};receipts=[];added=set()
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for model,modelid,run,taskid,cond,overrides,editorial in cases:
 stem=f'{modelid.replace("/","--")}--{taskid}--{cond}';p=root/'runs'/run/(stem+'.json');d=json.loads(p.read_text());text=p.with_suffix('.md').read_text();assert d['status']=='ok' and d['text']==text
 route=d['providerMetadata']['gateway']['routing'];assert d['model']==modelid and d['response']['modelId']==modelid and route['canonicalSlug']==modelid
 h=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=h
 if expected:assert expected[stem]==h,'Changed output requires a new review'
 task=tasks[taskid];os={x[0]:x for x in overrides};grades=[]
 for c in task['checks']:
  o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
 es=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in editorial];counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
 ready=not counts['fail'] and not counts['review'] and words<=task['maxWords']
 rows.append({'model':model,'task':taskid,'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':d['inputHash'],'gradeOrigin':'assistant-v7, explicit Opus identity verification','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':[],'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems,'readyWithoutEdits':bool(ready and not ems and not es),'originalGenerationCostUsd':d['billing']['totalCost']})
 receipts.append({'model':modelid,'returnedModel':d['response']['modelId'],'canonicalSlug':route['canonicalSlug'],'provider':route['finalProvider'],'task':taskid,'condition':cond,'words':words,'billingUsd':d['billing']['totalCost'],'generationId':d['providerMetadata']['gateway'].get('generationId')});added.add((model,taskid,cond))
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
ungraded=[r for r in base['ungraded'] if (r['model'],r['task'],r['condition']) not in added]
for taskid in tasks:
 for cond in ['default','house']:
  if ('Opus 4.6',taskid,cond) not in added:ungraded.append({'model':'Opus 4.6','task':taskid,'condition':cond,'status':'not generated'})
assert len(rows)==81 and len(ungraded)==47
method=copy.deepcopy(base['method']);method['revision']='User-requested exact Opus 5 retry succeeded. Opus 4.6 added separately to the registry and compared on the same initial email brief. No model substitution.'
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':ungraded},indent=2)+'\n');(out/'model-verification.json').write_text(json.dumps(receipts,indent=2)+'\n')
lines=['# Opus 5 retry and separate Opus 4.6 comparison','', 'Exact model IDs were checked against the requested model, returned model ID and Gateway canonical slug in each saved response. No 4.6 output is labelled as Opus 5.','', '| Model | Brief | Condition | Content checks | Words / limit | Em dashes | Successful charge |','|---|---|---|---:|---:|---:|---:|']
for r in rows[-3:]:lines.append(f'| {r["model"]} | {r["task"]} | {r["condition"]} | {r["counts"]["pass"]}/{len(r["grades"])} | {r["words"]}/{r["maxWords"]} | {len(r["emDashes"])} | ${r["originalGenerationCostUsd"]:.6f} |')
lines+=['','Provisional, unblinded assistant grades. Opus 4.6 house has one unresolved grounding check, not a confirmed grounding failure. Neither partial model sample supports an eight-brief ranking.','', '## Findings','']
for r in rows[-3:]:
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Saved draft](../../{r["path"]})','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if r['words']>r['maxWords']:lines.append(f'- **Length:** {r["words"]} words exceeds the {r["maxWords"]}-word limit.')
 lines.append('')
lines+=['[Model identity receipts](model-verification.json) preserve routing provider and generation IDs without credential details. Opus 5 used vertexAnthropic; Opus 4.6 used anthropic. The prior Opus 5 failures remain charged at their conservative reservations. Their cause is still not established by the generic 429 message.','', 'Opus 4.6 increases the requested roster to 22 models and the full target to 352 drafts. Earlier 21-model protocols remain intact. [Earlier complete comparisons](../assistant-v6/REPORT.md).','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps(receipts,indent=2))
