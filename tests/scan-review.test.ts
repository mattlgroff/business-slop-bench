import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

test('saved review scans preserve phrase and rhetorical candidates with exact anchors', () => {
  const directory = mkdtempSync(join(tmpdir(), 'businessslop-scan-'));
  const text = 'A load-bearing wall.\nUse facts rather than assumptions.';
  try {
    writeFileSync(join(directory, 'test--writer--pilot-client-email--default.json'),
      JSON.stringify({ status: 'ok', text, finishReason: 'stop' }));
    execFileSync(process.execPath, ['--import', 'tsx',
      fileURLToPath(new URL('../scripts/scan-review.ts', import.meta.url)),
      directory, directory, 'test/writer']);
    const [row] = JSON.parse(readFileSync(join(directory, 'scans.json'), 'utf8'));
    assert.ok(row.candidates.some((c: any) => c.family === 'claudisms' && c.text === 'load-bearing'));
    assert.ok(row.candidates.some((c: any) => c.family === 'negative_parallelism' && c.text === 'rather than '));
    for (const candidate of row.candidates) {
      assert.equal(text.slice(candidate.offset, candidate.offset + candidate.text.length), candidate.text);
      assert.equal(candidate.line, text.slice(0, candidate.offset).split('\n').length);
    }
    assert.equal(row.words, 8);
    assert.equal(row.withinWordLimit, true);
  } finally {
    rmSync(directory, { recursive: true });
  }
});
