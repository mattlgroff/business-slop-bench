"""Append explicit assistant review of the 16 frozen Luna drafts. No judge calls."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v5/grades.json').read_text());rows=copy.deepcopy(base['rows'])
tasks=json.loads((root/'data/tasks-v2.json').read_text())
for r in rows:assert hashlib.sha256((root/r['path']).read_bytes()).hexdigest()==r['outputSha256']
content={
 ('launch-delay-email','default'):[('grounding','review','The team remains focused on completing the required security work and moving forward responsibly.','The source does not establish current team focus or activity. This may be ordinary reassurance rather than a material factual assertion, so it remains unresolved.')],
 ('launch-delay-email','house'):[('grounding','review','The team remains focused on completing the required work','The source does not establish current team focus or activity; ordinary reassurance is a plausible reading, so this is unresolved.')],
 ('pilot-results-memo','default'):[('C01','fail','15 minutes at baseline','Gives the 15- and 12-minute endpoints but omits the required 3-minute or 20% reduction.')],
 ('ai-strategy-slides','house'):[('C05','fail','## Slide 4: Approval requested','Preserves Dana ownership and reporting but never names the COO as the pilot selection authority.')],
 ('handoff-slides','house'):[('grounding','review','Keep the service with Engineering pending acceptance.','May expand Engineering ownership beyond the stated defect-fix role, or may be shorthand for retaining that role. Broader service ownership is not supplied.')],
}
style={
 ('pilot-client-email','default'):[('21','The client’s target','Refers to the client in the third person while addressing that client directly. Your target would fit this email audience.')],
 ('pilot-client-email','house'):[('21','the client’s hope','Third-person client reference is unnatural in an email directly to that client; use your target.')],
 ('launch-delay-email','default'):[('20','The October 8 production launch is no longer the current position.','Current position obscures the concrete message that production cannot launch on October 8.')],
 ('vendor-decision-memo','default'):[('13','the only vendor in the source pack','Input-packet reference does not belong in the finished CFO memo.')],
 ('pilot-results-memo','house'):[('10','| Finding | Decision relevance |','The table repeats the findings already stated in the preceding paragraphs. Consolidate the presentation while retaining the baseline quality figure and numerical reduction.')],
 ('ai-strategy-slides','default'):[('13','Q[next]','Unresolved authoring notation in a finished slide title; the brief already supplies next quarter.')],
}
manifest=out/'reviewed-output-hashes.json';expected=json.loads(manifest.read_text()) if manifest.exists() else {};hashes={}
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for task in tasks:
 for cond in ['default','house']:
  key=(task['id'],cond);stem=f'openai--gpt-5.6-luna--{task["id"]}--{cond}';p=root/'runs/pilot-v13'/(stem+'.json');record=json.loads(p.read_text());text=p.with_suffix('.md').read_text();assert record['status']=='ok' and record['text']==text
  h=hashlib.sha256(text.encode()).hexdigest();hashes[stem]=h
  if expected:assert expected[stem]==h,'Changed output requires new review'
  os={x[0]:x for x in content.get(key,[])};grades=[]
  for c in task['checks']:
   o=os.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,o[2]) if o else None})
  es=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in style.get(key,[])]
  placeholders=[anchor(text,'Q[next]')] if 'Q[next]' in text else []
  counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']};words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
  ready=not counts['fail'] and not counts['review'] and words<=task['maxWords'] and not placeholders
  rows.append({'model':'Luna','task':task['id'],'condition':cond,'path':str(p.with_suffix('.md').relative_to(root)),'outputSha256':h,'writerInputHash':record['inputHash'],'gradeOrigin':'assistant-v6, direct Luna review','grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':placeholders,'editorialFindings':es,'contentReady':bool(ready),'styleGatePass':not ems,'readyWithoutEdits':bool(ready and not ems and not es),'originalGenerationCostUsd':record['billing']['totalCost']})
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
assert len(rows)==78
method=copy.deepcopy(base['method']);method['revision']='Adds all 16 Luna drafts under the same corrected task set, low reasoning and output cap. Model identities remain visible.'
method['exceptions']+=['Luna team-focus wording is unresolved, not a confirmed invention. It is less concrete than claims of proven performance or readiness, but broader than the author expressing personal confidence.','Luna handoff: keep the service with Engineering is unresolved because it could refer to the stated defect-fix responsibility or imply broader unassigned ownership.','Third-person client phrasing and duplicated presentation are editorial judgments, not factual failures.','Luna change-order signature fields are intentional form fields. Q[next] in a slide title is an unintended authoring placeholder.']
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':base['ungraded']},indent=2)+'\n')
summary=[]
for model in ['Qwen Flash','Kimi K3','Astra','Luna','DeepSeek Flash','Opus 5','Fable 5.1']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];c={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**c,'total':sum(c.values()),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant comparison with Luna','',method['status']+'. Same corrected briefs, no tools or revisions, one generation per condition. Model identities visible. No Jev judgments.','', '## Completed eight-draft conditions','', '| Model | Condition | Content checks passed | Failed | Unresolved | Content ready | Ready without edits | Generation cost |','|---|---|---:|---:|---:|---:|---:|---:|']
for s in summary:
 if s['completed']==8:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["contentReady"]}/8 | {s["readyWithoutEdits"]}/8 | ${s["generationCostUsd"]:.5f} |')
lines+=['','Unresolved checks earn no point. Content ready requires all task checks, the word limit and no unintended placeholders. Ready without edits additionally requires the style gate and no supported editorial findings. Default style results measure house-style fit without supplying the house instructions. These overlapping checks are not independent trials.','', 'Luna produced this complete set for $0.01141. It preserves most factual and commercial constraints, but misses a required calculation in the default readout and the COO decision owner in the house strategy slides. Three grounding judgments remain unresolved; the default slides also contain a Q[next] placeholder. This is a useful low-cost comparison, not proof of a general model ranking.','', '## Luna evidence','']
for r in rows[-16:]:
 lines+=['### '+r['task']+' / '+r['condition'],'',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 fs=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 for label,why,e in fs:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {why}')
 if not fs:lines.append('No supported content or editorial finding in this review; any em dash violations remain separate.')
 lines.append('')
lines+=['## Adjudication boundaries','']+['- '+x for x in method['exceptions'][-4:]]+['','All decisions and exact hashes are in [grades.json](grades.json). The partial Opus, Fable and DeepSeek house sets remain ungraded where outputs are missing. Successful generation prices here include each represented draft once and exclude failures and judge diagnostics.','']
(out/'REPORT.md').write_text('\n'.join(lines))
print(json.dumps([s for s in summary if s['model']=='Luna'],indent=2))
