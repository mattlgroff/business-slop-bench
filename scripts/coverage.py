"""Read-only coverage accounting for the current task set, without quality inference."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
models=json.loads((root/'data/models.json').read_text())
tasks=json.loads((root/'data/tasks-v2.json').read_text())
task_hash=hashlib.sha256(json.dumps(tasks,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
runs=[]
for name in ['pilot-v10','pilot-v11']:
 p=root/'runs'/name
 if (p/'protocol.json').exists():
  protocol=json.loads((p/'protocol.json').read_text())
  assert protocol['tasksHash']==task_hash,'Different task versions must not be combined'
  runs.append(p)
rows=[]
for model in models:
 successful=failed=0; errors=[]
 for task in tasks:
  for condition in ['default','house']:
   stem=f'{model["id"].replace("/","--")}--{task["id"]}--{condition}'
   records=[json.loads((r/(stem+'.json')).read_text()) for r in runs if (r/(stem+'.json')).exists()]
   good=[r for r in records if r['status']=='ok']
   if good:
    assert len({hashlib.sha256(r['text'].encode()).hexdigest() for r in good})==1,'Multiple samples require an explicit selection policy'
    successful+=1
   elif records:
    failed+=1;errors.append(str(records[-1].get('error',{}).get('statusCode','unknown')))
 rows.append({'model':model['id'],'generated':successful,'failed':failed,'unattempted':16-successful-failed,'errorCodes':sorted(set(errors))})
print(json.dumps({'taskFile':'data/tasks-v2.json','expectedModels':len(models),'expectedDrafts':len(models)*16,'models':rows},indent=2))
