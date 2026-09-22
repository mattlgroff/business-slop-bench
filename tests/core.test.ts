import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, rmSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { Budget, scan, verdict, rates, selectTasks, selectConditions, styleChecks, prompt, fitThreshold, type Task } from '../src/core.js';

test('style detector retains exact locations and does not equate candidates with defects', () => {
  const s = scan('Hello.\nA load-bearing wall\u2014inspect it.', 20);
  assert.equal(s.emDashes.length, 1); assert.equal(s.emDashes[0].line, 2);
  assert.equal(s.candidates[0].text, 'load-bearing'); assert.equal(s.candidates[0].line, 2);
  assert.equal(scan('  ', 20).nonempty, false);
  assert.equal(scan('one two three', 2).withinWordLimit, false);
  assert.equal(scan('STYLE GATE:\nAudit\n[Your Name]', 20).residue.length, 2);
  const fullSourceScan = scan("You're right to push back. Here's where it gets interesting.\n2025\u20132026", 30);
  assert.ok(fullSourceScan.candidates.some(c => /right to push back/.test(c.text)));
  assert.ok(fullSourceScan.candidates.some(c => /gets interesting/.test(c.text)));
  assert.equal(fullSourceScan.informationalPunctuation['2013'], 1);
  assert.equal(fullSourceScan.emDashes.length, 0);
});
test('probability polarity and uncertain grades remain explicit', () => {
  assert.equal(verdict(0.95), 'pass'); assert.equal(verdict(0.95, 'defect'), 'fail');
  assert.equal(verdict(0.5), 'review'); assert.throws(() => verdict(NaN));
});
test('threshold fitting uses both label classes and refuses overlapping evidence', () => {
  const t = fitThreshold([{ passProbability: 0.7, expected: 'pass' }, { passProbability: 0.3, expected: 'fail' }]);
  assert.equal(verdict(0.7, 'pass', t), 'pass'); assert.equal(verdict(0.5, 'pass', t), 'review');
  assert.throws(() => fitThreshold([{ passProbability: 0.4, expected: 'pass' }, { passProbability: 0.6, expected: 'fail' }]));
});
test('spending cap survives restart and preserves uncertain charges', () => {
  const d = mkdtempSync(join(tmpdir(), 'businessslop-budget-'));
  try {
    let b = new Budget(join(d, 'ledger.json'));
    b.reserve('first', 'a', 19); b.settle('first');
    b = new Budget(join(d, 'ledger.json'));
    assert.equal(b.total, 19); assert.throws(() => b.reserve('second', 'a', 1.01));
    assert.throws(() => b.reserve('first', 'a', 0.1));
    b.reserve('second', 'a', 1); b.settle('second', 0.2, 0.1);
    assert.equal(b.total, 19.2);
    assert.throws(() => b.settle('second', 1.1));
    const restarted = new Budget(join(d, 'ledger.json'));
    assert.throws(() => restarted.reserve('third', 'a', 0.001));
  } finally { rmSync(d, { recursive: true }); }
});
test('price bounds include premium, tier and peak pricing', () => {
  assert.deepEqual(rates({ pricing: { input: '0.01', output: '0.02', output_tiers: [{ cost: '0.04' }], regional: { us: { input: '0.03' } }, peak_pricing: { multiplier: 2 } } }), { input: 0.06, output: 0.08 });
  assert.throws(() => rates({ id: 'missing', pricing: {} }));
});
test('all source categories survive and task facts are identical across conditions', () => {
  const source = readFileSync(new URL('../sources/anti-slop-reviewer.md', import.meta.url), 'utf8');
  assert.equal(styleChecks(source).length, 29);
  const tasks: Task[] = JSON.parse(readFileSync(new URL('../data/tasks.json', import.meta.url), 'utf8'));
  assert.equal(tasks.length, 8); assert.equal(new Set(tasks.map(t => t.family)).size, 4);
  for (const task of tasks) {
    assert.ok(prompt(task, 'house', source).startsWith(prompt(task, 'default', source)));
    assert.ok(!prompt(task, 'default', source).includes('C01'));
    assert.ok(!prompt(task, 'house', source).includes('Run these read-only'));
    assert.ok(!prompt(task, 'house', source).includes('Report every instance'));
  }
});

test('quarter correction invalidates only the affected writer prompts', () => {
  const source = readFileSync(new URL('../sources/anti-slop-reviewer.md', import.meta.url), 'utf8');
  const before: Task[] = JSON.parse(readFileSync(new URL('../data/tasks.json', import.meta.url), 'utf8'));
  const after: Task[] = JSON.parse(readFileSync(new URL('../data/tasks-v2.json', import.meta.url), 'utf8'));
  assert.deepEqual(after.map(t => t.id), before.map(t => t.id));
  for (const task of after) {
    const old = before.find(t => t.id === task.id)!;
    for (const condition of ['default', 'house'] as const) {
      assert.equal(prompt(task, condition, source) === prompt(old, condition, source), task.id !== 'ai-strategy-slides');
    }
    assert.deepEqual(task.checks, old.checks);
  }
  const corrected = after.find(t => t.id === 'ai-strategy-slides')!;
  assert.match(corrected.brief, /next quarter/);
  assert.match(corrected.facts.capacity as string, /next quarter/);
});

test('targeted collection cannot silently expand on an unknown task', () => {
  const tasks: Task[] = JSON.parse(readFileSync(new URL('../data/tasks-v2.json', import.meta.url), 'utf8'));
  assert.deepEqual(selectTasks(tasks, 'vendor-decision-memo').map(t => t.id), ['vendor-decision-memo']);
  assert.equal(selectTasks(tasks).length, 8);
  assert.throws(() => selectTasks(tasks, 'vendor-decision-typo'), /refusing to expand/);
});

test('condition selection does not turn a typo into paid requests for both conditions', () => {
  assert.deepEqual(selectConditions('default'), ['default']);
  assert.deepEqual(selectConditions('house'), ['house']);
  assert.deepEqual(selectConditions(), ['default', 'house']);
  assert.throws(() => selectConditions('defualt'), /refusing to expand/);
});

test('unfinished quarter tokens in slide headings are located without flagging intentional fields or notation', () => {
  const text = '## Slide 1: Select one Q[next] AI pilot\n\nSignature: ______ Date: ______\nUse Q[next] as the queue index.\n## Slide 2: Explain `Q[next]` indexing';
  const findings = scan(text, 200).residue;
  assert.deepEqual(findings, [{ text: 'Q[next]', offset: text.indexOf('Q[next]'), line: 1 }]);
  assert.equal(scan('**Slide 1: Q[NEXT] plan**', 100).residue.length, 1);
  assert.equal(scan('Slide 1: Next-quarter plan\nSignature: ______', 100).residue.length, 0);
});
