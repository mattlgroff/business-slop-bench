# BusinessSlopBench

**Status: a one-person pilot, published as is, looking for someone to turn it into a real benchmark.**

This repository holds everything: the eight briefs, the anti-slop rubric, the frozen runner, every saved draft from every model, every grading decision with a quoted anchor into the draft, and the spending ledger. It is enough to reproduce or dispute any number in the tables. It is not enough to call the tables a scientific result, for the reasons in the disclaimers at the bottom of this file.

I am asking for someone with the time and the standing to take the concept and do it properly: more briefs, blind grading by people who do not work for a model vendor, repeated generations, published inter-rater agreement. Business writing is where most people meet these models, and there is no benchmark that pressures the labs on it. If you build that, take whatever is useful here. The rubric is CC BY-SA; the rest is MIT.

- [Current ranking, with and without the house rules, with list prices](reviews/assistant-v44/RANKING.md)
- [Same ranking with the zero-data-retention rule switched off](reviews/assistant-v44/RANKING-ignoring-zdr.md)
- [Cumulative grades and evidence](reviews/assistant-v44/REPORT.md)
- [Grader improvement log](IMPROVEMENTS.md), the running record of every rubric decision and correction

A small TypeScript benchmark for single-call English business writing. It targets 25 models on eight synthetic briefs in two conditions: ordinary task instructions and the same instructions plus Matthew Groff's Zero Defect anti-slop rules. It uses AI SDK 7 through Vercel AI Gateway for generation. Current grading is by the assistant; earlier Jev diagnostics are preserved.

## Why a business slop bench

When Matthew posted on X that he needed a business slop bench for SOWs, proposals and slide decks, Dex Horthy (@dexhorthy) replied: "lemme save you some time on that one - if a model wrote it, probably slop. wordcels vindicated etc", quoting Pedram (@pdrmnvd): "pretty wild that the hardest job for even the most frontier models is not shape rotation but writing, wordcels absolutely vindicated."

Probably true, and some are more slop than others. Across the 400 reviewed single-call uncapped drafts from 25 models, 117 drafts have a failed grounding check, from zero for Astra and Muse to 12 for Qwen Flash. These count drafts with findings, not individual claims; one draft can contain several unsupported claims. Most are invented commitments: reply and delivery deadlines, readiness or completion claims, prior discussions, payment or scope terms, and ownership the source never assigned. That criterion, with the per-task commitments checks, is the harness around promises: every material claim must trace to the source pack or be labeled a proposal. It catches what no compiler can, but only as one reviewer's provisional judgment on one generation per cell.

Opus comparison: [verified Opus 5 retry and separate Opus 4.6 sample](reviews/assistant-v7/REPORT.md).

Earlier results with a 4,096-token cap: [Muse compared with the other completed models](reviews/assistant-v13/REPORT.md). Jev retries stopped at the user's request. These are provisional assistant grades with verified evidence anchors, not human gold.

Uncapped results: [Sonnet 5, MiMo, Astra, Sol 6, Luna 6, Sol 5.6, Terra, Gemini Pro, Opus 5.5, Opus 5, Opus 4.6, Muse, Gemini Flash, Luna, Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax and Grok](reviews/assistant-v43/REPORT.md). Muse, Fable 5, Fable 5.1, Luna 6 and Sol 6 appear in the same report marked non-ZDR and disqualified; their writing scores are shown for information only. Eligibility follows the saved catalog and request policy, not a separate audit of provider retention practices. This cohort is not pooled with earlier capped scores.

[Current corrected ranking](reviews/assistant-v44/RANKING.md): Grok’s explicit request to authorize a signatory now receives the same passing judgment as Sol’s equivalent request. [Correction and evidence](reviews/assistant-v44/REPORT.md). All other 399 draft judgments are unchanged.

[Rubric audit](reviews/rubric-audit-v1/REPORT.md): all six Muse, Gemini Flash and Luna primary readouts give correct handling-time endpoints but omit a derived reduction that the rubric requires and the brief does not explicitly request. This is an analytical-completeness omission, not incorrect arithmetic. The audit shows its effect separately; official scores remain unchanged. A proposed clearer brief is inactive.

Current collection uses `pilot-v23` with no harness output-token cap and `data/tasks-v2.json`. The only brief change aligns the AI strategy capacity statement with next quarter. Exact matching outputs are imported from earlier runs; changed inputs generate new outputs. Historical results remain intact. Paid Jev commands are disabled while assistant grading is in use. `npx tsx src/draft-audit.ts pilot-v23` audits saved outputs and verifies their inputs against the frozen task version.

The current report covers all 400 primary drafts from 25 models, plus 40 separately tracked repeats. Sonnet 5 completed sixteen uncapped calls with seven-minute spacing and no errors. Its provisional review passes 48/54 content checks in each condition, with 2/8 content-ready drafts in each and 0/8 ready without edits. The house rules remove all sixteen default-condition em dashes but do not eliminate unsupported claims. MiMo completed after the Gateway advertised a ZDR route; its earlier routing rejection remains recorded. Run `python3 scripts/coverage.py --cohort uncapped` for current collection counts. The spending ceiling remains $100; the ledger includes retained reservations as well as settled charges.

## Run

Requires Node 22+, a mounted writable external SSD for this checkout, and the existing Gateway credential. Dependencies and disposable output stay on the SSD.

```sh
npm ci
npm run check
npm test
npm run bench -- collect alibaba/qwen3.8-flash
npm run bench -- collect moonshotai/kimi-k3
zsh scripts/paced-collect.sh anthropic/claude-opus-5
npx tsx src/draft-audit.ts pilot-v23
```

The CLI reads only `AI_GATEWAY_API_KEY` from the selected dotenv file. It does not execute the file or copy credentials. The compiled-in default path points at the author's machine and is part of the frozen runner hash, so it was left in place; set `BUSINESS_SLOP_ENV_FILE` to your own dotenv file, or supply `AI_GATEWAY_API_KEY` in the environment. Credential files, dependencies and run output are git-ignored.

The historical `pilot` command attempted the full 352-output screen, cheapest output-token rates first. It and the other paid Jev commands are now disabled. It is gated on control diagnostics: no opposite definitive validation judgments and at least 75% validation coverage. Validation labels are author-proposed; the first validation set was inspected during v2 development and is not a blind human gold set. Do not bypass the gate to obtain a leaderboard. Model and task lists are in `data/`; StepFun is excluded as requested. No agents, tools, browsing, exemplars, revision, or best-of selection are used by the writing models.

## What is frozen

The protocol hashes the task set, model settings, rubric source, control set, grader categories and runner code. The first paid command snapshots the catalog. Changes invalidate that run instead of mixing results. Source prompts, response text, token usage, warnings, provider routing, generation IDs, timing and every Jev answer are retained in `runs/pilot-v4/`. Interrupted completed generations are reused for grading; paid requests are never automatically retried. A filesystem lock prevents concurrent CLI processes from competing for the same budget.

Each model uses `low` reasoning except DeepSeek (`none`, since its catalog does not expose `low`). This is a declared economical configuration comparison, not a claim of equal compute. Sampling defaults remain provider-specific. Writer requests omit `maxOutputTokens` and the harness generation deadline. Provider-native limits and timeouts still apply. Runs v1-v16 used a 4,096-token cap; those results remain a separate historical cohort. Empty or truncated responses stop expansion and count as incomplete generations, not finished writing samples. Task word limits remain editorial requirements in the briefs.

Default and house conditions share the same source pack and task wording. Only the house condition receives the source style guide. Both are graded against the same style rules, but only the house condition tests explicit compliance. Every brief defines the whitespace word-count convention.

## Current assistant scoring

[Coverage against the supplied rubric](reviews/rubric-coverage-v1/REPORT.md): the pilot measures short-brief source fidelity, required decisions and style fit. Citation entailment, complex reconciliation, broader responsibility structures and independent judge calibration remain validation gaps.

[Grader calibration packet](reviews/grader-calibration-v1/README.md): ten full-context diagnostic cases with model metadata removed and a separate proposed answer key. Independent labels are still pending; this is not a held-out accuracy test.

[Luna full-panel repeat](reviews/repeatability-v3/REPORT.md): house content checks stay at 52/54, but the failing criterion changes and drafts ready without edits drop from 4/8 to 3/8. All 16 calls are fresh; older targeted repeats were not reused.

[Astra full-panel repeat](reviews/repeatability-v2/REPORT.md): all 108 content checks pass again, but house readiness without edits changes from 8/8 to 6/8. The 16 repeats are separate from the primary leaderboard. Two attempts do not establish population reliability.

[Grounding correction](reviews/assistant-v35/REPORT.md): Fable 5 default loses one check for an unsupported sample-adequacy claim, changing to 49/54 checks and 3/8 content-ready drafts. All other scores are unchanged. The correction is retained in the current assistant-v44 cumulative grades.

[Latest grading correction](reviews/assistant-v34/REPORT.md): four negative-parallelism findings were removed under the existing factual and decision-boundary exceptions. The comparison table and readiness counts are unchanged; The correction is retained in the current assistant-v44 cumulative grades.

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

The cumulative ceiling is $100 across all run versions, including calibration and generation; it was $20 until 2026-09-22, when the user raised it to $50 for pilot-v20 and then to $100 for pilot-v21. Reservations for requests the Gateway rejected with a sub-second 429 and no generation ID are released to zero by `scripts/release-rejected.py`, which logs each release; every other failed or canceled request keeps its full reservation. The shared ledger is runs/budget.json. Diagnostic v1, v2 and v3 results and source snapshots are retained separately; the corrected comparison is v4. Before dispatch, the ledger reserves a conservative bound using UTF-8 prompt bytes plus framing allowance, the model catalog's advertised maximum output capacity, and the highest listed input/output rate across regional, premium and long-context tiers, including peak multipliers, plus a $0.01 per-call surcharge allowance. The catalog output ceiling reserves dollars only and is never sent as a generation limit. If that worst-case reservation exceeds the remaining budget, the request does not run. SDK retries are zero; no cross-model fallbacks are configured. Full grading is split into fixed batches of 16 questions after large requests returned HTTP 503 while smaller probes succeeded. Three workers share one synchronous reservation ledger; a failure stops new jobs and lets in-flight calls settle. Same-model Gateway provider routing remains visible in saved metadata.

After success the reservation is settled using reported token counts at the conservative rates. When available, Gateway response metadata supplies the total billed cost including surcharges, with generation lookup as a fallback. Optional reporting tags are disabled because they incurred a surcharge in the first smoke test. An unknown or failed call retains its full reservation. Thus accounted cost may exceed actual billing, especially during promotions. A bound violation stops the process. This is an application spending guard based on catalog pricing and provider adherence to its advertised output capacity, not an independent Gateway account-wide billing limit.

Do not delete or reset the ledger to resume spending. It includes every attempt, including unsuccessful ones. The report distinguishes missing results from completed tasks. No paid calls occur during `report`, `check`, or `test`.

## Sources and attribution

The anti-slop rubric is copied from [mattlgroff/zero-defect](https://github.com/mattlgroff/zero-defect). `sources/provenance.json` records its source path, checkout commit and byte hash. The taxonomy carries CC BY-SA 4.0 attribution; copied notices and license information are preserved in `sources/`. It is used as rubric data, without invoking Zero Defect's multi-agent workflow.

- [AI SDK evaluation API](https://ai-sdk.dev/docs/ai-sdk-core/evaluation)
- [Jev on AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway)
- [LangChain's narrow Jev judge experiment](https://www.langchain.com/blog/jev-agent-evals-langsmith)
- [SlopCodeBench](https://arxiv.org/abs/2603.24755), inspiration for measuring quality independently from apparent task completion. This pilot does not test iterative degradation.

Published at [github.com/mattlgroff/business-slop-bench](https://github.com/mattlgroff/business-slop-bench). Run output under `runs/` is committed as evidence; the Gateway credit snapshot and collector logs are not.

## Transient failures

After inspecting a 429/502/503/504 result, `python3 scripts/retry-transient.py runs/pilot-v4/<failed-call>.json` archives that failed attempt, retains its entire budget reservation, and permits a new attempt when the original bench command is rerun. There are at most two manual retries per call. Successful generations and judge batches are reused. The retry helper never issues an inference call itself. An availability or permission failure still needs investigation; do not repeatedly retry it.

Fable 5, Fable 5.1 and Muse Spark 1.3 use declared non-ZDR routes because the catalog and live API reject ZDR for these models. Muse also has no no-training guarantee in the observed catalog. All test packets are synthetic and the style lens is public. Other writer models retain the ZDR setting. Since 2026-09-22 a model with no ZDR route fails the bench for business reasons: the failed request is retained and no further non-ZDR exception is added. MiMo failed on this rule. Whether to retire the earlier Fable and Muse exceptions is an open decision; their results are retained and marked. See [Gateway ZDR routing](https://vercel.com/docs/ai-gateway/security-and-compliance/zdr). `python3 scripts/coverage.py` reports generated, failed and unattempted cases across the current task version without assigning quality scores.

Target one cell without touching failed cells elsewhere:

```sh
npm run bench -- collect deepseek/deepseek-v4.1-flash vendor-decision-memo default
```

The brief and condition arguments are optional. Omit the condition to collect both conditions for that brief. Unknown brief IDs and conditions fail rather than expanding the run. Existing exact-match outputs are reused.

## Output-policy cohorts

The uncapped writer-input hash omits the old output-limit field, so capped outputs cannot be silently imported into the new cohort. Report coverage separately:

```sh
python3 scripts/coverage.py --cohort legacy-capped
python3 scripts/coverage.py --cohort uncapped
python3 -m unittest discover -s tests -p 'test_*.py'
```

Coverage separates complete drafts, incomplete generations, API failures and unattempted cells. Draft audits recognize reviews of identical imported artifacts only when model/task/condition identity, text hash and writer-input hash match. Imported copies remain excluded from new generation spending.

## Repeated attempts

[Targeted repeatability study](reviews/repeatability-v1/REPORT.md) compares three attempts for two house-style briefs with Muse and Luna. It is separate from primary model coverage and does not select the best answer.

```sh
npm run bench -- repeat meta/muse-spark-1.3 pilot-results-memo house 2
```

`repeat` requires an exact model, task, condition and integer sample number of at least 2. It uses the same writer input with a separate saved response ID. It never imports a primary output. Replaying an already-saved sample reuses that response without another charge. Primary coverage and draft audits exclude repeat IDs; the study report accounts for them separately.

## Disclaimers

Read these before quoting a number.

- **One generation per cell.** Each model wrote each brief once per condition. Two full-panel repeats (Astra, Luna) kept the content scores but moved the ready-without-edits counts by one or two drafts. A gap of one or two checks between models is within that variation.
- **The grader is an AI assistant, not a person, and it could see the model names.** Grades were written by whichever coding assistant was driving the session at the time. Every verdict quotes the exact line it rests on, so it can be audited, but it has not been audited by an independent human.
- **The rubric and the house rules were written by the same person who ran the bench.** The house condition measures compliance with one author's style rules, not writing quality in general.
- **The briefs are synthetic and short.** Eight briefs, six or seven checks each. They test source fidelity and invented commitments in short business documents, not long-form writing, research, or anything requiring outside knowledge.
- **Reasoning effort was set to `low` for every model** (`none` for DeepSeek). This is a cheap-configuration comparison, not a best-effort one.
- **Prices are Gateway list rates on the day of the run.** GPT-6 Sol and GPT-6 Luna were billed nothing during launch pricing.
- **The zero-data-retention rule is a business filter, not a quality judgment.** Models without a ZDR route on the Gateway are marked disqualified; the second ranking file shows them ranked with everyone else.
- **Provider routing varies.** The same model can be served by different providers behind the Gateway; the saved metadata records which one answered.

None of this means the drafts are wrong about what they show. Open a draft, open its grade, and check the quote. That is the whole method.
