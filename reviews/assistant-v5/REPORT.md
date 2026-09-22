# Assistant comparison: completed default samples

Provisional assistant-authored grades, not human gold or independent benchmark validation. Model identities visible; no Jev calls. Same corrected eight-brief task set.

## Default condition: eight drafts each

| Model | Content checks passed | Content ready | Ready without edits | Generation cost |
|---|---:|---:|---:|---:|
| Qwen Flash | 47/54 | 1/8 | 0/8 | $0.00345 |
| Kimi K3 | 51/54 | 5/8 | 4/8 | $0.06553 |
| Astra | 54/54 | 8/8 | 4/8 | $0.10989 |
| DeepSeek Flash | 50/54 | 4/8 | 0/8 | $0.00243 |

Content ready requires every task-content check, word-limit compliance and no unintended placeholders. Ready without edits also requires the house-style gate and no supported editorial finding. Default outputs did not receive house-style instructions, so those style results measure natural fit rather than explicit compliance. Unresolved checks earn no credit and remain separate in [summary.json](summary.json).

DeepSeek preserves many of the required facts at low generation cost. It still invents prior discussions and team-performance context, omits the requested time reduction calculation, and overstates next-quarter pilot feasibility. Several otherwise correct outputs need substantial repetition or structure edits. Its house condition remains only 1/8 collected; no overall default-versus-house conclusion is justified.

## New evidence

### vendor-decision-memo

[Draft](../../runs/pilot-v12/deepseek--deepseek-v4.1-flash--vendor-decision-memo--default.md): 6/6 content checks; 289/300 words; 0 em dashes.

- **Style 16:** [Alpha totals $92,000; Beta totals $70,000.](../../runs/pilot-v12/deepseek--deepseek-v4.1-flash--vendor-decision-memo--default.md:23). Repeats table totals and SSO comparison through several analysis and recommendation paragraphs.
- **Style 13:** [not established in the source pack](../../runs/pilot-v12/deepseek--deepseek-v4.1-flash--vendor-decision-memo--default.md:27). Refers to the model input packet inside a finished CFO memo.

### pilot-results-memo

[Draft](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--pilot-results-memo--default.md): 6/7 content checks; 228/300 words; 0 em dashes.

- **C01 fail:** [fell from 15 to 12 minutes](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--pilot-results-memo--default.md:7). Reports endpoints but not the required reduction of 3 minutes or 20%.
- **Style 10:** [**Conclusion**](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--pilot-results-memo--default.md:13). Repeats the no-scale recommendation, confounding, quality threshold and unmeasured savings already explained.

### discovery-proposal

[Draft](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--discovery-proposal--default.md): 7/7 content checks; 152/350 words; 1 em dashes.

- **Style 15:** [**Decision Requested**](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--discovery-proposal--default.md:41). Nine labelled sections in a short proposal include repeated opening and closing approval requests; consolidate sections without losing terms.

### change-order

[Draft](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--change-order--default.md): 7/7 content checks; 160/300 words; 0 em dashes.

- **Style 16:** [| Estimated effort | 40 hours |](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--change-order--default.md:16). The price table repeats all three quantities immediately after the price paragraph.

### ai-strategy-slides

[Draft](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--ai-strategy-slides--default.md): 6/7 content checks; 161/350 words; 4 em dashes.

- **grounding fail:** [Only Option A is executable next quarter.](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--ai-strategy-slides--default.md:21). Pending production approval does not establish that every other pilot is impossible throughout next quarter.

### handoff-slides

[Draft](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--handoff-slides--default.md): 7/7 content checks; 261/350 words; 2 em dashes.

- **Style 25:** [Option C: Reject handoff permanently.](../../runs/pilot-v13/deepseek--deepseek-v4.1-flash--handoff-slides--default.md:26). Adds an unsupported permanent-rejection option to create a three-option framework; it contributes no useful decision alternative.

## Collection boundaries

The runner now accepts a specific brief and condition. Unknown values fail instead of broadening the paid run. The vendor-house request timed out, like the earlier launch-house request. Targeted default collection then completed the untouched briefs without retrying either failed house request.

All grades in [grades.json](grades.json) retain exact output hashes and prior-review provenance. Remaining failed and unattempted cases are ungraded. See the [matched first-email comparison](../assistant-v4/REPORT.md) for the partial Fable and Opus samples.
