// Write scans.json for a review directory: mechanical checks on every completed draft of the listed models in one run.
// Usage: npx tsx scripts/scan-review.ts <reviewDir> <runDir> <modelId>...
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { scan, type Task } from '../src/core.js';
const root = resolve(new URL('..', import.meta.url).pathname);
const [reviewDir, runDir, ...modelIds] = process.argv.slice(2);
if (!reviewDir || !runDir || !modelIds.length) throw new Error('usage: scan-review.ts <reviewDir> <runDir> <modelId>...');
const tasks: Task[] = JSON.parse(readFileSync(resolve(root, 'data/tasks-v2.json'), 'utf8'));
const rows = [];
for (const modelId of modelIds) for (const task of tasks) for (const condition of ['default', 'house']) {
  const stem = `${modelId.replaceAll('/', '--')}--${task.id}--${condition}`;
  const path = resolve(root, runDir, stem + '.json');
  if (!existsSync(path)) continue;
  const record = JSON.parse(readFileSync(path, 'utf8'));
  if (record.status !== 'ok' || !record.text?.trim()) continue;
  const text: string = record.text;
  rows.push({ file: stem + '.md', ...scan(text, task.maxWords) });
}
writeFileSync(resolve(root, reviewDir, 'scans.json'), JSON.stringify(rows, null, 2) + '\n');
console.log(JSON.stringify({ reviewDir, scanned: rows.length, overLimit: rows.filter(r => !r.withinWordLimit).map(r => r.file), emDashes: rows.reduce((n, r) => n + r.emDashes.length, 0) }));
