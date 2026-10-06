# Uncapped ranking with prices (ZDR rule ignored)

This is a what-if view: models with no zero-data-retention route are ranked alongside the rest. The bench rule still disqualifies them; the committed ranking is RANKING.md.

Source: reviews/assistant-v48/summary.json and runs/pilot-v29/catalog.json. Eight business briefs, one generation per brief and condition, graded by the assistant unblinded. This what-if table includes models disqualified by the recorded ZDR policy; it does not change their bench eligibility.

Mistral Large 4 uses provider-default reasoning: low failed, and successful none requests warned that reasoning configuration was ignored. Its writing is shown with that configuration limitation. Unavailable pricing means the model was absent from this catalog snapshot; historical grades remain intact.

## What the columns mean

- **Plain brief**: the model gets the task and the source facts only. This measures how much slop it writes unprompted.
- **With house rules**: the same brief plus Matthew Groff's Zero Defect anti-slop rules. This measures how well it performs once told exactly what slop means.
- **Checks passed**: each brief has six or seven total content checks, including a grounding check that every material claim traces to the source. 54 per condition. Unresolved means the reviewer could not settle it from the source; it earns no credit.
- **Content ready**: the draft passes every check, stays within the word limit and has no authoring residue such as a `[Date]` placeholder or a reference to the source pack. Editorial findings may still require revision.
- **Ready without edits**: content ready, plus zero em dashes, no negative-parallelism rhetoric, and no supported slop finding (throat clearing, puffery, empty closers, repeated summaries). No edit was identified by this provisional review; this is not independent validation.
- **Prices**: Gateway list rates per million tokens, base tier; regional and fast tiers cost more. Observed cost is the reported charge for the eight drafts in that condition; $0 means the stored response reported zero charge; the reason is not inferred from that number.

Ordering within each table: checks passed, ready without edits, content ready, fewer failures. A difference of one or two checks is within what a second generation could change.

## Repeat-run evidence

The tables show the primary attempt, not a reliability rate. In the separate [Astra full-panel repeat](../repeatability-v2/REPORT.md), all content checks passed again, while house drafts ready without edits changed from 8/8 to 6/8. In the [GPT-5.6 Luna full-panel repeat](../repeatability-v3/REPORT.md), house content checks remained 52/54 but ready-without-edits changed from 4/8 to 3/8. These fixed-panel studies used the same unblinded reviewer. They do not establish general judge accuracy or failure rates, and repeats do not replace primary results.

## Plain brief, no house rules

Which models write the least slop unprompted?

| Rank | Model | Checks passed (of 54) | Failed | Unresolved | Content ready (of 8) | Ready without edits (of 8) | Input $/M | Output $/M | Observed cost, 8 drafts |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 0 | 0 | 8 | 4 | 10.00 | 50.00 | $0.1120 |
| 2 | Muse Spark 1.3 (non-ZDR) | 53 | 1 | 0 | 7 | 4 | 1.25 | 4.25 | $0.0382 |
| 3 | GPT-6 Luna (non-ZDR) | 53 | 1 | 0 | 7 | 3 | 0.10 | 0.50 | $0 (reported) |
| 4 | GPT-6.1 Sol | 53 | 0 | 1 | 7 | 2 | 2.00 | 10.00 | $0.0218 |
| 5 | GPT-5.6 Terra | 52 | 1 | 1 | 6 | 3 | 2.00 | 12.00 | $0.0278 |
| 6 | GPT-6 Sol (non-ZDR) | 52 | 1 | 1 | 6 | 3 | 2.00 | 10.00 | $0 (reported) |
| 7 | Grok 4.7 | 52 | 2 | 0 | 6 | 3 | 2.00 | 6.00 | $0.0182 |
| 8 | Claude Opus 5.5 | 52 | 1 | 1 | 4 | 2 | 4.00 | 20.00 | $0.1171 |
| 9 | GLM 5.3 | 52 | 2 | 0 | 4 | 1 | 1.40 | 4.40 | $0.0149 |
| 10 | GPT-5.6 Sol | 52 | 2 | 0 | 6 | 0 | 4.00 | 20.00 | $0.0601 |
| 11 | DeepSeek V4.1 Flash | 52 | 2 | 0 | 5 | 0 | 0.30 | 1.20 | $0.0029 |
| 12 | GPT-5.6 Luna | 51 | 2 | 1 | 5 | 2 | 0.20 | 1.20 | $0.0031 |
| 13 | DeepSeek V4 Pro | 51 | 1 | 2 | 3 | 1 | 0.66 | 1.98 | $0.0090 |
| 14 | Gemini 3.8 Flash | 51 | 2 | 1 | 5 | 0 | 0.75 | 3.75 | $0.0187 |
| 15 | Kimi K3 | 51 | 3 | 0 | 4 | 0 | 3.00 | 15.00 | $0.0566 |
| 16 | Claude Fable 5.1 (non-ZDR) | 51 | 3 | 0 | 4 | 0 | 10.00 | 50.00 | $0.2380 |
| 17 | Claude Sonnet 5.5 | 50 | 2 | 2 | 3 | 2 | 2.00 | 10.00 | $0.0502 |
| 18 | MiMo V2.6 Pro | 50 | 4 | 0 | 3 | 2 | 0.43 | 0.87 | $0.0034 |
| 19 | MiniMax M3 | 50 | 4 | 0 | 3 | 0 | 0.30 | 1.20 | $0.0328 |
| 20 | GLM 5.3 Flash | 49 | 3 | 2 | 4 | 1 | 0.15 | 0.50 | $0.0019 |
| 21 | Gemini 3.1 Pro | 49 | 4 | 1 | 3 | 1 | 2.00 | 12.00 | $0.0960 |
| 22 | Qwen 3.8 Max | 49 | 5 | 0 | 3 | 1 | 2.00 | 6.00 | $0.0269 |
| 23 | Claude Fable 5 (non-ZDR) | 49 | 4 | 1 | 3 | 0 | 10.00 | 50.00 | $0.2345 |
| 24 | Claude Opus 4.6 | 49 | 5 | 0 | 2 | 0 | 5.00 | 25.00 | $0.0760 |
| 25 | Claude Opus 5 | 49 | 4 | 1 | 1 | 0 | 5.00 | 25.00 | $0.1481 |
| 26 | Pixel Canary (non-ZDR) | 48 | 6 | 0 | 2 | 1 | unavailable | unavailable | $0 (reported) |
| 27 | Claude Sonnet 5 | 48 | 6 | 0 | 2 | 0 | 2.00 | 10.00 | $0.0510 |
| 28 | Mistral Large 4 (provider-default reasoning) | 46 | 7 | 1 | 1 | 0 | 0.68 | 2.09 | $0.0052 |
| 29 | Qwen 3.8 Flash | 46 | 8 | 0 | 0 | 0 | 0.15 | 0.47 | $0.0038 |

## Same brief plus the house anti-slop rules

Which models perform best once told exactly what slop means?

| Rank | Model | Checks passed (of 54) | Failed | Unresolved | Content ready (of 8) | Ready without edits (of 8) | Input $/M | Output $/M | Observed cost, 8 drafts |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 0 | 0 | 8 | 8 | 10.00 | 50.00 | $0.3581 |
| 2 | GPT-6.1 Sol | 54 | 0 | 0 | 7 | 4 | 2.00 | 10.00 | $0.0728 |
| 3 | GPT-6 Sol (non-ZDR) | 53 | 1 | 0 | 7 | 7 | 2.00 | 10.00 | $0 (reported) |
| 4 | GPT-6 Luna (non-ZDR) | 53 | 1 | 0 | 7 | 6 | 0.10 | 0.50 | $0 (reported) |
| 5 | Muse Spark 1.3 (non-ZDR) | 53 | 1 | 0 | 7 | 5 | 1.25 | 4.25 | $0.0572 |
| 6 | GPT-5.6 Sol | 53 | 1 | 0 | 7 | 4 | 4.00 | 20.00 | $0.1903 |
| 7 | GPT-5.6 Luna | 52 | 1 | 1 | 6 | 4 | 0.20 | 1.20 | $0.0081 |
| 8 | GPT-5.6 Terra | 52 | 2 | 0 | 6 | 3 | 2.00 | 12.00 | $0.0780 |
| 9 | Qwen 3.8 Max | 52 | 2 | 0 | 4 | 3 | 2.00 | 6.00 | $0.0866 |
| 10 | Gemini 3.1 Pro | 51 | 2 | 1 | 5 | 5 | 2.00 | 12.00 | $0.1492 |
| 11 | Claude Fable 5 (non-ZDR) | 51 | 2 | 1 | 4 | 4 | 10.00 | 50.00 | $0.5413 |
| 12 | Grok 4.7 | 51 | 3 | 0 | 5 | 3 | 2.00 | 6.00 | $0.0540 |
| 13 | Claude Opus 5.5 | 51 | 2 | 1 | 3 | 3 | 4.00 | 20.00 | $0.2533 |
| 14 | DeepSeek V4 Pro | 51 | 2 | 1 | 4 | 2 | 0.66 | 1.98 | $0.0374 |
| 15 | Claude Sonnet 5.5 | 51 | 3 | 0 | 4 | 2 | 2.00 | 10.00 | $0.1151 |
| 16 | MiMo V2.6 Pro | 51 | 3 | 0 | 5 | 1 | 0.43 | 0.87 | $0.0166 |
| 17 | Gemini 3.8 Flash | 50 | 3 | 1 | 4 | 3 | 0.75 | 3.75 | $0.0242 |
| 18 | Claude Fable 5.1 (non-ZDR) | 50 | 3 | 1 | 3 | 3 | 10.00 | 50.00 | $0.5702 |
| 19 | Kimi K3 | 50 | 3 | 1 | 3 | 2 | 3.00 | 15.00 | $0.1180 |
| 20 | DeepSeek V4.1 Flash | 50 | 4 | 0 | 3 | 0 | 0.30 | 1.20 | $0.0084 |
| 21 | Claude Opus 5 | 49 | 4 | 1 | 3 | 3 | 5.00 | 25.00 | $0.2880 |
| 22 | GLM 5.3 | 49 | 5 | 0 | 3 | 2 | 1.40 | 4.40 | $0.0426 |
| 23 | Pixel Canary (non-ZDR) | 49 | 5 | 0 | 3 | 2 | unavailable | unavailable | $0 (reported) |
| 24 | Claude Opus 4.6 | 49 | 5 | 0 | 1 | 1 | 5.00 | 25.00 | $0.1803 |
| 25 | GLM 5.3 Flash | 48 | 6 | 0 | 3 | 2 | 0.15 | 0.50 | $0.0046 |
| 26 | Mistral Large 4 (provider-default reasoning) | 48 | 6 | 0 | 2 | 1 | 0.68 | 2.09 | $0.0197 |
| 27 | Claude Sonnet 5 | 48 | 5 | 1 | 2 | 0 | 2.00 | 10.00 | $0.1085 |
| 28 | MiniMax M3 | 44 | 9 | 1 | 0 | 0 | 0.30 | 1.20 | $0.0322 |
| 29 | Qwen 3.8 Flash | 41 | 11 | 2 | 0 | 0 | 0.15 | 0.47 | $0.0077 |

