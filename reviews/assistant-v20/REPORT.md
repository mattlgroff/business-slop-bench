# Uncapped comparison: Qwen Max added

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
| DeepSeek Flash | default | 8/8 | 52/54 | 2 | 0 | 5/8 | 0/8 | $0.00286 |
| DeepSeek Flash | house | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.00837 |
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash and DeepSeek Flash are new uncapped generations on each attempted cell. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### Qwen Max / pilot-client-email / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-client-email--default.md): 6/7 content checks, 160/180 words, 1 em dashes.

- **grounding fail:** [Could you confirm approval by end of week?](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-client-email--default.md:22). Invents a reply deadline; the source authorizes none. Coordinating timing with a client security team is also not supplied.
- **Style 7:** [establishing the baseline we'll need to quantify savings going forward](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-client-email--default.md:13). Appends an unsupported implication that savings exist to be quantified; the source records no measured savings.

### Qwen Max / pilot-client-email / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-client-email--house.md): 7/7 content checks, 105/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Qwen Max / launch-delay-email / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--launch-delay-email--default.md): 5/6 content checks, 149/180 words, 0 em dashes.

- **grounding fail:** [Nia's review is progressing, and the staging environment is ready.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--launch-delay-email--default.md:17). Invents review progress and staging readiness, then asserts no capability concern while the source says remediation may be required.
- **Style 15:** [**Confidence**](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--launch-delay-email--default.md:15). Four bold section headings divide a 149-word email into a rigid framework that adds no decision value.

### Qwen Max / launch-delay-email / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--launch-delay-email--house.md): 5/6 content checks, 148/180 words, 0 em dashes.

- **grounding fail:** [The work is done and ready](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--launch-delay-email--house.md:11). Asserts completed, ready work while the source says the review may require remediation.
- **Style 28:** [Once Nia gives us a clear date, we will move fast.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--launch-delay-email--house.md:11). Empty positive ending without an owner, evidence or condition beyond the review itself.

### Qwen Max / vendor-decision-memo / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--vendor-decision-memo--default.md): 6/6 content checks, 219/300 words, 2 em dashes.

- **Style 10:** [Because SSO is required before production and Beta offers no committed delivery date, choosing Beta introduces an unbounded schedule risk that could delay or block production entirely.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--vendor-decision-memo--default.md:35). Restates the SSO evaluation already given in the numbered constraint check.
- **Authoring placeholder:** [**Date:** [Current]](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--vendor-decision-memo--default.md:6). Unfilled document-preparation date in the memo header.

### Qwen Max / vendor-decision-memo / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--vendor-decision-memo--house.md): 6/6 content checks, 178/300 words, 0 em dashes.

- **Style 10:** [Alpha meets both constraints: budget and SSO availability.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--vendor-decision-memo--house.md:27). Repeats the budget and SSO findings already stated in the Evaluation section.
- **Authoring placeholder:** [**Date:** [Current date]](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--vendor-decision-memo--house.md:5). Unfilled document-preparation date in the memo header.

### Qwen Max / pilot-results-memo / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-results-memo--default.md): 7/7 content checks, 117/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Qwen Max / pilot-results-memo / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-results-memo--house.md): 7/7 content checks, 191/300 words, 0 em dashes.

- **Style 10:** [1. The quality result is below the stated threshold by three points.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-results-memo--house.md:17). The two numbered problems repeat the quality and confounding findings already stated in the preceding section.
- **Style 29:** [Either finding alone would be sufficient to hold. Together they make the case clear.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--pilot-results-memo--house.md:20). Aphoristic mirrored landing that adds no information to the two findings.

### Qwen Max / discovery-proposal / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--discovery-proposal--default.md): 7/7 content checks, 219/350 words, 0 em dashes.

- **Style 10:** [(current-state process map, prioritized backlog, and implementation recommendation)](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--discovery-proposal--default.md:32). Repeats the three artifacts already listed in the scope table.
- **Style 28:** [We look forward to partnering with you on this engagement.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--discovery-proposal--default.md:44). Closing pleasantry adds no decision, owner or condition.

### Qwen Max / discovery-proposal / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--discovery-proposal--house.md): 7/7 content checks, 122/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Qwen Max / change-order / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--change-order--default.md): 7/7 content checks, 217/300 words, 0 em dashes.

- **Style 10:** [No work will commence without that written approval.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--change-order--default.md:36). Repeats the written-approval requirement stated in the preceding sentence; section 4 likewise repeats the credential condition from section 3.

### Qwen Max / change-order / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--change-order--house.md): 7/7 content checks, 166/300 words, 0 em dashes.

- **Authoring placeholder:** [**Date:** [current date]](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--change-order--house.md:3). Unfilled document-preparation date.
- **Authoring placeholder:** [**From:** [Project Manager]](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--change-order--house.md:5). Unfilled sender placeholder in the document header.

### Qwen Max / ai-strategy-slides / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--ai-strategy-slides--default.md): 6/7 content checks, 171/350 words, 1 em dashes.

- **grounding fail:** [| Production readiness | Pilot-ready | Not authorized for production |](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--ai-strategy-slides--default.md:13). Approved policy documents do not establish pilot readiness, and the source does not say Option B has no owner. The deck also claims no legal blockers.
- **Style 23:** [Named owner (Dana) ensures accountability.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--ai-strategy-slides--default.md:21). A named owner supports accountability; it does not ensure it.

### Qwen Max / ai-strategy-slides / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--ai-strategy-slides--house.md): 6/7 content checks, 156/350 words, 0 em dashes.

- **grounding fail:** [Option A is ready to start](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--ai-strategy-slides--house.md:24). Approved documents, an owner and a metric do not establish readiness to start; the source gives no start conditions.

### Qwen Max / handoff-slides / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--handoff-slides--default.md): 5/7 content checks, 153/350 words, 0 em dashes.

- **C04 fail:** [Handoff transfers incident ownership from Engineering Lead Lee to Operations Lead Jo.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--handoff-slides--default.md:5). States that Lee holds incident ownership before acceptance; the source gives Lee defect fixes only, so ownership conflicts with slide 3.
- **grounding fail:** [Handoff transfers incident ownership from Engineering Lead Lee to Operations Lead Jo.](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--handoff-slides--default.md:5). Invents pre-acceptance incident ownership for Lee, repeated on slide 4.

### Qwen Max / handoff-slides / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-max-0902--handoff-slides--house.md): 7/7 content checks, 121/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

## Adjudication boundaries

Qwen Max passes 49/54 default and 52/54 house content checks with no unresolved checks. Content-ready counts are 3/8 default and 4/8 house; ready-without-edits counts are 1/8 and 3/8. Three drafts are blocked only by unfilled header dates or a sender placeholder; the intentional sponsor signature fields are allowed. Default drafts contain four em dashes; house drafts contain none.

Confirmed failures are an invented end-of-week reply deadline, invented review progress and staging readiness, an assertion that the work is done and ready, pilot readiness and a missing Option B owner asserted in a comparison table, a bare readiness-to-start claim, and incident ownership moved from Lee before acceptance. The last error also appeared in the capped Qwen Max sample and is recorded as both an ownership conflict and a grounding failure. Both readouts state the reduction explicitly.

Readiness claims are failed consistently across this cohort when the source supplies no start conditions, whether stated bare or justified by listed facts. Rhetorical reassurance contrasts in the launch emails are not treated as style-gate negative parallelism; the unsupported assurance inside them is graded under grounding instead.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
