# BusinessSlopBench smoke results

Built September 22, 2026. The current frozen comparison is pilot-v4. Earlier versions are development diagnostics, not additional benchmark samples.

The TypeScript AI SDK runner, 21-model roster, eight synthetic briefs, two writing conditions, frozen Zero Defect rubric, Jev judging, saved evidence and cumulative $20 guard are implemented. Qwen Flash completed both conditions. Opus 5 completed the default condition; the house condition returned Gateway 429 twice. The broad model run has not started, following the agreed smoke-first sequence.

| Model | Condition | Words (limit 180) | Em dashes | Reported generation cost | Evidence |
|---|---|---:|---:|---:|---|
| alibaba/qwen3.8-flash | default | 148 | 0 | $0.000620 | [Draft](runs/pilot-v4/alibaba--qwen3.8-flash--pilot-client-email--default.md), [scores](runs/pilot-v4/score--alibaba--qwen3.8-flash--pilot-client-email--default.json) |
| alibaba/qwen3.8-flash | house | 107 | 0 | $0.001007 | [Draft](runs/pilot-v4/alibaba--qwen3.8-flash--pilot-client-email--house.md), [scores](runs/pilot-v4/score--alibaba--qwen3.8-flash--pilot-client-email--house.json) |
| anthropic/claude-opus-5 | default | 191 | 3 | $0.011280 | [Draft](runs/pilot-v4/anthropic--claude-opus-5--pilot-client-email--default.md), [scores](runs/pilot-v4/score--anthropic--claude-opus-5--pilot-client-email--default.json) |
| anthropic/claude-opus-5 | house | Unavailable | Unavailable | Unreconciled | Gateway 429 twice: No access to this model at this time |

## What this establishes

The character scanner and word-count checks expose Opus's three em dashes and 191-word output. Its sentence “No variable costs, no overrun exposure” also adds assurances beyond the supplied fixed-fee fact; Jev flags the broader grounding criterion. That semantic judgment remains provisional. A single brief does not establish relative model quality.

Qwen's default draft adds unsupported prior-discussion and risk-strategy claims. Jev flags grounding and verbosity. The house draft has no literal style-gate violations; Jev flags an unnecessary table. Human review is still needed to assess whether these semantic judgments and the acceptance criteria match the intended standard.

## Grader diagnostics

The final calibration has 45/48 matching control labels and 3 unresolved, with 0 opposite definitive grades. Two empty-output checks use deterministic failure while retaining Jev's raw responses. On the separate validation subset, coverage is 86.4% with no opposite definitive grades. Labels were authored during this task, not provided or validated by a human. Validation cases were inspected during v2; this is not a blind generalization claim.

Thresholds were fitted using development labels only: pass probability at least 0.585, fail probability at most 0.485, otherwise unresolved. These are operating thresholds, not calibrated statistical confidence. Raw probabilities, criterion polarity and exact inputs are archived.

## Operational findings and cost

The first raw-lens house prompt caused Qwen to emit a review audit. It was replaced with writer-facing rules preserving the source categories and exceptions. Those initial outputs remain in pilot-v1. No outputs were silently replaced.

Jev intermittently returned HTTP 503, including on small requests, so request size was not established as the cause. Fixed batches of 16 make grading resumable. Manual retries preserved prior reservations and reused completed outputs and batches. Those failures are saved separately. The bounded Opus availability retry also failed, so no further calls were made to Opus, Astra or Fable.

Gateway-reported successful-call charges across development and smoke runs total $0.06501931. Failed-call charges remain unreconciled. Conservative budget accounting is $1.312162922, including retained reservations. The cumulative ceiling remains $20. Optional reporting tags were removed after the first smoke revealed tag-write surcharges. Jev is currently promotional/free on the observed calls; the guard still budgets its listed paid rate.

## Verification and remaining work

TypeScript checking and six focused tests passed. They cover spending persistence and bounds, probability polarity and abstention, threshold fitting, source-category preservation, identical task facts across conditions, scan anchors, and residue detection. Successful live calls verified credential loading, generation, Jev grading, evidence saving and returned cost metadata.

The runner's numerical criteria currently ask Jev to compare claims with fixed expected facts. They do not constitute a general deterministic arithmetic parser. The corpus includes mathematically checkable totals, but the automated content verdict remains provisional.

The full 336-output screen is unrun. Resolve the Opus Gateway availability issue before continuing the agreed smoke-first sequence. A benchmark claim about model quality also needs human validation of the briefs, style interpretations and grader controls. All raw files stay local; no repository has been published.
