# Grader improvement log

## Uncapped Qwen Max comparison, v19

Collected all 16 Qwen Max drafts for `alibaba/qwen3.8-max-0902` under the unchanged v19 writer configuration and v2 task set, with no output-token cap, harness deadline or retry. The catalog lists a ZDR route for this model, so it qualifies under the ZDR rule. Every response has matching requested, returned and canonical model IDs, a normal stop reason, no warnings and no imported output. Direct assistant review gives 49/54 default and 52/54 house content checks, with five and two failures and none unresolved. Content-ready counts are 3/8 default and 4/8 house; ready-without-edits counts are 1/8 and 3/8. Default drafts contain four em dashes; house drafts contain none. This is provisional unblinded grading on one generation per cell.

Confirmed failures are an invented end-of-week reply deadline, invented review progress and staging readiness, an assertion that the work is done and ready, pilot readiness and a missing Option B owner asserted in a comparison table, a bare readiness-to-start claim, and incident ownership moved from Lee before acceptance. That last error also appeared in the capped Qwen Max sample. Three drafts are blocked only by unfilled header dates or a sender placeholder. Both readouts state the reduction explicitly. The remaining editorial findings are repeated summaries, one aphoristic landing, one unsupported ensure and two empty closings. [Full scores and evidence](reviews/assistant-v20/REPORT.md).

Against the capped Qwen Max sample (default 47/54, house 51/54), the uncapped scores are similar; the runs use different output policies and are not repetitions. Successful charges total $0.113514. Conservative cumulative accounting is $12.371658286 of $20. Primary uncapped coverage is now 117 drafts, with eight repeat outputs separate. Hash, identity, exact-quote and coverage assertions pass; the draft audit and uncapped coverage report were refreshed. TypeScript checking, 18 TypeScript tests and the Python coverage test pass. The collection process exited and the lock is absent.

Catalog check under the ZDR rule: Fable 5 and Fable 5.1 list no ZDR route, so they fail the bench on that rule regardless of the reservation guard; Muse likewise has no ZDR route and was collected only under the earlier exception. Astra, Sol, Terra, Gemini 3.1 Pro, DeepSeek Pro, GLM 5.3, Kimi K3 and MiniMax list partial ZDR coverage, and Opus 5, Opus 4.6, Sonnet 5, Grok 4.7 and Qwen Max list full coverage. The headline cheap-versus-frontier comparison therefore cannot include Fable at all; the reachable frontier references within the ceiling are Sonnet 5 at a $1.48 reservation per request and Gemini 3.1 Pro at $2.25, while Astra, Opus 5, Sol and Grok each reserve more than the remaining budget can absorb on a single failure.

## Uncapped DeepSeek Flash comparison and ZDR rule, v19

Collected all 16 DeepSeek Flash drafts for `deepseek/deepseek-v4.1-flash` under the unchanged v19 writer configuration and v2 task set, with no output-token cap, harness deadline or retry. Every response has matching requested, returned and canonical model IDs, a normal stop reason, no warnings and no imported output. Direct assistant review gives 52/54 default and 50/54 house content checks, with two and four failures and none unresolved. Content-ready counts are 5/8 default and 3/8 house. No draft in either condition is ready without edits. Default drafts contain seven em dashes; house drafts contain none. This is provisional unblinded grading on one generation per cell.

Three drafts are blocked by authoring residue rather than factual error: an unfilled reply-date bracket in the default launch email, an unfilled header date in the house vendor memo and house change order, and a sentence in the default vendor memo that refers to the source pack. Confirmed grounding failures are invented prior discussions, an on-track work assurance while remediation remains possible, an invented October 1 reply deadline, a randomized follow-up design the source does not offer, and runbook ownership assigned to Lee. The house readout omits the explicit reduction and fails the frozen criterion as in earlier reviews; the default readout states the 3-minute change. The remaining editorial findings are repeated summaries. [Full scores and evidence](reviews/assistant-v19/REPORT.md).

The MiMo request returned a Gateway 400 because no zero-data-retention route exists for `xiaomi/mimo-v2.6-pro`; the catalog lists no ZDR and no no-training guarantee. The user's rule, stated during this pass, is that a model without ZDR fails the bench for business reasons. The failed request and its $0.12801115 reservation are retained, no exception was added, and no retry was sent. The frozen protocol still carries earlier non-ZDR exceptions for Muse, Fable 5 and Fable 5.1; Muse results remain in the uncapped table and are marked as collected under that exception pending a decision on whether to retire it, which would require a new run.

Successful DeepSeek Flash charges total $0.01123206. Conservative cumulative accounting is $12.245097286 of $20, including the retained MiMo reservation. Primary uncapped coverage is now 101 drafts, with eight repeat outputs separate. Hash, identity, exact-quote and coverage assertions pass; the draft audit and uncapped coverage report were refreshed. TypeScript checking, 18 TypeScript tests and the Python coverage test pass. Both collection processes exited and the lock is absent. Among the completed cheap models, DeepSeek Flash and GLM Flash sit between Luna and Qwen Flash on content checks in this sample; none reaches Muse, and the Fable and Astra comparison remains blocked by the reservation guard rather than by any collected evidence.

## Uncapped GLM Flash comparison, v19

Collected all 16 GLM Flash drafts for `zai/glm-5.3-flash` under the unchanged v19 writer configuration and v2 task set, with no output-token cap, harness deadline or retry. Every response has matching requested, returned and canonical model IDs, a normal stop reason, no warnings and no imported output. Direct assistant review gives 48/54 content checks in both conditions. Default has four failures and two unresolved checks; house has six failures and none unresolved. Content-ready counts are 3/8 in each condition; ready-without-edits counts are 1/8 default and 2/8 house. Default drafts contain 14 em dashes; house drafts contain none. This is provisional unblinded grading on one generation per cell.

Confirmed defects include a same-week delivery promise for a security review package, a claimed absence of readiness setback while remediation remains possible, an assertion of solid past team execution, reversed budget headroom figures in one sentence of the vendor memo, acceptance added as a payment condition, a two-week start commitment, immediate launch readiness, a claim that production authorization cannot arrive this quarter, and runbook approval assigned to Pat. The default vendor memo names the vendors only as Vendor A and Vendor B, and the default change order calls every amount an estimate while presenting the fee as fixed; both are recorded as unresolved rather than failed. Both readouts state the reduction explicitly, so the disputed calculation gate does not affect this model. [Full scores and evidence](reviews/assistant-v18/REPORT.md).

The capped GLM Flash sample scored 48/54 default and 46/54 house. The uncapped scores are similar, but the two runs use different output policies and are not repetitions of each other. Successful generation charges total $0.00646615. Conservative cumulative accounting is $12.105071436 of $20. Primary uncapped coverage is now 85 drafts, with eight repeat outputs separate. The builder verifies output hashes, exact quoted evidence, generation identity and coverage; the draft audit checks all writer input hashes. TypeScript checking, 18 TypeScript tests and the Python coverage test pass. The collection process exited and the lock is absent.

A read-only reservation preflight shows why the headline frontier comparison remains open. Under the conservative all-tier guard, one uncapped Fable 5.1 request reserves $7.36 against $7.89 remaining, and Fable 5.1 previously returned 429 on two of three requests; one failed request would retain that reservation and leave under $0.55. One Astra request reserves $22.36, above the whole ceiling. Neither model was attempted. Collecting them requires a decision to raise the ceiling or change the reservation policy, so the cheaper uncollected models are being collected first.

## Uncapped Qwen Flash comparison, v19

Completed all 16 Qwen Flash drafts under the unchanged v19 writer configuration and v2 task set, with no output-token cap, harness deadline or retry. Every response has matching requested, returned and canonical model IDs, a normal stop reason, no warnings and a valid word count. No capped output was imported.

Direct assistant review gives default 46/54 content checks and house 41/54, with eight and eleven failures respectively and two unresolved house checks. Neither condition has a ready-without-edits draft in this sample. The default change order passes all content checks but retains an unfilled preparation date. Six default em dashes become zero with house instructions. This is provisional unblinded grading, not a model-wide reliability estimate.

Defects include the wrong email recipient, omitted remediation, unsupported operational readiness, invented follow-up guarantees, a missing recommendation and a three-slide response to a four-slide request. The default readout calculates the three-minute change correctly; the house readout omits it. Both readouts have additional grounding defects, so their failures do not depend solely on the disputed calculation-omission gate. Ambiguous CFO signing and credential-timing claims remain unresolved rather than confirmed failures. [Full scores and evidence](reviews/assistant-v17/REPORT.md).

Successful generation charges total $0.01150225. Conservative cumulative accounting is $12.098313636 of $20. Primary uncapped coverage is now 69 drafts, with eight repeat outputs separate. The builder verifies each output hash, exact quoted evidence, generation identity and coverage; the draft audit independently checks all writer input hashes. The original grades are preserved in the cumulative report. Broad uncapped coverage and stronger reviewer validation remain unfinished.

## Readout criterion audit

Compared the frozen readout prompt with C01 and the supplied numbers-integrity rubric. C01 requires an explicit 3-minute or 20% reduction, but the brief does not directly request this calculation. All six primary uncapped Muse, Gemini Flash and Luna readouts give correct endpoints and pass every other content check. Their omission should not be presented as incorrect arithmetic or inability to calculate.

Saved a six-case sensitivity analysis showing the effect of removing only this omission as a hard content gate. It is hypothetical, not a replacement leaderboard. Added an inactive proposed task-v3 file with one sentence explicitly asking for the change in minutes or percent and the distinction from causation. Every other brief, source fact, criterion, severity and word limit is unchanged. Fresh validation is needed before adoption. [Audit and evidence](reviews/rubric-audit-v1/REPORT.md).

The audit builder verifies output hashes, quoted evidence, the identity of C01 as the only failed check, all six primary readout cases, the exact proposed change and the continued use of live tasks-v2. Official task and grade hashes remain unchanged. No model calls were made, and the $20 ceiling remains in place. Broad uncapped coverage and reviewer validation remain unfinished.

## Targeted repeatability diagnostic, v19

Added a repeat command with separate immutable sample IDs, exact task/condition selection and no primary-output imports. It uses unchanged writer prompts and settings. Sample 1 remains the primary collection; explicit sample numbers start at 2. The v18 source snapshot is preserved, and v19 retains no harness output-token cap or generation deadline.

Before dispatch, froze a diagnostic plan for Muse and Luna on house-style pilot readouts and operational handoff slides. The plan selects previously inspected failure/ownership cases, so it is not a random reliability sample. Ran eight new calls, two per model/brief, and retained the four primary outputs for three-attempt comparisons. All new calls succeeded without warnings or retries. Every response has a distinct generation ID, and full writer inputs, input hashes, source/task/model hashes and routing policy match the baseline. All new outputs fit the word limits and have no em dashes.

The readout calculation verdict varies. Muse failed, passed, then failed the explicit-reduction criterion; Luna failed, passed, then passed. Both models passed all handoff content checks in all three attempts. Muse handoffs were ready without edits in all three; Luna handoffs had repetition in all three. The rubric and original grades were not changed. This demonstrates sample sensitivity and does not prove a population-level ranking. [Report, frozen plan and evidence](reviews/repeatability-v1/REPORT.md).

The eight new calls cost $0.03742557. Baseline costs are excluded from that amount. Conservative accounting is $12.085506686 of the unchanged $20 ceiling. Primary uncapped coverage remains 53 drafts, with eight repeat outputs counted separately; 178 older capped drafts remain historical evidence.

Verified idempotent replay of a completed sample: both its entire response file and the budget ledger retained identical hashes. TypeScript checking, 18 TypeScript tests and the Python coverage test pass. The study builder checks all 12 output hashes, exact quoted evidence and generation identities. Every task-owned process exited and the lock is absent. Broad uncapped coverage, stronger judge validation and broader repeatability work remain unfinished; Astra's budget decision is still pending.

## Uncapped Luna comparison and Astra budget preflight, v18

Luna completed all 16 uncapped drafts with exact requested, returned and canonical model identities, normal stop reasons, no warnings and no retries. Every draft fits the task word limit. Default passes 51/54 checks with two failures and one unresolved claim; house passes 52/54 with one failure and one unresolved claim. Content readiness is 5/8 and 6/8. Ready-without-edits counts are 2/8 and 4/8.

Both readouts omit the explicit reduction calculation required by the frozen rubric. The default strategy slides assert that pending approval will leave the whole quarter without authorized deployment, which the source does not establish. Team-focus statements remain unresolved in both launch emails. Editorial findings include third-person client references, repetition, a stray Q in a heading and an abstract responsibility named as the rehearsal's actor. Default has eight em dashes; house has none. The stray Q is an editorial wording defect, not a missing required quarter value.

Successful charges total $0.011212, compared with $0.0953667 for the uncapped Muse sample. This is observed generation cost, not a general pricing claim. Luna is cheaper and has lower readiness in this small unblinded comparison. [Scores and evidence](reviews/assistant-v16/REPORT.md). There are now 53 reviewed uncapped drafts, separate from 178 historical capped drafts. Hash, identity, input and exact-quote checks pass; audits and coverage were refreshed. The collection and audit commands exited; no task-owned processes remain and the lock is absent.

Read-only preflight found Astra requires a $22.35991 reservation under the existing all-tier conservative guard, exceeding the $8.011675604 remaining before Luna. No Astra request was sent. The [Gateway service-tier documentation](https://vercel.com/docs/ai-gateway/models-and-providers/service-tiers) documents standard, flex and priority tiers and billing by the tier actually served. Pricing-route investigation did not change the guard or authorize more spending. The user was asked whether to retain the $20 ceiling or raise it to $40; no answer has been received. The ceiling remains $20. Conservative accounting after Luna is $12.032259716. Broader uncapped coverage and repeatability validation remain unfinished.

## Uncapped Muse and Gemini Flash retest, v18

Collected 16 new drafts each for Muse Spark 1.3 and Gemini 3.8 Flash without a harness output-token cap or generation deadline. None was imported from the old capped cohort. All 32 calls completed with matching requested, returned and canonical identities, normal stop reasons, no warnings and no retries. Every draft fits its task word limit.

Muse passes 53/54 checks in both conditions, with 7/8 content-ready drafts in each. Ready-without-edits counts are 4/8 default and 5/8 house. Its only content-check failure is the required reduction calculation in both readouts. Some drafts repeat information; the default strategy slides contain three em dashes, while house outputs contain none. No new grounding failure was found in this review.

Gemini Flash passes 51/54 default and 50/54 house checks. Default has two failures and one unresolved claim; house has three failures and one unresolved claim. Content readiness is 5/8 default and 4/8 house; ready-without-edits is 0/8 and 3/8. Problems include the omitted reduction calculation, an unsupported fully funded claim, unsupported full preparedness, and asserting a rehearsal was unscheduled when only its non-completion is established. Team-focus reassurance and the CFO-signature requirement remain unresolved. Both conditions contain zero em dashes.

Muse is the more promising of these two models in this sample, not an established overall winner. The grades are unblinded assistant judgments on one generation per cell. The previous capped drafts are separate historical evidence; the protocol change prevents treating the two runs as repetitions under identical settings. [Uncapped comparison and quoted findings](reviews/assistant-v15/REPORT.md).

Actual successful generation charges are $0.0953667 for Muse and $0.0428445 for Gemini Flash, $0.1382112 combined. Conservative cumulative accounting is $11.9883244 of $20, including earlier failure reservations. There are now 37 reviewed uncapped drafts and 178 separate historical capped drafts. Frozen hash, identity, input and quote checks pass. The draft audit and uncapped coverage report were refreshed. Both collection commands and the audit process exited successfully; no task-owned processes remain and the global lock is absent. Wider uncapped coverage and repeatability validation remain unfinished.

## Uncapped writer requests and accurate execution coverage, v17-v18

The user explicitly removed output-token limits. Writer requests now omit `maxOutputTokens`. The model catalog's advertised maximum output capacity is used only to reserve dollars against the existing $20 ceiling; it is never passed as a generation parameter. Historical request hashes remain reconstructible for auditing. Removing the token-limit field changes current request hashes, so old capped outputs cannot be silently imported into the uncapped cohort.

The initial MiniMax M3 request in v16 used all 4,096 output tokens for reasoning, returned no text, and ended with `length`. Its reported charge was $0.00498054. An uncapped v17 retry reached the old 90-second harness deadline. The writer deadline was then removed in v18 as well. The canceled request retains its $0.6271438 reservation. Provider-native limits and timeouts still apply. These execution outcomes are not writing-quality scores.

Five v18 MiniMax drafts completed without harness token or generation-time limits. The house-style vendor request then ended with a Gateway 408 reporting an HTTP headers timeout after 300,000 ms. Its $0.6310897 reservation remains accounted. This transport failure is separate from the removed generation deadline. Collection stopped on the error; no repeated request was dispatched. The v16 and v17 source snapshots and all request records are preserved.

[The uncapped review](reviews/assistant-v14/REPORT.md) grades all five completed drafts separately from the historical capped cohort. Default passes 16/19 checks across three briefs; house passes 11/13 across two. Every completed draft has a supported grounding failure, including invented prior discussions, week-one work commitments, on-schedule verification delivery, or unsupported contractual terms. Successful charges total $0.01681512. Eleven cells remain ungraded. Conservative accounting is $11.803575 of $20, including retained failures. There are 178 historical capped reviews and five separate uncapped reviews; these are not pooled into a model ranking.

Fixed two audit problems exposed during this work. An identical imported draft now matches its existing review across run directories only when model/task/condition identity, text hash and writer-input hash match. The v15 audit consequently recognizes all 85 stored complete drafts as reviewed, including its two imported copies, without adding new charges or independent samples. Coverage and draft audits now separate empty or length-truncated API successes from complete drafts while retaining their reported costs. Coverage reports take `--cohort legacy-capped` or `--cohort uncapped`; conflicting completed samples still require an explicit selection policy.

TypeScript checking, 17 TypeScript tests and one Python coverage test pass. New regression checks cover imported-review identity, altered text and inputs, empty and clipped outputs, conflicting samples, cap omission, valid catalog reservations and reproduction of historical input hashes. No Jev calls were made. All task-owned processes have exited and the global lock is absent. The writing benchmark and repeatability study remain unfinished.

## Muse comparison and bounded Fable expansion, v15-v16

Fable 5.1 returned one new house-style launch email, then 429 errors on the default launch and vendor memo requests. The second failure followed a cooldown. The generic No access to this model at this time message does not distinguish capacity from account access. Further Fable requests stopped; both full reservations remain accounted. The successful draft passes 5/6 content checks, is 174/180 words with no em dashes, and invents build readiness plus a reply deadline. Its reported charge was $0.06312. [Fable review](reviews/assistant-v12/REPORT.md) preserves the three available drafts without presenting a full model ranking.

Muse initially returned 400 because no ZDR provider was available. Verified the live catalog, which lists `zdr: none` and `no_training: none`, and the current [Gateway ZDR documentation](https://vercel.com/docs/ai-gateway/security-and-compliance/zdr). Added only `meta/muse-spark-1.3` to the existing explicit non-ZDR exceptions for synthetic benchmark inputs. Preserved the v15 source snapshot and failed request, then froze v16 with unchanged prompts, tasks and model settings. Coverage includes v16 and successful exact-input imports can reuse v15 outputs. No failure reservation was refunded.

All 16 Muse calls succeeded with matching requested, returned and canonical model identities, stop finish reasons, no warnings and no retries. Every draft fits the word limit and none contains an em dash. Default passes 53/54 content checks; house passes 52/54. Content-ready counts are 7/8 and 6/8, while ready-without-edits counts are 4/8 in both conditions. Both readouts omit the required explicit reduction calculation. House handoff directs the committee to name the organizer instead of requesting Pat to assign that responsibility. Remaining editorial findings concern repetition, a redundant title and audience phrasing. [Muse comparison and evidence](reviews/assistant-v13/REPORT.md).

Muse generation charges total $0.1193425. Conservative cumulative accounting is $10.523297 of $20. There are now 178 reviewed drafts across 14 attempted models. Grades remain provisional, unblinded assistant judgments; these samples do not establish run-to-run reliability or an independent ranking.

TypeScript checking and all 14 existing tests pass. Review builders verify complete new-output coverage, frozen hashes, exact evidence quotations and model identities. Draft audits and coverage were refreshed. Every collection session is terminal and the global lock is absent. Broader model coverage and repeatability validation remain unfinished.

## Qwen Max compared with Qwen Flash, v15

Collected and directly reviewed all 16 drafts for `alibaba/qwen3.8-max-0902` using the unchanged eight briefs and settings. Requested, returned and canonical model identities match. All calls stopped normally with no warnings or retries, and all drafts meet the word limits. There are now 161 reviewed drafts across 13 attempted models.

Default passes 47/54 checks, with six failures and one unresolved team-condition claim. House passes 51/54, with three failures and none unresolved. Content-ready counts are 3/8 in each condition; ready-without-edits counts are 0/8 default and 1/8 house. Compared with Qwen Flash, Max improves the house content score from 41/54 to 51/54 and content readiness from 1/8 to 3/8, but both have only 1/8 house drafts ready without edits. This is a single paired task sample, not proof of model superiority.

Concrete failures include promises to prove savings, an invented schedule turnaround and reporting deadline, unsupported readiness reassurance, a 30-day offer expiry, an incorrect quarter, and invented pre-acceptance incident ownership. Both results memos include the required reduction calculation. Default has ten em dashes; house has one. Three unfilled document-preparation date fields block readiness, while intentional sponsor-signature date blanks remain allowed. The review builder now records these explicit placeholder decisions as anchored findings rather than assuming none exist. Existing outputs and earlier grades are unchanged.

Successful charges total $0.11085. Conservative cumulative accounting is $9.561514 of $20. [Report and exact evidence](reviews/assistant-v11/REPORT.md). Hash, identity, quote and review-coverage assertions pass, and coverage and draft audits were refreshed. The collection session exited successfully, the lock is absent and no task-owned processes remain. Broader model coverage and repeatability validation remain unfinished.

## Gemini Flash complete comparison, v15

Collected and directly reviewed all 16 drafts for `google/gemini-3.8-flash` under the unchanged task set and settings. Requested model, returned model and canonical Gateway identity match. Every call finished normally, with no warnings or retries, and every draft fits the requested word limit. The cumulative assistant review now covers 145 drafts across 12 attempted models.

Both default and house pass 51/54 content checks. Default has two failures and one unresolved team-focus claim; house has three failures. Five drafts in each condition are content-ready. Ready-without-edits counts are 1/8 default and 3/8 house. Default contains two em dashes, house none. The change-order house contrast between an estimate and an approved calendar date is necessary scope clarification and is not a style defect. Intentional signature and date fields in approval forms are allowed.

Confirmed problems include an invented October 24, 2023 memo date, calling the knowledge-search pilot fully authorized when only its documents are approved, and broadening Jo's incident-ownership boundary to all pre-acceptance operations tasks. Both results memos give the 15-to-12-minute endpoints but omit the explicit 3-minute or 20% calculation required by the frozen criterion. That rule matches the earlier Sol, Luna, DeepSeek and Qwen decisions. Unnecessary openings and repeated statements account for additional editorial findings. [Scores and exact quoted evidence](reviews/assistant-v10/REPORT.md).

Successful generation charges total $0.0467895. Conservative cumulative accounting is $9.437617 of $20, including retained earlier failure reservations. Output hash, quote, identity and complete review-coverage assertions pass; draft and coverage audits were refreshed. The collection process exited successfully and the global lock is absent. No task-owned processes remain. These unblinded assistant judgments are provisional; remaining model coverage and repeatability validation are unfinished.

## GLM Flash complete comparison and scoring documentation, v15

Collected all 16 outputs for `zai/glm-5.3-flash` and directly reviewed them against the existing eight briefs, content checks and anti-slop lens. All calls succeeded with normal stop reasons, no warnings and matching requested, returned and canonical model IDs. All drafts are within the word limits. No retries or Jev calls were needed.

Default passes 48/54 content checks with six failures; house passes 46/54 with seven failures and one unresolved check. Content-ready counts are 3/8 default and 2/8 house. Ready-without-edits counts are 0/8 and 1/8. Default contains 14 em dashes; house contains none. The two rather-than constructions in the results memos explain causal uncertainty and are necessary factual contrasts, so neither is a style defect.

The dominant issue is unsupported detail: promised measured savings, an invented schedule turnaround, favorable team-performance claims, immediate go-live capability, and unsourced ownership or authorization. The house vendor memo's procurement approval wording is unresolved; that receives no point but is not a confirmed failure. Discovery and change-order content performs better. [Full grades with exact evidence](reviews/assistant-v9/REPORT.md).

Successful charges total $0.0057761 for these 16 outputs. Conservative cumulative accounting is $9.35340 of $20. The cumulative assistant review now covers 129 outputs across 11 attempted models. Grades remain provisional and unblinded, with one output per cell. These results do not establish repeatability or a general model ranking.

README now separates current assistant scoring from archived Jev experiments, correcting text that could imply Jev still supplies current grades. The review builder validates frozen hashes, returned identities, complete decision coverage and quoted evidence. Coverage and draft audits were refreshed. All three collection sessions exited successfully and the global lock is absent. Broad roster coverage and independent or repeated validation remain unfinished.

## Sol and Terra complete comparisons, v15

Collected and directly reviewed all eight briefs in both conditions for Sol and Terra, adding 32 drafts and bringing the reviewed total to 113. All calls succeeded with the requested model IDs, normal stop reasons, and no retries. No Jev calls were made.

Sol passes 52/54 default and 53/54 house content checks; 2/8 default and 6/8 house drafts are ready without edits. Both results memos omit the explicit time-reduction calculation required by the frozen rubric. Terra passes 52/54 in each condition; 1/8 default and 5/8 house drafts are ready without edits. Its strategy slides introduce a conflicting quarter in default and an unsupported pilot authorization in house. Ambiguous reassurance and approval wording remain unresolved rather than forced failures.

Successful generation charges total $0.24955 for Sol and $0.105076 for Terra. Conservative cumulative accounting is $9.34762 of $20, including retained failure reservations. These are provisional, unblinded assistant judgments on one generation per cell. [Full report and anchored findings](reviews/assistant-v8/REPORT.md).

The review builder verifies output hashes, exact evidence quotes, returned model IDs and saved text consistency. Coverage and draft audits were refreshed. Collection exited successfully; broader model coverage and repeatability validation remain unfinished.

## Explicit Opus 5 retry and separate Opus 4.6 addition, v14-v15

The user-requested retry of `anthropic/claude-opus-5` succeeded for the previously failed house-style launch email. Requested ID, returned model ID and Gateway canonical slug all match Opus 5; the successful provider was vertexAnthropic. The output has 197 words against the 180-word limit and invents a history of early warnings from Nia's team. Its successful generation charge was $0.032225.

Verified the live catalog entry for `anthropic/claude-opus-4.6` and added it as a distinct requested model, increasing the roster to 22 and the full target to 352 outputs. Both initial-email conditions succeeded through the anthropic provider, with exact 4.6 identity verified in responses. Default is 178 words and misses explicit granted security approval before data access; it also invents prior discussions and delay costs. House is 164 words, explicitly requires clearance, and has an unresolved implication of actual improvement. Its two generation charges total $0.02953.

[Assistant review and identity receipts](reviews/assistant-v7/REPORT.md) preserve the samples separately. No 4.6 output was substituted for Opus 5. Earlier failures retain their reservations; their root cause remains unproven by the generic 429 message. All three new calls succeeded without SDK retries. There are now 81 reviewed drafts. Conservative cumulative accounting is $8.2264 of $20.

Fourteen tests and TypeScript checking pass. Both temporary collection sessions exited and the global lock is absent. Broader Opus coverage and the remaining model comparison are unfinished.

## Mechanical quarter-placeholder regression, v14

The deterministic scanner now detects `Q[next]` in slide headings, preserving its exact offset and line. The rule is scoped to slide headings and excludes an explicitly backticked inline-code token. It does not treat ordinary bracket notation in prose or intentional signature/date fields as unfinished authoring.

A before/after rescan verified all 78 reviewed outputs against their saved text hashes. Exactly one residue result changed: Luna's default AI strategy slides, line 1, offset 43. All other detector fields and all other drafts were unchanged. The prior manual grade already blocked that draft for the placeholder, so model scores did not change.

[Regression comparison](runs/quarter-placeholder-regression/comparison.json) preserves the detector hashes and exact new match. `src/rescan-quarter-placeholder.ts` refuses to overwrite a frozen phase with another detector or compare a changed review set. This is a regression check on the observed corpus, not proof of general placeholder-detection accuracy.

Fourteen tests and TypeScript checking pass. No model or judge calls occurred, and the spending ledger was not changed. Historical protocols and the v13 source snapshot are preserved; future collection targets v14 and reuses matching writer inputs. Broader model coverage and repeatability validation remain unfinished.

## Luna comparison under unchanged writer settings

Collected all sixteen Luna drafts in v13 without retries or warnings. Successful reported generation cost was $0.01141, close to Qwen's represented sample cost. [Assistant review v6](reviews/assistant-v6/REPORT.md) uses the same task checks, output caps and style lens. It freezes every new output hash and preserves earlier grades.

Luna passes 52/54 default content checks and 51/54 house checks. The confirmed failures are the missing 3-minute/20% reduction in the default results memo and the missing COO selection authority in the house strategy slides. Three grounding judgments remain unresolved: team-focus claims in the two launch updates and the scope of Engineering ownership in the house handoff slides. They are not forced into failures or awarded points.

The default strategy slides contain `Q[next]`, an unfinished authoring marker. The manual review records it as a placeholder and blocks readiness even though the task-specific content checks pass. The current narrow placeholder scanner does not yet recognize that spelling; this is a concrete detector gap for a future revision. Other editorial findings include third-person client references, a source-pack reference and repeated presentation. These are editorial judgments, not factual errors.

Content-ready counts are 5/8 in both conditions. Ready-without-edits counts are 2/8 default and 3/8 house. There are now 78 saved and assistant-reviewed drafts across seven attempted models. The full comparison and repeatability validation remain unfinished. No Jev calls occurred. Conservative cumulative accounting is $7.9193 of $20; collection exited and released its lock.

## Targeted collection and complete DeepSeek default coverage, v12-v13

Added optional brief and condition selectors to `collect`. Unknown selector values fail without expanding the paid run. Two regression tests cover this behavior. The writer prompts, model settings and task criteria are unchanged. Exact matching earlier outputs are still reused, and prior frozen runner sources are retained.

DeepSeek's vendor default succeeded; its house request timed out at 90 seconds. The runner then collected the five untouched default briefs without retrying the failed launch-house or vendor-house cells. Default coverage is now complete at eight drafts, while house coverage remains one draft. This separates model output quality from API availability and avoids using missing results as zero scores.

[Assistant review v5](reviews/assistant-v5/REPORT.md) grades the six new default drafts with verified passages and frozen output hashes. DeepSeek default passes 50/54 content checks; 4/8 drafts are content ready, but none is ready without editorial/style edits under the house lens. The eight default generations cost $0.002429 in successful reported charges. A suggested randomized-or-otherwise-defensible follow-up is accepted as a proposal; the required numerical time reduction is still missing and fails its specific check.

The combined audit now has 62 reviewed drafts across the six attempted models. Conservative cumulative accounting is $7.8747 of $20, including failed reservations. Thirteen tests and TypeScript checking pass. Every collection session exited, and the run lock is absent. No Jev calls occurred. The other requested models and incomplete conditions remain outstanding.

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
