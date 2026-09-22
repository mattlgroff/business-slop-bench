# Uncapped comparison: Grok added

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

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3, MiniMax and Grok are new uncapped generations on each attempted cell; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### Grok / pilot-client-email / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--pilot-client-email--default.md): 7/7 content checks, 101/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Grok / pilot-client-email / house

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--pilot-client-email--house.md): 7/7 content checks, 117/180 words, 0 em dashes.

- **Style 21:** [The client hopes for 20% shorter handling time.](../../runs/pilot-v20/spacexai--grok-4.7--pilot-client-email--house.md:7). Third-person client reference in an email addressed directly to that client.

### Grok / launch-delay-email / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--launch-delay-email--default.md): 6/6 content checks, 101/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Grok / launch-delay-email / house

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--launch-delay-email--house.md): 6/6 content checks, 74/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Grok / vendor-decision-memo / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--vendor-decision-memo--default.md): 6/6 content checks, 219/300 words, 1 em dashes.

- **Style 10:** [Signing still requires CFO approval; Priya remains procurement owner.](../../runs/pilot-v20/spacexai--grok-4.7--vendor-decision-memo--default.md:27). Repeats the approval and ownership constraints already listed under Constraints.

### Grok / vendor-decision-memo / house

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--vendor-decision-memo--house.md): 5/6 content checks, 122/300 words, 0 em dashes.

- **grounding review:** [authorize Priya to sign](../../runs/pilot-v20/spacexai--grok-4.7--vendor-decision-memo--house.md:15). The source grants the CFO approval authority before signing but does not identify the signatory; Priya signing may be an unsupported role assignment.

### Grok / pilot-results-memo / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--pilot-results-memo--default.md): 6/7 content checks, 171/300 words, 0 em dashes.

- **C01 fail:** [Mean handling time was 12 minutes on 100 pilot tickets versus 15 minutes on 200 baseline tickets.](../../runs/pilot-v20/spacexai--grok-4.7--pilot-results-memo--default.md:6). Correct endpoints, but omits the explicit 3-minute or 20% reduction required by the frozen criterion. This is an omission, not incorrect arithmetic.
- **Style 10:** [They do not support scaling now on speed, quality, or savings.](../../runs/pilot-v20/spacexai--grok-4.7--pilot-results-memo--default.md:12). Repeats the no-scaling conclusion already stated in the recommendation and the preceding section.

### Grok / pilot-results-memo / house

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--pilot-results-memo--house.md): 6/7 content checks, 128/300 words, 0 em dashes.

- **C01 fail:** [Mean handling time was 12 minutes on 100 pilot tickets, compared with 15 minutes on 200 baseline tickets.](../../runs/pilot-v20/spacexai--grok-4.7--pilot-results-memo--house.md:3). Correct endpoints, but omits the explicit 3-minute or 20% reduction required by the frozen criterion. This is an omission, not incorrect arithmetic.

### Grok / discovery-proposal / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--discovery-proposal--default.md): 7/7 content checks, 163/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Grok / discovery-proposal / house

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--discovery-proposal--house.md): 6/7 content checks, 128/350 words, 0 em dashes.

- **grounding fail:** [Sign this proposal, name the client contact, and pay 50% of the fee. The start date is then agreed.](../../runs/pilot-v20/spacexai--grok-4.7--discovery-proposal--house.md:21). Places the kickoff payment before the agreed start date; the source ties the payment to kickoff, which follows the agreed start.

### Grok / change-order / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--change-order--default.md): 7/7 content checks, 176/300 words, 0 em dashes.

- **Style 10:** [Work will not begin without written sponsor approval.](../../runs/pilot-v20/spacexai--grok-4.7--change-order--default.md:22). Repeats the written-approval requirement stated under Authority.

### Grok / change-order / house

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--change-order--house.md): 7/7 content checks, 109/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Grok / ai-strategy-slides / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--ai-strategy-slides--default.md): 6/7 content checks, 218/350 words, 4 em dashes.

- **grounding fail:** [It is the only option ready to run under current approvals.](../../runs/pilot-v20/spacexai--grok-4.7--ai-strategy-slides--default.md:13). Approved policy documents do not establish readiness to run; the source gives no start conditions.

### Grok / ai-strategy-slides / house

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--ai-strategy-slides--house.md): 6/7 content checks, 189/350 words, 0 em dashes.

- **grounding fail:** [the quarter should go to the authorized option](../../runs/pilot-v20/spacexai--grok-4.7--ai-strategy-slides--house.md:18). Calls the knowledge-search pilot authorized; the source says only that its policy documents are approved.

### Grok / handoff-slides / default

[Draft](../../runs/pilot-v20/spacexai--grok-4.7--handoff-slides--default.md): 7/7 content checks, 180/350 words, 4 em dashes.

- **Style 10:** [Defect-fix ownership stays with Lee until acceptance.](../../runs/pilot-v20/spacexai--grok-4.7--handoff-slides--default.md:18). Repeats the ownership boundary already stated on slide 1.

## Adjudication boundaries

Grok 4.7 completed 15 of 16 cells; the house handoff request ended with a Gateway 408 headers timeout after 300 seconds, retains its reservation and was not retried. Default passes 52/54 content checks with two failures; house passes 43/47 across seven briefs with three failures and one unresolved check. Content-ready counts are 6/8 default and 3/7 house; ready-without-edits counts are 3/8 and 2/7. Default drafts contain 9 em dashes; house drafts contain none. The Gateway reports the canonical slug xai/grok-4.7 for the requested spacexai/grok-4.7; the response model ID matches the request and the alias is recorded explicitly.

Both Grok readouts give correct endpoints and omit the explicit reduction, failing the frozen criterion as in earlier reviews. The other failures are a kickoff payment placed before the agreed start date, a readiness-to-run claim and an authorized label for the knowledge-search pilot. Priya signing is unresolved because the source names no signatory. The default launch email carries no sign-off, which is not a graded check.

Reviewer correction applied in this build: earlier reviews failed drafts that tie the final discovery payment to the sponsor confirming delivery. The source defines acceptance as exactly that confirmation, so the condition adds nothing. The four affected grounding failures, in GLM Flash default, DeepSeek Pro house, Kimi K3 default and GLM 5.3 default, are reversed and the review chain from v18 onward is rebuilt; the corrected counts appear in this table. A payment or start condition that reorders the source sequence, such as paying before the start date is agreed, remains a failure.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
