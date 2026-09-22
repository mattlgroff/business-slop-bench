# Assistant comparison: Astra, Kimi and Qwen

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight briefs and both conditions. One generation per cell. Model identities visible; no Jev grades used.

## Complete model samples

| Model | Condition | Content checks | Content ready | Style gate pass | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|
| Qwen Flash | default | 47/54 | 1/8 | 2/8 | 0/8 | $0.00345 |
| Qwen Flash | house | 41/54 | 1/8 | 8/8 | 1/8 | $0.00821 |
| Kimi K3 | default | 51/54 | 5/8 | 4/8 | 4/8 | $0.06553 |
| Kimi K3 | house | 48/54 | 3/8 | 8/8 | 1/8 | $0.10848 |
| Astra | default | 54/54 | 8/8 | 5/8 | 4/8 | $0.10989 |
| Astra | house | 54/54 | 8/8 | 8/8 | 7/8 | $0.36169 |

Content checks include factual support, numbers, conditions, decision requests and ownership. They are overlapping rubric items, not independent trials. Ready without edits also requires the word limit, no unintended placeholders, the style gate and no supported editorial finding. Unresolved checks earn no point; full pass/fail/review counts are in [summary.json](summary.json).

Astra preserved the required content in all sixteen observed drafts. Its house-style sample needed less editing than the other complete samples. Its default outputs still used em dashes, so a content pass is not a style pass. Kimi remains the cheaper option with several usable drafts, but more material errors. This limited unblinded sample does not identify a universal best model.

## Astra evidence and remaining edits

### pilot-client-email / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--pilot-client-email--default.md): 7/7 content checks, 124/180 words, 0 em dashes.

- **Style 16:** [Your approval would establish agreement on the scope and investment while keeping data access contingent on the required clearance.](../../runs/pilot-v10/openai--gpt-6-astra--pilot-client-email--default.md:11). Repeats the immediately preceding conditional approval request and previously stated security prerequisite.

### pilot-client-email / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--pilot-client-email--house.md): 7/7 content checks, 124/180 words, 0 em dashes.

- **Style 16:** [The pilot offers a bounded way to assess invoice handling before considering a production commitment.](../../runs/pilot-v10/openai--gpt-6-astra--pilot-client-email--house.md:7). Repeats the defined assessment period/cost and production exclusion without adding information.

### launch-delay-email / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--launch-delay-email--default.md): 6/6 content checks, 101/180 words, 0 em dashes.

No additional supported editorial finding in this review.

### launch-delay-email / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--launch-delay-email--house.md): 6/6 content checks, 86/180 words, 0 em dashes.

No additional supported editorial finding in this review.

### vendor-decision-memo / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--vendor-decision-memo--default.md): 6/6 content checks, 188/300 words, 0 em dashes.

No additional supported editorial finding in this review.

### vendor-decision-memo / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--vendor-decision-memo--house.md): 6/6 content checks, 164/300 words, 0 em dashes.

No additional supported editorial finding in this review.

### pilot-results-memo / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--pilot-results-memo--default.md): 7/7 content checks, 212/300 words, 2 em dashes.

No additional supported editorial finding in this review.

### pilot-results-memo / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--pilot-results-memo--house.md): 7/7 content checks, 151/300 words, 0 em dashes.

No additional supported editorial finding in this review.

### discovery-proposal / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--discovery-proposal--default.md): 7/7 content checks, 140/350 words, 0 em dashes.

No additional supported editorial finding in this review.

### discovery-proposal / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--discovery-proposal--house.md): 7/7 content checks, 120/350 words, 0 em dashes.

No additional supported editorial finding in this review.

### change-order / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--change-order--default.md): 7/7 content checks, 157/300 words, 0 em dashes.

No additional supported editorial finding in this review.

### change-order / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--change-order--house.md): 7/7 content checks, 149/300 words, 0 em dashes.

No additional supported editorial finding in this review.

### ai-strategy-slides / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--ai-strategy-slides--default.md): 7/7 content checks, 200/350 words, 5 em dashes.

No additional supported editorial finding in this review.

### ai-strategy-slides / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--ai-strategy-slides--house.md): 7/7 content checks, 178/350 words, 0 em dashes.

No additional supported editorial finding in this review.

### handoff-slides / default

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--handoff-slides--default.md): 7/7 content checks, 266/350 words, 4 em dashes.

- **Style 13:** [No further action identified in the source pack](../../runs/pilot-v10/openai--gpt-6-astra--handoff-slides--default.md:9). References the model input packet inside a finished steering-committee deliverable. State that the runbook criterion is met.

### handoff-slides / house

[Draft](../../runs/pilot-v10/openai--gpt-6-astra--handoff-slides--house.md): 7/7 content checks, 178/350 words, 0 em dashes.

No additional supported editorial finding in this review.

## Interpretation boundaries

- Handoff default Qwen: No further criteria exist is accepted as referring to the two supplied acceptance criteria, not unknown external policy. This revises the earlier tentative editorial concern.
- Matched-ticket randomization is treated as a new delivery commitment when asserted as what the test will do, rather than labelled as a proposed design.
- C01 for results requires the stated delta (3 minutes or 20%), not just endpoints from which a reader could calculate it.
- Astra launch default: personal confidence is an opinion invited by the brief. It does not invent objective claims of team performance or review quality, unlike earlier failed reassurance passages.
- Astra change-order default: signature/date blanks are intentional approval form fields, not leaked drafting placeholders.
- Astra content checks all pass in this one observed sample. That is not proof of general accuracy, a complete writing-quality score, or an independently validated result.

Opus still has only three graded emails; all exceed the word limit. Do not compare that partial sample as if it covered all eight briefs. Its incomplete collection is preserved in [previous report](../assistant-v2/REPORT.md).

Cost is the original successful generation charge for each represented draft, including reused originals once in this comparison. It excludes failed attempts, judge diagnostics, and earlier superseded slide drafts. The shared budget ledger remains authoritative for the spending ceiling.
