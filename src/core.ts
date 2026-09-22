import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync, renameSync } from 'node:fs';

export const LIMIT_USD = 100;
export type Condition = 'default' | 'house';
export function selectConditions(condition?: string): Condition[] {
  if (condition === undefined) return ['default', 'house'];
  if (condition !== 'default' && condition !== 'house') throw new Error('Unknown condition; refusing to expand collection');
  return [condition];
}
export type Check = { id: string; dimension: string; statement: string; severity: 'critical' | 'editorial' | 'style_gate'; polarity?: 'pass' | 'defect'; evaluation?: 'security-prerequisite' | 'grounding' | 'style' };
export type Task = { id: string; family: string; brief: string; facts: Record<string, string | number>; maxWords: number; checks: Check[] };
export type Model = { id: string; reasoning: 'low' | 'none' };
export function selectTasks(tasks: Task[], taskId?: string): Task[] {
  if (taskId === undefined) return tasks;
  const task = tasks.find(t => t.id === taskId);
  if (!task) throw new Error('Unknown task ID; refusing to expand collection');
  return [task];
}
export const hash = (v: unknown) => createHash('sha256').update(typeof v === 'string' ? v : JSON.stringify(v)).digest('hex');
export function atomic(path: string, value: unknown) {
  writeFileSync(path + '.tmp', JSON.stringify(value, null, 2) + '\n');
  renameSync(path + '.tmp', path);
}
export function styleRules(source: string) {
  const categories = source.slice(source.indexOf('### 1. Stock AI vocabulary'), source.indexOf('## Severity'))
    .replace(/\bFlag\b/g, 'Avoid').replace(/\bflag\b/g, 'penalize')
    .replace(/Report only instances/g, 'Avoid instances').replace(/Repair direction:/g, 'Write instead:');
  return `Write only the requested deliverable, without an audit, scores, scan counts or process notes.
Never use the em dash character (U+2014).
Avoid formulaic negative parallelism used only for rhetorical emphasis, including not X but Y, not just X but Y, This is not X. It is Y, less about X and more about Y, more than X it is Y, and X rather than Y. Necessary factual corrections, scope boundaries, mutually exclusive conditions and cumulative requirements are allowed.
The following categories and examples describe writing to avoid. Apply their contextual exceptions: a precise ordinary term is allowed; a keyword match alone is not a defect.\n\n${categories}`;
}
export function styleChecks(source: string): Check[] {
  const parts = [...source.matchAll(/^### (\d+)\. (.+)\n([\s\S]*?)(?=^### \d+\.|^## Severity)/gm)];
  return parts.map(m => ({
    id: `style_${m[1]}`, dimension: 'anti_slop', severity: 'editorial', polarity: 'defect', evaluation: 'style',
    statement: `Does the deliverable contain a supported ${m[2]} defect? Apply these rules: ${m[3].trim()} A keyword match alone is not a defect. Judge audience fit, necessity and information loss. Preserve the stated exceptions.`,
  }));
}
export function prompt(task: Task, condition: Condition, source: string) {
  return `${task.brief}\n\nSOURCE PACK (all facts are synthetic):\n${JSON.stringify(task.facts, null, 2)}\n\nUse only this source pack for factual claims. Produce the requested deliverable only. Maximum ${task.maxWords} whitespace-separated words, including titles and tables.${condition === 'house' ? '\n\nHOUSE STYLE: Apply the following Zero Defect anti-slop rules to your writing. The references to scans describe the evaluation rules; write the deliverable, not a review report.\n' + styleRules(source) : ''}`;
}
const scanSource = readFileSync(new URL('../sources/anti-slop-reviewer.md', import.meta.url), 'utf8');
const candidateSection = scanSource.slice(scanSource.indexOf('## Claudism candidate scan'), scanSource.indexOf('These searches find candidates'));
const candidatePatterns = [...candidateSection.matchAll(/^- `([^`]+)`/gm)].map(m => new RegExp(m[1], 'gi'));
if (!candidatePatterns.length) throw new Error('Source candidate scan is missing');
const scanPatterns: [string, RegExp][] = [
  ...candidatePatterns.map(regex => ['claudisms', regex] as [string, RegExp]),
  ['negative_parallelism', /\b(?:not (?:just |only |merely |simply )?[^.;!?\n]{1,60} but(?: also)? |less about [^\n]+ and more about |more than [^\n]+, it is |rather than |(?:is|was|are) not [^.;!?\n]{1,60}\. (?:it|they|this) (?:is|are) )/gi],
];
export function scan(text: string, maxWords: number) {
  const words = text.trim() ? text.trim().split(/\s+/u).length : 0;
  const locate = (offset: number, match: string) => ({ offset, line: text.slice(0, offset).split('\n').length, text: match });
  const quarterPlaceholders = [...text.matchAll(/\bQ\[next\]/gi)].filter(m => {
    const lineStart = text.lastIndexOf('\n', m.index! - 1) + 1;
    const line = text.slice(lineStart).split('\n')[0];
    // Scope this rule to slide headings, not ordinary bracket notation in prose/code.
    const inlineCode = text[m.index! - 1] === '`' && text[m.index! + m[0].length] === '`';
    return !inlineCode && /^\s*(?:#{1,6}\s*)?(?:\*\*)?Slide\s+\d+\b/i.test(line);
  }).map(m => locate(m.index!, m[0]));
  return {
    words, withinWordLimit: words <= maxWords, nonempty: words > 0,
    emDashes: [...text.matchAll(/\u2014/g)].map(m => locate(m.index!, m[0])),
    informationalPunctuation: Object.fromEntries(['2013', '2018', '2019', '201C', '201D'].map(code => [code, [...text].filter(c => c.codePointAt(0) === parseInt(code, 16)).length])),
    residue: [...text.matchAll(/^(?:STYLE GATE|EVALUATOR)\s*:|\[(?:Your Name|Name|insert[^\]\n]*)\]/gmi)].map(m => locate(m.index!, m[0])).concat(quarterPlaceholders).sort((a, b) => a.offset - b.offset),
    candidates: scanPatterns.flatMap(([family, regex]) => [...text.matchAll(regex)].map(m => ({ family, ...locate(m.index!, m[0]) }))),
  };
}
export function verdict(probability: number, polarity: 'pass' | 'defect' = 'pass', thresholds = { pass: 0.8, fail: 0.2 }) {
  if (!Number.isFinite(probability) || probability < 0 || probability > 1) throw new Error('Invalid probability');
  const p = polarity === 'pass' ? probability : 1 - probability;
  return p >= thresholds.pass ? 'pass' : p <= thresholds.fail ? 'fail' : 'review';
}

export function fitThreshold(rows: { passProbability: number; expected: string }[]) {
  const positives = rows.filter(r => r.expected === 'pass').map(r => r.passProbability);
  const negatives = rows.filter(r => r.expected === 'fail').map(r => r.passProbability);
  if (!positives.length || !negatives.length) throw new Error('Need positive and negative development labels');
  const minPositive = Math.min(...positives), maxNegative = Math.max(...negatives);
  if (minPositive <= maxNegative) throw new Error('Development labels overlap: no separating threshold');
  const midpoint = (minPositive + maxNegative) / 2;
  // A narrow abstention band is a policy choice, not a statistical confidence interval.
  return { pass: midpoint + 0.05, fail: midpoint - 0.05 };
}

export type Entry = { id: string; model: string; reserve: number; charged: number; status: 'reserved' | 'settled' | 'unknown' | 'released'; actualUsd?: number; releasedCharge?: number };
export class Budget {
  entries: Entry[];
  constructor(readonly path: string) {
    try { this.entries = JSON.parse(readFileSync(path, 'utf8')).entries; }
    catch (e: any) { if (e.code !== 'ENOENT') throw e; this.entries = []; }
  }
  get total() { return this.entries.reduce((sum, x) => sum + x.charged, 0); }
  save() { atomic(this.path, { limitUsd: LIMIT_USD, accountedUsd: this.total, entries: this.entries }); }
  reserve(id: string, model: string, amount: number) {
    if (this.entries.some(e => e.charged > e.reserve)) throw new Error('Prior cost bound violation requires inspection');
    if (!Number.isFinite(amount) || amount <= 0) throw new Error('Invalid reservation');
    if (this.entries.some(e => e.id === id)) throw new Error(`Call already reserved: ${id}`);
    if (this.total + amount > LIMIT_USD) throw new Error(`BUDGET_STOP: $${this.total.toFixed(4)} + $${amount.toFixed(4)} exceeds $${LIMIT_USD}`);
    this.entries.push({ id, model, reserve: amount, charged: amount, status: 'reserved' }); this.save();
  }
  settle(id: string, conservativeUsageCost?: number, actualUsd?: number) {
    const entry = this.entries.find(e => e.id === id)!;
    if (!entry) throw new Error('Unknown reservation');
    if (actualUsd !== undefined && (!Number.isFinite(actualUsd) || actualUsd < 0)) throw new Error('Invalid actual cost');
    // Unknown usage retains the entire reservation, even if promotional billing is zero.
    const known = conservativeUsageCost !== undefined && Number.isFinite(conservativeUsageCost) && conservativeUsageCost >= 0;
    entry.charged = known ? Math.max(conservativeUsageCost!, actualUsd ?? 0) : Math.max(entry.reserve, actualUsd ?? 0);
    entry.status = known ? 'settled' : 'unknown'; entry.actualUsd = actualUsd; this.save();
    if (entry.charged > entry.reserve || this.total > LIMIT_USD) throw new Error('COST_BOUND_VIOLATION: stop all further calls');
  }
}

// Use the greatest listed rate, including long-context, regional and premium tiers,
// plus peak multiplier. We settle using the same upper rate, not optimistic discounts.
export function rates(model: any) {
  const inputs: number[] = [], outputs: number[] = []; let multiplier = 1;
  function visit(value: any, mode?: 'input' | 'output') {
    if (!value || typeof value !== 'object') return;
    for (const [key, v] of Object.entries(value)) {
      if (key === 'multiplier' && typeof v === 'number') multiplier = Math.max(multiplier, v);
      if (['input', 'input_cache_write'].includes(key) && Number.isFinite(Number(v))) inputs.push(Number(v));
      if (key === 'output' && Number.isFinite(Number(v))) outputs.push(Number(v));
      if (key === 'cost' && mode && Number.isFinite(Number(v))) (mode === 'input' ? inputs : outputs).push(Number(v));
      visit(v, key.startsWith('input') ? 'input' : key.startsWith('output') ? 'output' : mode);
    }
  }
  visit(model.pricing);
  if (!inputs.length || !outputs.length) throw new Error(`Missing pricing: ${model.id}`);
  return { input: Math.max(...inputs) * multiplier, output: Math.max(...outputs) * multiplier };
}

// The catalog ceiling reserves dollars; it is never a generation parameter.
export function catalogOutputReservation(model: { max_tokens?: number }): number {
  if (!Number.isSafeInteger(model.max_tokens) || model.max_tokens! <= 0) {
    throw new Error('Missing valid catalog output maximum; cannot bound spending before an uncapped request');
  }
  return model.max_tokens!;
}

export function writerInput(task: Task, condition: Condition, source: string, reasoning: Model['reasoning'], historicalOutputLimit?: number) {
  return {
    prompt: prompt(task, condition, source), reasoning,
    ...(historicalOutputLimit === undefined ? {} : { maxOutputTokens: historicalOutputLimit }),
  };
}

export function repeatSample(value?: string): number {
  const n = Number(value);
  if (!value || !/^[1-9]\d*$/.test(value) || !Number.isSafeInteger(n) || n < 2) {
    throw new Error('Repeat sample must be an integer at least 2; sample 1 is the primary collection');
  }
  return n;
}

export function generationId(model: string, task: string, condition: Condition, sample = 1): string {
  if (!Number.isSafeInteger(sample) || sample < 1) throw new Error('Invalid sample index');
  const base = `${model.replaceAll('/', '--')}--${task}--${condition}`;
  return sample === 1 ? base : `${base}--sample-${sample}`;
}
