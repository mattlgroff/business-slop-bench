"""Save explicit assistant grades for Astra and preserve prior reviewed outputs.
No inference calls. Passing content grades below are the assistant's reviewed decisions.
"""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
base=json.loads((root/'reviews/assistant-v2/grades.json').read_text())
tasks=json.loads((root/'data/tasks-v2.json').read_text())
rows=copy.deepcopy(base['rows'])
for r in rows:
 text=(root/r['path']).read_text()
 assert hashlib.sha256(text.encode()).hexdigest()==r['outputSha256']
# All sixteen complete Astra drafts were read against every existing task check.
# This is a frozen assistant assessment, not an automatic all-pass rule for new text.
expected_hashes={}
manifest_path=out/'reviewed-output-hashes.json'
if manifest_path.exists():expected_hashes=json.loads(manifest_path.read_text())
style={
 ('pilot-client-email','default'):('16','Your approval would establish agreement on the scope and investment while keeping data access contingent on the required clearance.','Repeats the immediately preceding conditional approval request and previously stated security prerequisite.'),
 ('pilot-client-email','house'):('16','The pilot offers a bounded way to assess invoice handling before considering a production commitment.','Repeats the defined assessment period/cost and production exclusion without adding information.'),
 ('handoff-slides','default'):('13','No further action identified in the source pack','References the model input packet inside a finished steering-committee deliverable. State that the runbook criterion is met.'),
}
new_hashes={}
for task in tasks:
 for cond in ['default','house']:
  stem=f'openai--gpt-6-astra--{task["id"]}--{cond}';path=root/'runs/pilot-v10'/f'{stem}.json'
  record=json.loads(path.read_text());assert record['status']=='ok'
  text=path.with_suffix('.md').read_text();assert text==record['text']
  digest=hashlib.sha256(text.encode()).hexdigest();new_hashes[stem]=digest
  if expected_hashes:assert expected_hashes[stem]==digest,'Changed output requires a new review'
  findings=[]
  if (task['id'],cond) in style:
   cat,q,why=style[(task['id'],cond)];assert q in text;i=text.index(q)
   findings=[{'category':cat,'reason':why,'evidence':{'quote':q,'offset':i,'line':text[:i].count('\n')+1}}]
  grades=[{'id':c['id'],'criterion':c['statement'],'verdict':'pass','reason':'Criterion satisfied on full-draft review against the supplied source pack.','evidence':None} for c in task['checks']]
  words=len(text.split());ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
  ready=words<=task['maxWords']
  rows.append({'model':'Astra','task':task['id'],'condition':cond,'path':str(path.with_suffix('.md').relative_to(root)),'outputSha256':digest,'writerInputHash':record['inputHash'],'gradeOrigin':'assistant-v3: direct review of saved Astra output','grades':grades,'counts':{'pass':len(grades),'fail':0,'review':0},'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':[],'editorialFindings':findings,'contentReady':ready,'styleGatePass':not ems,'readyWithoutEdits':ready and not ems and not findings,'originalGenerationCostUsd':record['billing']['totalCost']})
assert len(new_hashes)==16
if not expected_hashes:manifest_path.write_text(json.dumps(new_hashes,indent=2)+'\n')
method=copy.deepcopy(base['method']);method['revision']='Adds 16 Astra drafts under the same corrected task set. Prior grades carried only across unchanged output hashes.'
method['exceptions']+=['Astra launch default: personal confidence is an opinion invited by the brief. It does not invent objective claims of team performance or review quality, unlike earlier failed reassurance passages.','Astra change-order default: signature/date blanks are intentional approval form fields, not leaked drafting placeholders.','Astra content checks all pass in this one observed sample. That is not proof of general accuracy, a complete writing-quality score, or an independently validated result.']
(out/'grades.json').write_text(json.dumps({'method':method,'rows':rows,'ungraded':base['ungraded']},indent=2)+'\n')
summary=[]
for model in ['Qwen Flash','Kimi K3','Astra','Opus 5']:
 for cond in ['default','house']:
  rs=[r for r in rows if r['model']==model and r['condition']==cond];counts={v:sum(r['counts'][v] for r in rs) for v in ['pass','fail','review']}
  summary.append({'model':model,'condition':cond,'completed':len(rs),'expected':8,**counts,'total':sum(counts.values()),'contentReady':sum(r['contentReady'] for r in rs),'styleGatePass':sum(r['styleGatePass'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'wordLimitFailures':sum(r['words']>r['maxWords'] for r in rs),'generationCostUsd':sum(r['originalGenerationCostUsd'] for r in rs)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant comparison: Astra, Kimi and Qwen','',method['status']+'. Same eight briefs and both conditions. One generation per cell. Model identities visible; no Jev grades used.','', '## Complete model samples','', '| Model | Condition | Content checks | Content ready | Style gate pass | Ready without edits | Generation cost |','|---|---|---:|---:|---:|---:|---:|']
for s in summary:
 if s['completed']==8:lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["contentReady"]}/8 | {s["styleGatePass"]}/8 | {s["readyWithoutEdits"]}/8 | ${s["generationCostUsd"]:.5f} |')
lines+=['','Content checks include factual support, numbers, conditions, decision requests and ownership. They are overlapping rubric items, not independent trials. Ready without edits also requires the word limit, no unintended placeholders, the style gate and no supported editorial finding. Unresolved checks earn no point; full pass/fail/review counts are in [summary.json](summary.json).','', 'Astra preserved the required content in all sixteen observed drafts. Its house-style sample needed less editing than the other complete samples. Its default outputs still used em dashes, so a content pass is not a style pass. Kimi remains the cheaper option with several usable drafts, but more material errors. This limited unblinded sample does not identify a universal best model.','', '## Astra evidence and remaining edits','']
for r in rows:
 if r['model']!='Astra':continue
 lines+=[f'### {r["task"]} / {r["condition"]}','',f'[Draft](../../{r["path"]}): {r["counts"]["pass"]}/{len(r["grades"])} content checks, {r["words"]}/{r["maxWords"]} words, {len(r["emDashes"])} em dashes.','']
 for f in r['editorialFindings']:
  e=f['evidence'];lines.append(f'- **Style {f["category"]}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {f["reason"]}')
 if not r['editorialFindings']:lines.append('No additional supported editorial finding in this review.')
 lines.append('')
lines+=['## Interpretation boundaries','']+['- '+x for x in method['exceptions']]+['','Opus still has only three graded emails; all exceed the word limit. Do not compare that partial sample as if it covered all eight briefs. Its incomplete collection is preserved in [previous report](../assistant-v2/REPORT.md).','', 'Cost is the original successful generation charge for each represented draft, including reused originals once in this comparison. It excludes failed attempts, judge diagnostics, and earlier superseded slide drafts. The shared budget ledger remains authoritative for the spending ceiling.','']
(out/'REPORT.md').write_text('\n'.join(lines))
print(json.dumps(summary,indent=2))
