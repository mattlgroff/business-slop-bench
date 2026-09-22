# BusinessSlopBench

A small TypeScript benchmark for single-call English business writing. It targets 22 models on eight synthetic briefs in two conditions: ordinary task instructions and the same instructions plus Matthew Groff's Zero Defect anti-slop rules. It uses AI SDK 7 through Vercel AI Gateway for generation. Current grading is by the assistant; earlier Jev diagnostics are preserved.

Opus comparison: [verified Opus 5 retry and separate Opus 4.6 sample](reviews/assistant-v7/REPORT.md).

Current results: [Gemini Flash added to the complete model comparisons](reviews/assistant-v10/REPORT.md). Jev retries stopped at the user's request. These are provisional assistant grades with verified evidence anchors, not human gold.

Current collection uses `pilot-v15` and `data/tasks-v2.json`. The only brief change aligns the AI strategy capacity statement with next quarter. Exact matching outputs are imported from earlier runs; changed inputs generate new outputs. Historical results remain intact. Paid Jev commands are disabled while assistant grading is in use. `npx tsx src/draft-audit.ts pilot-v15` audits saved outputs and verifies their inputs against the frozen task version.

## Run

Requires Node 22+, a mounted writable external SSD for this checkout, and the existing Gateway credential. Dependencies and disposable output stay on the SSD.

```sh
npm ci
npm run check
npm test
npm run bench -- collect alibaba/qwen3.8-flash
npm run bench -- collect moonshotai/kimi-k3
npm run bench -- collect anthropic/claude-opus-5
npx tsx src/draft-audit.ts pilot-v15
```

The CLI reads only `AI_GATEWAY_API_KEY` from the selected dotenv file. It does not execute the file or copy credentials. Default path: `/Users/deathstar/working/elios/elios-insights/apps/api-elios/.env`. Set `BUSINESS_SLOP_ENV_FILE` to select another file, or supply `AI_GATEWAY_API_KEY` in the environment. Credential files, dependencies and run output are git-ignored.

The historical `pilot` command attempted the full 352-output screen, cheapest output-token rates first. It and the other paid Jev commands are now disabled. It is gated on control diagnostics: no opposite definitive validation judgments and at least 75% validation coverage. Validation labels are author-proposed; the first validation set was inspected during v2 development and is not a blind human gold set. Do not bypass the gate to obtain a leaderboard. Model and task lists are in `data/`; StepFun is excluded as requested. No agents, tools, browsing, exemplars, revision, or best-of selection are used by the writing models.

## What is frozen

The protocol hashes the task set, model settings, rubric source, control set, grader categories and runner code. The first paid command snapshots the catalog. Changes invalidate that run instead of mixing results. Source prompts, response text, token usage, warnings, provider routing, generation IDs, timing and every Jev answer are retained in `runs/pilot-v4/`. Interrupted completed generations are reused for grading; paid requests are never automatically retried. A filesystem lock prevents concurrent CLI processes from competing for the same budget.

Each model uses `low` reasoning except DeepSeek (`none`, since its catalog does not expose `low`). This is a declared economical configuration comparison, not a claim of equal compute. Sampling defaults remain provider-specific. The 4,096-token response cap includes the model's output budget; cap hits and empty responses stop expansion for inspection.

Default and house conditions share the same source pack and task wording. Only the house condition receives the source style guide. Both are graded against the same style rules, but only the house condition tests explicit compliance. Every brief defines the whitespace word-count convention.

## Current assistant scoring

The assistant reads each complete draft against its source packet, task-specific checks and the full anti-slop lens. Every check is marked pass, fail or unresolved. Unresolved earns no credit and is reported separately from confirmed failure. API errors are ungraded. Findings include exact quotations with verified offsets and line numbers.

`contentReady` requires all critical content checks to pass, the word limit to be met, and no unintended authoring placeholders. `readyWithoutEdits` additionally requires no style-gate violations or supported editorial findings. Mechanical character matches are counted directly; phrase matches are candidates requiring contextual judgment, including the lens's exceptions.

Review builders save explicit assistant decisions and verify evidence against frozen output hashes. They are not automated semantic graders. Model identities were visible during review, and one generation per task does not establish repeatability. These results are provisional assistant judgments, not human gold or independent validation. Historical Jev scores are not pooled with these grades.

## Historical Jev scoring

The following describes the archived Jev experiments. Jev inference is currently disabled in the CLI.

- Task-specific critical criteria cover facts, commitments, numerical statements, dependencies, decision readiness and accountability.
- Code checks empty responses, whitespace word count, obvious audit/placeholder residue, and literal U+2014 occurrences, with exact offsets and line numbers.
- Phrase scans preserve candidates. Jev evaluates rhetorical contrasts and all 29 categories from the source anti-slop lens with their exceptions. A matched word is not automatically a defect.
- Jev answers are probabilities of the question being true. Defect questions invert this into probability of passing. The operating thresholds are fitted only to development controls: the midpoint separating positive and negative pass scores, with an abstention band of 0.05 on either side. Overlapping development labels abort calibration. The actual thresholds are saved in calibration.json; the interval remains unresolved. The band is a policy choice, not a statistical confidence interval. Empty required deliverables fail deterministically. In control summaries, empty-response critical labels use that deterministic failure while retaining the raw Jev answers.
- Pass, fail and unresolved are separate outcomes, not an overall point score. Unresolved means the judge is uncertain or its status conflicts with its evidence. It is neither an earned point nor a confirmed defect. API failures are ungraded, not unresolved. Passing anti-slop checks does not establish usefulness or excellent writing.
- `contentReady` requires all critical checks to pass and the deterministic completeness checks to pass. Unresolved criteria prevent a Ready verdict; they do not prove an error. Style gate and editorial defects are reported separately.
- Editorial counts are failed categories, not unique defect counts. Categories can overlap. Do not turn them into a weighted universal quality score.
- Jev does not write explanations or verified evidence quotations. Inspect the archived output and question to adjudicate a disputed semantic flag. Scanner matches alone have deterministic text anchors.

Nineteen authored diagnostic controls exercise clean and broken examples before expansion. Their labels are **author-proposed, not human-validated gold**. Calibration results are development evidence. The initial pilot is one response per task and condition, so it does not establish run-to-run reliability or statistical superiority. Do not infer a best model from one smoke-test brief.

The full source taxonomy is also visible to the writer in the house condition. This intentionally measures instruction-following; it must not be confused with default writing quality. Provider names never enter Jev's state.

## Cost controls

The cumulative ceiling is $20 across all run versions, including calibration and generation. The shared ledger is runs/budget.json. Diagnostic v1, v2 and v3 results and source snapshots are retained separately; the corrected comparison is v4. Before dispatch, the ledger reserves a conservative bound using UTF-8 prompt bytes plus framing allowance, the response token cap, and the highest listed input/output rate across regional, premium and long-context tiers, including peak multipliers, plus a $0.01 per-call surcharge allowance. SDK retries are zero; no cross-model fallbacks are configured. Full grading is split into fixed batches of 16 questions after large requests returned HTTP 503 while smaller probes succeeded. Three workers share one synchronous reservation ledger; a failure stops new jobs and lets in-flight calls settle. Same-model Gateway provider routing remains visible in saved metadata.

After success the reservation is settled using reported token counts at the conservative rates. When available, Gateway response metadata supplies the total billed cost including surcharges, with generation lookup as a fallback. Optional reporting tags are disabled because they incurred a surcharge in the first smoke test. An unknown or failed call retains its full reservation. Thus accounted cost may exceed actual billing, especially during promotions. A bound violation stops the process. This is an application spending guard based on catalog pricing and provider adherence to token limits, not an independent Gateway account-wide billing limit.

Do not delete or reset the ledger to resume spending. It includes every attempt, including unsuccessful ones. The report distinguishes missing results from completed tasks. No paid calls occur during `report`, `check`, or `test`.

## Sources and attribution

The anti-slop rubric is copied from [mattlgroff/zero-defect](https://github.com/mattlgroff/zero-defect). `sources/provenance.json` records its source path, checkout commit and byte hash. The taxonomy carries CC BY-SA 4.0 attribution; copied notices and license information are preserved in `sources/`. It is used as rubric data, without invoking Zero Defect's multi-agent workflow.

- [AI SDK evaluation API](https://ai-sdk.dev/docs/ai-sdk-core/evaluation)
- [Jev on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)
- [LangChain's narrow Jev judge experiment](https://www.langchain.com/blog/jev-agent-evals-langsmith)
- [SlopCodeBench](https://arxiv.org/abs/2603.24755), inspiration for measuring quality independently from apparent task completion. This pilot does not test iterative degradation.

Local build only. No repository has been published and no remote has been configured.

## Transient failures

After inspecting a 429/502/503/504 result, `python3 scripts/retry-transient.py runs/pilot-v4/<failed-call>.json` archives that failed attempt, retains its entire budget reservation, and permits a new attempt when the original bench command is rerun. There are at most two manual retries per call. Successful generations and judge batches are reused. The retry helper never issues an inference call itself. An availability or permission failure still needs investigation; do not repeatedly retry it.

Fable 5 and 5.1 use a declared non-ZDR route because the catalog and live API reject ZDR for these models. All test packets are synthetic. Other writer models retain the ZDR setting. `python3 scripts/coverage.py` reports generated, failed and unattempted cases across the current task version without assigning quality scores.

Target one cell without touching failed cells elsewhere:

```sh
npm run bench -- collect deepseek/deepseek-v4.1-flash vendor-decision-memo default
```

The brief and condition arguments are optional. Omit the condition to collect both conditions for that brief. Unknown brief IDs and conditions fail rather than expanding the run. Existing exact-match outputs are reused.
