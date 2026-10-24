"""Materialize manually reviewed Kimi v3 decisions; never pool v2 vendor scores."""
import hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
load=lambda p:json.loads((root/p).read_text())
tasks=load('data/tasks-v3.json'); decisions=json.loads((out/'decisions.json').read_text())
assert len(decisions)==16
indexed={(d['task'],d['condition']):d for d in decisions}
assert len(indexed)==16
rows=[]
for task in tasks:
 for condition in ['default','house']:
  dec=indexed[task['id'],condition]
  path=Path('runs/pilot-v34')/f'moonshotai--kimi-k3.1-pro--{task["id"]}--{condition}.json'
  record=load(path);text=(root/path.with_suffix('.md')).read_text();digest=hashlib.sha256(text.encode()).hexdigest()
  assert record['status']=='ok' and record['finishReason']=='stop' and record['text']==text
  assert record['model']==record['response']['modelId']=='moonshotai/kimi-k3.1-pro'
  route=record['providerMetadata']['gateway']['routing']
  assert route['canonicalSlug']==record['model'] and route['totalProviderAttemptCount']==1
  assert record['input']['reasoning']=='low' and 'maxOutputTokens' not in record['input']
  assert all(w['feature']=='temperature' and w['type']=='unsupported' for w in record.get('warnings',[]))
  assert digest==dec['outputSha256']
  def anchor(q):
   assert q in text,q
   i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
  overrides={c[0]:c for c in dec['content']};assert set(overrides)<=set(c['id'] for c in task['checks'])
  grades=[]
  for check in task['checks']:
   c=overrides.get(check['id'])
   grades.append({'id':check['id'],'criterion':check['statement'],'verdict':c[1] if c else 'pass','reason':c[3] if c else 'Satisfied on full-draft review against the frozen v3 source pack.','evidence':anchor(c[2]) if c else None})
  counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']}
  style=[{'category':cat,'reason':why,'evidence':anchor(q)} for cat,q,why in dec['style']]
  residue=[{**anchor(q),'reason':why} for q,why in dec.get('placeholders',[])]
  negatives=[{**anchor(q),'reason':why} for q,why in dec.get('negative',[])]
  ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
  ready=not counts['fail'] and not counts['review'] and len(text.split())<=task['maxWords'] and not residue
  rows.append({'model':'Kimi K3.1 Pro','task':task['id'],'condition':condition,'path':str(path.with_suffix('.md')),'outputSha256':digest,'writerInputHash':record['inputHash'],'gradeOrigin':'assistant-v53 manual unblinded assistant review','grades':grades,'counts':counts,'words':len(text.split()),'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':negatives,'placeholderFindings':residue,'editorialFindings':style,'contentReady':bool(ready),'styleGatePass':not ems and not negatives,'readyWithoutEdits':bool(ready and not ems and not negatives and not style),'originalGenerationCostUsd':record['billing']['totalCost'],'warnings':record.get('warnings',[]),'benchEligible':True})
method={'status':'Provisional, unblinded assistant judgments, without independent human gold','taskFile':'data/tasks-v3.json','run':'pilot-v34','configuration':'Low reasoning requested; provider reports fixed temperature. No harness output cap or generation deadline. One attempt per cell.','comparison':'Full v3 totals are separate from historical v2. Only the unchanged seven briefs are compared directly.'}
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':[]},indent=2)+'\n')
def summarize(rs,model,cond):
 return {'model':model,'condition':cond,'completed':len(rs),'pass':sum(r['counts']['pass'] for r in rs),'fail':sum(r['counts']['fail'] for r in rs),'review':sum(r['counts']['review'] for r in rs),'total':sum(len(r['grades']) for r in rs),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)}
summary=[summarize([r for r in rows if r['condition']==c],'Kimi K3.1 Pro',c) for c in ['default','house']]
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
old=load('reviews/assistant-v52/grades.json')['rows'];common=[];verification=[]
for model in ['Astra','Muse Wonder 1.0','Sol 6.1','Kimi K3','Kimi K3.1 Pro']:
 for cond in ['default','house']:
  rs=[r for r in (rows if model=='Kimi K3.1 Pro' else old) if r['model']==model and r['condition']==cond and r['task']!='vendor-decision-memo']
  assert len(rs)==7
  for r in rs:
   saved=load(Path(r['path']).with_suffix('.json'));current=load(Path('runs/pilot-v34')/f'moonshotai--kimi-k3.1-pro--{r["task"]}--{cond}.json')
   assert saved['input']==current['input']
   verification.append({'model':model,'task':r['task'],'condition':cond,'inputHash':saved['inputHash'],'matchesKimi31':True})
  common.append(summarize(rs,model,cond))
(out/'common-seven.json').write_text(json.dumps(common,indent=2)+'\n');(out/'input-verification.json').write_text(json.dumps(verification,indent=2)+'\n')
lines=['# Kimi K3.1 Pro on BusinessSlopBench v3','','October 24, 2026. '+method['status']+'.', '',method['configuration'],'','Kimi passes all 54 content checks in each condition, including explicit signing authority. Only the discovery proposal and change order are ready without edits in each condition. Six house drafts need repetition edits; house instructions remove all eleven plain-condition em dashes. On the unchanged seven briefs, factual-check performance improves over Kimi K3 but editing readiness remains below Astra and Muse Wonder. These are findings on this sample, not a general reliability claim.', '', '## Full v3 results','','| Condition | Checks | Content ready | Ready without edits | Cost, 8 drafts |','|---|---:|---:|---:|---:|']
for s in summary:lines.append(f'| {s["condition"]} | {s["pass"]}/{s["total"]} | {s["contentReady"]}/8 | {s["readyWithoutEdits"]}/8 | ${s["generationCostUsd"]:.6f} |')
lines+=['','The replacement vendor task explicitly names Alex as sole signatory, Priya as procurement coordinator and the CFO as prior approver. This is the first v3 panel. Historical full-panel rankings remain unchanged; no v3 rank against v2 is assigned.','', '## Comparable seven-brief subset','','Vendor memo excluded for every model. All remaining saved writer inputs match exactly, including requested low reasoning. Primary attempts only; this subset was chosen because of the declared v2/v3 task change, not performance. Provider sampling can differ, and fixed-temperature warnings prevent an equal-temperature claim.','', '| Model | Condition | Checks | Content ready | Ready without edits |','|---|---|---:|---:|---:|']
for s in common:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["contentReady"]}/7 | {s["readyWithoutEdits"]}/7 |')
lines+=['','## Draft evidence','']
for r in rows:
 lines += [f'### {r["task"]} / {r["condition"]}','',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 for g in r['grades']:
  if g['verdict']!='pass':lines.append(f'- {g["id"]} {g["verdict"]}: "{g["evidence"]["quote"]}". {g["reason"]}')
 for g in r['editorialFindings']:lines.append(f'- Style {g["category"]}: "{g["evidence"]["quote"]}". {g["reason"]}')
 for g in r['placeholderFindings']+r['negativeParallelismFindings']:lines.append(f'- "{g["quote"]}": {g["reason"]}')
 for note in indexed[r['task'],r['condition']].get('adjudicationNotes',[]):lines.append('- Boundary: '+note)
 lines.append('')
lines+=['[All grades and anchored evidence](grades.json), [authored decisions](decisions.json), [mechanical scans](scans.json), [matched inputs](input-verification.json).','', 'Rebuild with `python3 reviews/assistant-v53/build.py`. No API calls are made by this builder. Prices in the saved Gateway catalog: $2 input / $10 output per million tokens. Costs above are reported billing. Blog not updated as part of this run.','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps(summary,indent=2))
