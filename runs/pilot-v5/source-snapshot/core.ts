import { createHash } from 'node:crypto';
import { readFileSync, writeFileSync, renameSync } from 'node:fs';

export const LIMIT_USD = 20;
export const MAX_OUTPUT_TOKENS = 4096;
export type Condition = 'default' | 'house';
export type Check = { id: string; dimension: string; statement: string; severity: 'critical' | 'editorial' | 'style_gate'; polarity?: 'pass' | 'defect'; evaluation?: 'security-prerequisite' };
export type Task = { id: string; family: string; brief: string; facts: Record<string, string | number>; maxWords: number; checks: Check[] };
export type Model = { id: string; reasoning: 'low' | 'none' };
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
    id: `style_${m[1]}`, dimension: 'anti_slop', severity: 'editorial', polarity: 'defect',
    statement: `Does the deliverable contain a supported ${m[2]} defect? Apply these rules: ${m[3].trim()} A keyword match alone is not a defect. Judge audience fit, necessity and information loss. Preserve the stated exceptions.`,
  }));
}
export function prompt(task: Task, condition: Condition, source: string) {
  return `${task.brief}\n\nSOURCE PACK (all facts are synthetic):\n${JSON.stringify(task.facts, null, 2)}\n\nUse only this source pack for factual claims. Produce the requested deliverable only. Maximum ${task.maxWords} whitespace-separated words, including titles and tables.${condition === 'house' ? '\n\nHOUSE STYLE: Apply the following Zero Defect anti-slop rules to your writing. The references to scans describe the evaluation rules; write the deliverable, not a review report.\n' + styleRules(source) : ''}`;
}
const scanPatterns: [string, RegExp][] = [
  ['claudisms', /\b(?:load[- ]bearing|heavy lifting|doing a lot of the work|the shape of|blast radius|chokepoint|backstop|friction|trade-offs?|worth (?:stating|noting|flagging|remembering|considering)|one (?:caveat|wrinkle|practical note)|honest take|honestly|frankly|here['’]s why (?:that|this) matters|this matters because|the (?:deeper|real|most important) (?:point|thing|issue)|that['’]s not nothing|sit with|keep coming back to|where (?:I|we) landed)\b/gi],
  ['negative_parallelism', /\b(?:not (?:just |only |merely |simply )?[^.;!?\n]{1,60} but(?: also)? |less about [^\n]+ and more about |more than [^\n]+, it is |rather than |(?:is|was|are) not [^.;!?\n]{1,60}\. (?:it|they|this) (?:is|are) )/gi],
];
export function scan(text: string, maxWords: number) {
  const words = text.trim() ? text.trim().split(/\s+/u).length : 0;
  const locate = (offset: number, match: string) => ({ offset, line: text.slice(0, offset).split('\n').length, text: match });
  return {
    words, withinWordLimit: words <= maxWords, nonempty: words > 0,
    emDashes: [...text.matchAll(/\u2014/g)].map(m => locate(m.index!, m[0])),
    residue: [...text.matchAll(/^(?:STYLE GATE|EVALUATOR)\s*:|\[(?:Your Name|Name|insert[^\]\n]*)\]/gmi)].map(m => locate(m.index!, m[0])),
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

export type Entry = { id: string; model: string; reserve: number; charged: number; status: 'reserved' | 'settled' | 'unknown'; actualUsd?: number };
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
    if (this.total + amount > LIMIT_USD) throw new Error(`BUDGET_STOP: $${this.total.toFixed(4)} + $${amount.toFixed(4)} exceeds $20`);
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
