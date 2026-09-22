"""Append direct assistant review of six newly collected DeepSeek default drafts."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v4/grades.json').read_text());rows=copy.deepcopy(base['rows'])
tasks={t['id']:t for t in json.loads((root/'data/tasks-v2.json').read_text())}
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
reviews=[
 ('pilot-v12','vendor-decision-memo',[],[('16','Alpha totals $92,000; Beta totals $70,000.','Repeats table totals and SSO comparison through several analysis and recommendation paragraphs.'),('13','not established in the source pack','Refers to the model input packet inside a finished CFO memo.')]),
 ('pilot-v13','pilot-results-memo',[('C01','fail','fell from 15 to 12 minutes','Reports endpoints but not the required reduction of 3 minutes or 20%.')],[('10','**Conclusion**','Repeats the no-scale recommendation, confounding, quality threshold and unmeasured savings already explained.')]),
 ('pilot-v13','discovery-proposal',[],[('15','**Decision Requested**','Nine labelled sections in a short proposal include repeated opening and closing approval requests; consolidate sections without losing terms.')]),
 ('pilot-v13','change-order',[],[('16','| Estimated effort | 40 hours |','The price table repeats all three quantities immediately after the price paragraph.')]),
 ('pilot-v13','ai-strategy-slides',[('grounding','fail','Only Option A is executable next quarter.','Pending production approval does not establish that every other pilot is impossible throughout next quarter.')],[]),
 ('pilot-v13','handoff-slides',[],[('25','Option C: Reject handoff permanently.','Adds an unsupported permanent-rejection option to create a three-option framework; it contributes no useful decision alternative.')]),
]
manifest=out/'reviewed-output-hashes.json';expected=json.loads(manifest.read_text()) if manifest.exists() else {};hashes={}
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
added=set()
for run,taskid,overrides,editorial in reviews:
 stem=f'deepseek--deepseek-v4.1-flash--{taskid}--default';p=root/'runs'/run/(stem+'.json');record=json.loads(p.read_text());text=p.with_suffix('.md').read_text();assert record['status']=='ok' and record['text']==text
 digest=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=digest
 if expected:assert expected[stem]==digest,'Output changed; a new review is required'
 task=tasks[taskid];os={x[0]:x for x in overrides};grades=[]
 for c in task['checks']:
  o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
 findings=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in editorial];counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
 ready=not counts['fail'] and not counts['review'] and words<=task['maxWords'];added.add(('DeepSeek Flash',taskid,'default'))
 rows.append({'model':'DeepSeek Flash','task':taskid,'condition':'default','path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':digest,'writerInputHash':record['inputHash'],'gradeOrigin':'assistant-v5, targeted default collection','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':[],'editorialFindings':findings,'contentReady':bool(ready),'styleGatePass':not ems,'readyWithoutEdits':bool(ready and not ems and not findings),'originalGenerationCostUsd':record['billing']['totalCost']})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
ungraded=[r for r in base['ungraded'] if (r['model'],r['task'],r['condition']) not in added]
for r in ungraded:
 if r['model']=='DeepSeek Flash' and r['task']=='vendor-decision-memo' and r['condition']=='house':r['status']='generation failed'
assert len(rows)==62 and len(ungraded)==34
method=copy.deepcopy(base['method']);method['revision']='Adds six targeted default DeepSeek drafts. Default coverage is now 8/8; house remains 1/8. Unchanged task set, settings and prompts. No failed house request was retried during targeted default collection.'
method['exceptions']+=['DeepSeek results: should compare under randomized or otherwise defensible allocation is a labelled methodological proposal, unlike a definite will-randomize commitment. It passes grounding.','DeepSeek change-order signature blanks are intentional approval fields, not unfinished drafting placeholders.']
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':ungraded},indent=2)+'\n')
summary=[]
for model in ['Qwen Flash','Kimi K3','Astra','DeepSeek Flash','Opus 5','Fable 5.1']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'contentReady':sum(r['contentReady'] for r in rs),'styleGatePass':sum(r['styleGatePass'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant comparison: completed default samples','',method['status']+'. Model identities visible; no Jev calls. Same corrected eight-brief task set.','', '## Default condition: eight drafts each','', '| Model | Content checks passed | Content ready | Ready without edits | Generation cost |','|---|---:|---:|---:|---:|']
for s in summary:
 if s['condition']=='default' and s['completed']==8:lines.append(f'| {s["model"]} | {s["pass"]}/{s["total"]} | {s["contentReady"]}/8 | {s["readyWithoutEdits"]}/8 | ${s["generationCostUsd"]:.5f} |')
lines+=['','Content ready requires every task-content check, word-limit compliance and no unintended placeholders. Ready without edits also requires the house-style gate and no supported editorial finding. Default outputs did not receive house-style instructions, so those style results measure natural fit rather than explicit compliance. Unresolved checks earn no credit and remain separate in [summary.json](summary.json).','', 'DeepSeek preserves many of the required facts at low generation cost. It still invents prior discussions and team-performance context, omits the requested time reduction calculation, and overstates next-quarter pilot feasibility. Several otherwise correct outputs need substantial repetition or structure edits. Its house condition remains only 1/8 collected; no overall default-versus-house conclusion is justified.','', '## New evidence','']
for r in rows[-6:]:
 lines+=['### '+r['task'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks; {r["words"]}/{r["maxWords"]} words; {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 for label,reason,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {reason}')
 lines.append('')
lines+=['## Collection boundaries','','The runner now accepts a specific brief and condition. Unknown values fail instead of broadening the paid run. The vendor-house request timed out, like the earlier launch-house request. Targeted default collection then completed the untouched briefs without retrying either failed house request.','', 'All grades in [grades.json](grades.json) retain exact output hashes and prior-review provenance. Remaining failed and unattempted cases are ungraded. See the [matched first-email comparison](../assistant-v4/REPORT.md) for the partial Fable and Opus samples.','']
(out/'REPORT.md').write_text('\n'.join(lines))
print(json.dumps([s for s in summary if s['model']=='DeepSeek Flash'],indent=2))
