# Assistant comparison: Gemini Flash added

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
| Gemini Flash | default | 51/54 | 2 | 1 | 5/8 | 1/8 | $0.02266 |
| Gemini Flash | house | 51/54 | 3 | 0 | 5/8 | 3/8 | $0.02413 |
| GLM Flash | default | 48/54 | 6 | 0 | 3/8 | 0/8 | $0.00129 |
| GLM Flash | house | 46/54 | 7 | 1 | 2/8 | 1/8 | $0.00448 |
| Luna | default | 52/54 | 1 | 1 | 5/8 | 2/8 | $0.00324 |
| Luna | house | 51/54 | 1 | 2 | 5/8 | 3/8 | $0.00817 |
| Kimi K3 | default | 51/54 | 2 | 1 | 5/8 | 4/8 | $0.06553 |
| Kimi K3 | house | 48/54 | 6 | 0 | 3/8 | 1/8 | $0.10848 |
| Qwen Flash | default | 47/54 | 7 | 0 | 1/8 | 0/8 | $0.00345 |
| Qwen Flash | house | 41/54 | 12 | 1 | 1/8 | 1/8 | $0.00821 |
| DeepSeek Flash | default | 50/54 | 4 | 0 | 4/8 | 0/8 | $0.00243 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

Gemini Flash preserves many source constraints but still uses redundant openings and can omit the explicit reduction calculation. House-style readiness and content readiness are reported separately; this single sample does not establish reliability.

## New review evidence

### Gemini Flash / pilot-client-email / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-client-email--default.md): 7/7 content checks, 105/180 words, 0 em dashes.

- **Style 2:** [I am writing to propose](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-client-email--default.md:5). Unnecessary announcement delays the proposal.

### Gemini Flash / pilot-client-email / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-client-email--house.md): 7/7 content checks, 113/180 words, 0 em dashes.

- **Style 2:** [I am writing to propose](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-client-email--house.md:5). Unnecessary announcement remains despite the house instruction.

### Gemini Flash / launch-delay-email / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--launch-delay-email--default.md): 5/6 content checks, 115/180 words, 2 em dashes.

- **grounding review:** [Our team remains completely focused on delivering a secure, high-quality release](../../runs/pilot-v15/google--gemini-3.8-flash--launch-delay-email--default.md:7). Current team focus is not supplied. This may be ordinary reassurance, so it remains unresolved consistently with earlier model reviews.

### Gemini Flash / launch-delay-email / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--launch-delay-email--house.md): 6/6 content checks, 86/180 words, 0 em dashes.

- **Style 2:** [We have an update on our launch schedule.](../../runs/pilot-v15/google--gemini-3.8-flash--launch-delay-email--house.md:3). Announces the update instead of starting with the changed timeline.

### Gemini Flash / vendor-decision-memo / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--vendor-decision-memo--default.md): 6/6 content checks, 194/300 words, 0 em dashes.

- **Style 2:** [This memo evaluates Vendor Alpha and Vendor Beta against our year-one constraints to obtain CFO approval before signing.](../../runs/pilot-v15/google--gemini-3.8-flash--vendor-decision-memo--default.md:8). The purpose preamble delays the recommendation and repeats the subject; the signing gate is stated again in the closing request.

### Gemini Flash / vendor-decision-memo / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--vendor-decision-memo--house.md): 5/6 content checks, 175/300 words, 0 em dashes.

- **grounding fail:** [October 24, 2023](../../runs/pilot-v15/google--gemini-3.8-flash--vendor-decision-memo--house.md:5). Invents a memo date absent from the source pack.

### Gemini Flash / pilot-results-memo / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-results-memo--default.md): 6/7 content checks, 149/300 words, 0 em dashes.

- **C01 fail:** [Mean handling time decreased from 15 minutes (across 200 baseline tickets) to 12 minutes (across 100 pilot tickets).](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-results-memo--default.md:7). Gives endpoints but omits the explicit 3-minute or 20% reduction required by the frozen criterion.
- **Style 10:** [We recommend against scaling the pilot at this time.](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-results-memo--default.md:4). Repeats the immediately preceding Do Not Scale Now recommendation heading without adding information.

### Gemini Flash / pilot-results-memo / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-results-memo--house.md): 6/7 content checks, 156/300 words, 0 em dashes.

- **C01 fail:** [Mean handling time was 12 minutes across 100 pilot tickets, compared to 15 minutes across 200 baseline tickets.](../../runs/pilot-v15/google--gemini-3.8-flash--pilot-results-memo--house.md:9). Gives endpoints but omits the explicit 3-minute or 20% reduction required by the frozen criterion.

### Gemini Flash / discovery-proposal / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--discovery-proposal--default.md): 7/7 content checks, 142/350 words, 0 em dashes.

- **Style 27:** [Please note that](../../runs/pilot-v15/google--gemini-3.8-flash--discovery-proposal--default.md:25). Unnecessary reader coaching; state the start-date prerequisites directly.

### Gemini Flash / discovery-proposal / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--discovery-proposal--house.md): 7/7 content checks, 127/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / change-order / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--change-order--default.md): 7/7 content checks, 117/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / change-order / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--change-order--house.md): 7/7 content checks, 158/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / ai-strategy-slides / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--ai-strategy-slides--default.md): 6/7 content checks, 251/350 words, 0 em dashes.

- **grounding fail:** [Fully Authorized](../../runs/pilot-v15/google--gemini-3.8-flash--ai-strategy-slides--default.md:18). Approval of the input documents does not establish full authorization of the pilot, which still requires COO selection.

### Gemini Flash / ai-strategy-slides / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--ai-strategy-slides--house.md): 7/7 content checks, 194/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / handoff-slides / default

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--handoff-slides--default.md): 7/7 content checks, 186/350 words, 0 em dashes.

- **Style 10:** [* **Criteria Checklist:**
  * Approved Runbook: Complete.
  * Successful Rollback Rehearsal: Incomplete.](../../runs/pilot-v15/google--gemini-3.8-flash--handoff-slides--default.md:12). Repeats both statuses from the previous slide; the acceptance requirements and missing owner provide the new information on this slide.

### Gemini Flash / handoff-slides / house

[Draft](../../runs/pilot-v15/google--gemini-3.8-flash--handoff-slides--house.md): 6/7 content checks, 165/350 words, 0 em dashes.

- **grounding fail:** [Jo does not own pre-acceptance operations tasks.](../../runs/pilot-v15/google--gemini-3.8-flash--handoff-slides--house.md:19). Broadens the incident-ownership boundary into a blanket exclusion from all pre-acceptance operations tasks. The source does not establish that.
- **Style 10:** [Organizing the rehearsal currently lacks an assigned owner.](../../runs/pilot-v15/google--gemini-3.8-flash--handoff-slides--house.md:21). Repeats the same slide's first bullet about no accepted rehearsal organizer.

## Adjudication boundaries

- Team-focus reassurance remains unresolved consistently with prior reviews. Readiness for the explicitly available staging demo is supported.
- Necessary scope and causal contrasts are allowed. Courtesy requests natural to emails are not assistant residue.

[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Partial Opus, Fable and DeepSeek house coverage remains separate. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
