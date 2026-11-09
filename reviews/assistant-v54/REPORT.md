# Claude Fable 5.2 on BusinessSlopBench v3

November 9, 2026. Provisional, unblinded assistant judgments, without independent human gold.

Low reasoning requested; always-on adaptive thinking, no temperature setting sent. No harness output cap or generation deadline. One attempt per cell.

Fable 5.2 avoids all em dashes, but both strategy decks infer pilot readiness from approved documents. The house handoff retains one unresolved service-ownership claim. Two plain drafts exceed word limits. Clean house drafts are the pilot email, vendor memo, discovery proposal and change order; the plain clean drafts are the pilot email and discovery proposal.

## Full v3 results

| Condition | Checks | Content ready | Ready without edits | Cost, 8 drafts |
|---|---:|---:|---:|---:|
| default | 53/54 | 5/8 | 2/8 | $0.208728 |
| house | 52/54 | 6/8 | 4/8 | $0.464784 |

The replacement vendor task explicitly names Alex as sole signatory, Priya as procurement coordinator and the CFO as prior approver. This is the second v3 model panel; Kimi K3.1 Pro was the first. Historical full-panel rankings remain unchanged; no v3 rank against v2 is assigned.

## Comparable seven-brief subset

Vendor memo excluded for every model. All remaining saved writer inputs match exactly, including requested low reasoning. Primary attempts only; this subset was chosen because of the declared v2/v3 task change, not performance. Provider sampling can differ; identical requested low reasoning does not establish equal compute or sampling.

| Model | Condition | Checks | Content ready | Ready without edits |
|---|---|---:|---:|---:|
| Astra | default | 48/48 | 7/7 | 3/7 |
| Astra | house | 48/48 | 7/7 | 7/7 |
| Muse Wonder 1.0 | default | 47/48 | 6/7 | 2/7 |
| Muse Wonder 1.0 | house | 48/48 | 7/7 | 6/7 |
| Sol 6.1 | default | 47/48 | 6/7 | 2/7 |
| Sol 6.1 | house | 48/48 | 6/7 | 3/7 |
| Fable 5.1 | default | 45/48 | 3/7 | 0/7 |
| Fable 5.1 | house | 45/48 | 3/7 | 3/7 |
| Fable 5 | default | 44/48 | 3/7 | 0/7 |
| Fable 5 | house | 46/48 | 4/7 | 4/7 |
| Claude Fable 5.2 | default | 47/48 | 5/7 | 2/7 |
| Claude Fable 5.2 | house | 46/48 | 5/7 | 3/7 |

## Full v3 comparison with Kimi K3.1 Pro

Both models used identical v3 writer inputs, with requested low reasoning. Kimi reported fixed-temperature warnings; Fable returned no warnings. Content checks take priority in the existing ranking order, so Kimi leads on factual checks while Fable produces more house drafts without editing.

| Model | Condition | Checks | Content ready | Ready without edits |
|---|---|---:|---:|---:|
| Kimi K3.1 Pro | default | 54/54 | 8/8 | 2/8 |
| Kimi K3.1 Pro | house | 54/54 | 8/8 | 2/8 |
| Claude Fable 5.2 | default | 53/54 | 5/8 | 2/8 |
| Claude Fable 5.2 | house | 52/54 | 6/8 | 4/8 |

## Draft evidence

### pilot-client-email / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--pilot-client-email--default.md): 7/7 checks, 172/180 words, 0 em dashes.

- Boundary: The cost/exposure wording is read in its immediate fixed-fee, six-week pilot context. The source supports a fixed price and exclusion of production rollout. It does not assert the stronger no-overrun-at-any-volume or no-risk claim rejected in earlier reviews. Requests to begin approval planning and conditional scheduling are ordinary proposed next steps.

### pilot-client-email / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--pilot-client-email--house.md): 7/7 checks, 177/180 words, 0 em dashes.

- Boundary: The cost/exposure wording is read in its immediate fixed-fee, six-week pilot context. The source supports a fixed price and exclusion of production rollout. It does not assert the stronger no-overrun-at-any-volume or no-risk claim rejected in earlier reviews. Requests to begin approval planning and conditional scheduling are ordinary proposed next steps.

### launch-delay-email / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--launch-delay-email--default.md): 6/6 checks, 186/180 words, 0 em dashes.

- Style 2: "Here is where the launch stands, and one decision I need from you.". Opening preamble announces the structure instead of stating the launch position; the following headings already identify both subjects.
- Boundary: Routine promise to update the client after the review, without a new deadline, is allowed. The draft exceeds the 180-word limit.

### launch-delay-email / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--launch-delay-email--house.md): 6/6 checks, 165/180 words, 0 em dashes.

- Style 16: "No new date has been authorized, and I will not commit to one until Nia's review is complete.". The preceding sentence already says the review may require fixes and the sender cannot give a production date. These adjacent date qualifications can be combined without information loss.

### vendor-decision-memo / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--vendor-decision-memo--default.md): 6/6 checks, 302/300 words, 0 em dashes.

- Style 10: "**Conclusion.** Beta's savings do not offset a failed mandatory constraint. Cost is a differentiator only between options that qualify, and Beta does not qualify. Alpha meets every stated requirement with $8,000 of headroom.". Restates the recommendation, SSO comparison and budget headroom already established above.
- Boundary: All three v3 authority roles and the approval sequence are correct. The draft is 302 words against the 300-word limit.

### vendor-decision-memo / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--vendor-decision-memo--house.md): 6/6 checks, 270/300 words, 0 em dashes.

- Boundary: All three authority roles and approval-before-signature are explicit. The final request identifies the concrete approval needed; repeating the price there is functional decision wording. Annual subscription comparisons use the supplied rates, not a claim of locked future renewal pricing.

### pilot-results-memo / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--pilot-results-memo--default.md): 7/7 checks, 263/300 words, 0 em dashes.

- Style 10: "**Handling time was lower in the pilot.** Mean handling time was 12 minutes against 15 at baseline.". Repeats the handling-time row immediately above without adding interpretation or a decision.
- Boundary: The matched-ticket follow-up is a recommendation to observe whether differences persist, not a claim that causal identification is guaranteed.

### pilot-results-memo / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--pilot-results-memo--house.md): 7/7 checks, 283/300 words, 0 em dashes.

- Style 10: "- A claim that the pilot process cuts handling time by 20%.
- A claim that the pilot meets the quality requirement.
- Any savings figure.". The three-item recap repeats the causal, quality and financial limitations already explained in the preceding paragraphs.
- Boundary: Necessary factual negations distinguish observations from causal effects and are not style-gate violations. A matched-ticket follow-up controls the stated ticket-mix difference; the draft does not promise causal isolation.

### discovery-proposal / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--discovery-proposal--default.md): 7/7 checks, 284/350 words, 0 em dashes.

- Boundary: Commercial labels, acceptance terms and the intentional approval fields are functional proposal structure. Start-date agreement remains conditional on signature and named contact.

### discovery-proposal / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--discovery-proposal--house.md): 7/7 checks, 262/350 words, 0 em dashes.

- Boundary: The proposed sequence repeats payment milestones in operational context; it does not replace the stated 50% kickoff / 50% delivery payment terms. A request to flag unavailable interviewees or documents is allowed.

### change-order / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--change-order--default.md): 7/7 checks, 263/300 words, 0 em dashes.

- Style 10: "Add a CRM connector to the current engagement.". An entire Requested work section repeats the immediately preceding description and opening approval request without adding scope detail.
- Boundary: Intentional sponsor decision and signature fields are allowed. Declining a proposed change leaves the existing signed scope and fee in place.

### change-order / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--change-order--house.md): 7/7 checks, 186/300 words, 0 em dashes.

- Boundary: Approval wording and credential dependencies are functional in the acceptance choices, rather than an empty closing recap.

### ai-strategy-slides / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--ai-strategy-slides--default.md): 6/7 checks, 334/350 words, 0 em dashes.

- grounding fail: "Only knowledge search is clear to proceed today". Approved input documents do not establish current pilot readiness or approval. The following slide also claims Ready now, while the source leaves pilot selection to the COO.

### ai-strategy-slides / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--ai-strategy-slides--house.md): 6/7 checks, 262/350 words, 0 em dashes.

- grounding fail: "Option A can start on approved inputs with a named IT owner.". Treats approved source documents and a named owner as sufficient for current execution readiness. The source supplies neither start readiness nor pilot approval; the COO still selects the pilot.
- Boundary: The later request for COO approval does not supply evidence for the earlier unqualified can-start claim.

### handoff-slides / default

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--handoff-slides--default.md): 7/7 checks, 338/350 words, 0 em dashes.

- Style 10: "**Committee takeaway:** One criterion is met, one is open, and the open one has no owner.". The slide-ending takeaway repeats its four preceding bullets. Similar takeaway blocks after slides 2 and 3 repeat the stated status and ownership gap.
- Boundary: The no-accepted-organizer and Pat-assignment instructions preserve the source gap. Required successful rehearsal is an acceptance condition, not a guaranteed outcome.

### handoff-slides / house

[Draft](../../runs/pilot-v35/anthropic--claude-fable-5.2--handoff-slides--house.md): 6/7 checks, 281/350 words, 0 em dashes.

- grounding review: "the service stays with engineering". May broaden Lee defect-fix ownership into overall service or incident ownership before acceptance. The source specifies defect fixes and post-acceptance incidents separately; retain the same unresolved boundary used for Argon.
- Style 10: "Both arrangements stay as they are while the rehearsal is outstanding. Lee's defect-fix ownership continues, and Jo's incident ownership has not started.". Repeats the immediately preceding two ownership bullets without adding a condition.

[All grades and anchored evidence](grades.json), [authored decisions](decisions.json), [mechanical scans](scans.json), [matched inputs](input-verification.json).

Rebuild with `python3 reviews/assistant-v54/build.py`. No API calls are made by this builder. Prices in the saved Gateway catalog: $8 input / $40 output per million tokens. Costs above are reported billing. Blog not updated as part of this run.
