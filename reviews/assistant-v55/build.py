"""Materialize manually reviewed Carbon v3 decisions; never pool v2 vendor scores."""
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
  path=Path('runs/pilot-v36')/f'google--gemini-4-carbon--{task["id"]}--{condition}.json'
  record=load(path);text=(root/path.with_suffix('.md')).read_text();digest=hashlib.sha256(text.encode()).hexdigest()
  assert record['status']=='ok' and record['finishReason']=='stop' and record['text']==text
  assert record['model']==record['response']['modelId']=='google/gemini-4-carbon'
  route=record['providerMetadata']['gateway']['routing']
  assert route['canonicalSlug']==record['model'] and route['totalProviderAttemptCount']==1
  assert record['input']['reasoning']=='low' and 'maxOutputTokens' not in record['input']
  assert not record.get('warnings'), record.get('warnings')
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
  rows.append({'model':'Gemini 4 Carbon','task':task['id'],'condition':condition,'path':str(path.with_suffix('.md')),'outputSha256':digest,'writerInputHash':record['inputHash'],'gradeOrigin':'assistant-v55 manual unblinded assistant review','grades':grades,'counts':counts,'words':len(text.split()),'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':negatives,'placeholderFindings':residue,'editorialFindings':style,'contentReady':bool(ready),'styleGatePass':not ems and not negatives,'readyWithoutEdits':bool(ready and not ems and not negatives and not style),'originalGenerationCostUsd':record['billing']['totalCost'],'warnings':record.get('warnings',[]),'benchEligible':True})
method={'status':'Provisional, unblinded assistant judgments, without independent human gold','taskFile':'data/tasks-v3.json','run':'pilot-v36','configuration':'Low reasoning requested; provider defaults otherwise unchanged. No harness output cap or generation deadline. One attempt per cell.','comparison':'Full v3 totals are separate from historical v2. Only the unchanged seven briefs are compared directly.'}
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':[]},indent=2)+'\n')
def summarize(rs,model,cond):
 return {'model':model,'condition':cond,'completed':len(rs),'pass':sum(r['counts']['pass'] for r in rs),'fail':sum(r['counts']['fail'] for r in rs),'review':sum(r['counts']['review'] for r in rs),'total':sum(len(r['grades']) for r in rs),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)}
summary=[summarize([r for r in rows if r['condition']==c],'Gemini 4 Carbon',c) for c in ['default','house']]
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
v3summary=load('reviews/assistant-v54/v3-summary.json')+summary
(out/'v3-summary.json').write_text(json.dumps(v3summary,indent=2)+'\n')
old=load('reviews/assistant-v52/grades.json')['rows'];common=[];verification=[]
for model in ['Astra','Muse Wonder 1.0','Sol 6.1','Gemini 4 Argon','Gemini Flash','Gemini 4 Carbon']:
 for cond in ['default','house']:
  rs=[r for r in (rows if model=='Gemini 4 Carbon' else old) if r['model']==model and r['condition']==cond and r['task']!='vendor-decision-memo']
  assert len(rs)==7
  for r in rs:
   saved=load(Path(r['path']).with_suffix('.json'));current=load(Path('runs/pilot-v36')/f'google--gemini-4-carbon--{r["task"]}--{cond}.json')
   assert saved['input']==current['input']
   verification.append({'model':model,'task':r['task'],'condition':cond,'inputHash':saved['inputHash'],'matchesCarbon':True})
  common.append(summarize(rs,model,cond))
(out/'common-seven.json').write_text(json.dumps(common,indent=2)+'\n');(out/'input-verification.json').write_text(json.dumps(verification,indent=2)+'\n')
lines=['# Gemini 4 Carbon on BusinessSlopBench v3','','November 11, 2026. '+method['status']+'.', '',method['configuration'],'','Carbon has three failed checks in the plain condition and five in the house condition. The latter represent four affected drafts because the invented pre-acceptance incident owner fails both C04 and grounding. The house rules remove two em dashes but leave unsupported claims, a causal overstatement and document-description preambles. Only the house launch email and vendor memo are ready without edits.', '', '## Full v3 results','','| Condition | Checks | Content ready | Ready without edits | Cost, 8 drafts |','|---|---:|---:|---:|---:|']
for s in summary:lines.append(f'| {s["condition"]} | {s["pass"]}/{s["total"]} | {s["contentReady"]}/8 | {s["readyWithoutEdits"]}/8 | ${s["generationCostUsd"]:.6f} |')
lines+=['','The replacement vendor task explicitly names Alex as sole signatory, Priya as procurement coordinator and the CFO as prior approver. This is a v3 panel, comparable in full with the saved Kimi K3.1 Pro and Fable 5.2 v3 runs. Historical full-panel rankings remain unchanged; no v3 rank against v2 is assigned.','', '## Comparable seven-brief subset','','Vendor memo excluded for every model. All remaining saved writer inputs match exactly, including requested low reasoning. Primary attempts only; this subset was chosen because of the declared v2/v3 task change, not performance. Provider sampling can differ. Requested low reasoning does not establish equal compute or sampling.','', '| Model | Condition | Checks | Content ready | Ready without edits |','|---|---|---:|---:|---:|']
for s in common:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["contentReady"]}/7 | {s["readyWithoutEdits"]}/7 |')
lines+=['','## Full v3 comparison','','Same v3 writer inputs for all eight briefs. These are separate primary attempts with low reasoning requested; provider implementations may differ.','', '| Model | Condition | Checks | Content ready | Ready without edits |', '|---|---|---:|---:|---:|']
for s in v3summary:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["contentReady"]}/8 | {s["readyWithoutEdits"]}/8 |')
market_cost=0
for task in tasks:
 for cond in ['default','house']:
  current=load(Path('runs/pilot-v36')/f'google--gemini-4-carbon--{task["id"]}--{cond}.json')
  market_cost+=float(current['providerMetadata']['gateway']['marketCost'])
  for run,stem in [('pilot-v34','moonshotai--kimi-k3.1-pro'),('pilot-v35','anthropic--claude-fable-5.2')]:
   other=load(Path('runs')/run/f'{stem}--{task["id"]}--{cond}.json')
   assert current['input']==other['input']
lines+=['','## Billing and configuration','',f'Gateway reports $0 charged across sixteen calls. Its separate marketCost field sums to ${market_cost:.6f}; that is not a charged amount. The saved catalog lists $2 input / $10 output per million tokens. The budget ledger retains its conservative accounting. No promotion or future free pricing is inferred. All responses report zero reasoning tokens despite the low reasoning request and return no warnings; internal reasoning behavior is not independently verified.','', '## Draft evidence','']
for r in rows:
 lines += [f'### {r["task"]} / {r["condition"]}','',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 for g in r['grades']:
  if g['verdict']!='pass':lines.append(f'- {g["id"]} {g["verdict"]}: "{g["evidence"]["quote"]}". {g["reason"]}')
 for g in r['editorialFindings']:lines.append(f'- Style {g["category"]}: "{g["evidence"]["quote"]}". {g["reason"]}')
 for g in r['placeholderFindings']+r['negativeParallelismFindings']:lines.append(f'- "{g["quote"]}": {g["reason"]}')
 for note in indexed[r['task'],r['condition']].get('adjudicationNotes',[]):lines.append('- Boundary: '+note)
 lines.append('')
lines+=['[All grades and anchored evidence](grades.json), [authored decisions](decisions.json), [mechanical scans](scans.json), [matched inputs](input-verification.json).','', 'Rebuild with `python3 reviews/assistant-v55/build.py`. No API calls are made by this builder. Prices in the saved Gateway catalog: $2 input / $10 output per million tokens. Costs above are reported billing. Blog not updated as part of this run.','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps(summary,indent=2))
