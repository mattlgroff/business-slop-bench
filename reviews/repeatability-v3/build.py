"""Materialize the frozen full-panel repeat with explicit assistant judgments."""
import copy, hashlib, json, re
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
sha=lambda text:hashlib.sha256(text.encode()).hexdigest()
plan=read(out/'plan.json');base_path=root/plan['baseGrades'];base_text=base_path.read_text();base=read(base_path)
tasks={t['id']:t for t in read(root/'data/tasks-v2.json')}
assert sha((root/'data/tasks-v2.json').read_text())==base['method']['tasksSha256']
decisions=read(out/'decisions.json');ds={(r['task'],r['condition']):r for r in decisions}
assert len(ds)==len(decisions)==len(plan['cases'])==16
assert set(ds)=={(c['task'],c['condition']) for c in plan['cases']}
manifest=out/'output-hashes.json';expected=read(manifest) if manifest.exists() else {};hashes={};rows=[];ids=[]
def anchor(text,q):
 assert q in text,q
 i=text.index(q);return {'quote':q,'offset':i,'line':text[:i].count('\n')+1}
for case in plan['cases']:
 task=tasks[case['task']];old_md=Path(case['baseline']);old_record=read((root/old_md).with_suffix('.json'))
 baseline=next(r for r in base['rows'] if r['path']==str(old_md))
 new_md=Path('runs')/plan['run']/f"openai--gpt-5.6-luna--{case['task']}--{case['condition']}--sample-{case['sampleId']}.md"
 protocols=[read(root/p.parent/'protocol.json') for p in [old_md,new_md]]
 for key in ['sourceHash','tasksHash']:assert protocols[0][key]==protocols[1][key]
 for p in protocols:
  assert p['limits']['maxOutputTokens'] is None and p['limits']['timeoutMs'] is None
  assert p['writerGatewayPolicy']['zeroDataRetentionDefault'] and plan['model'] not in p['writerGatewayPolicy']['nonZdrModels']
 for sample,md in [(1,old_md),(2,new_md)]:
  d=read((root/md).with_suffix('.json'));text=(root/md).read_text()
  assert text==d['text'] and d['status']=='ok' and d['finishReason']=='stop' and not d['warnings']
  assert d['input']==old_record['input'] and d['inputHash']==case['writerInputHash']
  assert 'maxOutputTokens' not in d['input']
  assert d['model']==d['response']['modelId']==d['providerMetadata']['gateway']['routing']['canonicalSlug']==plan['model']
  generation=d['providerMetadata']['gateway'].get('generationId') or d['response']['id'];assert generation;ids.append(generation)
  hashes[str(md)]=sha(text)
  if expected:assert expected[str(md)]==sha(text)
  row=copy.deepcopy(baseline)
  if sample==1:assert sha(text)==case['baselineOutputSha256']==baseline['outputSha256']
  else:
   assert d['id'].endswith(f"--sample-{case['sampleId']}") and not d.get('importedFrom')
   decision=ds[case['task'],case['condition']];overrides={x[0]:x for x in decision['content']};assert set(overrides)<=set(c['id'] for c in task['checks'])
   grades=[]
   for c in task['checks']:
    override=overrides.get(c['id']);grades.append({'id':c['id'],'criterion':c['statement'],'verdict':override[1] if override else 'pass','reason':override[3] if override else 'Criterion satisfied on complete-draft review against the frozen source.','evidence':anchor(text,override[2]) if override else None})
   counts={v:sum(g['verdict']==v for g in grades) for v in ['pass','fail','review']}
   editorial=[{'category':cat,'reason':why,'evidence':anchor(text,q)} for cat,q,why in decision['style']]
   placeholders=[{**anchor(text,q),'reason':why} for q,why in decision.get('placeholders',[])]
   negatives=[{**anchor(text,q),'reason':why} for q,why in decision.get('negative',[])]
   ems=[{'offset':m.start(),'line':text[:m.start()].count('\n')+1} for m in re.finditer(chr(8212),text)]
   ready=not counts['fail'] and not counts['review'] and len(text.split())<=task['maxWords'] and not placeholders
   row.update(path=str(md),outputSha256=sha(text),writerInputHash=d['inputHash'],gradeOrigin='repeatability-v3, direct unblinded assistant review',grades=grades,counts=counts,words=len(text.split()),emDashes=ems,negativeParallelismFindings=negatives,placeholderFindings=placeholders,editorialFindings=editorial,contentReady=bool(ready),styleGatePass=not ems and not negatives,readyWithoutEdits=bool(ready and not ems and not negatives and not editorial),originalGenerationCostUsd=d['billing']['totalCost'])
  row.update(round=sample,sampleId=1 if sample==1 else case['sampleId'],generationId=generation);rows.append(row)
assert len(rows)==len(set(ids))==32
assert base_path.read_text()==base_text
if not expected:manifest.write_text(json.dumps(hashes,indent=2)+'\n')
summary=[]
for condition in ['default','house']:
 for sample in [1,2]:
  rs=[r for r in rows if r['condition']==condition and r['round']==sample];assert len(rs)==8
  summary.append({'condition':condition,'round':sample,'contentPasses':sum(r['counts']['pass'] for r in rs),'contentTotal':sum(len(r['grades']) for r in rs),'contentReady':sum(r['contentReady'] for r in rs),'readyWithoutEdits':sum(r['readyWithoutEdits'] for r in rs),'emDashes':sum(len(r['emDashes']) for r in rs)})
cost=sum(r['originalGenerationCostUsd'] for r in rows if r['round']==2)
(out/'grades.json').write_text(json.dumps({'method':plan,'rows':rows,'newGenerationCostUsd':cost,'primaryGradesSha256':sha(base_text)},indent=2)+'\n')
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Luna full-panel repeat','',plan['purpose'],'', 'The plan was frozen before new calls. All 16 writer inputs match the baseline exactly; task/lens hashes and the selected ZDR policy also match. All 32 generation IDs are distinct. Every new full-panel draft is retained separately, with no best-of replacement. Grades are unblinded assistant judgments.','', '| Condition | Round | Content checks | Content ready | Ready without edits | Em dashes |','|---|---:|---:|---:|---:|---:|']
for s in summary:lines.append(f"| {s['condition']} | {s['round']} | {s['contentPasses']}/{s['contentTotal']} | {s['contentReady']}/8 | {s['readyWithoutEdits']}/8 | {s['emDashes']} |")
lines+=['', 'Round 1 is the primary sample; round 2 is the new full-panel repeat. The two previously repeated house briefs use sample ID 4; all other new files use sample ID 2. Existing diagnostic outputs were not reused or overwritten.', '', f'New reported generation charges: ${cost:.6f}. Primary charges are excluded. The primary leaderboard remains unchanged. This is a small, fixed-panel, unblinded same-reviewer study, not a population reliability estimate.', '', '## New-round findings','']
for r in rows:
 if r['round']!=2:continue
 fs=[(g['id'],g['reason'],g['evidence']) for g in r['grades'] if g['verdict']!='pass']+[(g['category'],g['reason'],g['evidence']) for g in r['editorialFindings']]+[('Authoring residue',g['reason'],g) for g in r['placeholderFindings']]
 if not fs:continue
 lines += [f"### {r['task']} / {r['condition']}", '']
 for label,why,e in fs:lines.append(f"- **{label}:** [{e['quote']}](../../{r['path']}:{e['line']}). {why}")
 lines.append('')
lines += ['## Comparison with Astra repeats', '', 'Luna house remains at 52/54 content checks, but the failure moves: the new readout includes the reduction, while the new strategy deck asserts execution readiness. Default improves from 51/54 to 52/54 because the earlier strategy grounding failure is absent. Both launch reassurances remain unresolved.', '', 'Ready without edits changes from 2/8 to 1/8 default and 4/8 to 3/8 house. The Astra full-panel repeat retains 54/54 content checks in each condition and 6/8 house drafts ready without edits, versus Luna at 3/8. The new Luna calls cost $0.011698 versus Astra at $0.475830. This is a fixed-panel observation, not a cost-adjusted model ranking or a population reliability estimate.', '', '[Astra full-panel repeat](../repeatability-v2/REPORT.md).', '']
lines+=['[Frozen plan](plan.json), [explicit decisions](decisions.json), [all grades](grades.json), and [output hashes](output-hashes.json). Mechanical em dash findings are preserved in the grades; phrase candidates are not automatically defects.','']
(out/'REPORT.md').write_text('\n'.join(lines));print(json.dumps({'summary':summary,'newGenerationCostUsd':cost},indent=2))
