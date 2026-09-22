"""Append explicit assistant decisions for the uncapped Qwen Max samples."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v19/grades.json').read_text());rows=copy.deepcopy(base['rows'])
models=[('Qwen Max','alibaba/qwen3.8-max-0902')]
tasks=json.loads((root/'data/tasks-v2.json').read_text())
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
decisions=json.loads((out/'decisions.json').read_text())
content={(r['model'],r['task'],r['condition']):r['content'] for r in decisions}
style={(r['model'],r['task'],r['condition']):r['style'] for r in decisions}
assert len(decisions)==len(content)
successes=set()
for model,modelid in models:
 for t in tasks:
  for c in ['default','house']:
   f=root/'runs/pilot-v19'/f"{modelid.replace('/','--')}--{t['id']}--{c}.json"
   if f.exists():
    d=json.loads(f.read_text())
    if d['status']=='ok' and d.get('text','').strip() and d.get('finishReason')!='length':successes.add((model,t['id'],c))
assert set(content)==successes,'Review every completed uncapped draft'
residue={(r['model'],r['task'],r['condition']):r.get('placeholders',[]) for r in decisions}
negative={(r['model'],r['task'],r['condition']):r.get('negative',[]) for r in decisions}
manifest=out/'reviewed-output-hashes.json';expected=json.loads(manifest.read_text()) if manifest.exists() else {};hashes={}
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for model,modelid in models:
 for task in tasks:
  for cond in ['default','house']:
   key=(model,task['id'],cond)
   if key not in content:continue
   stem=f'{modelid.replace("/","--")}--{task["id"]}--{cond}';p=root/'runs/pilot-v19'/(stem+'.json');d=json.loads(p.read_text());text=p.with_suffix('.md').read_text()
   assert 'maxOutputTokens' not in d['input']
   assert not d.get('warnings') and not d.get('importedFrom')
   assert d['status']=='ok' and d['finishReason']=='stop' and text==d['text'] and d['model']==modelid and d['response']['modelId']==modelid and d['providerMetadata']['gateway']['routing']['canonicalSlug']==modelid
   h=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=h
   if expected:assert expected[stem]==h,'Changed output requires new review'
   os={x[0]:x for x in content.get(key,[])};assert set(os)<=set(c['id'] for c in task['checks']);grades=[]
   for c in task['checks']:
    o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
   es=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in style.get(key,[])];counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   placeholders=[{**anchor(text,q),'reason':why} for q,why in residue.get(key,[])]
   negatives=[{**anchor(text,q),'reason':why} for q,why in negative.get(key,[])]
   ready=not counts['fail'] and not counts['review'] and words<=task['maxWords'] and not placeholders
   rows.append({'model':model,'task':task['id'],'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':d['inputHash'],'gradeOrigin':'assistant-v20, uncapped direct Qwen Max review','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':negatives,'placeholderFindings':placeholders,'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems and not negatives,'readyWithoutEdits':bool(ready and not ems and not negatives and not es),'originalGenerationCostUsd':d['billing']['totalCost']})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
assert len(rows)==len(base['rows'])+len(decisions) and len(hashes)==len(decisions)
method=copy.deepcopy(base['method']);method['revision']='Adds Qwen Max to the uncapped comparison. All earlier uncapped grades are retained; historical capped outputs remain separate.'
method['exceptions']=['Provider-native limits still apply; catalog capacity is used only to reserve spending.','Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.']
method['cohort']='uncapped'
for model,modelid in models:
 for task in tasks:
  for cond in ['default','house']:
   if (model,task['id'],cond) not in content:
    f=root/'runs/pilot-v19'/f"{modelid.replace('/','--')}--{task['id']}--{cond}.json"
    base['ungraded'].append({'model':model,'task':task['id'],'condition':cond,'status':'generation failed' if f.exists() else 'not generated'})
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':base['ungraded']},indent=2)+'\n')
summary=[]
for model in ['Muse','Gemini Flash','Luna','Qwen Flash','Qwen Max','GLM Flash','DeepSeek Flash','MiniMax']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Uncapped comparison: Qwen Max added','',method['status']+'. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.','', '## Uncapped results','', '| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |','|---|---|---:|---:|---:|---:|---:|---:|---:|']
for s in summary:
 if s['completed']:lines.append(f'| {s["model"]} | {s["condition"]} | {s["completed"]}/8 | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["contentReady"]}/{s["completed"]} | {s["readyWithoutEdits"]}/{s["completed"]} | ${s["generationCostUsd"]:.5f} |')
lines+=['','Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.','', 'These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash and DeepSeek Flash are new uncapped generations on each attempted cell. MiniMax retains partial coverage after its transport timeout.','', '## New review evidence','']
for r in rows[-len(decisions):]:
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 fs += [('Negative parallelism',g['reason'],g) for g in r['negativeParallelismFindings']]
 fs += [('Authoring placeholder',g['reason'],g) for g in r['placeholderFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not fs:lines.append('No supported content or editorial finding in this review; any em dash violations remain separate.')
 lines.append('')
lines+=['## Adjudication boundaries','', 'Qwen Max passes 49/54 default and 52/54 house content checks with no unresolved checks. Content-ready counts are 3/8 default and 4/8 house; ready-without-edits counts are 1/8 and 3/8. Three drafts are blocked only by unfilled header dates or a sender placeholder; the intentional sponsor signature fields are allowed. Default drafts contain four em dashes; house drafts contain none.', '', 'Confirmed failures are an invented end-of-week reply deadline, invented review progress and staging readiness, an assertion that the work is done and ready, pilot readiness and a missing Option B owner asserted in a comparison table, a bare readiness-to-start claim, and incident ownership moved from Lee before acceptance. The last error also appeared in the capped Qwen Max sample and is recorded as both an ownership conflict and a grounding failure. Both readouts state the reduction explicitly.', '', 'Readiness claims are failed consistently across this cohort when the source supplies no start conditions, whether stated bare or justified by listed facts. Rhetorical reassurance contrasts in the launch emails are not treated as style-gate negative parallelism; the unsupported assurance inside them is graded under grounding instead.', '']+['- '+x for x in method['exceptions'][-2:]]+['','[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps([s for s in summary if s['model'] in ['Qwen Max']],indent=2))
