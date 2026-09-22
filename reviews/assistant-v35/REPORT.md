# Readout grounding correction

Provisional assistant-authored grades, not human gold or independent benchmark validation.

Fable 5 labels the pilot sample "Adequate for a pilot." The source supplies ticket counts but no sample-adequacy criterion or evidence. This is an unsupported factual assessment under the existing grounding rule.

[Exact passage, line 10](../../runs/pilot-v21/anthropic--claude-fable-5--pilot-results-memo--default.md:10). The output hash and quote location were verified.

Fable 5 default changes from 50/54 to 49/54 content checks and from 4/8 to 3/8 content-ready drafts. Ready without edits remains 0/8. Fable remains non-ZDR and disqualified regardless of these writing scores. No other model score changes.

## Follow-up-study language reviewed

Claims that a matched follow-up will isolate the true effect deserve closer review, but an objective for a proposed study is different from a promise of conclusive results. No blanket keyword rule was applied. The MiniMax default and Fable 5 house readouts remain candidates for reviewer calibration; their grades are unchanged in this correction.

Opus 5 house refers to isolating the handling-time difference rather than expressly promising the true causal effect. Fable 5.1 default describes what the proposed study should test. Conditional rules that permit scaling only if results meet criteria do not guarantee that those results will occur. These cases were left unchanged.

For methodological background, [Austin (2011)](https://pubmed.ncbi.nlm.nih.gov/21818162/) discusses matching methods for reducing confounding in observational studies. This benchmark does not specify a propensity-score design, and that reference is not an additional requirement imposed on writers. The correction above follows solely from the supplied source pack.

[Corrected cumulative grades](grades.json), [summary](summary.json), and [explicit correction](correction.json). All 303 other rows are unchanged; earlier style-exception corrections remain applied. No paid request was made for this audit.

## Current reviewed comparison

| Model | Condition | Checks passed | Content ready | Ready without edits |
|---|---|---:|---:|---:|
| Muse (non-ZDR, disqualified) | default | 53/54 | 7/8 | 4/8 |
| Muse (non-ZDR, disqualified) | house | 53/54 | 7/8 | 5/8 |
| Gemini Flash | default | 51/54 | 5/8 | 0/8 |
| Gemini Flash | house | 50/54 | 4/8 | 3/8 |
| Luna | default | 51/54 | 5/8 | 2/8 |
| Luna | house | 52/54 | 6/8 | 4/8 |
| Qwen Flash | default | 46/54 | 0/8 | 0/8 |
| Qwen Flash | house | 41/54 | 0/8 | 0/8 |
| Qwen Max | default | 49/54 | 3/8 | 1/8 |
| Qwen Max | house | 52/54 | 4/8 | 3/8 |
| GLM Flash | default | 49/54 | 4/8 | 1/8 |
| GLM Flash | house | 48/54 | 3/8 | 2/8 |
| GLM 5.3 | default | 52/54 | 4/8 | 1/8 |
| GLM 5.3 | house | 49/54 | 3/8 | 2/8 |
| DeepSeek Flash | default | 52/54 | 5/8 | 0/8 |
| DeepSeek Flash | house | 50/54 | 3/8 | 0/8 |
| DeepSeek Pro | default | 51/54 | 3/8 | 1/8 |
| DeepSeek Pro | house | 51/54 | 4/8 | 2/8 |
| Kimi K3 | default | 51/54 | 4/8 | 0/8 |
| Kimi K3 | house | 50/54 | 3/8 | 2/8 |
| MiniMax | default | 50/54 | 3/8 | 0/8 |
| MiniMax | house | 44/54 | 0/8 | 0/8 |
| Grok | default | 52/54 | 6/8 | 3/8 |
| Grok | house | 50/54 | 4/8 | 2/8 |
| Astra | default | 54/54 | 8/8 | 4/8 |
| Astra | house | 54/54 | 8/8 | 8/8 |
| Opus 5 | default | 49/54 | 1/8 | 0/8 |
| Opus 5 | house | 49/54 | 3/8 | 3/8 |
| Opus 4.6 | default | 49/54 | 2/8 | 0/8 |
| Opus 4.6 | house | 49/54 | 1/8 | 1/8 |
| Fable 5.1 (non-ZDR, disqualified) | default | 51/54 | 4/8 | 0/8 |
| Fable 5.1 (non-ZDR, disqualified) | house | 50/54 | 3/8 | 3/8 |
| Fable 5 (non-ZDR, disqualified) | default | 49/54 | 3/8 | 0/8 |
| Fable 5 (non-ZDR, disqualified) | house | 51/54 | 4/8 | 4/8 |
| Opus 5.5 | default | 52/54 | 4/8 | 2/8 |
| Opus 5.5 | house | 51/54 | 3/8 | 3/8 |
| Terra | default | 52/54 | 6/8 | 3/8 |
| Terra | house | 52/54 | 6/8 | 3/8 |

This table covers the 304 reviewed drafts in assistant-v34 plus the correction above. Concurrent collections are not included until reviewed.
