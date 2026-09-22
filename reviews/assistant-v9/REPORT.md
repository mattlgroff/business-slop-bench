# Assistant comparison: GLM Flash added

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

GLM Flash often preserves the requested decision but adds unsupported claims or commitments. The house instruction removes mechanical dash violations without consistently fixing content. This is one sample per cell, not a reliability ranking.

## New review evidence

### GLM Flash / pilot-client-email / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--default.md): 5/7 content checks, 166/180 words, 1 em dashes.

- **C03 fail:** [the pilot itself will establish measured savings](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--default.md:11). Promises measured savings although the source has only an aspiration and no baseline or evidence of savings.
- **grounding fail:** [the pilot itself will establish measured savings](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--default.md:11). Introduces an unsupported outcome commitment. The approved engagement assesses invoice handling; savings are not assured.
- **Style 2:** [I'd like to move us forward on the proposed pilot for invoice handling and ask for your approval on two points.](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--default.md:5). Long announcement delays the scope and fee request.

### GLM Flash / pilot-client-email / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--house.md): 4/7 content checks, 168/180 words, 0 em dashes.

- **C02 fail:** [followed by a decision on production rollout](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--house.md:5). A later rollout decision does not explicitly exclude production rollout from the pilot scope.
- **C04 fail:** [Your team needs to grant access to client data first](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--house.md:9). Security approval is stated as a kickoff dependency, but the required approval-before-data-access relationship is missing; this sentence instead puts data access first.
- **grounding fail:** [I can return a proposed schedule within a few days of clearance.](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-client-email--house.md:15). Adds an unsupported turnaround commitment. The draft also adds weekly measurement and a this-week response deadline.

### GLM Flash / launch-delay-email / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--launch-delay-email--default.md): 5/6 content checks, 143/180 words, 2 em dashes.

- **grounding fail:** [they've kept everything moving despite the security timeline](../../runs/pilot-v15/zai--glm-5.3-flash--launch-delay-email--default.md:9). Invents favorable team performance, beyond the brief's invitation to convey confidence.
- **Style 2:** [Quick update on the launch.](../../runs/pilot-v15/zai--glm-5.3-flash--launch-delay-email--default.md:5). Opening announces the update instead of starting with the changed security timeline.

### GLM Flash / launch-delay-email / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--launch-delay-email--house.md): 5/6 content checks, 166/180 words, 0 em dashes.

- **grounding fail:** [The team has kept every deliverable ahead of this dependency](../../runs/pilot-v15/zai--glm-5.3-flash--launch-delay-email--house.md:7). Invents the status of every deliverable. The end-of-day Thursday decision deadline is also absent from the source.

### GLM Flash / vendor-decision-memo / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--vendor-decision-memo--default.md): 5/6 content checks, 248/300 words, 1 em dashes.

- **grounding fail:** [immediate go-live capability](../../runs/pilot-v15/zai--glm-5.3-flash--vendor-decision-memo--default.md:21). Available SSO and satisfaction of the listed requirements do not establish immediate production readiness.
- **Style 10:** [Alpha is fully compliant today: SSO is available, and the $92,000 total fits within the $100,000 ceiling with $8,000 of headroom.](../../runs/pilot-v15/zai--glm-5.3-flash--vendor-decision-memo--default.md:21). Repeats the same eligibility and arithmetic already shown in the table and constraint evaluation.

### GLM Flash / vendor-decision-memo / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--vendor-decision-memo--house.md): 5/6 content checks, 166/300 words, 0 em dashes.

- **C05 review:** [Priya to initiate procurement with Alpha pending your approval.](../../runs/pilot-v15/zai--glm-5.3-flash--vendor-decision-memo--house.md:21). Identifies Priya and the CFO approval request, but pending approval may mean procurement can start while approval is outstanding. The signing gate is not clear.
- **Style 13:** [The source pack gives no basis for estimating that delay](../../runs/pilot-v15/zai--glm-5.3-flash--vendor-decision-memo--house.md:19). Refers to the benchmark source packet inside the finished CFO memo.

### GLM Flash / pilot-results-memo / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-results-memo--default.md): 6/7 content checks, 230/300 words, 1 em dashes.

- **grounding fail:** [Sam's proposed matched-ticket follow-up](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-results-memo--default.md:15). Attributes an existing proposal to Sam. The source only says Sam can run the follow-up; the memo may propose it without inventing prior authorship.
- **Style 10:** [Results support continuing evaluation via the matched-ticket follow-up. They do not support scaling now, given non-randomized allocation, a quality pass rate below threshold, and unmeasured savings.](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-results-memo--default.md:18). Repeats the recommendation and reasons already explained above the next-decision section.

### GLM Flash / pilot-results-memo / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-results-memo--house.md): 6/7 content checks, 189/300 words, 0 em dashes.

- **grounding fail:** [Speed gains that come with lower pass rates would shift rework onto other teams.](../../runs/pilot-v15/zai--glm-5.3-flash--pilot-results-memo--house.md:7). Invents a consequence and destination of rework not established by the supplied pass rates. The closing also assigns rollout approval authority to the COO, whose stated authority covers the follow-up only.

### GLM Flash / discovery-proposal / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--discovery-proposal--default.md): 7/7 content checks, 150/350 words, 0 em dashes.

- **Style 10:** [Included: current-state process map, prioritized backlog, implementation recommendation.](../../runs/pilot-v15/zai--glm-5.3-flash--discovery-proposal--default.md:12). Repeats the complete deliverable list from the opening without adding scope detail.

### GLM Flash / discovery-proposal / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--discovery-proposal--house.md): 7/7 content checks, 233/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM Flash / change-order / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--change-order--default.md): 7/7 content checks, 168/300 words, 2 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM Flash / change-order / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--change-order--house.md): 7/7 content checks, 189/300 words, 0 em dashes.

- **Style 10:** [| Item | Detail |](../../runs/pilot-v15/zai--glm-5.3-flash--change-order--house.md:20). The closing summary table repeats scope, price, timing and dependencies already stated immediately above.

### GLM Flash / ai-strategy-slides / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--ai-strategy-slides--default.md): 6/7 content checks, 182/350 words, 4 em dashes.

- **grounding fail:** [authorized scope](../../runs/pilot-v15/zai--glm-5.3-flash--ai-strategy-slides--default.md:19). The documents are approved; the pilot scope has not been selected by the COO. The draft also invents a today deadline.
- **Style 4:** [Decision shapes how we validate AI value before broader investment](../../runs/pilot-v15/zai--glm-5.3-flash--ai-strategy-slides--default.md:4). Generic significance claim adds no concrete reason or constraint to the decision slide.

### GLM Flash / ai-strategy-slides / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--ai-strategy-slides--house.md): 6/7 content checks, 193/350 words, 0 em dashes.

- **grounding fail:** [Decide on credit decisions next quarter, once legal approval lands](../../runs/pilot-v15/zai--glm-5.3-flash--ai-strategy-slides--house.md:21). Assumes pending legal approval will arrive by next quarter. The Q3 heading and today selection deadline are also unsupported by the source.

### GLM Flash / handoff-slides / default

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--handoff-slides--default.md): 7/7 content checks, 193/350 words, 3 em dashes.

- **Style 14:** [✅ Done](../../runs/pilot-v15/zai--glm-5.3-flash--handoff-slides--default.md:9). Status emojis decorate a professional decision table; plain met or not met labels communicate the same information.

### GLM Flash / handoff-slides / house

[Draft](../../runs/pilot-v15/zai--glm-5.3-flash--handoff-slides--house.md): 6/7 content checks, 259/350 words, 0 em dashes.

- **grounding fail:** [| Approved runbook | Met | Lee |](../../runs/pilot-v15/zai--glm-5.3-flash--handoff-slides--house.md:11). Assigns runbook ownership to Lee, although the source assigns Lee only defect fixes until acceptance.

## Adjudication boundaries

- GLM vendor house approval wording is unresolved because procurement initiation pending approval does not clearly identify the contract-signing gate.
- Suggestions and conditional future evaluation are allowed; invented prior proposals, team performance and delivery promises are not.

[All decisions](grades.json) and [summary](summary.json) retain previous grades and exact output hashes. Partial Opus, Fable and DeepSeek house coverage remains separate. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
