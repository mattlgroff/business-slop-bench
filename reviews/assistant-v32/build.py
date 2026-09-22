"""Append explicit assistant decisions for the uncapped Opus 5.5 samples collected in pilot-v22 with per-model pacing, in pilot-v21 with per-model pacing."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v31/grades.json').read_text());rows=copy.deepcopy(base['rows']);replaced=0
models=[('Opus 5.5','anthropic/claude-opus-5.5')]
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
   f=root/'runs/pilot-v22'/f"{modelid.replace('/','--')}--{t['id']}--{c}.json"
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
   stem=f'{modelid.replace("/","--")}--{task["id"]}--{cond}';p=root/'runs/pilot-v22'/(stem+'.json');d=json.loads(p.read_text());text=p.with_suffix('.md').read_text()
   assert 'maxOutputTokens' not in d['input']
   assert not d.get('warnings') and (not d.get('importedFrom') or d['importedFrom'].startswith(('pilot-v21/','pilot-v20/')))
   assert d['status']=='ok' and d['finishReason']=='stop' and text==d['text'] and d['model']==modelid and d['response']['modelId']==modelid and d['providerMetadata']['gateway']['routing']['canonicalSlug'] in (modelid, {'spacexai/grok-4.7':'xai/grok-4.7'}.get(modelid))
   h=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=h
   if expected:assert expected[stem]==h,'Changed output requires new review'
   os={x[0]:x for x in content.get(key,[])};assert set(os)<=set(c['id'] for c in task['checks']);grades=[]
   for c in task['checks']:
    o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
   es=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in style.get(key,[])];counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   placeholders=[{**anchor(text,q),'reason':why} for q,why in residue.get(key,[])]
   negatives=[{**anchor(text,q),'reason':why} for q,why in negative.get(key,[])]
   ready=not counts['fail'] and not counts['review'] and words<=task['maxWords'] and not placeholders
   rows.append({'model':model,'task':task['id'],'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':d['inputHash'],'gradeOrigin':'assistant-v32, uncapped direct Opus 5.5 review','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':negatives,'placeholderFindings':placeholders,'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems and not negatives,'readyWithoutEdits':bool(ready and not ems and not negatives and not es),'originalGenerationCostUsd':d['billing']['totalCost'],'zdrRoute':True,'benchEligible':True})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
assert len(rows)==len(base['rows'])-replaced+len(decisions) and len(hashes)==len(decisions)
method=copy.deepcopy(base['method']);method['revision']='Adds Opus 5.5, released 2026-09-22, to the uncapped comparison from pilot-v22 (protocol 0.22.0, roster of 23 models) under the $100 ceiling, collected one call every seven minutes on a ZDR route. All earlier uncapped grades are retained; historical capped outputs remain separate.'
method['exceptions']=['Provider-native limits still apply; catalog capacity is used only to reserve spending.','Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.']
method['cohort']='uncapped'
method['zdrRule']='Since 2026-09-22 a model with no ZDR route fails the bench for business reasons. Rows with benchEligible false are shown for information and are never pooled with eligible models.'
for model,modelid in models:
 for task in tasks:
  for cond in ['default','house']:
   if (model,task['id'],cond) not in content:
    f=root/'runs/pilot-v22'/f"{modelid.replace('/','--')}--{task['id']}--{cond}.json"
    base['ungraded'].append({'model':model,'task':task['id'],'condition':cond,'status':'generation failed' if f.exists() else 'not generated'})
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':base['ungraded']},indent=2)+'\n')
summary=[]
for model in ['Muse','Gemini Flash','Luna','Qwen Flash','Qwen Max','GLM Flash','GLM 5.3','DeepSeek Flash','DeepSeek Pro','Kimi K3','MiniMax','Grok','Astra','Opus 5','Opus 4.6','Fable 5.1','Fable 5','Opus 5.5']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs),'benchEligible':all(r.get('benchEligible',True) for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Uncapped comparison: Opus 5.5 added','',method['status']+'. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.','', '## Uncapped results','', '| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |','|---|---|---:|---:|---:|---:|---:|---:|---:|']
for s in summary:
 if s['completed']:lines.append(f'| {s["model"]}{"" if s["benchEligible"] else " (non-ZDR, disqualified)"} | {s["condition"]} | {s["completed"]}/8 | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["contentReady"]}/{s["completed"]} | {s["readyWithoutEdits"]}/{s["completed"]} | ${s["generationCostUsd"]:.5f} |')
lines+=['','Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.','', 'These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax, Grok and Astra are new uncapped generations on each attempted cell; the Grok house handoff deck comes from pilot-v21 after its pilot-v20 request timed out; Opus 5 is a pilot-v21 collection with one pilot-v20 import; Opus 4.6 is a full pilot-v21 collection; Fable 5.1 and Fable 5 are pilot-v21 collections with one pilot-v20 import each on a declared non-ZDR route; Opus 5.5 is a full pilot-v22 collection on a ZDR route; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.','', '## New review evidence','']
for r in rows[-len(decisions):]:
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 fs += [('Negative parallelism',g['reason'],g) for g in r['negativeParallelismFindings']]
 fs += [('Authoring placeholder',g['reason'],g) for g in r['placeholderFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not fs:lines.append('No supported content or editorial finding in this review; any em dash violations remain separate.')
 lines.append('')
lines+=['## Adjudication boundaries','', 'Opus 5.5 passes 52/54 default and 51/54 house content checks. Its only default failure is readiness for the knowledge-search pilot in the strategy deck; house repeats that failure and adds an on-track team claim in the launch update that the default draft did not make. Both vendor memos are unresolved only on who signs. Both readouts state the 3-minute and 20% reduction and the correct 3-point and 5-point differences. No draft invents a reply deadline, a start date or a prior discussion, which every other Anthropic model in this cohort did at least once. Three default drafts and one house draft exceed their word limits, by 1 to 18 words.', '', 'Against the release note claim the user asked about: the house rules remove every em dash (4 default, 0 house) and every editorial finding (4 default, 0 house), exactly as they do for Opus 5, so this bench cannot separate the two models on rule-following. On putting the point up front, Opus 5.5 opens two default drafts with an announcing sentence and Opus 5 also opens two that way, so there is no measurable difference there either. Where Opus 5.5 does differ is grounding: one and two failures against four and four for Opus 5, and content-ready counts of 4 of 8 default and 3 of 8 house against 1 and 3. Its default change order and handoff deck are ready without edits, which no other Anthropic default draft in this cohort achieves. Two house drafts and one default draft refer to the source pack in the body, which blocks content ready.', '', 'These are 16 single generations, graded unblinded by the same reviewer, collected one call every seven minutes on a ZDR route on the day the model was released. A difference of a few checks between Opus 5.5 and Opus 5 is within what a second generation could change, and the Astra sample remains the only one with every draft content ready.', '']+['- '+x for x in method['exceptions'][-2:]]+['','[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps([s for s in summary if s['model'] in ['Opus 5.5']],indent=2))
