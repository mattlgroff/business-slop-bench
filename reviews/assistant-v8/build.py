"""Append explicit assistant decisions for the complete Sol and Terra samples."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v7/grades.json').read_text());rows=copy.deepcopy(base['rows'])
tasks=json.loads((root/'data/tasks-v2.json').read_text())
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
content={
 ('Sol','launch-delay-email','default'):[('grounding','review','The team remains focused on launch readiness','Current team focus is not supplied; ordinary reassurance is a plausible reading, so this is unresolved rather than a confirmed invention.')],
 ('Sol','pilot-results-memo','default'):[('C01','fail','12 minutes across 100 tickets, compared with 15 minutes','Reports endpoints but omits the required 3-minute or 20% reduction.')],
 ('Sol','pilot-results-memo','house'):[('C01','fail','12 minutes across 100 tickets, compared with 15 minutes','Reports endpoints but omits the required 3-minute or 20% reduction.')],
 ('Terra','launch-delay-email','default'):[('grounding','review','The team remains focused and is continuing to prepare for release.','Current focus and preparation are not supplied; this may be routine reassurance rather than a material status assertion.')],
 ('Terra','launch-delay-email','house'):[('grounding','review','release requires Nia’s completed approval','The source makes Nia review owner without explicitly naming the approval authority. This may be shorthand for completion of her review or a new authority assignment.')],
 ('Terra','ai-strategy-slides','default'):[('grounding','fail','Why Not Customer Credit Decisions This Quarter','Changes the planning horizon in this heading to this quarter; the corrected brief and the opening slide consistently concern next quarter.')],
 ('Terra','ai-strategy-slides','house'):[('grounding','fail','select the authorized knowledge search pilot','The source authorizes the policy documents, not the pilot itself. COO selection is still requested.')],
}
style={
 ('Sol','pilot-client-email','default'):[('16','Once approved, we can move the discussion forward.','Tautological closing adds no next action or information beyond the approval request.')],
 ('Sol','pilot-client-email','house'):[('21','the client’s goal','Refers to the client in the third person while addressing that client directly; your goal fits the audience.')],
 ('Terra','pilot-client-email','default'):[('2','I’m writing to request approval','Unnecessary announcement of writing the request.'),('21','the client’s target','Third-person client reference inside an email directly to the client.')],
 ('Terra','pilot-client-email','house'):[('21','the client’s 20% reduction goal','Third-person client reference inside an email directly to the client.')],
 ('Terra','discovery-proposal','default'):[('10','Upon kickoff, the initial 50% payment is due. The remaining 50% is due on delivery of the three agreed discovery artifacts.','Repeats the payment terms already given in the commercial table after the next-step sequence.')],
 ('Terra','change-order','default'):[('16','The proposed change includes work to add the CRM connector.','Repeats the requested connector addition stated immediately above without adding scope detail.')],
}
manifest=out/'reviewed-output-hashes.json';expected=json.loads(manifest.read_text()) if manifest.exists() else {};hashes={}
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for model,modelid in [('Sol','openai/gpt-5.6-sol'),('Terra','openai/gpt-5.6-terra')]:
 for task in tasks:
  for cond in ['default','house']:
   key=(model,task['id'],cond);stem=f'{modelid.replace("/","--")}--{task["id"]}--{cond}';p=root/'runs/pilot-v15'/(stem+'.json');d=json.loads(p.read_text());text=p.with_suffix('.md').read_text()
   assert d['status']=='ok' and d['finishReason']=='stop' and text==d['text'] and d['model']==modelid and d['response']['modelId']==modelid
   h=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=h
   if expected:assert expected[stem]==h,'Changed output requires new review'
   os={x[0]:x for x in content.get(key,[])};assert set(os)<=set(c['id'] for c in task['checks']);grades=[]
   for c in task['checks']:
    o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
   es=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in style.get(key,[])];counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   ready=not counts['fail'] and not counts['review'] and words<=task['maxWords']
   rows.append({'model':model,'task':task['id'],'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':d['inputHash'],'gradeOrigin':'assistant-v8, direct Sol and Terra review','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':[],'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems,'readyWithoutEdits':bool(ready and not ems and not es),'originalGenerationCostUsd':d['billing']['totalCost']})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
assert len(rows)==113 and len(hashes)==32
method=copy.deepcopy(base['method']);method['revision']='Adds complete Sol and Terra samples under the unchanged corrected task set, low reasoning and output cap. Exact returned model IDs and stop finish reasons verified.'
method['exceptions']+=['Team-focus claims remain unresolved consistently with the Luna review. Personal confidence is distinct from objective performance claims.','Terra launch house: Nia review ownership may or may not imply approval authority. This is unresolved, not a forced failure.','Terra this-quarter heading is penalized because the revised source no longer contains the earlier quarter ambiguity.','Naming a pilot as authorized is distinct from recommending it or using approved source documents.']
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':base['ungraded']},indent=2)+'\n')
summary=[]
for model in ['Astra','Sol','Terra','Luna','Kimi K3','Qwen Flash','DeepSeek Flash','Opus 5','Opus 4.6','Fable 5.1']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant comparison: Sol and Terra added','',method['status']+'. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.','', '## Completed eight-draft conditions','', '| Model | Condition | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |','|---|---|---:|---:|---:|---:|---:|---:|']
for s in summary:
 if s['completed']==8:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["contentReady"]}/8 | {s["readyWithoutEdits"]}/8 | ${s["generationCostUsd"]:.5f} |')
lines+=['','Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.','', 'Sol preserves the supplied facts in most drafts but misses the required time reduction calculation in both readouts. Terra includes the calculation, but its strategy slides introduce an inconsistent quarter and an unsupported authorization claim. Both have stronger house-style readiness than Luna in this sample, at higher observed generation cost. This is not a reliability ranking from repeated trials.','', '## New review evidence','']
for r in rows[-32:]:
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not fs:lines.append('No supported content or editorial finding in this review; any em dash violations remain separate.')
 lines.append('')
lines+=['## Adjudication boundaries','']+['- '+x for x in method['exceptions'][-4:]]+['','[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Partial Opus, Fable and DeepSeek house coverage remains separate. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps([s for s in summary if s['model'] in ['Sol','Terra']],indent=2))
