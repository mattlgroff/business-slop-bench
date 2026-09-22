# Uncapped ranking with prices

Source: reviews/assistant-v43/summary.json and runs/pilot-v23/catalog.json. Eight business briefs, one generation per brief and condition, graded by the assistant unblinded. Models disqualified by the recorded ZDR policy are shown for information without a rank.

## What the columns mean

- **Plain brief**: the model gets the task and the source facts only. This measures how much slop it writes unprompted.
- **With house rules**: the same brief plus Matthew Groff's Zero Defect anti-slop rules. This measures how well it performs once told exactly what slop means.
- **Checks passed**: each brief has six or seven total content checks, including a grounding check that every material claim traces to the source. 54 per condition. Unresolved means the reviewer could not settle it from the source; it earns no credit.
- **Content ready**: the draft passes every check, stays within the word limit and has no authoring residue such as a `[Date]` placeholder or a reference to the source pack. Editorial findings may still require revision.
- **Ready without edits**: content ready, plus zero em dashes, no negative-parallelism rhetoric, and no supported slop finding (throat clearing, puffery, empty closers, repeated summaries). No edit was identified by this provisional review; this is not independent validation.
- **Prices**: Gateway list rates per million tokens, base tier; regional and fast tiers cost more. Observed cost is the reported charge for the eight drafts in that condition; $0 means the stored response reported zero charge; the reason is not inferred from that number.

Ordering within each table: eligible models first, then checks passed, ready without edits, content ready, fewer failures. A difference of one or two checks is within what a second generation could change.

## Repeat-run evidence

The tables show the primary attempt, not a reliability rate. In the separate [Astra full-panel repeat](../repeatability-v2/REPORT.md), all content checks passed again, while house drafts ready without edits changed from 8/8 to 6/8. In the [GPT-5.6 Luna full-panel repeat](../repeatability-v3/REPORT.md), house content checks remained 52/54 but ready-without-edits changed from 4/8 to 3/8. These fixed-panel studies used the same unblinded reviewer. They do not establish general judge accuracy or failure rates, and repeats do not replace primary results.

## Plain brief, no house rules

Which models write the least slop unprompted?

| Rank | Model | Checks passed (of 54) | Failed | Unresolved | Content ready (of 8) | Ready without edits (of 8) | Input $/M | Output $/M | Observed cost, 8 drafts |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 0 | 0 | 8 | 4 | 10.00 | 50.00 | $0.1120 |
| 2 | GPT-5.6 Terra | 52 | 1 | 1 | 6 | 3 | 2.00 | 12.00 | $0.0278 |
| 3 | Grok 4.7 | 52 | 2 | 0 | 6 | 3 | 1.20 | 3.60 | $0.0182 |
| 4 | Claude Opus 5.5 | 52 | 1 | 1 | 4 | 2 | 4.00 | 20.00 | $0.1171 |
| 5 | GLM 5.3 | 52 | 2 | 0 | 4 | 1 | 1.40 | 4.40 | $0.0149 |
| 6 | GPT-5.6 Sol | 52 | 2 | 0 | 6 | 0 | 4.00 | 20.00 | $0.0601 |
| 7 | DeepSeek V4.1 Flash | 52 | 2 | 0 | 5 | 0 | 0.30 | 1.20 | $0.0029 |
| 8 | GPT-5.6 Luna | 51 | 2 | 1 | 5 | 2 | 0.20 | 1.20 | $0.0031 |
| 9 | DeepSeek V4 Pro | 51 | 1 | 2 | 3 | 1 | 0.66 | 1.98 | $0.0090 |
| 10 | Gemini 3.8 Flash | 51 | 2 | 1 | 5 | 0 | 0.75 | 3.75 | $0.0187 |
| 11 | Kimi K3 | 51 | 3 | 0 | 4 | 0 | 3.00 | 15.00 | $0.0566 |
| 12 | MiMo V2.6 Pro | 50 | 4 | 0 | 3 | 2 | 0.43 | 0.87 | $0.0034 |
| 13 | MiniMax M3 | 50 | 4 | 0 | 3 | 0 | 0.30 | 1.20 | $0.0328 |
| 14 | GLM 5.3 Flash | 49 | 3 | 2 | 4 | 1 | 0.15 | 0.50 | $0.0019 |
| 15 | Gemini 3.1 Pro | 49 | 4 | 1 | 3 | 1 | 2.00 | 12.00 | $0.0960 |
| 16 | Qwen 3.8 Max | 49 | 5 | 0 | 3 | 1 | 2.00 | 6.00 | $0.0269 |
| 17 | Claude Opus 4.6 | 49 | 5 | 0 | 2 | 0 | 5.00 | 25.00 | $0.0760 |
| 18 | Claude Opus 5 | 49 | 4 | 1 | 1 | 0 | 5.00 | 25.00 | $0.1481 |
| 19 | Claude Sonnet 5 | 48 | 6 | 0 | 2 | 0 | 2.00 | 10.00 | $0.0510 |
| 20 | Qwen 3.8 Flash | 46 | 8 | 0 | 0 | 0 | 0.15 | 0.47 | $0.0038 |
| - | Muse Spark 1.3 (non-ZDR, disqualified) | 53 | 1 | 0 | 7 | 4 | 1.25 | 4.25 | $0.0382 |
| - | GPT-6 Luna (non-ZDR, disqualified) | 53 | 1 | 0 | 7 | 3 | 0.10 | 0.50 | $0 (reported) |
| - | GPT-6 Sol (non-ZDR, disqualified) | 52 | 1 | 1 | 6 | 3 | 2.00 | 10.00 | $0 (reported) |
| - | Claude Fable 5.1 (non-ZDR, disqualified) | 51 | 3 | 0 | 4 | 0 | 10.00 | 50.00 | $0.2380 |
| - | Claude Fable 5 (non-ZDR, disqualified) | 49 | 4 | 1 | 3 | 0 | 10.00 | 50.00 | $0.2345 |

## Same brief plus the house anti-slop rules

Which models perform best once told exactly what slop means?

| Rank | Model | Checks passed (of 54) | Failed | Unresolved | Content ready (of 8) | Ready without edits (of 8) | Input $/M | Output $/M | Observed cost, 8 drafts |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 0 | 0 | 8 | 8 | 10.00 | 50.00 | $0.3581 |
| 2 | GPT-5.6 Sol | 53 | 1 | 0 | 7 | 4 | 4.00 | 20.00 | $0.1903 |
| 3 | GPT-5.6 Luna | 52 | 1 | 1 | 6 | 4 | 0.20 | 1.20 | $0.0081 |
| 4 | GPT-5.6 Terra | 52 | 2 | 0 | 6 | 3 | 2.00 | 12.00 | $0.0780 |
| 5 | Qwen 3.8 Max | 52 | 2 | 0 | 4 | 3 | 2.00 | 6.00 | $0.0866 |
| 6 | Gemini 3.1 Pro | 51 | 2 | 1 | 5 | 5 | 2.00 | 12.00 | $0.1492 |
| 7 | Claude Opus 5.5 | 51 | 2 | 1 | 3 | 3 | 4.00 | 20.00 | $0.2533 |
| 8 | DeepSeek V4 Pro | 51 | 2 | 1 | 4 | 2 | 0.66 | 1.98 | $0.0374 |
| 9 | MiMo V2.6 Pro | 51 | 3 | 0 | 5 | 1 | 0.43 | 0.87 | $0.0166 |
| 10 | Gemini 3.8 Flash | 50 | 3 | 1 | 4 | 3 | 0.75 | 3.75 | $0.0242 |
| 11 | Grok 4.7 | 50 | 3 | 1 | 4 | 2 | 1.20 | 3.60 | $0.0540 |
| 12 | Kimi K3 | 50 | 3 | 1 | 3 | 2 | 3.00 | 15.00 | $0.1180 |
| 13 | DeepSeek V4.1 Flash | 50 | 4 | 0 | 3 | 0 | 0.30 | 1.20 | $0.0084 |
| 14 | Claude Opus 5 | 49 | 4 | 1 | 3 | 3 | 5.00 | 25.00 | $0.2880 |
| 15 | GLM 5.3 | 49 | 5 | 0 | 3 | 2 | 1.40 | 4.40 | $0.0426 |
| 16 | Claude Opus 4.6 | 49 | 5 | 0 | 1 | 1 | 5.00 | 25.00 | $0.1803 |
| 17 | GLM 5.3 Flash | 48 | 6 | 0 | 3 | 2 | 0.15 | 0.50 | $0.0046 |
| 18 | Claude Sonnet 5 | 48 | 5 | 1 | 2 | 0 | 2.00 | 10.00 | $0.1085 |
| 19 | MiniMax M3 | 44 | 9 | 1 | 0 | 0 | 0.30 | 1.20 | $0.0322 |
| 20 | Qwen 3.8 Flash | 41 | 11 | 2 | 0 | 0 | 0.15 | 0.47 | $0.0077 |
| - | GPT-6 Sol (non-ZDR, disqualified) | 53 | 1 | 0 | 7 | 7 | 2.00 | 10.00 | $0 (reported) |
| - | GPT-6 Luna (non-ZDR, disqualified) | 53 | 1 | 0 | 7 | 6 | 0.10 | 0.50 | $0 (reported) |
| - | Muse Spark 1.3 (non-ZDR, disqualified) | 53 | 1 | 0 | 7 | 5 | 1.25 | 4.25 | $0.0572 |
| - | Claude Fable 5 (non-ZDR, disqualified) | 51 | 2 | 1 | 4 | 4 | 10.00 | 50.00 | $0.5413 |
| - | Claude Fable 5.1 (non-ZDR, disqualified) | 50 | 3 | 1 | 3 | 3 | 10.00 | 50.00 | $0.5702 |

