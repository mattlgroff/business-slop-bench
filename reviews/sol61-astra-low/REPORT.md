# GPT-6.1 Sol versus fresh Astra, low reasoning

September 29, 2026. Every model writes all eight frozen briefs once in both conditions. Both request low reasoning. All sixteen paired inputs match exactly. No output-token cap, generation deadline, retry or replacement of historical primary results. All 32 generations completed with normal stops and distinct generation IDs.

| Model | Condition | Checks | Content ready | Ready without edits | Em dashes | Reported charge |
|---|---|---:|---:|---:|---:|---:|
| Sol 6.1 | default | 53/54 | 7/8 | 2/8 | 9 | $0.021788 |
| Sol 6.1 | house | 54/54 | 7/8 | 4/8 | 0 | $0.072768 |
| Astra fresh sample 3 | default | 54/54 | 6/8 | 2/8 | 9 | $0.112390 |
| Astra fresh sample 3 | house | 54/54 | 8/8 | 6/8 | 0 | $0.358840 |

Content ready requires all content checks, the word limit and no authoring residue. Ready without edits additionally requires no style-gate violations and no supported editorial findings. Every draft meets the word limit. The Sol plain launch reassurance remains unresolved, not a confirmed fabrication. Astra states personal confidence in its team rather than asserting an unsupplied operational status; the brief expressly asks for confidence.

House Astra needs two editorial edits: generic progress commentary in the launch email and a repeated savings caution in the pilot readout. House Sol needs three repetition edits and removal of a source-pack reference in the handoff deck. Default Astra has source-pack residue in its vendor memo and handoff deck. Necessary factual contrasts and intentional signature fields are allowed.

These are provisional, unblinded assistant judgments on one fixed panel, not independent evidence of a population win rate. The original Astra house result was 8/8 ready without edits; its prior full repeat was 6/8. This third sample is reported separately, without replacing either.

## Astra findings

### pilot-client-email / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--pilot-client-email--default--sample-3.md): 7/7 content checks; 131/180 words; 0 em dashes.

- Style 10: Your approval would move the proposal forward while keeping data access conditional on security approval and production rollout outside this engagement. Closing recap repeats the approval request, security gate and exclusion without a new action.

### pilot-client-email / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--pilot-client-email--house--sample-3.md): 7/7 content checks; 114/180 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### launch-delay-email / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--launch-delay-email--default--sample-3.md): 6/6 content checks; 106/180 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### launch-delay-email / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--launch-delay-email--house--sample-3.md): 6/6 content checks; 81/180 words; 0 em dashes.

- Style 16: That gives us a concrete next step while Nia completes the review. Generic progress commentary restates the offered demo and ongoing review without new information.

### vendor-decision-memo / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--vendor-decision-memo--default--sample-3.md): 6/6 content checks; 236/300 words; 0 em dashes.

- Style 10: The decision should therefore prioritize compliance with the stated constraints rather than the lowest price. Standalone recap repeats the mandatory-SSO rationale already explained. The contrast itself is a necessary decision boundary, not empty negative parallelism.
- Authoring residue: based on the source pack Internal source-pack reference belongs to the drafting process, not the CFO memo.

### vendor-decision-memo / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--vendor-decision-memo--house--sample-3.md): 6/6 content checks; 164/300 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### pilot-results-memo / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--pilot-results-memo--default--sample-3.md): 7/7 content checks; 199/300 words; 1 em dashes.

- Style 10: Revisit the scaling decision using those results, keeping any efficiency gains distinct from measured financial savings. Final sentence repeats follow-up-based scaling and the stated absence of measured savings.

### pilot-results-memo / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--pilot-results-memo--house--sample-3.md): 7/7 content checks; 141/300 words; 0 em dashes.

- Style 10: do not treat the observed time reduction as measured cash savings. Closing caution repeats the already explicit absence of measured cash savings. Apply the same removable-recap boundary used for Sol.

### discovery-proposal / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--discovery-proposal--default--sample-3.md): 7/7 content checks; 141/350 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### discovery-proposal / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--discovery-proposal--house--sample-3.md): 7/7 content checks; 120/350 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### change-order / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--change-order--default--sample-3.md): 7/7 content checks; 195/300 words; 0 em dashes.

- Style 10: This change order proposes adding the requested CRM connector. Separate sentence repeats the immediately preceding requested connector scope without adding terms.

### change-order / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--change-order--house--sample-3.md): 7/7 content checks; 148/300 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### ai-strategy-slides / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--ai-strategy-slides--default--sample-3.md): 7/7 content checks; 192/350 words; 4 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### ai-strategy-slides / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--ai-strategy-slides--house--sample-3.md): 7/7 content checks; 155/350 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

### handoff-slides / default

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--handoff-slides--default--sample-3.md): 7/7 content checks; 235/350 words; 4 em dashes.

- Authoring residue: No further action identified in the source pack Internal source-pack reference is authoring residue in the committee deck.

### handoff-slides / house

[Draft](../../runs/pilot-v27/openai--gpt-6-astra--handoff-slides--house--sample-3.md): 7/7 content checks; 181/350 words; 0 em dashes.

No supported judgment findings. Mechanical punctuation violations, if any, remain separate.

[Sol findings](../assistant-v47/REPORT.md), [all comparison grades](grades.json), [paired-input verification](verification.json), [frozen plan](plan.json).
