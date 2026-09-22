import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { hash, MAX_OUTPUT_TOKENS, prompt, scan, type Model, type Task } from './core.js';

const root = fileURLToPath(new URL('../', import.meta.url));
const run = process.argv[2];
if (!run || !/^pilot-v\d+$/.test(run)) throw new Error('Specify a pilot run, for example pilot-v8');
const dir = resolve(root, 'runs', run);
const read = (path: string) => JSON.parse(readFileSync(path, 'utf8'));
const models: Model[] = read(resolve(root, 'data/models.json'));
const protocol = read(resolve(dir, 'protocol.json'));
const taskFile = protocol.taskFile ?? 'data/tasks.json';
if (!['data/tasks.json', 'data/tasks-v2.json'].includes(taskFile)) throw new Error('Unknown frozen task file');
const tasks: Task[] = read(resolve(root, taskFile));
const source = readFileSync(resolve(root, 'sources/anti-slop-reviewer.md'), 'utf8');
const reviewRoot = resolve(root, 'reviews');
const assistantGrades: any[] = existsSync(reviewRoot) ? readdirSync(reviewRoot)
  .filter(name => /^assistant-v\d+$/.test(name))
  .flatMap(name => {
    const path = resolve(reviewRoot, name, 'grades.json');
    return existsSync(path) ? read(path).rows : [];
  }) : [];
const rows: string[] = [];
let generated = 0, graded = 0, assistantReviewed = 0, imported = 0, billed = 0, unknownBilling = 0;
for (const model of models) for (const task of tasks) for (const condition of ['default', 'house'] as const) {
  const id = `${model.id.replaceAll('/', '--')}--${task.id}--${condition}`;
  const path = resolve(dir, id + '.json');
  if (!existsSync(path)) continue;
  const record = read(path);
  if (record.status !== 'ok') {
    rows.push(`| ${model.id} | ${task.id} | ${condition} | API failure, ungraded | - | - | - |`);
    continue;
  }
  const expected = { prompt: prompt(task, condition, source), reasoning: model.reasoning, maxOutputTokens: MAX_OUTPUT_TOKENS };
  if (record.inputHash !== hash(expected)) throw new Error(`Writer input mismatch: ${id}`);
  const checks = scan(record.text, task.maxWords);
  const hasGrade = existsSync(resolve(dir, 'score--' + id + '.json'));
  const hasAssistantGrade = assistantGrades.some(r => r.path === `runs/${run}/${id}.md` && r.outputSha256 === hash(record.text) && r.writerInputHash === record.inputHash);
  assistantReviewed += Number(hasAssistantGrade);
  generated++; graded += Number(hasGrade); imported += Number(Boolean(record.importedFrom));
  if (!record.importedFrom) {
    if (Number.isFinite(record.billing?.totalCost)) billed += record.billing.totalCost;
    else unknownBilling++;
  }
  rows.push(`| ${model.id} | [${task.id}](${id}.md) | ${condition} | ${hasAssistantGrade ? 'Assistant reviewed' : hasGrade ? 'Jev score saved' : 'Ungraded'} | ${checks.words}/${task.maxWords}${checks.withinWordLimit ? '' : ' FAIL'} | ${checks.emDashes.length} | ${record.importedFrom ? 'Reused' : 'New'} |`);
}
writeFileSync(resolve(dir, 'DRAFT_AUDIT.md'), `# Draft collection audit\n\n${generated} saved generations; ${graded} have Jev score records; ${assistantReviewed} have verified assistant reviews; ${imported} reused from earlier runs. Writer input hashes verified against current briefs and settings. New successful generation charges: $${billed.toFixed(6)}${unknownBilling ? ` plus ${unknownBilling} unknown charges` : ''}. This excludes judge calls and failed-call reservations; the shared ledger remains authoritative for the spending cap.\n\nUngraded means no completed Jev score or matching assistant review record. It is different from an unresolved judge decision. Word counts and em dashes are mechanical observations, not overall writing scores.\n\n| Model | Brief | Condition | Grading | Words/limit | Em dashes | Origin |\n|---|---|---|---|---:|---:|---|\n${rows.join('\n')}\n`);
console.log(JSON.stringify({ run, generated, graded, assistantReviewed, imported, newSuccessfulGenerationUsd: billed, unknownBilling }));
