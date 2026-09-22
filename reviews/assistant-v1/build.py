"""Materialize the assistant's explicit review decisions and verify evidence locations.
This script does not infer semantic grades or call a model.
"""
import json, hashlib, re
from pathlib import Path
root = Path(__file__).resolve().parents[2]
out = Path(__file__).parent
source = root / 'runs/pilot-v8'
tasks = json.loads((root/'data/tasks.json').read_text())
models = [('Qwen Flash','alibaba--qwen3.8-flash'),('Kimi K3','moonshotai--kimi-k3')]
# Each override is (criterion, verdict, exact passage, review reason).
reviews = {
('Qwen Flash','pilot-client-email','default'): [('grounding','fail','Following recent discussions','Invents prior discussions and an initial risk mitigation strategy absent from the source.')],
('Qwen Flash','pilot-client-email','house'): [('C04','fail','I will submit the access request for security clearance once you reply.','Submitting an access request does not explicitly require granted approval before data access.'),('C06','fail','Please confirm acceptance of the scope and fee.','The requested approval is not explicitly conditional on security clearance.'),('grounding','review',"production rollout and specific dates remain out of scope until we review the pilot's results.",'Unclear whether specific dates means rollout dates or all scheduling; the latter adds an unsupported dependency.')],
('Qwen Flash','launch-delay-email','default'): [('grounding','fail',"The team is moving efficiently. Nia's review is thorough, and the demo path is ready now.",'Invents team performance, review quality and present readiness.')],
('Qwen Flash','launch-delay-email','house'): [('grounding','fail','The team is fully prepared and remains confident in the quality of the release.','Readiness and confidence are asserted without evidence in the source.')],
('Qwen Flash','vendor-decision-memo','default'): [('grounding','fail','the platform cannot reach production within year one under any planned timeline.','An uncommitted SSO date does not prove impossibility throughout year one.')],
('Qwen Flash','vendor-decision-memo','house'): [('C05','fail','Sign with Alpha.','Names Priya in the sender line but does not explicitly preserve CFO approval before signing.')],
('Qwen Flash','pilot-results-memo','default'): [('grounding','fail','the scaling threshold fails on both speed and quality grounds','Failure of a quality threshold does not establish a failure of speed; also attributes a proposed design to Sam without source support.')],
('Qwen Flash','pilot-results-memo','house'): [('C01','fail','from 15 to 12 minutes','Reports endpoints but not the requested reduction of 3 minutes or 20%.'),('C02','fail','The pass rate fell to 89%, below the required 92%.','Omits the required 94% baseline quality rate.'),('grounding','fail','This test will control for ticket mix and randomize allocation','Adds a definite randomization commitment to a source that only authorizes a matched-ticket follow-up.')],
('Qwen Flash','discovery-proposal','default'): [('C05','fail','Sign** this proposal (or reply confirming approval via email).','Offers email confirmation as an alternative to signature, conflicting with the signature prerequisite later in the draft.'),('grounding','fail','or reply confirming approval via email','Adds an unsupported approval alternative.')],
('Qwen Flash','discovery-proposal','house'): [('C06','fail','You approve the engagement by confirming delivery of the three listed artifacts.','Confuses approval to engage with acceptance of completed deliverables.'),('grounding','fail','You approve the engagement by confirming delivery','Changes the meaning and timing of the approval step.')],
('Qwen Flash','change-order','default'): [],
('Qwen Flash','change-order','house'): [],
('Qwen Flash','ai-strategy-slides','default'): [('grounding','review','Option A is ready: approved source documents, defined IT owner, low risk','Low risk and ready go beyond the given facts, but may be read as recommendation rationale rather than a verified status.')],
('Qwen Flash','ai-strategy-slides','house'): [('C01','fail','Slide 4: Evaluation Criteria and Success Threshold','Lists options and a metric but never recommends choosing knowledge search.'),('C05','fail','COO selects the pilot and reports results before expansion.','Source assigns selection to COO and reporting to Dana.'),('grounding','fail','COO selects the pilot and reports results before expansion.','Misassigns reporting responsibility.')],
('Qwen Flash','handoff-slides','default'): [],
('Qwen Flash','handoff-slides','house'): [('grounding','fail','| Runbook approved | Lee | Done |','Source assigns Lee defect fixes, not ownership of the approved runbook.')],
('Kimi K3','pilot-client-email','default'): [],
('Kimi K3','pilot-client-email','house'): [('grounding','fail','begin baseline measurement in week one','Adds a definite delivery sequence not supplied or labelled as a proposed plan.')],
('Kimi K3','launch-delay-email','default'): [('grounding','fail','not a delivery concern','Rules out delivery concerns and asserts team performance without evidence.')],
('Kimi K3','launch-delay-email','house'): [('grounding','fail','Work continues on schedule against the original scope','Invents delivery status and separately promises preparation this week.')],
('Kimi K3','vendor-decision-memo','default'): [('grounding','review','the savings purchase zero usable capability.','The brief blocks production without SSO, but does not establish that every capability is unusable. The sentence may be intended to refer only to production value.')],
('Kimi K3','vendor-decision-memo','house'): [],
('Kimi K3','pilot-results-memo','default'): [],
('Kimi K3','pilot-results-memo','house'): [],
('Kimi K3','discovery-proposal','default'): [],
('Kimi K3','discovery-proposal','house'): [('C06','fail','delivery of the artifacts closes the engagement','A later statement treats delivery itself as closing acceptance rather than preserving sponsor confirmation.'),('grounding','fail','There is no extended acceptance process','Adds an unauthorized acceptance limitation; also claims an attached agreement and scheduling availability not provided.')],
('Kimi K3','change-order','default'): [],
('Kimi K3','change-order','house'): [],
('Kimi K3','ai-strategy-slides','default'): [('grounding','fail','Cannot be the compliant near-term pilot','Pending production authorization does not establish that every pilot is impermissible.')],
('Kimi K3','ai-strategy-slides','house'): [('grounding','fail','Option B cannot enter production this quarter.','No approval date is known. A current authorization gap does not establish impossibility for the whole quarter. This is not a penalty for the brief\'s next/this-quarter ambiguity.')],
('Kimi K3','handoff-slides','default'): [('grounding','fail','incident ownership moves from Lee to Jo','Invents Lee as pre-acceptance incident owner. Source only assigns Lee defect fixes.')],
('Kimi K3','handoff-slides','house'): [('grounding','fail','Incident ownership transfers from Lee to Jo','Invents Lee as pre-acceptance incident owner. Source only assigns Lee defect fixes.')],
}
# Editorial findings are distinct passages, not one point per overlapping smell category.
style = {
('Qwen Flash','pilot-client-email','default'): [('16','This pilot offers a low-risk opportunity to validate efficiency gains before committing to broader implementation.','Generic reassurance repeats the bounded-pilot rationale without adding decision information.')],
('Qwen Flash','vendor-decision-memo','default'): [('14','✅','Emojis used as professional decision-table structural markers.')],
('Qwen Flash','vendor-decision-memo','house'): [('16','Beta offers a $70,000 first-year cost','Repeats both vendor totals immediately after a table already displaying them.')],
('Qwen Flash','pilot-results-memo','default'): [('10','### Summary','Final summary repeats the recommendation, caveat, quality gate and savings status already stated.')],
('Qwen Flash','discovery-proposal','default'): [('20','designed to de-risk a larger investment by separating discovery from delivery.','Generic consulting close repeats the discovery-only scope.')],
('Qwen Flash','change-order','default'): [('13','[Insert Date]','Unfilled template placeholders in a requested finished proposal; [Project Lead] is also unfilled.')],
('Qwen Flash','handoff-slides','default'): [('29','The gap is structural: the handoff boundary creates a zone of unowned work.','Abstract restatement adds no information beyond the explicit unassigned rehearsal organizer.')],
('Kimi K3','pilot-client-email','house'): [('16','Over the six weeks we will establish a handling-time baseline','Overlong email repeats the pilot rationale and approval request across several paragraphs; exceeds the explicit limit.')],
('Kimi K3','launch-delay-email','default'): [('2','A quick update on where we stand with the launch.','Throat clearing before the actual launch update.')],
('Kimi K3','launch-delay-email','house'): [('10','Action needed from you:','Repeats the staging-demo decision already requested earlier in the email.')],
('Kimi K3','vendor-decision-memo','default'): [('16','Alpha totals $92,000; Beta totals $70,000.','Repeats the table values, then repeats Alpha cost and headroom again in the recommendation.')],
('Kimi K3','vendor-decision-memo','house'): [('10','## Requested action','Third request for Alpha approval after Recommendation and Decision sections.')],
('Kimi K3','pilot-results-memo','house'): [('29','a clear bar it did not clear','Manufactured phrasing repeats the already explicit 89% versus 92% result.')],
('Kimi K3','discovery-proposal','house'): [('10','Discovery ends with delivery of the process map, backlog, and recommendation','Repeats the deliverables and payment sequence after describing both in prior sections.')],
}
rows=[]
def anchor(text,quote):
 assert quote in text, quote
 start=text.index(quote)
 return {'quote':quote,'offset':start,'line':text[:start].count('\n')+1}
for label,slug in models:
 for task in tasks:
  for condition in ['default','house']:
   key=(label,task['id'],condition); assert key in reviews
   stem=f'{slug}--{task["id"]}--{condition}'
   text=(source/(stem+'.md')).read_text();record=json.loads((source/(stem+'.json')).read_text())
   assert text == record['text'], 'Markdown and saved generation differ'
   overrides={g[0]:g for g in reviews[key]}; assert set(overrides)<=set(c['id'] for c in task['checks'])
   grades=[]
   for check in task['checks']:
    g=overrides.get(check['id'])
    grades.append({'id':check['id'],'criterion':check['statement'],'verdict':g[1] if g else 'pass','reason':g[3] if g else 'Criterion satisfied on full-draft review against the supplied source pack.','evidence':anchor(text,g[2]) if g else None})
   editorial=[{'category':cat,'reason':reason,'evidence':anchor(text,quote)} for cat,quote,reason in style.get(key,[])]
   words=len(text.split()); ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   placeholders=[anchor(text,q) for q in ['[Insert Date]','[Project Lead]'] if q in text]
   counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']}
   content_ready=counts['fail']==0 and counts['review']==0 and words<=task['maxWords'] and not placeholders
   rows.append({'model':label,'task':task['id'],'condition':condition,'path':str((source/(stem+'.md')).relative_to(root)),'outputSha256':hashlib.sha256(text.encode()).hexdigest(),'writerInputHash':record['inputHash'],'grades':grades,'counts':counts,'words':words,'maxWords':task['maxWords'],'emDashes':ems,'negativeParallelismFindings':[],'placeholderFindings':placeholders,'editorialFindings':editorial,'contentReady':content_ready,'styleGatePass':not ems,'readyWithoutEdits':content_ready and not ems and not editorial,'originalGenerationCostUsd':record['billing']['totalCost']})
meta={'reviewer':'Assistant in this thread; model identities visible','status':'Provisional assistant-authored grades, not human gold or independent benchmark validation','scoring':'Existing per-task content checks, with pass/fail/review kept separate. No credit for review. Every task check has equal weight in the displayed content-check fraction; checks overlap and are not independent. Word limit, placeholders, style gate and editorial polish remain separate.','styleScope':'Full frozen anti-slop catalog reviewed; supported editorial findings recorded, not one point per category. Necessary factual contrasts are allowed.','readiness':'Content ready requires all content checks pass, word limit compliance and no placeholders. Ready without edits also requires the style gate and no recorded editorial findings.','exceptions':['Do not score this/next-quarter inconsistency introduced by the AI strategy brief itself.','Handoff default Qwen: No further criteria exist is accepted as referring to the two supplied acceptance criteria, not unknown external policy. This revises the earlier tentative editorial concern.','Matched-ticket randomization is treated as a new delivery commitment when asserted as what the test will do, rather than labelled as a proposed design.','C01 for results requires the stated delta (3 minutes or 20%), not just endpoints from which a reader could calculate it.'],'tasksSha256':hashlib.sha256((root/'data/tasks.json').read_bytes()).hexdigest(),'lensSha256':hashlib.sha256((root/'sources/anti-slop-reviewer.md').read_bytes()).hexdigest()}
(out/'grades.json').write_text(json.dumps({'method':meta,'rows':rows},indent=2)+'\n')
summary=[]
for label,_ in models:
 for cond in ['default','house']:
  r=[x for x in rows if x['model']==label and x['condition']==cond]
  c={v:sum(x['counts'][v] for x in r) for v in ['pass','fail','review']}
  summary.append({'model':label,'condition':cond,**c,'total':sum(c.values()),'contentReady':sum(x['contentReady'] for x in r),'readyWithoutEdits':sum(x['readyWithoutEdits'] for x in r),'styleGatePass':sum(x['styleGatePass'] for x in r),'editorialFindings':sum(len(x['editorialFindings']) for x in r),'wordLimitFailures':sum(x['words']>x['maxWords'] for x in r),'generationCost':sum(x['originalGenerationCostUsd'] for x in r)})
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Assistant grading: Qwen Flash and Kimi K3','',meta['status']+'. Model identities were visible. Same eight briefs, default and house-style conditions, one output per cell. No Jev calls were used for these decisions.','', '## Summary','', 'Content checks are the existing task-specific rubric, not an invented overall quality score. Unresolved checks receive no credit and are reported separately. A high check fraction can coexist with a critical failure. Counts of overlapping checks are not independent observations.','', '| Model | Condition | Content checks passed | Failed | Unresolved | Content ready | Style gate pass | Ready without edits |','|---|---|---:|---:|---:|---:|---:|---:|']
for s in summary: lines.append(f'| {s["model"]} | {s["condition"]} | {s["pass"]}/{s["total"]} | {s["fail"]} | {s["review"]} | {s["contentReady"]}/8 | {s["styleGatePass"]}/8 | {s["readyWithoutEdits"]}/8 |')
lines+=['','Content ready requires all content checks to pass, within the word limit, with no placeholders. Ready without edits also requires the house style gate and no recorded editorial findings. Default style scores describe house-style fit without having supplied the house-style instructions. They are not instruction-following failures.','', '## Per-draft results','', '| Model | Brief | Condition | Content checks | Main reason to edit |','|---|---|---|---:|---|']
for r in rows:
 reasons=[g['reason'] for g in r['grades'] if g['verdict']!='pass']
 if r['words']>r['maxWords']:reasons.append(f'{r["words"]} words exceeds {r["maxWords"]}.')
 if r['placeholderFindings']:reasons.append('Unfilled placeholders.')
 if not reasons and r['editorialFindings']:reasons.append(r['editorialFindings'][0]['reason'])
 if not reasons and r['emDashes']:reasons.append('Em dash style violations.')
 lines.append(f'| {r["model"]} | [{r["task"]}](../../{r["path"]}) | {r["condition"]} | {r["counts"]["pass"]}/{len(r["grades"])} | {reasons[0] if reasons else "No supported edits found in this review."} |')
lines+=['','## Evidence and repairs','']
for r in rows:
 findings=[(g['id']+' '+g['verdict'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+ [('Style '+g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]
 if not findings:continue
 lines+=['### '+r['model']+' / '+r['task']+' / '+r['condition'],'']
 for label,reason,e in findings:lines.append(f'- **{label}:** [{e["quote"]}](../../{r["path"]}:{e["line"]}). {reason}')
 lines.append('')
lines+=['## Limits and preserved decisions','']+[ '- '+x for x in meta['exceptions']]+['','All quoted findings are checked against the saved text and carry line/offset anchors in [grades.json](grades.json). Missing content is assessed against the full draft; an excerpt is context, not proof of absence. No statistical model ranking is justified by eight briefs and a single unblinded assistant reviewer.','']
(out/'REPORT.md').write_text('\n'.join(lines))
print(json.dumps(summary,indent=2))
