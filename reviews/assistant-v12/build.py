"""Append explicit assistant decisions for the additional Fable 5.1 samples."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v11/grades.json').read_text());rows=copy.deepcopy(base['rows'])
tasks=json.loads((root/'data/tasks-v2.json').read_text())
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
decisions=json.loads((out/'decisions.json').read_text())
content={("Fable 5.1",r['task'],r['condition']):r['content'] for r in decisions}
style={("Fable 5.1",r['task'],r['condition']):r['style'] for r in decisions}
assert len(decisions)==len(content)
existing={(r['model'],r['task'],r['condition']) for r in rows}
assert not (set(content)&existing)
successes=set()
for t in tasks:
 for c in ['default','house']:
  f=root/'runs/pilot-v15'/f"anthropic--claude-fable-5.1--{t['id']}--{c}.json"
  key=('Fable 5.1',t['id'],c)
  if f.exists() and json.loads(f.read_text())['status']=='ok' and key not in existing:successes.add(key)
assert set(content)==successes,'All new successful drafts must be reviewed'
residue={("Fable 5.1",r['task'],r['condition']):r.get('placeholders',[]) for r in decisions}
manifest=out/'reviewed-output-hashes.json';expected=json.loads(manifest.read_text()) if manifest.exists() else {};hashes={}
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for model,modelid in [('Fable 5.1','anthropic/claude-fable-5.1')]:
 for task in tasks:
  for cond in ['default','house']:
   key=(model,task['id'],cond)
   if key not in content:continue
   stem=f'{modelid.replace("/","--")}--{task["id"]}--{cond}';p=root/'runs/pilot-v15'/(stem+'.json');d=json.loads(p.read_text());text=p.with_suffix('.md').read_text()
   assert d['status']=='ok' and d['finishReason']=='stop' and text==d['text'] and d['model']==modelid and d['response']['modelId']==modelid and d['providerMetadata']['gateway']['routing']['canonicalSlug']==modelid
   h=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=h
   if expected:assert expected[stem]==h,'Changed output requires new review'
   os={x[0]:x for x in content.get(key,[])};assert set(os)<=set(c['id'] for c in task['checks']);grades=[]
   for c in task['checks']:
    o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
   es=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in style.get(key,[])];counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   placeholders=[{**anchor(text,q),'reason':why} for q,why in residue.get(key,[])]
   ready=not counts['fail'] and not counts['review'] and words<=task['maxWords'] and not placeholders
   rows.append({'model':model,'task':task['id'],'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':d['inputHash'],'gradeOrigin':'assistant-v12, direct Fable 5.1 review','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':placeholders,'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems,'readyWithoutEdits':bool(ready and not ems and not es),'originalGenerationCostUsd':d['billing']['totalCost']})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
assert len(rows)==len(base['rows'])+len(decisions) and len(hashes)==len(decisions)
method=copy.deepcopy(base['method']);method['revision']='Adds new successful Fable 5.1 drafts; existing pilot emails retain their original grades. Availability failures remain ungraded.'
method['exceptions']+=['Build readiness is a factual status claim, unlike personal confidence or ambiguous team-focus reassurance.','A reply deadline or offer-expiration term requires source support; an open request for the next decision is allowed.']
ungraded=[r for r in base['ungraded'] if (r['model'],r['task'],r['condition']) not in content]
for r in ungraded:
 if r['model']=='Fable 5.1' and r['condition']=='default' and r['task'] in ['launch-delay-email','vendor-decision-memo']:
  failure=root/'runs/pilot-v15'/f"anthropic--claude-fable-5.1--{r['task']}--default.json"
  d=json.loads(failure.read_text());assert d['status']=='error' and d['error']['statusCode']==429
  r['status']='generation failed';r['failurePath']=str(failure.relative_to(root))
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':ungraded},indent=2)+'\n')
summary=[]
for model in ['Astra','Sol','Terra','Qwen Max','Gemini Flash','GLM Flash','Luna','Kimi K3','Qwen Flash','DeepSeek Flash','Opus 5','Opus 4.6','Fable 5.1']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant comparison: Fable 5.1 added','',method['status']+'. Same corrected briefs and conditions; Fable coverage remains partial. Model identities visible; no Jev calls.','', '## Completed eight-draft conditions','', '| Model | Condition | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |','|---|---|---:|---:|---:|---:|---:|---:|']
for s in summary:
 if s['completed']==8:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["contentReady"]}/8 | {s["readyWithoutEdits"]}/8 | ${s["generationCostUsd"]:.5f} |')
lines+=['','Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.','', 'Fable coverage expands only with successful responses. Failed availability requests are ungraded, and earlier pilot emails retain their grades. This is a provisional single-sample comparison.','', '## New review evidence','']
for r in rows[-len(decisions):]:
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 fs += [('Authoring placeholder',g['reason'],g) for g in r['placeholderFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not fs:lines.append('No supported content or editorial finding in this review; any em dash violations remain separate.')
 lines.append('')
lines+=['## Adjudication boundaries','']+['- '+x for x in method['exceptions'][-2:]]+['','[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Incomplete conditions remain separate from the completed-condition table. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps([s for s in summary if s['model'] in ['Fable 5.1']],indent=2))
