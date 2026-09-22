# Uncapped comparison: Qwen Flash added

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
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash is a new uncapped generation on each attempted cell. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### Qwen Flash / pilot-client-email / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-client-email--default.md): 6/7 content checks, 116/180 words, 1 em dashes.

- **grounding fail:** [Thank you for the productive discussion on improving invoice handling.](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-client-email--default.md:5). Invents a prior discussion absent from the source pack.
- **Style 23:** [ensuring any future rollout is grounded in measured data rather than assumptions.](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-client-email--default.md:12). Establishing a baseline does not ensure the basis of every future rollout.

### Qwen Flash / pilot-client-email / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-client-email--house.md): 5/7 content checks, 100/180 words, 0 em dashes.

- **C06 fail:** [Jordan,](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-client-email--house.md:3). Addresses the approval request to Jordan, the engagement lead, rather than Morgan, the authorized client recipient.
- **grounding fail:** [Jordan,](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-client-email--house.md:3). Confuses the sender with the recipient and assigns the client approval request to the wrong person.

### Qwen Flash / launch-delay-email / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--launch-delay-email--default.md): 4/6 content checks, 100/180 words, 0 em dashes.

- **C02 fail:** [No new production date is authorized until the review concludes.](../../runs/pilot-v19/alibaba--qwen3.8-flash--launch-delay-email--default.md:13). Explains approval dependency but omits the possibility of remediation.
- **grounding fail:** [The review is thorough because it should be.](../../runs/pilot-v19/alibaba--qwen3.8-flash--launch-delay-email--default.md:7). Asserts review thoroughness without source evidence.
- **Style 29:** [The review is thorough because it should be.](../../runs/pilot-v19/alibaba--qwen3.8-flash--launch-delay-email--default.md:7). A circular reassurance adds no evidence or useful explanation.

### Qwen Flash / launch-delay-email / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--launch-delay-email--house.md): 4/6 content checks, 69/180 words, 0 em dashes.

- **C02 fail:** [Release requires approval.](../../runs/pilot-v19/alibaba--qwen3.8-flash--launch-delay-email--house.md:5). Omits the possibility that the security review may require remediation.
- **grounding fail:** [staging will be fully operational and ready for a client demonstration on October 8 using synthetic data.](../../runs/pilot-v19/alibaba--qwen3.8-flash--launch-delay-email--house.md:7). A synthetic-data demonstration is possible; full staging operational readiness is not established.

### Qwen Flash / vendor-decision-memo / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--vendor-decision-memo--default.md): 5/6 content checks, 161/300 words, 1 em dashes.

- **C05 fail:** [Approve the $92,000 contract with Vendor Alpha for year one.](../../runs/pilot-v19/alibaba--qwen3.8-flash--vendor-decision-memo--default.md:30). Requests CFO approval and identifies Priya in the header, but does not communicate approval as a prerequisite to signing.
- **Style 10:** [Although Beta offers a $22,000 cost savings, it cannot go to production because SSO is unavailable with no committed delivery date. This makes Beta non-viable under the stated constraints regardless of its lower price.](../../runs/pilot-v19/alibaba--qwen3.8-flash--vendor-decision-memo--default.md:24). Repeats the preceding SSO rejection twice; the price difference can be stated without repeating the whole constraint analysis.

### Qwen Flash / vendor-decision-memo / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--vendor-decision-memo--house.md): 5/6 content checks, 107/300 words, 0 em dashes.

- **grounding review:** [Priya will draft the Alpha contract for your signature upon approval.](../../runs/pilot-v19/alibaba--qwen3.8-flash--vendor-decision-memo--house.md:21). The source grants the CFO approval authority but does not identify the contract signatory. The request may imply an unsupported signing role.

### Qwen Flash / pilot-results-memo / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-results-memo--default.md): 6/7 content checks, 205/300 words, 0 em dashes.

- **grounding fail:** [Sam is prepared to run a randomized comparison with identical ticket mixes, which will yield a valid handling-time signal and clarify whether quality regression is caused by the intervention or by ticket-mix differences.](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-results-memo--default.md:23). The source says Sam can run a matched-ticket follow-up; it does not establish a prepared randomized design or guarantee conclusive causal results.

### Qwen Flash / pilot-results-memo / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-results-memo--house.md): 5/7 content checks, 217/300 words, 0 em dashes.

- **C01 fail:** [Handling time improved from 15 to 12 minutes](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-results-memo--house.md:9). Correct endpoints, but omits the explicit 3-minute or 20% reduction required by the frozen criterion. This is an omission, not incorrect arithmetic.
- **grounding fail:** [against a required 94% baseline and 92% threshold.](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-results-memo--house.md:11). Incorrectly describes the observed 94% baseline as required; the source specifies only a 92% scaling threshold.
- **Style 10:** [| Metric | Baseline | Pilot | Gate |](../../runs/pilot-v19/alibaba--qwen3.8-flash--pilot-results-memo--house.md:19). The closing table repeats all metrics already given in the prose without adding a decision or analysis.

### Qwen Flash / discovery-proposal / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--discovery-proposal--default.md): 6/7 content checks, 272/350 words, 0 em dashes.

- **grounding fail:** [Payment of the initial 50% deposit triggers the kickoff meeting.](../../runs/pilot-v19/alibaba--qwen3.8-flash--discovery-proposal--default.md:42). Adds a payment-before-kickoff trigger; the source only specifies payment at kickoff. The separate promise to secure a delivery-schedule spot also lacks support.
- **Style 20:** [The goal is to move from ambiguity to actionable strategy through three core deliverables:](../../runs/pilot-v19/alibaba--qwen3.8-flash--discovery-proposal--default.md:4). Generic consulting language adds no concrete objective beyond the listed discovery deliverables.

### Qwen Flash / discovery-proposal / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--discovery-proposal--house.md): 6/7 content checks, 112/350 words, 0 em dashes.

- **grounding fail:** [We require a named client contact to manage logistics and confirm artifact delivery.](../../runs/pilot-v19/alibaba--qwen3.8-flash--discovery-proposal--house.md:10). Assigns artifact-confirmation responsibility to the contact without support; the source assigns acceptance confirmation to the sponsor.

### Qwen Flash / change-order / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--change-order--default.md): 7/7 content checks, 157/300 words, 2 em dashes.

- **Authoring placeholder:** [**Date:** [TBD]](../../runs/pilot-v19/alibaba--qwen3.8-flash--change-order--default.md:3). Unfilled document-preparation date; the separate sponsor signature and date fields are intentional form fields.

### Qwen Flash / change-order / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--change-order--house.md): 6/7 content checks, 169/300 words, 0 em dashes.

- **grounding review:** [That estimate holds only if sandbox credentials arrive without delay.](../../runs/pilot-v19/alibaba--qwen3.8-flash--change-order--house.md:21). The source starts the estimate after credentials arrive. This sentence may add an unsupported timeliness condition, although the following paragraph correctly says the window has not started without them.
- **Style 10:** [The fee is fixed at $7,000.](../../runs/pilot-v19/alibaba--qwen3.8-flash--change-order--house.md:17). Immediately repeats the fixed fee already stated in the one-row pricing table.

### Qwen Flash / ai-strategy-slides / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--default.md): 6/7 content checks, 254/350 words, 2 em dashes.

- **grounding fail:** [Cannot deploy safely or legally next quarter.](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--default.md:23). Pending approval does not establish that authorization cannot arrive next quarter. Other unsupported assertions include no regulatory risk for knowledge search, an already approved pilot, and unavoidable wasted budget for the alternative.
- **Style 20:** [Strategic Imperative & Constraints](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--default.md:1). Inflated strategic-imperative framing adds no information to the concrete budget and capacity constraints.
- **Style 14:** [*   **Hard Reality:** The team can execute only one AI pilot next quarter.](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--default.md:2). Nearly every bullet has a bold mini-heading, including routine facts. This repeated formatting and emphatic labeling make a simple four-slide decision harder to scan.

### Qwen Flash / ai-strategy-slides / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--house.md): 5/7 content checks, 106/350 words, 0 em dashes.

- **C01 fail:** [COO selects one AI pilot for next quarter.](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:3). Lists the options and asks for selection, but never recommends the knowledge-search pilot.
- **grounding fail:** [*   Status: Ready to launch.](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:12). Approved source documents do not establish complete launch readiness. The credit option also invents a customer-financial-records source and places approval status in an owner field.
- **Style 15:** [*   Owner: Pending legal approval.](../../runs/pilot-v19/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:18). An approval status is not an owner. The rigid option template forces every slide into the same four fields, producing a label that adds no decision value.

### Qwen Flash / handoff-slides / default

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--handoff-slides--default.md): 6/7 content checks, 344/350 words, 0 em dashes.

- **grounding fail:** [leaving operations ownership undefined for the current state.](../../runs/pilot-v19/alibaba--qwen3.8-flash--handoff-slides--default.md:29). Jo taking ownership after acceptance does not establish that nobody owns current operations. The request to authorize Pat also introduces a committee authorization step absent from the source.
- **Style 10:** [**Readiness Explanation:** Operational handoff is blocked. The service is not ready for delivery to operations because the mandatory acceptance gate has not been cleared.](../../runs/pilot-v19/alibaba--qwen3.8-flash--handoff-slides--default.md:4). Repeats the immediately preceding blocked-handoff explanation, then repeats it again under Actions Required; similar recap padding recurs on slide 2.

### Qwen Flash / handoff-slides / house

[Draft](../../runs/pilot-v19/alibaba--qwen3.8-flash--handoff-slides--house.md): 5/7 content checks, 124/350 words, 0 em dashes.

- **C06 fail:** [**Slide 3: Decision Required**](../../runs/pilot-v19/alibaba--qwen3.8-flash--handoff-slides--house.md:19). Only three slide outlines are present; exactly four were requested.
- **grounding fail:** [Jo cannot own it because acceptance has not happened. Lee cannot own it because the role definition covers only defect fixes until acceptance.](../../runs/pilot-v19/alibaba--qwen3.8-flash--handoff-slides--house.md:17). Existing incident and defect responsibilities do not prohibit either person from being assigned rehearsal organization. The source says no one has accepted that role, not that these people are ineligible.

## Adjudication boundaries

Qwen passes many individual checks, but no draft satisfies every readiness condition in this small sample. The default change order passes all content checks and is blocked by an unfilled preparation date; this is different from a factual failure. The two unresolved house claims concern the CFO signing role and credential timing. They receive no credit but are not confirmed defects.

The default readout includes the correct three-minute reduction. Its failure concerns invented follow-up readiness and promised conclusions. The house readout omits the explicit reduction and incorrectly calls the baseline required. The earlier calculation-gate audit remains relevant; these other defects survive removal of that gate.

The single negative-parallelism scan candidate contrasts measured data with assumptions. That contrast conveys a substantive evidence distinction and is not independently flagged as empty rhetoric; the unsupported assurance in the same sentence is recorded separately.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
