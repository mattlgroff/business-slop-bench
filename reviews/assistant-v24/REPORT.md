# Uncapped comparison: GLM 5.3 added

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

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, GLM 5.3, DeepSeek Flash, DeepSeek Pro, Kimi K3 and MiniMax are new uncapped generations on each attempted cell; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### GLM 5.3 / pilot-client-email / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--pilot-client-email--default.md): 7/7 content checks, 198/180 words, 2 em dashes.

- **Style 29:** [I want to be transparent:](../../runs/pilot-v20/zai--glm-5.3--pilot-client-email--default.md:13). Candor script preceding a fact that can be stated directly; the opening also announces clarity on boundaries. The draft is 198 words against the 180-word limit.

### GLM 5.3 / pilot-client-email / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--pilot-client-email--house.md): 6/7 content checks, 187/180 words, 0 em dashes.

- **grounding fail:** [Thanks to the internal review, the pilot proposal is approved on our side](../../runs/pilot-v20/zai--glm-5.3--pilot-client-email--house.md:5). Invents an internal review and internal approval absent from the source. The draft is also 187 words against the 180-word limit.

### GLM 5.3 / launch-delay-email / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--launch-delay-email--default.md): 5/6 content checks, 213/180 words, 3 em dashes.

- **grounding fail:** [The team has been executing well under a shifting timeline](../../runs/pilot-v20/zai--glm-5.3--launch-delay-email--default.md:13). Asserts favorable team performance that the source does not supply.
- **Style 2:** [I want to give you a clear picture of where we stand and what we need from you.](../../runs/pilot-v20/zai--glm-5.3--launch-delay-email--default.md:5). Announces the update instead of starting with the changed position. The draft is 213 words against the 180-word limit.
- **Style 29:** [I want to be upfront that](../../runs/pilot-v20/zai--glm-5.3--launch-delay-email--default.md:7). Candor script preceding the remediation caveat.

### GLM 5.3 / launch-delay-email / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--launch-delay-email--house.md): 5/6 content checks, 184/180 words, 0 em dashes.

- **grounding fail:** [Reply with your choice by end of week](../../runs/pilot-v20/zai--glm-5.3--launch-delay-email--house.md:14). Invents a reply deadline that the source does not authorize.
- **Style 29:** [I want to be straightforward about the remaining uncertainty:](../../runs/pilot-v20/zai--glm-5.3--launch-delay-email--house.md:5). Candor script preceding the remediation caveat. The draft is 184 words against the 180-word limit.

### GLM 5.3 / vendor-decision-memo / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--vendor-decision-memo--default.md): 6/6 content checks, 240/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM 5.3 / vendor-decision-memo / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--vendor-decision-memo--house.md): 5/6 content checks, 290/300 words, 0 em dashes.

- **grounding fail:** [so I can sign before the end of the quarter](../../runs/pilot-v20/zai--glm-5.3--vendor-decision-memo--house.md:36). Invents an end-of-quarter signing deadline and assigns the signature to Priya; the memo also says Beta declined to commit, where the source records only no committed date.
- **Style 10:** [Beta's $22,000 savings would buy a system that cannot go into production use.](../../runs/pilot-v20/zai--glm-5.3--vendor-decision-memo--house.md:28). The Why not Beta section repeats the constraint check and cost comparison already given.

### GLM 5.3 / pilot-results-memo / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--pilot-results-memo--default.md): 7/7 content checks, 247/300 words, 1 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM 5.3 / pilot-results-memo / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--pilot-results-memo--house.md): 7/7 content checks, 162/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM 5.3 / discovery-proposal / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--discovery-proposal--default.md): 7/7 content checks, 270/350 words, 0 em dashes.

- **Style 10:** [the three listed artifacts: the current-state process map, the prioritized backlog, and the implementation recommendation.](../../runs/pilot-v20/zai--glm-5.3--discovery-proposal--default.md:40). Repeats the three artifacts already listed under Purpose.

### GLM 5.3 / discovery-proposal / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--discovery-proposal--house.md): 6/7 content checks, 240/350 words, 0 em dashes.

- **grounding fail:** [Once we receive the signature, the named contact, and the kickoff payment, we will agree a start date](../../runs/pilot-v20/zai--glm-5.3--discovery-proposal--house.md:41). Adds the kickoff payment as a precondition for agreeing the start date; the source ties payment to kickoff, which follows the agreed start.
- **Style 10:** [the three listed artifacts: the current-state process map, the prioritized backlog, and the implementation recommendation.](../../runs/pilot-v20/zai--glm-5.3--discovery-proposal--house.md:31). Repeats the three artifacts already listed under Scope.

### GLM 5.3 / change-order / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--change-order--default.md): 7/7 content checks, 276/300 words, 2 em dashes.

- **Style 10:** [No work on the CRM connector will commence without your written sign-off.](../../runs/pilot-v20/zai--glm-5.3--change-order--default.md:32). Repeats the preceding sentence.

### GLM 5.3 / change-order / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--change-order--house.md): 7/7 content checks, 239/300 words, 0 em dashes.

- **Style 10:** [Connector work begins only after you approve this change order in writing.](../../runs/pilot-v20/zai--glm-5.3--change-order--house.md:27). Repeats the written-approval requirement already stated under Requested work.

### GLM 5.3 / ai-strategy-slides / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--ai-strategy-slides--default.md): 6/7 content checks, 307/350 words, 9 em dashes.

- **grounding fail:** [execution can begin immediately](../../runs/pilot-v20/zai--glm-5.3--ai-strategy-slides--default.md:22). A named owner does not establish immediate readiness. The deck also asserts no legal barriers and calls Option B unlaunchable this quarter.
- **Style 28:** [Acting now positions us with a low-risk, measurable first step — and the data to make the next investment decision with confidence](../../runs/pilot-v20/zai--glm-5.3--ai-strategy-slides--default.md:35). Empty positive ending without evidence beyond the facts already stated.
- **Style 14:** [**De-risked:** built exclusively on approved internal documents — no legal barriers](../../runs/pilot-v20/zai--glm-5.3--ai-strategy-slides--default.md:21). Bold mini-headings on every bullet of slide 3 and most of slide 4.

### GLM 5.3 / ai-strategy-slides / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--ai-strategy-slides--house.md): 6/7 content checks, 275/350 words, 0 em dashes.

- **grounding fail:** [| Legal status | Cleared to run | Legal approval pending; production use not authorized |](../../runs/pilot-v20/zai--glm-5.3--ai-strategy-slides--house.md:14). Invents legal clearance for the knowledge-search pilot, a customer-credit-data source and an unassigned owner for Option B; the source supplies none of these.

### GLM 5.3 / handoff-slides / default

[Draft](../../runs/pilot-v20/zai--glm-5.3--handoff-slides--default.md): 7/7 content checks, 352/350 words, 3 em dashes.

- **Style 14:** [**Criteria met:** Runbook is approved. ✅](../../runs/pilot-v20/zai--glm-5.3--handoff-slides--default.md:4). Emoji status markers and bold mini-headings on every bullet in a committee deck.
- **Style 10:** [**Readiness restated:**](../../runs/pilot-v20/zai--glm-5.3--handoff-slides--default.md:35). An explicit recap repeats the readiness conclusion already stated on slides 1 and 2. The draft is 352 words against the 350-word limit.

### GLM 5.3 / handoff-slides / house

[Draft](../../runs/pilot-v20/zai--glm-5.3--handoff-slides--house.md): 7/7 content checks, 204/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

## Adjudication boundaries

GLM 5.3 passes 52/54 default and 49/54 house content checks with no unresolved checks. Content-ready counts are 4/8 default and 3/8 house; ready-without-edits counts are 1/8 default and 2/8 house. Five drafts exceed their word limits: both pilot emails, both launch emails and the default handoff deck. Default drafts contain 20 em dashes; house drafts contain none.

Confirmed failures are an invented internal review and approval, favorable team-performance reassurance, an end-of-week reply deadline, an end-of-quarter signing deadline with Priya as signatory, the kickoff payment added as a precondition for agreeing the start date, immediate execution readiness, and legal clearance invented for the knowledge-search pilot. Candor scripts such as wanting to be transparent, upfront or straightforward recur across the emails and are recorded as editorial findings, not content failures.

The default vendor memo, the house readout and the house handoff deck are ready without edits. Both readouts state the 3-minute reduction explicitly.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
