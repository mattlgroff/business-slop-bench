# Uncapped comparison: Luna added

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
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Luna is a new uncapped generation on each attempted cell. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### Luna / pilot-client-email / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-client-email--default.md): 7/7 content checks, 125/180 words, 0 em dashes.

- **Style 21:** [the client’s goal](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-client-email--default.md:5). Third-person client reference in an email addressed directly to that client.

### Luna / pilot-client-email / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-client-email--house.md): 7/7 content checks, 125/180 words, 0 em dashes.

- **Style 21:** [The client hopes to reduce handling time by 20%.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-client-email--house.md:7). Third-person client reference in an email addressed directly to that client.

### Luna / launch-delay-email / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--launch-delay-email--default.md): 5/6 content checks, 123/180 words, 0 em dashes.

- **grounding review:** [The team remains focused on completing the required work and moving forward with care.](../../runs/pilot-v18/openai--gpt-5.6-luna--launch-delay-email--default.md:7). Current team focus is not supplied; this may be general reassurance rather than a material factual status claim.
- **Style 2:** [I’m writing with the latest launch position.](../../runs/pilot-v18/openai--gpt-5.6-luna--launch-delay-email--default.md:5). Unnecessary announcement before the changed timeline.

### Luna / launch-delay-email / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--launch-delay-email--house.md): 5/6 content checks, 102/180 words, 0 em dashes.

- **grounding review:** [The team remains focused on completing the work and supporting the review.](../../runs/pilot-v18/openai--gpt-5.6-luna--launch-delay-email--house.md:7). Current team focus and activity are not supplied. General reassurance is a plausible reading, so this remains unresolved.

### Luna / vendor-decision-memo / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--vendor-decision-memo--default.md): 6/6 content checks, 189/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Luna / vendor-decision-memo / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--vendor-decision-memo--house.md): 6/6 content checks, 156/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Luna / pilot-results-memo / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--default.md): 6/7 content checks, 175/300 words, 0 em dashes.

- **C01 fail:** [Mean handling time fell from **15 minutes across 200 baseline tickets** to **12 minutes across 100 pilot tickets**.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--default.md:9). Reports endpoints but omits the required explicit 3-minute or 20% reduction.

### Luna / pilot-results-memo / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--house.md): 6/7 content checks, 151/300 words, 0 em dashes.

- **C01 fail:** [The pilot reduced mean handling time from 15 minutes at baseline to 12 minutes across 100 tickets.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--house.md:3). Reports endpoints but omits the required explicit 3-minute or 20% reduction.
- **Style 10:** [The pilot provides an efficiency signal, but the quality result is below threshold and the evidence is not causal.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--house.md:9). Repeats the handling-time caveat and failed quality threshold already explained in the two preceding paragraphs.

### Luna / discovery-proposal / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--discovery-proposal--default.md): 7/7 content checks, 202/350 words, 0 em dashes.

- **Style 10:** [The first 50% payment is due at kickoff, with the remaining 50% due on delivery.](../../runs/pilot-v18/openai--gpt-5.6-luna--discovery-proposal--default.md:54). Repeats payment terms already given in the commercial table without adding information.

### Luna / discovery-proposal / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--discovery-proposal--house.md): 7/7 content checks, 153/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Luna / change-order / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--change-order--default.md): 7/7 content checks, 155/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Luna / change-order / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--change-order--house.md): 7/7 content checks, 139/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Luna / ai-strategy-slides / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--ai-strategy-slides--default.md): 6/7 content checks, 238/350 words, 4 em dashes.

- **grounding fail:** [Selecting this option would leave the quarter without an authorized production deployment.](../../runs/pilot-v18/openai--gpt-5.6-luna--ai-strategy-slides--default.md:23). Current pending approval does not establish that authorization will remain unavailable throughout the quarter.
- **Style 21:** [Select One Q Next-Quarter AI Pilot](../../runs/pilot-v18/openai--gpt-5.6-luna--ai-strategy-slides--default.md:1). The stray Q makes the heading unnatural and adds no meaning to Next-Quarter.

### Luna / ai-strategy-slides / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--ai-strategy-slides--house.md): 7/7 content checks, 176/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Luna / handoff-slides / default

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--handoff-slides--default.md): 7/7 content checks, 222/350 words, 4 em dashes.

- **Style 19:** [Assigned responsibility leads the rehearsal.](../../runs/pilot-v18/openai--gpt-5.6-luna--handoff-slides--default.md:19). Names an abstract responsibility as the actor; the assigned owner or role must lead the rehearsal.
- **Style 10:** [- Lee continues owning defect fixes until acceptance.
- Jo does not assume incident ownership until acceptance.](../../runs/pilot-v18/openai--gpt-5.6-luna--handoff-slides--default.md:22). Repeats both ownership rules already stated on the preceding slide.

### Luna / handoff-slides / house

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--handoff-slides--house.md): 7/7 content checks, 167/350 words, 0 em dashes.

- **Style 10:** [- **Now:** Pat assigns the rehearsal responsibility.
- **Next:** The assigned owner completes a successful rollback rehearsal.](../../runs/pilot-v18/openai--gpt-5.6-luna--handoff-slides--house.md:24). Repeats the assignment and execution steps from the preceding slide without adding an action or condition.

## Adjudication boundaries

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
