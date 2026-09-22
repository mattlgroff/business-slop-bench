# Uncapped comparison: DeepSeek Pro added

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
| DeepSeek Pro | default | 8/8 | 51/54 | 1 | 2 | 3/8 | 1/8 | $0.00903 |
| DeepSeek Pro | house | 8/8 | 51/54 | 2 | 1 | 4/8 | 2/8 | $0.03741 |
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, DeepSeek Flash and DeepSeek Pro are new uncapped generations on each attempted cell. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### DeepSeek Pro / pilot-client-email / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--pilot-client-email--default.md): 6/7 content checks, 161/180 words, 2 em dashes.

- **grounding fail:** [Following our discussions](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--pilot-client-email--default.md:5). Invents prior discussions absent from the source pack; the closing also invents a this-week reply deadline.

### DeepSeek Pro / pilot-client-email / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--pilot-client-email--house.md): 7/7 content checks, 140/180 words, 0 em dashes.

- **Style 21:** [The client is looking for 20% shorter handling time.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--pilot-client-email--house.md:7). Third-person client reference in an email addressed directly to that client.
- **Style 10:** [Your approval now would let us move from proposal to preparation without committing to a start date or data access.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--pilot-client-email--house.md:11). Repeats the preceding paragraph, which already says approval starts preparation without a start date or data access.

### DeepSeek Pro / launch-delay-email / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--launch-delay-email--default.md): 5/6 content checks, 166/180 words, 0 em dashes.

- **grounding review:** [The delay is driven by the security review, not by a loss of execution quality.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--launch-delay-email--default.md:16). The review timing is the supported cause of the delay, but the source says the review may require remediation, so the quality reassurance may be an unsupported claim or a general reassurance.
- **Style 2:** [I want to give you a clear picture of where the launch stands and what we need from you.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--launch-delay-email--default.md:5). Announces the update instead of starting with the changed position.

### DeepSeek Pro / launch-delay-email / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--launch-delay-email--house.md): 5/6 content checks, 141/180 words, 0 em dashes.

- **grounding review:** [Nia is tracking the review closely](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--launch-delay-email--house.md:9). The source does not describe how Nia is handling the review; this may be general reassurance rather than a material status claim.

### DeepSeek Pro / vendor-decision-memo / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--vendor-decision-memo--default.md): 6/6 content checks, 141/300 words, 1 em dashes.

- **Authoring placeholder:** [**Date:** [Current Date]](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--vendor-decision-memo--default.md:5). Unfilled document-preparation date in the memo header.

### DeepSeek Pro / vendor-decision-memo / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--vendor-decision-memo--house.md): 6/6 content checks, 111/300 words, 0 em dashes.

- **Authoring placeholder:** [**Date:** [Date]](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--vendor-decision-memo--house.md:5). Unfilled document-preparation date in the memo header.

### DeepSeek Pro / pilot-results-memo / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--pilot-results-memo--default.md): 7/7 content checks, 219/300 words, 3 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### DeepSeek Pro / pilot-results-memo / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--pilot-results-memo--house.md): 7/7 content checks, 172/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### DeepSeek Pro / discovery-proposal / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--discovery-proposal--default.md): 7/7 content checks, 129/350 words, 0 em dashes.

- **Style 10:** [Start date agreed only after signature and named client contact.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--discovery-proposal--default.md:26). The closing Start section repeats step 3 of How to proceed word for word.

### DeepSeek Pro / discovery-proposal / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--discovery-proposal--house.md): 7/7 content checks, 185/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### DeepSeek Pro / change-order / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--change-order--default.md): 7/7 content checks, 135/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### DeepSeek Pro / change-order / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--change-order--house.md): 7/7 content checks, 145/300 words, 0 em dashes.

- **Style 10:** [The proposed fixed change fee is $7,000.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--change-order--house.md:13). Immediately repeats the total already stated in the one-row pricing table.

### DeepSeek Pro / ai-strategy-slides / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--ai-strategy-slides--default.md): 6/7 content checks, 107/350 words, 0 em dashes.

- **grounding review:** [No legal blocker.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--ai-strategy-slides--default.md:16). Approved policy documents do not establish the absence of any legal blocker for the knowledge-search pilot; the inference may be reasonable but is not supplied.
- **Style 15:** [Slide 1: Title](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--ai-strategy-slides--default.md:1). One of four slides carries only a title and no decision content.

### DeepSeek Pro / ai-strategy-slides / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--ai-strategy-slides--house.md): 6/7 content checks, 193/350 words, 0 em dashes.

- **grounding fail:** [Slide 2: Internal knowledge search is ready to run](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--ai-strategy-slides--house.md:10). Approved documents, an owner and a target do not establish readiness to run; the source gives no start conditions. Slide 1 likewise calls it the pilot that can start now.
- **Style 10:** [Blocked pilot would consume most of the budget ceiling.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--ai-strategy-slides--house.md:24). Repeats the cost and blocked status already stated on slides 1 and 3; slide 4 then repeats the cost, target and reporting rule from slide 2.

### DeepSeek Pro / handoff-slides / default

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--handoff-slides--default.md): 7/7 content checks, 167/350 words, 1 em dashes.

- **Authoring placeholder:** [Current answer from source facts: Not ready.](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--handoff-slides--default.md:3). Refers to the source facts inside the committee deck; prompt residue.

### DeepSeek Pro / handoff-slides / house

[Draft](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--handoff-slides--house.md): 6/7 content checks, 219/350 words, 0 em dashes.

- **grounding fail:** [| Approved runbook | Done | Operations lead Jo |](../../runs/pilot-v19/deepseek--deepseek-v4-pro-0813--handoff-slides--house.md:15). Assigns runbook ownership to Jo, which the source does not state. Slide 4 also invents an exception path that Pat may approve; Pat can approve acceptance only once criteria are met.

## Adjudication boundaries

DeepSeek Pro passes 51/54 default and 51/54 house content checks. Default has one failure and two unresolved checks; house has two failures and one unresolved check. Content-ready counts are 3/8 default and 4/8 house; ready-without-edits counts are 1/8 and 2/8. Two memos are blocked by unfilled header dates and the default handoff deck by a sentence that refers to the source facts. Default drafts contain seven em dashes, three of them table cell fillers; house drafts contain none.

Three checks are unresolved rather than failed. The default launch email attributes the delay to the review, which the source supports, while denying any loss of execution quality; the house launch email says Nia is tracking the review closely; the default strategy deck asserts no legal blocker for the knowledge-search pilot. Each may be a reasonable inference or general reassurance, so none is recorded as a confirmed defect. Invented review progress or staging readiness, as in other models, remains a confirmed failure.

Confirmed failures are invented prior discussions, a readiness-to-run claim for the knowledge-search pilot, and runbook ownership assigned to Jo together with an invented exception path. Both readouts state the 3-minute reduction and the 3-point quality shortfall correctly.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
