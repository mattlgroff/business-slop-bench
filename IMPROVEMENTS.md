# Grader improvement log

## Fable 5.1 and DeepSeek partial samples, v11

Fable 5.1 rejected the initial ZDR request with a 400 eligibility error. The catalog reports no ZDR support for Fable 5 and 5.1. The new frozen protocol declares a non-ZDR exception for those explicitly requested models and these synthetic test packets. Other writer routes remain unchanged; no private repo content or credential was added to the prompts.

Fable completed the default pilot email. Its house request returned 429, then succeeded after a cooldown and one bounded retry. The next default launch email returned 429. DeepSeek Flash completed both pilot emails and the default launch update; the house launch update timed out at 90 seconds twice. Further retries stopped. The retry helper now recognizes this specific inspected Gateway timeout signature while retaining the full failed reservation; arbitrary 500 errors remain ineligible.

[Assistant review v4](reviews/assistant-v4/REPORT.md) adds five reviewed outputs, giving a matched first-email comparison across six models. Fable house passes all seven content checks and needs no supported edits in this review. Its default email invents prior discussions. DeepSeek default also invents discussions; its house approval promise remains unresolved. Partial models are not included as complete eight-brief totals.

The coverage audit validates the frozen task hash, rejects competing successful samples for one cell, and separates generated, failed and unattempted cases. Current six attempted models have 56 saved and reviewed outputs; 40 cases across those models remain ungraded, and other planned models have not been attempted. The full target remains 336 drafts across 21 models.

Successful v11 generation charges total $0.087805. Conservative cumulative accounting is $7.8505 of $20, including previous failed reservations. No Jev calls occurred. All collection sessions exited and released their locks.

## Astra reference sample and assistant grading

Collected all sixteen Astra drafts under the same corrected task set and existing economical settings. Every call completed without retries or warnings. Successful generation cost was $0.47158. No Jev calls occurred.

[Updated comparison](reviews/assistant-v3/REPORT.md) grades Astra against the same 54 content checks per condition. All 108 content checks passed in this observed sample; word limits were met. This is not a claim of general accuracy. Default outputs still fail the em dash gate on three tasks. Editorial findings identify redundant wording in both pilot emails and a source-pack reference in the default handoff slides. Ready-without-edits results are 4/8 default and 7/8 house style.

The report documents why ordinary personal confidence in the launch email is allowed while invented objective claims of team performance fail other models. Intentional signature fields in the change order are also distinguished from unfilled authoring placeholders. Findings use exact verified passages. All Astra output hashes are frozen so rerunning the report builder cannot silently apply old decisions to changed text.

The audit now identifies 51 saved and assistant-reviewed drafts. Earlier grades are carried forward unchanged. Conservative cumulative accounting is $6.4317 of $20, including failed-call reservations from earlier work. This is distinct from billed cost. The collection process exited and the global lock is absent. Remaining model coverage and repeatability validation are unfinished.

## Corrected quarter wording and partial Opus expansion, v10

Created `data/tasks-v2.json` with one fact correction: AI pilot capacity now refers to next quarter, matching the brief. All other task facts and every grading criterion are unchanged. A focused test verifies that only this task's two writer prompts change. Historical tasks, generations and reports remain intact.

Collection now reuses exact matching inputs from prior runs and regenerates changed briefs. Qwen and Kimi each produced one replacement draft per condition for the corrected slide task. Opus produced one additional default launch email; the house-style call returned 429 with “No access to this model at this time” on the original attempt and two bounded retries. Retries stopped. No available header establishes the root cause. Missing Opus drafts are ungraded, not counted as poor output.

[Updated assistant report](reviews/assistant-v2/REPORT.md) covers all 32 Qwen/Kimi drafts and the three available Opus drafts. Prior grades are carried forward only when both output bytes and task are unchanged. Newly reviewed passages are verified against the text. Qwen house content checks are now 41/54 and Kimi default 51/54; ready-without-edits counts remain 1/8 and 4/8 respectively. These are new samples under a corrected prompt, not evidence of a causal improvement from the wording change.

All three available Opus emails exceed the 180-word limit. The two default emails contain unsupported factual assurances; the house email's staffing-pressure wording remains unresolved. This is an incomplete Opus sample, not an eight-brief ranking.

Paid Jev commands now fail before API initialization, respecting the user's request for assistant grading. The audit recognizes assistant reviews only when path, text hash and writer input hash match. It reports 35 reviewed drafts, 30 imported and five new generations. Successful new generation charges total $0.038976. Conservative cumulative accounting is $4.5287 of $20 because each failed Opus request retains its full maximum reservation; that is not a claim of $4.53 billed spend.

TypeScript checking and eleven tests pass. The collector exited and released its lock. Full Opus coverage and the remaining model comparison remain unfinished.

## Assistant replaces Jev for the current comparison

At the user's request, stopped Jev retries and graded all 32 Qwen and Kimi drafts directly with the existing 54 task-content checks per model/condition. The last Jev process had exited; 26 of 32 Jev score records exist and six remain incomplete. They are preserved as diagnostics and are not used for the assistant's grades.

[Assistant report](reviews/assistant-v1/REPORT.md), [all decisions and exact evidence](reviews/assistant-v1/grades.json), and [reproducible report builder](reviews/assistant-v1/build.py). The builder validates passages and assembles explicit assistant-authored decisions; it is not an automated semantic grader. Model identities were visible, and this is not human gold or independent validation.

| Model | Condition | Content checks passed | Ready without edits |
|---|---|---:|---:|
| Qwen Flash | Default | 47/54 | 0/8 |
| Qwen Flash | House | 40/54 | 1/8 |
| Kimi K3 | Default | 50/54 | 4/8 |
| Kimi K3 | House | 48/54 | 1/8 |

Readiness requires all critical content checks, word-limit compliance, no placeholders, a clean style gate and no supported editorial findings. Three unresolved judgments remain separate and earn no point. Source ambiguity about this/next quarter is not penalized. The report explicitly revises the earlier tentative concern about Qwen's statement that no further acceptance criteria exist: in this closed source pack it reasonably refers to the two supplied criteria.

No new writer calls or paid calls were needed for the assistant review. Cumulative conservative accounting after the earlier Jev attempts is $2.8396 of $20. SDK tests and type checking passed before v9 grading began. The global run lock is absent and there are no task-owned live processes.

## Kimi K3 added to the v8 screen

Completed the user-requested Kimi K3 run: sixteen successful generations, the same eight briefs and two conditions, no retries or agent loop. Actual generation cost was $0.168232. Conservative cumulative budget accounting is $2.3122 of $20. The collection process exited successfully and released its lock.

[Editorial observations and mechanical comparison](KIMI_SCREEN.md) show useful default proposal drafts, unsupported assertions in other outputs, and one house-style word-limit failure. Both models avoided em dashes in all house-style samples. The AI strategy brief has an ambiguity between next quarter and this quarter that should be corrected in a new frozen version before scoring temporal consistency. No current prompt or output was rewritten. New Jev grading is still pending.

## Eight-brief Qwen collection, v8

Collected both conditions for all eight tasks with Qwen Flash. Fourteen new writer calls completed successfully, and the two first-brief drafts were reused only after matching their input hashes. No API retries were needed. Successful new generation charges total $0.009630; conservative cumulative accounting is $2.0545 of $20.

The new `collect` command separates obtaining diagnostic drafts from publishing calibrated scores. It does not unlock the full pilot. A read-only draft audit reports input verification, generation provenance, word counts, em dashes, and ungraded status. Imported generation charges are excluded from new spending. The original user-supplied rubric is now preserved in `sources/strategy-consulting-bench-rubric.v0.json`.

All sixteen Qwen drafts fit their word limits. Six default drafts contain ten em dashes in total; all eight house-style drafts contain none. The broader sample exposes errors that clean style cannot offset: unsupported readiness claims, approval/acceptance confusion, misassigned ownership, and omitted recommendations. The change-order house draft is comparatively strong. [Read the editorial assessment](QWEN_SCREEN.md), which identifies passages and explicitly does not present author opinions as human gold or automated scores.

TypeScript checking and the ten existing tests pass. The collection process exited successfully, and its lock was removed. New task-level Jev grading and broader model comparison remain unfinished.

## Editorial evidence and unresolved results, v7

All 29 editorial categories now return clean, defect or unclear plus an original paragraph selection. A clean verdict with no defect passage passes. A defect with a verified passage fails. Disagreement remains unresolved. This prevents uncertain allegations from becoming confirmed defects, but can also leave real problems unclassified. These outcomes are not an overall quality score.

The scanner now reads all five Claudism patterns from the frozen source lens instead of a partial hardcoded list. Other punctuation is recorded for inspection, not automatically penalized.

The style comparison used 58 category controls and 12 transfer examples, each repeated twice. With neutral audience descriptions, the old method matched 138/140 labelled judgments with two unresolved; the revised method matched 140/140. These are 70 author-labelled examples, not human gold or 140 independent samples. Four saved drafts were also inspected without expected labels. Their match rate is undefined; the study report's `0/32` diagnostic rows must not be interpreted as zero accuracy. The earlier v1 study is excluded because some context descriptions leaked clean/defect labels. Its inputs and runner were preserved before correction.

| Saved draft | Confirmed readiness problem | Editorial defects | Unresolved checks |
|---|---|---:|---:|
| Qwen default | Unsupported prior-discussion claim | 0 | 4 |
| Qwen house | Missing approval-before-data-access prerequisite | 0 | 0 |
| Opus default | Unsupported blanket cost assurance; 191 words against 180 limit | 0 | 0 |
| Opus house | 185 words against 180 limit | 0 | 2 |

Opus default also has three em dashes and fails the style gate. Both house-style drafts have none. Opus house's unresolved checks concern staffing-pressure grounding and a rhetorical question classification. Qwen default's four editorial reviews are clean status judgments paired with selected defect passages. Zero confirmed editorial defects does not prove excellent writing, and this one-brief sample does not establish a model winner.

[Study report](runs/style-judge-study-v2/REPORT.md), [fixtures](data/style-judge-study.json), [regraded outputs](runs/pilot-v7/REPORT.md). No writer outputs were regenerated. Interrupted Jev batches returned 503 and were resumed individually with prior failure reservations preserved. All four regrades finished. Conservative cumulative accounting is $2.0437 of $20, including reserved failed attempts. TypeScript checking and all ten tests passed.

Next evidence needed: broader task coverage, quality/usefulness checks, and judge consistency on natural drafts. The full model comparison remains unfinished.

## Unsupported assurances and evidence, v6

The grounding judge now distinguishes supported statements, unsupported statements and unresolved interpretations. A second typed question selects an original paragraph as evidence. The code verifies that the paragraph exists at its recorded offset and line. A failure requires both an unsupported judgment and a real passage; disagreements remain unresolved. A real quotation establishes location, not the truth of the allegation.

The frozen comparison covers eight development snippets, 20 separate validation snippets and the four saved drafts, each judged twice. It includes source-authorized staffing holds, authorized dates, and an approved conditional fee credit, so strong commitments can pass when the source supports them. Ordinary requests and proposals also pass. Labels are author-proposed, not human gold.

| Approach | Development matches | Validation matches | Existing drafts | False accepts across all decisions |
|---|---:|---:|---:|---:|
| Previous Boolean grounding | 12/16 | 40/40 | 4/8 | 4 |
| Choice plus original passage | 15/16 | 40/40 | 6/8 | 0 |

The remaining three revised judgments were unresolved, including both repeats of Opus's staffing-pressure sentence. The status judgment and selected passage did not support a definitive failure consistently. This ambiguity is preserved, not forced into the expected label.

The integrated v6 regrade finds:

- Qwen default: unsupported prior-discussion claim, original paragraph P3, line 5.
- Qwen house: grounding passes; the independently validated missing security prerequisite still fails.
- Opus default: unsupported blanket cost assurance, paragraph P5, line 9.
- Opus house: unresolved staffing-pressure wording, paragraph P7, line 13. Its deterministic word-count failure remains.

Links: [fixtures](data/grounding-judge-study.json), [study report](runs/grounding-judge-study-v1/REPORT.md), [updated scores](runs/pilot-v6/REPORT.md). Grounding score JSON files now contain verified paragraph anchors; the report's older generic footnote about semantic flags without anchors applies to the other semantic checks.

Nine tests and TypeScript checking pass. The same four writer outputs were reused, with input hashes verified and import provenance retained. No new generation was purchased. Jev reported zero new billed charges in this pass. Conservative cumulative accounting is approximately $1.9509 of $20. Broader criterion validation and the full model run remain unfinished; the goal remains active.

## Security prerequisite, v5

The v4 grader incorrectly accepted Qwen's house-style email as explicitly requiring security approval before data access. Its text only promised to submit an access request after the client replied. That is a missing condition, even though the source pack contains the condition.

The v5 requirement judge receives the deliverable alone and distinguishes `met`, `missing`, and `contradicted`. It accepts equivalent wording and conditions spread across sentences. A request for approval does not count as granted approval, and a contradictory permission overrides a correct sentence elsewhere. The other Boolean checks retain the original v4 operating thresholds during this regrading comparison.

### Evidence

The frozen study contains eight development snippets, 16 separate validation snippets, and the four existing model drafts. Each was judged twice by three approaches. These are author-proposed diagnostic labels, not human-validated gold. Repeats are not additional independent examples.

| Approach | Development exact matches | Validation exact matches | Existing drafts | False accepts across all decisions |
|---|---:|---:|---:|---:|
| Original Boolean with source pack | 14/16 | 27/32 | 6/8 | 6 |
| Narrow Boolean, draft only | 14/16 | 32/32 | 8/8 | 0 |
| Explicit choice, draft only | 16/16 | 31/32 | 8/8 | 0 |

The choice discrepancy was `missing` versus `contradicted`, both failures. All choice pass/fail decisions matched the proposed labels in this study. That does not establish general judging accuracy, and only this requirement has been changed.

- [Frozen fixtures](data/security-judge-study.json)
- [Study report](runs/security-judge-study-v1/REPORT.md)
- [Raw judgments](runs/security-judge-study-v1/rows.json)
- [Updated four-draft report](runs/pilot-v5/REPORT.md)

The original four drafts were reused only after verifying their saved input hashes match current writer prompts and settings. No new writer generation was purchased. Source generation IDs and original protocol hashes are preserved; copied outputs are marked `importedFrom` and must not be counted as additional spending or independent samples.

Qwen's house-style security grade changed from **pass** to **missing**, with the live choice response assigning 0.99 to missing. Its content-ready result is now false. The other three drafts passed this specific requirement. Broader content/style results remain provisional.

### Running and boundaries

`npx tsx src/judge-study.ts` resumes the frozen comparison and reuses existing responses. Explicit bounded retries have their own budget entries and preserve safe request identifiers and retry headers. SDK retries remain disabled.

`npm run bench -- regrade-v4` regrades the four saved drafts with v5. It marks the inherited Boolean calibration as insufficient for a full v5 pilot, so widening the run remains gated until broader validation is performed. Do not claim that every other criterion was validated by the security study.

Seven focused tests and TypeScript checking pass. Successful Jev calls in this improvement pass reported zero billed cost under the observed promotion. Conservative accounting across all work is about $1.9463 of the $20 ceiling, including old failed-call reservations. The goal remains active: other missing prerequisites, unsupported assurances, style interpretation and judge consistency still need evaluation before a broad model ranking is justified.
