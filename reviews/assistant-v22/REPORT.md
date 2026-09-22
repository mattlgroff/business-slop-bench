# Uncapped comparison: Kimi K3 added

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
| GLM Flash | default | 8/8 | 48/54 | 4 | 2 | 3/8 | 1/8 | $0.00187 |
| GLM Flash | house | 8/8 | 48/54 | 6 | 0 | 3/8 | 2/8 | $0.00459 |
| DeepSeek Flash | default | 8/8 | 52/54 | 2 | 0 | 5/8 | 0/8 | $0.00286 |
| DeepSeek Flash | house | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.00837 |
| DeepSeek Pro | default | 8/8 | 51/54 | 1 | 2 | 3/8 | 1/8 | $0.00903 |
| DeepSeek Pro | house | 8/8 | 50/54 | 3 | 1 | 3/8 | 1/8 | $0.03741 |
| Kimi K3 | default | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.05660 |
| Kimi K3 | house | 8/8 | 50/54 | 3 | 1 | 3/8 | 2/8 | $0.11798 |
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, DeepSeek Flash, DeepSeek Pro and Kimi K3 are new uncapped generations on each attempted cell; six Kimi K3 outputs are exact-input imports from pilot-v19 into pilot-v20, counted once. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### Kimi K3 / pilot-client-email / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-client-email--default.md): 7/7 content checks, 203/180 words, 4 em dashes.

- **Style 5:** [no surprises, no scope creep](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-client-email--default.md:9). Promotional assurance without a defined comparison; the fixed fee already states the commercial protection. The draft is also 203 words against the 180-word limit.

### Kimi K3 / pilot-client-email / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-client-email--house.md): 7/7 content checks, 223/180 words, 0 em dashes.

- **Style 23:** [the output is a clear answer on whether the 20% target is achievable](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-client-email--house.md:16). A six-week pilot without a baseline may not produce a clear answer; the claim asserts certainty the source does not support. The draft is also 223 words against the 180-word limit.

### Kimi K3 / launch-delay-email / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--launch-delay-email--default.md): 5/6 content checks, 158/180 words, 2 em dashes.

- **grounding fail:** [The work is progressing well](../../runs/pilot-v20/moonshotai--kimi-k3--launch-delay-email--default.md:9). Asserts favorable work progress while the source says the review may require remediation and no production date is authorized.

### Kimi K3 / launch-delay-email / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--launch-delay-email--house.md): 6/6 content checks, 148/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Kimi K3 / vendor-decision-memo / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--vendor-decision-memo--default.md): 6/6 content checks, 247/300 words, 1 em dashes.

- **Style 10:** [**Select Vendor Alpha at a year-one cost of $92,000**](../../runs/pilot-v20/moonshotai--kimi-k3--vendor-decision-memo--default.md:35). The recommendation is stated in the summary, again here with the same figures, and a third time in the approval request.

### Kimi K3 / vendor-decision-memo / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--vendor-decision-memo--house.md): 5/6 content checks, 200/300 words, 0 em dashes.

- **grounding review:** [I will proceed with signing per procurement process.](../../runs/pilot-v20/moonshotai--kimi-k3--vendor-decision-memo--house.md:30). The source grants the CFO approval authority before signing but does not identify the signatory; Priya signing may be an unsupported role assignment.

### Kimi K3 / pilot-results-memo / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-results-memo--default.md): 6/7 content checks, 167/300 words, 0 em dashes.

- **C01 fail:** [12 minutes on 100 tickets versus 15 minutes on 200 baseline tickets](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-results-memo--default.md:6). Correct endpoints, but omits the explicit 3-minute or 20% reduction required by the frozen criterion. This is an omission, not incorrect arithmetic.

### Kimi K3 / pilot-results-memo / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-results-memo--house.md): 7/7 content checks, 376/300 words, 0 em dashes.

- **Style 10:** [Recommendation to the COO: authorize the matched-ticket follow-up.](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-results-memo--house.md:30). Repeats the recommendation already given in the opening section and the next-decision paragraph. The draft is also 376 words against the 300-word limit.
- **Style 16:** [On the stated criteria alone, the pilot does not qualify to expand.](../../runs/pilot-v20/moonshotai--kimi-k3--pilot-results-memo--house.md:17). Restates the preceding sentence; the readout carries repeated claims and a risk section that add length without new decision content.

### Kimi K3 / discovery-proposal / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--discovery-proposal--default.md): 6/7 content checks, 277/350 words, 4 em dashes.

- **grounding fail:** [triggering the final payment (50%, $8,000)](../../runs/pilot-v20/moonshotai--kimi-k3--discovery-proposal--default.md:52). Makes acceptance confirmation the trigger for the second payment; the source specifies payment on delivery.
- **Style 10:** [the three listed artifacts: the process map, the prioritized backlog, and the implementation recommendation.](../../runs/pilot-v20/moonshotai--kimi-k3--discovery-proposal--default.md:44). Repeats the three artifacts already listed in the scope section.
- **Style 28:** [We look forward to your approval and to beginning discovery.](../../runs/pilot-v20/moonshotai--kimi-k3--discovery-proposal--default.md:54). Closing pleasantry adds no decision, owner or condition.

### Kimi K3 / discovery-proposal / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--discovery-proposal--house.md): 7/7 content checks, 217/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Kimi K3 / change-order / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--change-order--default.md): 7/7 content checks, 200/300 words, 3 em dashes.

- **Style 10:** [No connector work will start without written approval.](../../runs/pilot-v20/moonshotai--kimi-k3--change-order--default.md:25). Repeats the preceding sentence.

### Kimi K3 / change-order / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--change-order--house.md): 7/7 content checks, 192/300 words, 0 em dashes.

- **Style 10:** [Without written approval, the team will continue with the original dashboard scope and no connector work will proceed.](../../runs/pilot-v20/moonshotai--kimi-k3--change-order--house.md:28). Repeats the written-approval condition stated in the preceding sentence and in the schedule section.

### Kimi K3 / ai-strategy-slides / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--ai-strategy-slides--default.md): 6/7 content checks, 230/350 words, 4 em dashes.

- **grounding fail:** [Fund the Authorized Pilot](../../runs/pilot-v20/moonshotai--kimi-k3--ai-strategy-slides--default.md:1). Calls the knowledge-search pilot authorized; the source says only that its policy documents are approved. The deck also asserts reduced compliance friction without support.
- **Style 29:** [reducing compliance friction](../../runs/pilot-v20/moonshotai--kimi-k3--ai-strategy-slides--default.md:8). Systems metaphor replaces the literal fact that the documents are already approved.
- **Style 14:** [Cost: **$30,000**, within the **$50,000** quarterly pilot ceiling.](../../runs/pilot-v20/moonshotai--kimi-k3--ai-strategy-slides--default.md:3). Bold on nearly every figure and term across all four slides makes routine facts compete for emphasis.

### Kimi K3 / ai-strategy-slides / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--ai-strategy-slides--house.md): 6/7 content checks, 243/350 words, 0 em dashes.

- **grounding fail:** [It is the only option that can start and finish within the quarter on cleared data and within budget.](../../runs/pilot-v20/moonshotai--kimi-k3--ai-strategy-slides--house.md:26). The source gives no start or completion conditions for the pilot, and both options fit the budget.
- **Style 10:** [Judge it on the agreed metric: at least 90% accuracy on 100 reviewed questions.](../../runs/pilot-v20/moonshotai--kimi-k3--ai-strategy-slides--house.md:27). Repeats the metric, owner and cost already stated on slide 2.

### Kimi K3 / handoff-slides / default

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--handoff-slides--default.md): 7/7 content checks, 206/350 words, 4 em dashes.

- **Style 10:** [- Lee: continue defect-fix ownership until acceptance.](../../runs/pilot-v20/moonshotai--kimi-k3--handoff-slides--default.md:22). Repeats the ownership boundary already stated on slides 1 and 2.

### Kimi K3 / handoff-slides / house

[Draft](../../runs/pilot-v20/moonshotai--kimi-k3--handoff-slides--house.md): 5/7 content checks, 226/350 words, 0 em dashes.

- **C04 fail:** [Incident ownership transfers from Lee to Jo.](../../runs/pilot-v20/moonshotai--kimi-k3--handoff-slides--house.md:35). States that Lee holds incident ownership before acceptance; the source gives Lee defect fixes only, so ownership conflicts with slide 2.
- **grounding fail:** [Incident ownership transfers from Lee to Jo.](../../runs/pilot-v20/moonshotai--kimi-k3--handoff-slides--house.md:35). Invents pre-acceptance incident ownership for Lee.
- **Style 29:** [The gap is ownership, not capability.](../../runs/pilot-v20/moonshotai--kimi-k3--handoff-slides--house.md:27). Aphoristic contrast; capability is not discussed in the source and the sentence adds no information to the stated gap.

## Adjudication boundaries

Kimi K3 passes 50/54 content checks in both conditions. Default has four failures; house has three failures and one unresolved check. Content-ready counts are 3/8 in each condition; ready-without-edits counts are 0/8 default and 2/8 house. Three drafts exceed their word limits: both pilot emails and the house readout. Default drafts contain 22 em dashes; house drafts contain none.

Confirmed failures are favorable work-progress reassurance, a readout with correct endpoints but no explicit reduction, acceptance confirmation made the trigger for the second discovery payment, the knowledge-search pilot called authorized, an unsupported claim that only one option can start and finish within the quarter, and incident ownership moved from Lee before acceptance. Priya signing the contract is unresolved because the source names no signatory.

Six Kimi K3 outputs were generated in pilot-v19 before that collection was interrupted; pilot-v20 imports them as exact-input copies with their original generation identities and charges, so they are neither re-spent nor counted twice. The interrupted seventh request retains its canceled reservation in the ledger and is not represented here.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
