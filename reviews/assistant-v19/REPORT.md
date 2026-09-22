# Uncapped comparison: DeepSeek Flash added

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
| GLM Flash | default | 8/8 | 49/54 | 3 | 2 | 4/8 | 1/8 | $0.00187 |
| GLM Flash | house | 8/8 | 48/54 | 6 | 0 | 3/8 | 2/8 | $0.00459 |
| DeepSeek Flash | default | 8/8 | 52/54 | 2 | 0 | 5/8 | 0/8 | $0.00286 |
| DeepSeek Flash | house | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.00837 |
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, GLM Flash and DeepSeek Flash are new uncapped generations on each attempted cell. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### DeepSeek Flash / pilot-client-email / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-client-email--default.md): 6/7 content checks, 161/180 words, 1 em dashes.

- **grounding fail:** [Following our discussions](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-client-email--default.md:5). Invents prior discussions absent from the source pack.
- **Style 2:** [To be clear, no baseline or measured savings exists yet](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-client-email--default.md:7). Throat-clearing opener delays a fact that can be stated directly.

### DeepSeek Flash / pilot-client-email / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-client-email--house.md): 7/7 content checks, 99/180 words, 0 em dashes.

- **Style 21:** [The client hopes for 20% shorter handling time](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-client-email--house.md:5). Third-person client reference in an email addressed directly to that client.

### DeepSeek Flash / launch-delay-email / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--launch-delay-email--default.md): 5/6 content checks, 154/180 words, 1 em dashes.

- **grounding fail:** [Work is on track](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--launch-delay-email--default.md:9). Asserts on-track work and unaffected quality while the source says the review may require remediation and no production date is authorized.
- **Authoring placeholder:** [Please confirm by [date]](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--launch-delay-email--default.md:15). Unfilled reply-deadline placeholder; the source authorizes no deadline, and the bracket is left for the sender to fill.

### DeepSeek Flash / launch-delay-email / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--launch-delay-email--house.md): 5/6 content checks, 96/180 words, 0 em dashes.

- **grounding fail:** [Please confirm by October 1](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--launch-delay-email--house.md:11). Invents a reply deadline that the source pack does not authorize.

### DeepSeek Flash / vendor-decision-memo / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--vendor-decision-memo--default.md): 6/6 content checks, 199/300 words, 0 em dashes.

- **Style 10:** [Approve Alpha for year one at $92,000.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--vendor-decision-memo--default.md:27). A second Recommendation section repeats the recommendation already stated at the top of the memo.
- **Authoring placeholder:** [Neither condition is present in the source pack.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--vendor-decision-memo--default.md:29). Refers to the source pack inside a memo addressed to the CFO; prompt residue.

### DeepSeek Flash / vendor-decision-memo / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--vendor-decision-memo--house.md): 6/6 content checks, 183/300 words, 0 em dashes.

- **Authoring placeholder:** [**Date:** [Date]](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--vendor-decision-memo--house.md:5). Unfilled document-preparation date in the memo header.

### DeepSeek Flash / pilot-results-memo / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-results-memo--default.md): 7/7 content checks, 266/300 words, 0 em dashes.

- **Style 10:** [They do not support scaling, a full rollout, or claims of savings.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-results-memo--default.md:21). Repeats the no-scaling and no-savings conclusions already stated in the recommendation and the preceding section.

### DeepSeek Flash / pilot-results-memo / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-results-memo--house.md): 5/7 content checks, 242/300 words, 0 em dashes.

- **C01 fail:** [Handling time fell from a 15 minute mean at baseline to 12 minutes in the pilot.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-results-memo--house.md:7). Correct endpoints, but omits the explicit 3-minute or 20% reduction required by the frozen criterion. This is an omission, not incorrect arithmetic.
- **grounding fail:** [That study would compare like tickets under randomized allocation](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-results-memo--house.md:19). The source offers a matched-ticket follow-up; it does not establish a randomized design.
- **Style 10:** [The pilot fails the stated quality gate. The time result is confounded and cannot carry a scaling decision on its own.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--pilot-results-memo--house.md:15). The Assessment section restates the quality and confounding findings already given in the preceding paragraphs.

### DeepSeek Flash / discovery-proposal / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--discovery-proposal--default.md): 7/7 content checks, 161/350 words, 1 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### DeepSeek Flash / discovery-proposal / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--discovery-proposal--house.md): 7/7 content checks, 163/350 words, 0 em dashes.

- **Style 10:** [This engagement defines the current-state process, a prioritized backlog, and an implementation recommendation.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--discovery-proposal--house.md:4). The purpose sentence lists the three artifacts that the Scope section immediately lists again.

### DeepSeek Flash / change-order / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--change-order--default.md): 7/7 content checks, 218/300 words, 0 em dashes.

- **Style 10:** [It does not alter the original dashboard scope or fee.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--change-order--default.md:11). Repeats the scope boundary stated under Requested Work and again in the closing Note.

### DeepSeek Flash / change-order / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--change-order--house.md): 7/7 content checks, 145/300 words, 0 em dashes.

- **Authoring placeholder:** [**Date:** [Date]](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--change-order--house.md:5). Unfilled document-preparation date; the sponsor signature table is an intentional form field.

### DeepSeek Flash / ai-strategy-slides / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--ai-strategy-slides--default.md): 7/7 content checks, 183/350 words, 4 em dashes.

- **Style 10:** [Decision requested now: select the internal knowledge search pilot.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--ai-strategy-slides--default.md:24). Repeats the ask and the Dana reporting rule already stated on slide 1.

### DeepSeek Flash / ai-strategy-slides / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--ai-strategy-slides--house.md): 7/7 content checks, 131/350 words, 0 em dashes.

- **Style 15:** [**Slide 1: Title**](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--ai-strategy-slides--house.md:1). One of four slides carries only a title, and the recommendation is placed under the Option B slide instead of its own slide.

### DeepSeek Flash / handoff-slides / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--handoff-slides--default.md): 7/7 content checks, 214/350 words, 0 em dashes.

- **Style 10:** [Until then, operational handoff cannot proceed.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--handoff-slides--default.md:24). Repeats the not-ready conclusion already stated on slides 1 and 2; slide 4 then repeats the acceptance and ownership steps from slide 3.
- **Style 25:** [Option B: Defer handoff until ownership is assigned.](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--handoff-slides--default.md:28). Presents deferral as an alternative decision when handoff is already blocked; the options framework adds no decision value.

### DeepSeek Flash / handoff-slides / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--handoff-slides--house.md): 6/7 content checks, 176/350 words, 0 em dashes.

- **grounding fail:** [| Approved runbook | Met | Engineering lead Lee |](../../runs/pilot-v19/deepseek--deepseek-v4.1-flash--handoff-slides--house.md:7). Assigns runbook ownership to Lee; the source says only that the runbook is approved.

## Adjudication boundaries

DeepSeek Flash passes 52/54 default and 50/54 house content checks, with five and three content-ready drafts, but no draft in either condition is ready without edits. Three drafts are blocked by authoring residue rather than factual error: an unfilled reply-date bracket, an unfilled header date in two documents, and a sentence that refers to the source pack inside the CFO memo. Default drafts contain seven em dashes; house drafts contain none.

Confirmed grounding failures are invented prior discussions, an on-track work assurance while remediation remains possible, an October 1 reply deadline, a randomized follow-up design, and runbook ownership assigned to Lee. The house readout gives correct endpoints and omits the explicit reduction, which fails the frozen criterion as in earlier reviews; the default readout states the 3-minute change. Rather-than wording in the default readout explains causal uncertainty and is not a style defect.

The MiMo request failed with a Gateway 400 because no zero-data-retention route exists for that model. Under the ZDR rule stated on 2026-09-22, a model without a ZDR route fails the bench for business reasons; no exception was added and no retry was sent. The frozen protocol still carries earlier non-ZDR exceptions for Muse, Fable 5 and Fable 5.1, so Muse rows in this table were collected outside that rule and are retained pending a decision on those exceptions.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
