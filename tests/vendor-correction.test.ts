import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { prompt, type Task } from '../src/core.js';

const read = (file: string) => JSON.parse(readFileSync(file, 'utf8'));

test('authority correction preserves all unrelated judgments, costs and draft provenance', () => {
  const before = read('reviews/assistant-v51/grades.json').rows;
  const after = read('reviews/assistant-v52/grades.json').rows;
  assert.equal(after.length, before.length);
  let changed = 0;
  for (let i = 0; i < before.length; i++) {
    const a = before[i], b = after[i];
    if (a.task !== 'vendor-decision-memo') { assert.deepEqual(b, a); continue; }
    for (const key of ['path', 'outputSha256', 'writerInputHash', 'originalGenerationCostUsd', 'editorialFindings', 'emDashes', 'placeholderFindings']) assert.deepEqual(b[key], a[key]);
    assert.deepEqual(b.grades.filter((g: any) => g.id !== 'grounding'), a.grades.filter((g: any) => g.id !== 'grounding'));
    const old = a.grades.find((g: any) => g.id === 'grounding');
    const now = b.grades.find((g: any) => g.id === 'grounding');
    if (old.verdict !== now.verdict) changed++;
  }
  assert.equal(changed, 17);
  const grounding = (model: string, condition: string) => after.find((r: any) => r.model === model && r.condition === condition && r.task === 'vendor-decision-memo').grades.find((g: any) => g.id === 'grounding').verdict;
  assert.equal(grounding('Muse Wonder 1.0', 'house'), 'pass');
  assert.equal(grounding('Mistral Large 4', 'house'), 'pass');
  assert.equal(grounding('GLM 5.3', 'house'), 'fail');
  assert.equal(grounding('GLM Flash', 'default'), 'review');
});

test('v3 exposes explicit signing facts to both writer conditions and changes only the vendor authority point', () => {
  const old: Task[] = read('data/tasks-v2.json');
  const next: Task[] = read('data/tasks-v3.json');
  assert.equal(next.reduce((n, t) => n + t.checks.length, 0), 54);
  const vendor = next.find(t => t.id === 'vendor-decision-memo')!;
  const previous = old.find(t => t.id === vendor.id)!;
  for (const condition of ['default', 'house'] as const) {
    const text = prompt(vendor, condition, 'House rules');
    assert.ok(text.includes('Priya is not authorized to sign.'));
    assert.ok(text.includes('Alex, the commercial director, is the sole authorized contract signatory.'));
    assert.ok(text.includes('that approval does not delegate signing authority'));
  }
  const restored = structuredClone(next);
  const task = restored.find(t => t.id === vendor.id)!;
  task.facts.owner = previous.facts.owner;
  task.checks[task.checks.findIndex(c => c.id === 'C05')] = previous.checks.find(c => c.id === 'C05')!;
  assert.deepEqual(restored, old);
});


test('coverage keeps legacy and replacement-authority run cohorts separate', () => {
  const result = JSON.parse(execFileSync('python3', ['-c', `
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,'scripts')
from coverage import matching_runs
result={}
for version in ['v2','v3']:
 tasks=json.loads(Path('data/tasks-'+version+'.json').read_text())
 digest=hashlib.sha256(json.dumps(tasks,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
 result[version]=[p.name for p in matching_runs(Path('runs'),digest,'uncapped')]
print(json.dumps(result))
`], { encoding: 'utf8' }));
  assert.ok(result.v2.length > 0);
  assert.ok(result.v2.every((name: string) => !result.v3.includes(name)));
  assert.ok(!result.v3.includes('pilot-v32'));
});
