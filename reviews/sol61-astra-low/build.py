"""Compare every fresh low-reasoning Astra draft with the retained Sol 6.1 primary."""
import copy,hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
sha=lambda text:hashlib.sha256(text.encode()).hexdigest()
plan=read(out/'plan.json');tasks={t['id']:t for t in read(root/'data/tasks-v2.json')}
base=read(root/'reviews/assistant-v47/grades.json');sol=[r for r in base['rows'] if r['model']=='Sol 6.1']
decisions=read(out/'decisions.json');assert len(decisions)==len(plan['cases'])==len(sol)==16
assert {(d['task'],d['condition']) for d in decisions}=={(d['task'],d['condition']) for d in plan['cases']}
rows=copy.deepcopy(sol);verification=[];seen=set();hashes={}
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for d in decisions:
 t=tasks[d['task']];stem=f"openai--gpt-6-astra--{t['id']}--{d['condition']}--sample-3";p=root/'runs/pilot-v27'/f'{stem}.json';record=read(p);text=p.with_suffix('.md').read_text()
 s=next(r for r in sol if r['task']==t['id'] and r['condition']==d['condition']);sr=read((root/s['path']).with_suffix('.json'))
 assert record['status']=='ok' and record['finishReason']=='stop' and record['text']==text and not record['warnings'] and not record.get('importedFrom')
 assert record['input']==sr['input'] and record['inputHash']==sr['inputHash'] and record['input']['reasoning']=='low'
 assert 'maxOutputTokens' not in record['input']
 assert record['model']==record['response']['modelId']==record['providerMetadata']['gateway']['routing']['canonicalSlug']=='openai/gpt-6-astra'
 for rr in [record,sr]:
  gen=rr['providerMetadata']['gateway']['generationId'];assert gen not in seen;seen.add(gen)
  assert rr['providerMetadata']['gateway']['routing']['totalProviderAttemptCount']==1
 verification.append({'task':t['id'],'condition':d['condition'],'identicalInputs':True,'writerInputHash':record['inputHash']})
 overrides={x[0]:x for x in d['content']};assert set(overrides)<=set(c['id'] for c in t['checks'])
 grades=[]
 for c in t['checks']:
  o=overrides.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':o[1] if o else 'pass','reason':o[3] if o else 'Criterion satisfied on full-draft review against the frozen source facts.','evidence':anchor(text,o[2]) if o else None})
 counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']}
 styles=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in d['style']]
 residue=[{**anchor(text,q),'reason':why} for q,why in d['placeholders']]
 ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
 ready=not counts['fail'] and not counts['review'] and len(text.split())<=t['maxWords'] and not residue
 row=copy.deepcopy(s);row.update(model='Astra fresh sample 3',path=str(p.with_suffix('.md').relative_to(root)),outputSha256=sha(text),writerInputHash=record['inputHash'],gradeOrigin='sol61-astra-low, direct unblinded assistant review',grades=grades,counts=counts,words=len(text.split()),emDashes=ems,negativeParallelismFindings=[],placeholderFindings=residue,editorialFindings=styles,contentReady=ready,styleGatePass=not ems,readyWithoutEdits=bool(ready and not ems and not styles),originalGenerationCostUsd=record['billing']['totalCost'])
 rows.append(row);hashes[row['path']]=sha(text)
manifest=out/'output-hashes.json'
if manifest.exists():assert read(manifest)==hashes
else:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
summary=[]
for m in ['Sol 6.1','Astra fresh sample 3']:
 for c in ['default','house']:
  rs=[r for r in rows if r['model']==m and r['condition']==c];assert len(rs)==8
  summary.append(dict(model=m,condition=c,completed=8,checks=sum(r['counts']['pass'] for r in rs),total=54,contentReady=sum(r['contentReady'] for r in rs),readyWithoutEdits=sum(r['readyWithoutEdits'] for r in rs),emDashes=sum(len(r['emDashes']) for r in rs),costUsd=sum(r['originalGenerationCostUsd'] for r in rs)))
(out/'grades.json').write_text(json.dumps({'method':'Same-day low-reasoning comparison; unblinded provisional assistant judgments; no independent human gold. Historical Astra samples remain separate.','rows':rows},indent=2)+'\n')
(out/'verification.json').write_text(json.dumps({'distinctGenerations':len(seen),'cases':verification},indent=2)+'\n')
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# GPT-6.1 Sol versus fresh Astra, low reasoning','','September 29, 2026. Every model writes all eight frozen briefs once in both conditions. Both request low reasoning. All sixteen paired inputs match exactly. No output-token cap, generation deadline, retry or replacement of historical primary results. All 32 generations completed with normal stops and distinct generation IDs.','','| Model | Condition | Checks | Content ready | Ready without edits | Em dashes | Reported charge |','|---|---|---:|---:|---:|---:|---:|']
for s in summary:lines.append(f"| {s['model']} | {s['condition']} | {s['checks']}/54 | {s['contentReady']}/8 | {s['readyWithoutEdits']}/8 | {s['emDashes']} | ${s['costUsd']:.6f} |")
lines+=['','Content ready requires all content checks, the word limit and no authoring residue. Ready without edits additionally requires no style-gate violations and no supported editorial findings. Every draft meets the word limit. The Sol plain launch reassurance remains unresolved, not a confirmed fabrication. Astra states personal confidence in its team rather than asserting an unsupplied operational status; the brief expressly asks for confidence.','','House Astra needs two editorial edits: generic progress commentary in the launch email and a repeated savings caution in the pilot readout. House Sol needs three repetition edits and removal of a source-pack reference in the handoff deck. Default Astra has source-pack residue in its vendor memo and handoff deck. Necessary factual contrasts and intentional signature fields are allowed.','','These are provisional, unblinded assistant judgments on one fixed panel, not independent evidence of a population win rate. The original Astra house result was 8/8 ready without edits; its prior full repeat was 6/8. This third sample is reported separately, without replacing either.','','## Astra findings','']
for r in rows[16:]:
 lines+=['### '+r['task']+' / '+r['condition'],'',f"[Draft](../../{r['path']}): {r['counts']['pass']}/{len(r['grades'])} content checks; {r['words']}/{r['maxWords']} words; {len(r['emDashes'])} em dashes.",'']
 for f in r['editorialFindings']:lines.append(f"- Style {f['category']}: {f['evidence']['quote']} {f['reason']}")
 for f in r['placeholderFindings']:lines.append(f"- Authoring residue: {f['quote']} {f['reason']}")
 if not r['editorialFindings'] and not r['placeholderFindings']:lines.append('No supported judgment findings. Mechanical punctuation violations, if any, remain separate.')
 lines+=['']
lines+=['[Sol findings](../assistant-v47/REPORT.md), [all comparison grades](grades.json), [paired-input verification](verification.json), [frozen plan](plan.json).','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps(summary,indent=2))
