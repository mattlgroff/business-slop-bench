# Assistant comparison: Sol and Terra added

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.

## Completed eight-draft conditions

| Model | Condition | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|
| Astra | default | 54/54 | 0 | 0 | 8/8 | 4/8 | $0.10989 |
| Astra | house | 54/54 | 0 | 0 | 8/8 | 7/8 | $0.36169 |
| Sol | default | 52/54 | 1 | 1 | 6/8 | 2/8 | $0.06108 |
| Sol | house | 53/54 | 1 | 0 | 7/8 | 6/8 | $0.18847 |
| Terra | default | 52/54 | 1 | 1 | 6/8 | 1/8 | $0.02792 |
| Terra | house | 52/54 | 1 | 1 | 6/8 | 5/8 | $0.07715 |
| Luna | default | 52/54 | 1 | 1 | 5/8 | 2/8 | $0.00324 |
| Luna | house | 51/54 | 1 | 2 | 5/8 | 3/8 | $0.00817 |
| Kimi K3 | default | 51/54 | 2 | 1 | 5/8 | 4/8 | $0.06553 |
| Kimi K3 | house | 48/54 | 6 | 0 | 3/8 | 1/8 | $0.10848 |
| Qwen Flash | default | 47/54 | 7 | 0 | 1/8 | 0/8 | $0.00345 |
| Qwen Flash | house | 41/54 | 12 | 1 | 1/8 | 1/8 | $0.00821 |
| DeepSeek Flash | default | 50/54 | 4 | 0 | 4/8 | 0/8 | $0.00243 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

Sol preserves the supplied facts in most drafts but misses the required time reduction calculation in both readouts. Terra includes the calculation, but its strategy slides introduce an inconsistent quarter and an unsupported authorization claim. Both have stronger house-style readiness than Luna in this sample, at higher observed generation cost. This is not a reliability ranking from repeated trials.

## New review evidence

### Sol / pilot-client-email / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-client-email--default.md): 7/7 content checks, 122/180 words, 0 em dashes.

- **Style 16:** [Once approved, we can move the discussion forward.](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-client-email--default.md:9). Tautological closing adds no next action or information beyond the approval request.

### Sol / pilot-client-email / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-client-email--house.md): 7/7 content checks, 101/180 words, 0 em dashes.

- **Style 21:** [the client’s goal](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-client-email--house.md:5). Refers to the client in the third person while addressing that client directly; your goal fits the audience.

### Sol / launch-delay-email / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--launch-delay-email--default.md): 5/6 content checks, 114/180 words, 0 em dashes.

- **grounding review:** [The team remains focused on launch readiness](../../runs/pilot-v15/openai--gpt-5.6-sol--launch-delay-email--default.md:7). Current team focus is not supplied; ordinary reassurance is a plausible reading, so this is unresolved rather than a confirmed invention.

### Sol / launch-delay-email / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--launch-delay-email--house.md): 6/6 content checks, 77/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / vendor-decision-memo / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--vendor-decision-memo--default.md): 6/6 content checks, 183/300 words, 2 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / vendor-decision-memo / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--vendor-decision-memo--house.md): 6/6 content checks, 103/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / pilot-results-memo / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-results-memo--default.md): 6/7 content checks, 136/300 words, 0 em dashes.

- **C01 fail:** [12 minutes across 100 tickets, compared with 15 minutes](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-results-memo--default.md:7). Reports endpoints but omits the required 3-minute or 20% reduction.

### Sol / pilot-results-memo / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-results-memo--house.md): 6/7 content checks, 125/300 words, 0 em dashes.

- **C01 fail:** [12 minutes across 100 tickets, compared with 15 minutes](../../runs/pilot-v15/openai--gpt-5.6-sol--pilot-results-memo--house.md:5). Reports endpoints but omits the required 3-minute or 20% reduction.

### Sol / discovery-proposal / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--discovery-proposal--default.md): 7/7 content checks, 144/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / discovery-proposal / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--discovery-proposal--house.md): 7/7 content checks, 118/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / change-order / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--change-order--default.md): 7/7 content checks, 170/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / change-order / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--change-order--house.md): 7/7 content checks, 138/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / ai-strategy-slides / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--ai-strategy-slides--default.md): 7/7 content checks, 174/350 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / ai-strategy-slides / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--ai-strategy-slides--house.md): 7/7 content checks, 156/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / handoff-slides / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--handoff-slides--default.md): 7/7 content checks, 203/350 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Sol / handoff-slides / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-sol--handoff-slides--house.md): 7/7 content checks, 168/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / pilot-client-email / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--pilot-client-email--default.md): 7/7 content checks, 148/180 words, 0 em dashes.

- **Style 2:** [I’m writing to request approval](../../runs/pilot-v15/openai--gpt-5.6-terra--pilot-client-email--default.md:5). Unnecessary announcement of writing the request.
- **Style 21:** [the client’s target](../../runs/pilot-v15/openai--gpt-5.6-terra--pilot-client-email--default.md:7). Third-person client reference inside an email directly to the client.

### Terra / pilot-client-email / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--pilot-client-email--house.md): 7/7 content checks, 113/180 words, 0 em dashes.

- **Style 21:** [the client’s 20% reduction goal](../../runs/pilot-v15/openai--gpt-5.6-terra--pilot-client-email--house.md:5). Third-person client reference inside an email directly to the client.

### Terra / launch-delay-email / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--launch-delay-email--default.md): 5/6 content checks, 120/180 words, 0 em dashes.

- **grounding review:** [The team remains focused and is continuing to prepare for release.](../../runs/pilot-v15/openai--gpt-5.6-terra--launch-delay-email--default.md:7). Current focus and preparation are not supplied; this may be routine reassurance rather than a material status assertion.

### Terra / launch-delay-email / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--launch-delay-email--house.md): 5/6 content checks, 90/180 words, 0 em dashes.

- **grounding review:** [release requires Nia’s completed approval](../../runs/pilot-v15/openai--gpt-5.6-terra--launch-delay-email--house.md:3). The source makes Nia review owner without explicitly naming the approval authority. This may be shorthand for completion of her review or a new authority assignment.

### Terra / vendor-decision-memo / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--vendor-decision-memo--default.md): 6/6 content checks, 187/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / vendor-decision-memo / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--vendor-decision-memo--house.md): 6/6 content checks, 107/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / pilot-results-memo / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--pilot-results-memo--default.md): 7/7 content checks, 188/300 words, 1 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / pilot-results-memo / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--pilot-results-memo--house.md): 7/7 content checks, 116/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / discovery-proposal / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--discovery-proposal--default.md): 7/7 content checks, 221/350 words, 0 em dashes.

- **Style 10:** [Upon kickoff, the initial 50% payment is due. The remaining 50% is due on delivery of the three agreed discovery artifacts.](../../runs/pilot-v15/openai--gpt-5.6-terra--discovery-proposal--default.md:40). Repeats the payment terms already given in the commercial table after the next-step sequence.

### Terra / discovery-proposal / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--discovery-proposal--house.md): 7/7 content checks, 159/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / change-order / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--change-order--default.md): 7/7 content checks, 160/300 words, 0 em dashes.

- **Style 16:** [The proposed change includes work to add the CRM connector.](../../runs/pilot-v15/openai--gpt-5.6-terra--change-order--default.md:9). Repeats the requested connector addition stated immediately above without adding scope detail.

### Terra / change-order / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--change-order--house.md): 7/7 content checks, 132/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / ai-strategy-slides / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--ai-strategy-slides--default.md): 6/7 content checks, 166/350 words, 4 em dashes.

- **grounding fail:** [Why Not Customer Credit Decisions This Quarter](../../runs/pilot-v15/openai--gpt-5.6-terra--ai-strategy-slides--default.md:14). Changes the planning horizon in this heading to this quarter; the corrected brief and the opening slide consistently concern next quarter.

### Terra / ai-strategy-slides / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--ai-strategy-slides--house.md): 6/7 content checks, 146/350 words, 0 em dashes.

- **grounding fail:** [select the authorized knowledge search pilot](../../runs/pilot-v15/openai--gpt-5.6-terra--ai-strategy-slides--house.md:17). The source authorizes the policy documents, not the pilot itself. COO selection is still requested.

### Terra / handoff-slides / default

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--handoff-slides--default.md): 7/7 content checks, 212/350 words, 4 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Terra / handoff-slides / house

[Draft](../../runs/pilot-v15/openai--gpt-5.6-terra--handoff-slides--house.md): 7/7 content checks, 148/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

## Adjudication boundaries

- Team-focus claims remain unresolved consistently with the Luna review. Personal confidence is distinct from objective performance claims.
- Terra launch house: Nia review ownership may or may not imply approval authority. This is unresolved, not a forced failure.
- Terra this-quarter heading is penalized because the revised source no longer contains the earlier quarter ambiguity.
- Naming a pilot as authorized is distinct from recommending it or using approved source documents.

[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Partial Opus, Fable and DeepSeek house coverage remains separate. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
