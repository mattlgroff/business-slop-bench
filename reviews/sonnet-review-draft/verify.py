"""Validate partial review evidence without promoting it to a complete model result."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
rows=json.loads((out/'decisions.json').read_text())['rows']
tasks={t['id']:t for t in json.loads((root/'data/tasks-v2.json').read_text())}
assert len({(r['task'],r['condition']) for r in rows})==len(rows)
for row in rows:
 text=(root/row['path']).read_text();assert hashlib.sha256(text.encode()).hexdigest()==row['outputSha256']
 record=json.loads((root/row['path']).with_suffix('.json').read_text())
 assert record['status']=='ok' and record['finishReason']=='stop' and text==record['text']
 for criterion,verdict,quote,reason in row['content']:
  assert criterion in {c['id'] for c in tasks[row['task']]['checks']}
  assert verdict in ['pass','fail','review'] and quote in text and reason
 for category,quote,reason in row['style']:assert category.isdigit() and quote in text and reason
 print(json.dumps({'task':row['task'],'condition':row['condition'],'words':len(text.split()),'limit':tasks[row['task']]['maxWords']}))
print(f'{len(rows)}/16 primary drafts reviewed; collector status is tracked separately.')
