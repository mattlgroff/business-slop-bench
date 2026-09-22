"""Create a model-name-hidden diagnostic packet, not independent gold labels."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
sha=lambda b:hashlib.sha256(b).hexdigest()
tasks={t['id']:t for t in read(root/'data/tasks-v2.json')}
primary=read(root/'reviews/assistant-v42/grades.json')['rows']
repeats=read(root/'reviews/repeatability-v2/grades.json')['rows']
selection=[
 ('Sol 5.6','vendor-decision-memo','house','grounding'),
 ('Terra','vendor-decision-memo','default','grounding'),
 ('MiMo','vendor-decision-memo','house','grounding'),
 ('Opus 5','handoff-slides','house','negative_parallelism'),
 ('Fable 5','pilot-results-memo','default','grounding'),
 ('Astra','pilot-results-memo','house','C01'),
 ('Luna','pilot-results-memo','house','C01'),
 ('Luna','launch-delay-email','default','grounding'),
 ('Astra repeat','handoff-slides','default','authoring_residue'),
 ('MiMo','pilot-results-memo','house','grounding'),
]
selected=[]
for model,task,condition,target in selection:
 if model=='Astra repeat':
  matches=[r for r in repeats if r['task']==task and r['condition']==condition and r['sample']==2]
  source='reviews/repeatability-v2/grades.json'
 else:
  matches=[r for r in primary if (r['model'],r['task'],r['condition'])==(model,task,condition)]
  source='reviews/assistant-v42/grades.json'
 assert len(matches)==1
 row=matches[0];text=(root/row['path']).read_text();assert sha(text.encode())==row['outputSha256']
 if target=='negative_parallelism':
  criterion='Does the draft avoid empty rhetorical negative parallelism? Necessary factual corrections, scope boundaries, mutually exclusive conditions and cumulative requirements are permitted. A not/rather-than keyword match alone is not a failure.'
  expected='fail' if row['negativeParallelismFindings'] else 'pass'
  rationale='Apply the existing factual-contrast exception. Other content or punctuation issues are outside this target.'
 elif target=='authoring_residue':
  criterion='Does the finished deliverable avoid unintentional authoring residue, such as references to the internal source pack? Intentional signature/date form fields are permitted.'
  expected='fail' if row['placeholderFindings'] else 'pass'
  rationale='The saved review flags an internal source-pack reference in a finished committee deck.'
 else:
  grade=next(g for g in row['grades'] if g['id']==target)
  criterion=grade['criterion'];expected=grade['verdict'];rationale=grade['reason']
 selected.append((sha((row['path']+'::'+target).encode()),row,source,text,criterion,expected,rationale,target))
selected.sort(key=lambda item:item[0])
cases=[];key=[]
for index,(_,row,source,text,criterion,expected,rationale,target) in enumerate(selected,1):
 case_id=f'case-{index:02d}';task=tasks[row['task']]
 cases.append({'id':case_id,'task':task['id'],'brief':task['brief'],'sourcePack':task['facts'],'wordLimit':task['maxWords'],'condition':row['condition'],'criterion':criterion,'deliverable':text})
 key.append({'id':case_id,'model':row['model'],'path':row['path'],'outputSha256':row['outputSha256'],'sourceGrades':source,'criterionId':target,'expected':expected,'rationale':rationale})
packet={'status':'Selected diagnostic examples from already reviewed outputs. Model names withheld, but writing may reveal identity. Not held-out or independently validated gold.','instructions':'Grade only the displayed criterion using the full brief, source and deliverable. Return pass, fail or review with a reason and exact evidence. Review means materially ambiguous, not an automatic failure. Do not open answer-key.json before submitting judgments.','styleGuide':'../../sources/anti-slop-reviewer.md','cases':cases}
assert len(cases)==len({c['id'] for c in cases})==10
assert {k['expected'] for k in key}=={'pass','fail','review'}
# The participant artifact has no model metadata, source-file paths, expected verdicts or old explanations.
assert all(set(c)=={'id','task','brief','sourcePack','wordLimit','condition','criterion','deliverable'} for c in cases)
artifacts={
 'packet.json':packet,
 'answer-key.json':{'labelStatus':'Prior unblinded assistant decisions, open to correction; not gold.','cases':key},
 'response-template.json':[{'id':c['id'],'verdict':None,'reason':'','evidenceQuote':''} for c in cases],
}
for name,value in artifacts.items():
 payload=json.dumps(value,indent=2)+'\n';path=out/name
 if path.exists():assert path.read_text()==payload,'Frozen calibration artifact changed; create a new version'
 else:path.write_text(payload)
print(json.dumps({'cases':len(cases),'proposedLabels':{v:sum(k['expected']==v for k in key) for v in ['pass','fail','review']}}))
