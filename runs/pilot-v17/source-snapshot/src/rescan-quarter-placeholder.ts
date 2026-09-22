import { existsSync, mkdirSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { atomic, hash, scan } from './core.js';

const root = fileURLToPath(new URL('../', import.meta.url));
const phase = process.argv[2];
if (phase !== 'before' && phase !== 'after') throw new Error('Specify before or after');
const review = JSON.parse(readFileSync(resolve(root, 'reviews/assistant-v6/grades.json'), 'utf8'));
const dir = resolve(root, 'runs/quarter-placeholder-regression');
mkdirSync(dir, { recursive: true });
const snapshot = {
  detectorHash: hash(readFileSync(resolve(root, 'src/core.ts'), 'utf8')),
  reviewHash: hash(review),
  rows: review.rows.map((row: any) => {
    const text = readFileSync(resolve(root, row.path), 'utf8');
    if (hash(text) !== row.outputSha256) throw new Error(`Changed reviewed output: ${row.path}`);
    return { path: row.path, deterministic: scan(text, row.maxWords) };
  }),
};
const target = resolve(dir, phase + '.json');
if (existsSync(target) && JSON.parse(readFileSync(target, 'utf8')).detectorHash !== snapshot.detectorHash) {
  throw new Error('Snapshot is frozen; do not overwrite it with a different detector');
}
atomic(target, snapshot);
if (phase === 'after') {
  const before = JSON.parse(readFileSync(resolve(dir, 'before.json'), 'utf8'));
  if (before.reviewHash !== snapshot.reviewHash) throw new Error('Review set changed');
  const changed = snapshot.rows.flatMap((row: any, i: number) => {
    const old = before.rows[i];
    if (old.path !== row.path) throw new Error('Review order changed');
    if (hash({ ...old.deterministic, residue: [] }) !== hash({ ...row.deterministic, residue: [] })) throw new Error('Unrelated detector result changed');
    return hash(old.deterministic.residue) === hash(row.deterministic.residue) ? [] : [{ path: row.path, before: old.deterministic.residue, after: row.deterministic.residue }];
  });
  atomic(resolve(dir, 'comparison.json'), { drafts: snapshot.rows.length, changed, beforeDetectorHash: before.detectorHash, afterDetectorHash: snapshot.detectorHash });
  console.log(JSON.stringify({ drafts: snapshot.rows.length, changed }));
} else console.log(JSON.stringify({ phase, drafts: snapshot.rows.length, detectorHash: snapshot.detectorHash }));
