"""Materialize explicit assistant repeat grades; preserve every baseline and response."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
sha=lambda text:hashlib.sha256(text.encode()).hexdigest()
plan=read(out/'plan.json');assert hashlib.sha256((root/plan['taskFile']).read_bytes()).hexdigest()==plan['taskFileSha256']
tasks={t['id']:t for t in read(root/plan['taskFile'])}
base=read(root/plan['baselineGrades'])['rows']
decisions=read(out/'decisions.json');ds={(r['model'],r['task'],r['sample']):r for r in decisions}
assert len(ds)==len(decisions)==8
assert set(ds)=={(c['model'],c['task'],n) for c in plan['cases'] for n in [2,3]}
p18=read(root/'runs/pilot-v18/protocol.json');p19=read(root/'runs/pilot-v19/protocol.json')
for field in ['sourceHash','tasksHash','modelsHash','writerGatewayPolicy']:assert p18[field]==p19[field]
for p in [p18,p19]:assert p['limits']['maxOutputTokens'] is None and p['limits']['timeoutMs'] is None
manifest=out/'output-hashes.json';expected=read(manifest) if manifest.exists() else {};hashes={};rows=[];generation_ids=[]
def anchor(text,quote):
 assert quote in text,quote
 i=text.index(quote);return {'quote':quote,'offset':i,'line':text[:i].count('\n')+1}
for case in plan['cases']:
 task=tasks[case['task']]
 original=read(root/case['baseline'])
 baseline=[r for r in base if r['model']==case['model'] and r['task']==case['task'] and r['condition']=='house'];assert len(baseline)==1
 for sample,path in enumerate([case['baseline'],*case['repeatPaths']],1):
  d=read(root/path);text=d['text'];md=Path(path).with_suffix('.md');assert (root/md).read_text()==text
  assert d['status']=='ok' and d['finishReason']=='stop' and not d['warnings']
  assert d['input']==original['input']
  assert d['inputHash']==case['writerInputHash'] and 'maxOutputTokens' not in d['input']
  assert d['model']==d['response']['modelId']==d['providerMetadata']['gateway']['routing']['canonicalSlug']==case['modelId']
  if sample>1:assert d['id'].endswith(f'--sample-{sample}') and not d.get('importedFrom')
  generation=d['providerMetadata']['gateway'].get('generationId') or d['response']['id'];assert generation;generation_ids.append(generation)
  hashes[path]=sha(text)
  if expected:assert expected[path]==hashes[path]
  if sample==1:
   assert sha(text)==case['baselineTextSha256']==baseline[0]['outputSha256']
   row=copy.deepcopy(baseline[0])
  else:
   decision=ds[(case['model'],case['task'],sample)];overrides={x[0]:x for x in decision['content']}
   assert set(overrides)<=set(c['id'] for c in task['checks'])
   grades=[]
   for c in task['checks']:
    item=overrides.get(c['id']);grades.append({'id':c['id'],'verdict':item[1] if item else 'pass','reason':item[3] if item else 'Criterion satisfied on complete-draft review against the frozen source.','evidence':anchor(text,item[2]) if item else None})
   editorial=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in decision['style']]
   counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());emdashes=[anchor(text,m.group())|{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   ready=not counts['fail'] and not counts['review'] and words<=task['maxWords']
   row={'model':case['model'],'task':case['task'],'condition':'house','path':str(md),'outputSha256':sha(text),'writerInputHash':d['inputHash'],'grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':emdashes,'negativeParallelismFindings':[],'placeholderFindings':[],'editorialFindings':editorial,'contentReady':ready,'readyWithoutEdits':ready and not emdashes and not editorial,'originalGenerationCostUsd':d['billing']['totalCost']}
  row['sample']=sample;row['generationId']=generation;rows.append(row)
assert len(rows)==12 and len(set(generation_ids))==12
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
new_cost=sum(r['originalGenerationCostUsd'] for r in rows if r['sample']>1)
summary=[]
for case in plan['cases']:
 rs=[r for r in rows if r['model']==case['model'] and r['task']==case['task']]
 changes={c['id']:[next(g['verdict'] for g in r['grades'] if g['id']==c['id']) for r in rs] for c in tasks[case['task']]['checks']}
 summary.append({'model':case['model'],'task':case['task'],'contentPasses':[r['counts']['pass'] for r in rs],'contentReady':[r['contentReady'] for r in rs],'readyWithoutEdits':[r['readyWithoutEdits'] for r in rs],'changedCriteria':{k:v for k,v in changes.items() if len(set(v))>1}})
(out/'grades.json').write_text(json.dumps({'method':plan,'rows':rows,'newGenerationCostUsd':new_cost},indent=2)+'\n')
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Targeted repeatability diagnostic','',plan['purpose'],'','Two new house-style calls per model and brief, plus the existing uncapped sample. Prompts, source facts, reasoning settings and routing policy match. All 12 generation IDs are distinct; the eight new calls imported no saved outputs. Grades are unblinded assistant decisions under the frozen criteria.','', '| Model | Brief | Content checks passed, attempts 1 / 2 / 3 | Ready without edits, attempts 1 / 2 / 3 |','|---|---|---|---|']
for s in summary:lines.append(f'| {s["model"]} | {s["task"]} | '+ ' / '.join(map(str,s['contentPasses']))+' out of 7 | '+' / '.join('yes' if x else 'no' for x in s['readyWithoutEdits'])+' |')
lines+=['','Both models omitted the required reduction calculation on attempt 1. Muse included it on attempt 2 and omitted it again on attempt 3; Luna included it on attempts 2 and 3. All handoff content checks passed on all attempts. Luna handoff repetition remained an editorial defect on every attempt.','',f'The eight new calls cost ${new_cost:.8f}. Baseline charges are excluded from that amount. Results are not selected by best score or merged into the primary leaderboard. Three attempts on two selected briefs do not estimate general reliability or prove one model better. The calculation criterion measures whether the reduction is explicitly written, not whether a model can subtract.','', '## Evidence by attempt','']
for r in rows:
 lines += [f'### {r["model"]} / {r["task"]} / attempt {r["sample"]}','',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/7 content checks; {r["words"]}/{r["maxWords"]} words.','']
 findings=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 for label,why,e in findings:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not findings:lines.append('No supported content or editorial finding in this review.')
 lines.append('')
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps({'summary':summary,'newGenerationCostUsd':new_cost},indent=2))
