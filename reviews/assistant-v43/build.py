"""Append all sixteen reviewed Sonnet outputs, preserving the prior cohort."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v42/grades.json').read_text());rows=copy.deepcopy(base['rows']);replaced=0
models=[('Sonnet 5','anthropic/claude-sonnet-5')]
tasks=json.loads((root/'data/tasks-v2.json').read_text())
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
decisions=json.loads((out/'decisions.json').read_text())
assert len(decisions)==16, 'Full Sonnet review is required before promotion'
content={(r['model'],r['task'],r['condition']):r['content'] for r in decisions}
style={(r['model'],r['task'],r['condition']):r['style'] for r in decisions}
assert len(decisions)==len(content)
successes=set()
for model,modelid in models:
 for t in tasks:
  for c in ['default','house']:
   f=root/'runs/pilot-v23'/f"{modelid.replace('/','--')}--{t['id']}--{c}.json"
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
   stem=f'{modelid.replace("/","--")}--{task["id"]}--{cond}';p=root/'runs/pilot-v23'/(stem+'.json');d=json.loads(p.read_text());text=p.with_suffix('.md').read_text()
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
   rows.append({'model':model,'task':task['id'],'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':d['inputHash'],'gradeOrigin':'assistant-v43, uncapped direct Sonnet review','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':negatives,'placeholderFindings':placeholders,'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems and not negatives,'readyWithoutEdits':bool(ready and not ems and not negatives and not es),'originalGenerationCostUsd':d['billing']['totalCost'],'zdrRoute':True,'benchEligible':True})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
assert len(rows)==400 and len(hashes)==16
assert rows[:len(base['rows'])]==base['rows'], 'Prior judgments must remain unchanged'
method=copy.deepcopy(base['method']);method['revision']='Adds Sonnet 5 under the unchanged pilot-v23 protocol, v2 briefs and uncapped settings. All earlier grades are retained.'
method['exceptions']=['Provider-native limits still apply; catalog capacity is used only to reserve spending.','Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.']
method['cohort']='uncapped'
method['zdrRule']='Since 2026-09-22 a model with no ZDR route fails the bench for business reasons. Eligibility is derived for every row from its saved catalog and frozen request policy. Muse, Fable 5, Fable 5.1, Luna 6 and Sol 6 have no ZDR route and are shown for information only. This checks recorded routing requirements, not independent provider retention compliance.'
for model,modelid in models:
 for task in tasks:
  for cond in ['default','house']:
   if (model,task['id'],cond) not in content:
    f=root/'runs/pilot-v23'/f"{modelid.replace('/','--')}--{task['id']}--{cond}.json"
    base['ungraded'].append({'model':model,'task':task['id'],'condition':cond,'status':'generation failed' if f.exists() else 'not generated'})
# Derive eligibility for inherited rows too; missing metadata is not permission.
eligibility_evidence={}
for row in rows:
 record_path=(root/row['path']).with_suffix('.json')
 record=json.loads(record_path.read_text())
 protocol=json.loads((record_path.parent/'protocol.json').read_text())
 catalog=json.loads((record_path.parent/'catalog.json').read_text())['models']
 catalog_model=next(m for m in catalog if m['id']==record['model'])
 coverage=catalog_model.get('zdr')
 assert coverage in ('all','some','none'),'Unknown ZDR coverage requires review'
 policy=protocol['writerGatewayPolicy']
 requested=policy['zeroDataRetentionDefault'] and record['model'] not in policy['nonZdrModels']
 row['benchEligible']=coverage in ('all','some') and requested
 eligibility_evidence[row['path']]={'catalog':str((record_path.parent/'catalog.json').relative_to(root)),'catalogZdr':coverage,'zdrRequested':requested,'benchEligible':row['benchEligible']}
(out/'eligibility-evidence.json').write_text(json.dumps(eligibility_evidence,indent=2)+'\n')
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':base['ungraded']},indent=2)+'\n')
summary=[]
for model in ['Muse','Gemini Flash','Luna','Qwen Flash','Qwen Max','GLM Flash','GLM 5.3','DeepSeek Flash','DeepSeek Pro','Kimi K3','MiniMax','Grok','Astra','Opus 5','Opus 4.6','Fable 5.1','Fable 5','Opus 5.5','Terra','Gemini Pro','Sol 5.6','Luna 6','Sol 6','MiMo','Sonnet 5']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs),'benchEligible':bool(rs) and all(r['benchEligible'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Uncapped comparison: Sonnet 5 added','',method['status']+'. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.','', '## Uncapped results','', '| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |','|---|---|---:|---:|---:|---:|---:|---:|---:|']
for s in summary:
 if s['completed']:lines.append(f'| {s["model"]}{"" if s["benchEligible"] else " (non-ZDR, disqualified)"} | {s["condition"]} | {s["completed"]}/8 | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["contentReady"]}/{s["completed"]} | {s["readyWithoutEdits"]}/{s["completed"]} | ${s["generationCostUsd"]:.5f} |')
lines+=['','Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.','', 'All 400 primary drafts were generated without a harness output-token cap or generation deadline. Earlier capped outputs and the 40 repeated samples remain separate. The 384 prior judgments are preserved from [assistant-v42](../assistant-v42/REPORT.md); each row records its draft path, writer input hash and output hash. Sonnet adds sixteen pilot-v23 outputs with no generation retries.','', 'Eligibility is derived from each saved catalog and frozen request policy, including inherited rows. Muse, Fable 5, Fable 5.1, Luna 6 and Sol 6 are non-ZDR and disqualified; their writing scores remain visible. This is a routing-policy check, not independent verification of provider retention. [Eligibility evidence](eligibility-evidence.json).','', '## New review evidence','']
for r in rows[-len(decisions):]:
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 fs += [('Negative parallelism',g['reason'],g) for g in r['negativeParallelismFindings']]
 fs += [('Authoring placeholder',g['reason'],g) for g in r['placeholderFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not fs:lines.append('No supported content or editorial finding in this review; any em dash violations remain separate.')
 lines.append('')
lines+=['## Adjudication boundaries', '', 'All sixteen Sonnet drafts use the unchanged v2 briefs with no harness output-token cap. Grounding findings concern invented authorization, readiness, deadlines, commercial conditions, contractual provenance and incident ownership. The ambiguous CFO-signature wording remains unresolved. Factual contrasts and intentional signature fields are allowed. Each judgment is a provisional unblinded assistant review, not independent human gold.', '', '[All decisions](grades.json), [summary](summary.json), and [eligibility evidence](eligibility-evidence.json). Costs cover successful represented generations.', '']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps([s for s in summary if s['model']=='Sonnet 5'],indent=2))
