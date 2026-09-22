// Reproduce candidate evidence without modifying any judgment or generation.
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { hash, scan } from '../../src/core.js';
const directory = fileURLToPath(new URL('.', import.meta.url));
const root = resolve(directory, '../..');
const source = 'reviews/assistant-v33/grades.json';
const original = readFileSync(resolve(root, source), 'utf8');
const grades = JSON.parse(original);
const rows = grades.rows.map((row: any) => {
  const text = readFileSync(resolve(root, row.path), 'utf8');
  if (hash(text) !== row.outputSha256) throw new Error(`Changed output: ${row.path}`);
  return { path: row.path, outputSha256: row.outputSha256, candidates: scan(text, row.maxWords).candidates };
});
const matches = rows.flatMap((row: any) => row.candidates);
const audit = {
  source, sourceSha256: hash(original), inspectedDrafts: rows.length,
  candidateCounts: Object.fromEntries(['claudisms', 'negative_parallelism'].map(family =>
    [family, matches.filter((c: any) => c.family === family).length])),
  status: 'Scanner evidence only. Matches require contextual review; no grades changed.',
  rows: rows.filter((row: any) => row.candidates.length),
};
if (readFileSync(resolve(root, source), 'utf8') !== original) throw new Error('Grades changed during audit');
writeFileSync(resolve(directory, 'candidates.json'), JSON.stringify(audit, null, 2) + '\n');
console.log(JSON.stringify({ inspectedDrafts: audit.inspectedDrafts, candidateCounts: audit.candidateCounts }));
