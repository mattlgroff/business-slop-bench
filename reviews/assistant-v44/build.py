"""Correct inconsistent treatment of an explicit signing-authorization request."""
import copy,json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
base=read(root/'reviews/assistant-v43/grades.json');result=copy.deepcopy(base)
c=read(out/'correction.json');row=next(r for r in result['rows'] if r['path']==c['path'])
text=(root/row['path']).read_text();assert hashlib.sha256(text.encode()).hexdigest()==c['outputSha256']==row['outputSha256']
e=c['evidence'];assert text[e['offset']:e['offset']+len(e['quote'])]==e['quote']
g=next(g for g in row['grades'] if g['id']==c['check']);assert g['verdict']==c['previousVerdict']
g.update(verdict=c['verdict'],reason=c['reason'],evidence=e)
row['counts']={v:sum(g['verdict']==v for g in row['grades']) for v in ['pass','fail','review']}
row['contentReady']=all(g['verdict']=='pass' for g in row['grades']) and row['words']<=row['maxWords'] and not row['placeholderFindings']
row['readyWithoutEdits']=bool(row['contentReady'] and row['styleGatePass'] and not row['editorialFindings'])
for old,new in zip(base['rows'],result['rows']):
 if old['path']!=c['path']:assert old==new
 else:
  assert {k:v for k,v in old.items() if k not in ['grades','counts','contentReady','readyWithoutEdits']}=={k:v for k,v in new.items() if k not in ['grades','counts','contentReady','readyWithoutEdits']}
  assert [g for g in old['grades'] if g['id']!='grounding']==[g for g in new['grades'] if g['id']!='grounding']
result['method']['revision']='Corrects Grok house vendor grounding from unresolved to pass under the existing explicit-proposal exception. All other 399 rows remain unchanged. Unblinded assistant review, not independent validation.'
summary=read(root/'reviews/assistant-v43/summary.json')
for s in summary:
 rs=[r for r in result['rows'] if r['model']==s['model'] and r['condition']==s['condition']]
 for v in ['pass','fail','review']:s[v]=sum(r['counts'][v] for r in rs)
 for k in ['contentReady','readyWithoutEdits']:s[k]=sum(r[k] for r in rs)
(out/'grades.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'eligibility-evidence.json').write_bytes((root/'reviews/assistant-v43/eligibility-evidence.json').read_bytes())
s=next(s for s in summary if s['model']=='Grok' and s['condition']=='house')
lines=['# Signing-authorization grading correction','',result['method']['status']+'.','',
'Grok requests: "Approve Alpha and authorize Priya to sign within the $100,000 year-one ceiling." Sol 5.6 requests: "Approve Alpha and authorize Priya, the procurement owner, to proceed with signing." The earlier review passed Sol and left Grok unresolved. Both explicitly propose authorization; neither says that authority already exists. Under the existing proposal exception, Grok passes too.', '',
f'[Grok evidence](../../{c["path"]}:{e["line"]}); [Sol comparison](../../runs/pilot-v23/openai--gpt-5.6-sol--vendor-decision-memo--house.md). Source hashes and the exact quotation were verified.', '',
f'Grok house changes from 50/54 to {s["pass"]}/54 content checks, 4/8 to {s["contentReady"]}/8 content-ready drafts, and 2/8 to {s["readyWithoutEdits"]}/8 ready without edits. All other 399 judgments, costs and eligibility are unchanged. No new model calls were made.', '',
'This does not settle ambiguous phrases such as "for CFO signature" or imply a blanket pass for all suggested signatories. Those require contextual review. The correction applies the already-used explicit-authorization distinction consistently and remains provisional assistant adjudication.', '',
'[Full ranking](RANKING.md), [cumulative grades](grades.json), [summary](summary.json), [recorded correction](correction.json), and [prior full report](../assistant-v43/REPORT.md).', '']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps(s,indent=2))
