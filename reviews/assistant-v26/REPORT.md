# Uncapped comparison: Astra added

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.

## Uncapped results

| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Muse | default | 8/8 | 53/54 | 1 | 0 | 7/8 | 4/8 | $0.03816 |
| Muse | house | 8/8 | 53/54 | 1 | 0 | 7/8 | 5/8 | $0.05720 |
| Gemini Flash | default | 8/8 | 51/54 | 2 | 1 | 5/8 | 0/8 | $0.01866 |
| Gemini Flash | house | 8/8 | 50/54 | 3 | 1 | 4/8 | 3/8 | $0.02418 |
| Luna | default | 8/8 | 51/54 | 2 | 1 | 5/8 | 2/8 | $0.00313 |
| Luna | house | 8/8 | 52/54 | 1 | 1 | 6/8 | 4/8 | $0.00809 |
| Qwen Flash | default | 8/8 | 46/54 | 8 | 0 | 0/8 | 0/8 | $0.00376 |
| Qwen Flash | house | 8/8 | 41/54 | 11 | 2 | 0/8 | 0/8 | $0.00774 |
| Qwen Max | default | 8/8 | 49/54 | 5 | 0 | 3/8 | 1/8 | $0.02687 |
| Qwen Max | house | 8/8 | 52/54 | 2 | 0 | 4/8 | 3/8 | $0.08665 |
| GLM Flash | default | 8/8 | 49/54 | 3 | 2 | 4/8 | 1/8 | $0.00187 |
| GLM Flash | house | 8/8 | 48/54 | 6 | 0 | 3/8 | 2/8 | $0.00459 |
| GLM 5.3 | default | 8/8 | 52/54 | 2 | 0 | 4/8 | 1/8 | $0.01492 |
| GLM 5.3 | house | 8/8 | 49/54 | 5 | 0 | 3/8 | 2/8 | $0.04255 |
| DeepSeek Flash | default | 8/8 | 52/54 | 2 | 0 | 5/8 | 0/8 | $0.00286 |
| DeepSeek Flash | house | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.00837 |
| DeepSeek Pro | default | 8/8 | 51/54 | 1 | 2 | 3/8 | 1/8 | $0.00903 |
| DeepSeek Pro | house | 8/8 | 51/54 | 2 | 1 | 4/8 | 2/8 | $0.03741 |
| Kimi K3 | default | 8/8 | 51/54 | 3 | 0 | 4/8 | 0/8 | $0.05660 |
| Kimi K3 | house | 8/8 | 50/54 | 3 | 1 | 3/8 | 2/8 | $0.11798 |
| MiniMax | default | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.03275 |
| MiniMax | house | 8/8 | 44/54 | 9 | 1 | 0/8 | 0/8 | $0.03217 |
| Grok | default | 8/8 | 52/54 | 2 | 0 | 6/8 | 3/8 | $0.01822 |
| Grok | house | 7/8 | 43/47 | 3 | 1 | 3/7 | 2/7 | $0.04831 |
| Astra | default | 8/8 | 54/54 | 0 | 0 | 8/8 | 4/8 | $0.11204 |
| Astra | house | 8/8 | 54/54 | 0 | 0 | 8/8 | 8/8 | $0.35814 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax, Grok and Astra are new uncapped generations on each attempted cell; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### Astra / pilot-client-email / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--pilot-client-email--default.md): 7/7 content checks, 137/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / pilot-client-email / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--pilot-client-email--house.md): 7/7 content checks, 118/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / launch-delay-email / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--launch-delay-email--default.md): 6/6 content checks, 106/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / launch-delay-email / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--launch-delay-email--house.md): 6/6 content checks, 86/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / vendor-decision-memo / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--vendor-decision-memo--default.md): 6/6 content checks, 194/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / vendor-decision-memo / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--vendor-decision-memo--house.md): 6/6 content checks, 161/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / pilot-results-memo / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--pilot-results-memo--default.md): 7/7 content checks, 191/300 words, 1 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / pilot-results-memo / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--pilot-results-memo--house.md): 7/7 content checks, 149/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / discovery-proposal / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--discovery-proposal--default.md): 7/7 content checks, 133/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / discovery-proposal / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--discovery-proposal--house.md): 7/7 content checks, 104/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / change-order / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--change-order--default.md): 7/7 content checks, 184/300 words, 0 em dashes.

- **Style 10:** [This change order proposes adding the CRM connector.](../../runs/pilot-v20/openai--gpt-6-astra--change-order--default.md:9). Restates the heading and the preceding paragraph without adding information.

### Astra / change-order / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--change-order--house.md): 7/7 content checks, 144/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / ai-strategy-slides / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--ai-strategy-slides--default.md): 7/7 content checks, 204/350 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / ai-strategy-slides / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--ai-strategy-slides--house.md): 7/7 content checks, 162/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Astra / handoff-slides / default

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--handoff-slides--default.md): 7/7 content checks, 265/350 words, 6 em dashes.

- **Style 10:** [- **Ownership transition:** Lee owns defect fixes until acceptance; Jo owns incidents only after acceptance.](../../runs/pilot-v20/openai--gpt-6-astra--handoff-slides--default.md:31). Slide 4 repeats the acceptance gate from slide 1 and the ownership boundaries from slide 2.

### Astra / handoff-slides / house

[Draft](../../runs/pilot-v20/openai--gpt-6-astra--handoff-slides--house.md): 7/7 content checks, 177/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

## Adjudication boundaries

Astra passes 54/54 content checks in both conditions with no failures and no unresolved checks. All 16 drafts are content ready. Ready-without-edits counts are 4/8 default and 8/8 house: the default readout, strategy deck and handoff deck carry em dashes, and the default change order and handoff deck each have one repetition finding. Default drafts contain 11 em dashes; house drafts contain none. Every response has a normal stop reason, no warnings, matching requested, returned and canonical identities, and no reasoning tokens reported.

Both readouts state the 3-minute or 20% reduction and the 5-point quality decline explicitly. The pilot emails label the 20% figure as a target rather than a promised result. The vendor memos keep CFO approval before signing without naming a signatory. The handoff decks name the missing rehearsal organizer and route the assignment through Pat. No draft invents a date, deadline, readiness state, prior discussion or ownership beyond the source pack.

This is the first uncapped sample in the cohort with every draft content ready. It is one generation per cell, graded unblinded by the same reviewer, and it does not establish repeatability; the capped Astra sample in assistant-v12 also scored 54/54 in both conditions. Astra generation charges are the highest in the cohort by a wide margin.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
