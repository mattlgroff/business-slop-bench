import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';

test('performance ranking includes previously excluded models without a retention flag', () => {
  const report = execFileSync('python3', ['scripts/ranking.py', 'reviews/assistant-v52', 'runs/pilot-v32'], { encoding: 'utf8' });
  for (const name of ['Claude Fable 5.1', 'Nemotron 3.5 Lightning Free', 'Muse Spark 1.3']) {
    const rows = report.split('\n').filter(line => line.includes(`| ${name} |`));
    assert.equal(rows.length, 2);
    assert.ok(rows.every(line => /^\| \d+ \|/.test(line)));
  }
  assert.ok(!report.includes('disqualified'));
});
