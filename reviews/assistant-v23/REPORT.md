# Uncapped comparison: MiniMax completed

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
| Kimi K3 | default | 8/8 | 51/54 | 3 | 0 | 4/8 | 0/8 | $0.05660 |
| Kimi K3 | house | 8/8 | 50/54 | 3 | 1 | 3/8 | 2/8 | $0.11798 |
| MiniMax | default | 8/8 | 50/54 | 4 | 0 | 3/8 | 0/8 | $0.03275 |
| MiniMax | house | 8/8 | 44/54 | 9 | 1 | 0/8 | 0/8 | $0.03217 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash, Qwen Max, GLM Flash, DeepSeek Flash, DeepSeek Pro, Kimi K3 and MiniMax are new uncapped generations on each attempted cell; six Kimi K3 outputs and five MiniMax outputs are exact-input imports into pilot-v20, counted once. MiniMax now has full coverage; its earlier partial rows are replaced. The MiniMax cell that timed out in pilot-v18 was generated afresh in pilot-v20; the failed request retains its reservation.

## New review evidence

### MiniMax / pilot-client-email / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--pilot-client-email--default.md): 6/7 content checks, 169/180 words, 1 em dashes.

- **grounding fail:** [Thanks for our recent conversation.](../../runs/pilot-v20/minimax--minimax-m3--pilot-client-email--default.md:5). Invents a prior conversation and agreed terms. Also commits to a week-one baseline and parallel onboarding absent from the source.
- **Style 2:** [I'd like to formally propose](../../runs/pilot-v20/minimax--minimax-m3--pilot-client-email--default.md:5). Unnecessary announcement before the actual scope and fee.

### MiniMax / pilot-client-email / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--pilot-client-email--house.md): 6/7 content checks, 125/180 words, 0 em dashes.

- **grounding fail:** [Week one establishes current throughput by invoice type](../../runs/pilot-v20/minimax--minimax-m3--pilot-client-email--house.md:11). Invents scheduled work and measurement detail absent from the approved source; the closing also promises a kickoff plan and target start week.

### MiniMax / launch-delay-email / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--launch-delay-email--default.md): 5/6 content checks, 173/180 words, 2 em dashes.

- **grounding fail:** [The team is steady and the delivery work is intact.](../../runs/pilot-v20/minimax--minimax-m3--launch-delay-email--default.md:19). Invents delivery readiness. The next sentence also asserts that the build has not slipped, which the source does not establish.
- **Style 2:** [Quick update on launch readiness as we close out the week.](../../runs/pilot-v20/minimax--minimax-m3--launch-delay-email--default.md:5). Announces the update instead of stating the changed timeline.

### MiniMax / launch-delay-email / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--launch-delay-email--house.md): 5/6 content checks, 125/180 words, 0 em dashes.

- **grounding fail:** [The team has shipped verification work, the staging environment, and demo assets on the original schedule](../../runs/pilot-v20/minimax--minimax-m3--launch-delay-email--house.md:5). Invents completed work and on-schedule delivery. The end-of-day response deadline is also absent from the source.

### MiniMax / vendor-decision-memo / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--vendor-decision-memo--default.md): 5/6 content checks, 226/300 words, 3 em dashes.

- **grounding fail:** [no contractual remedy or delivery protection](../../runs/pilot-v20/minimax--minimax-m3--vendor-decision-memo--default.md:26). Invents contractual terms for Beta. The source only establishes unavailable SSO and no committed delivery date.

### MiniMax / vendor-decision-memo / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--vendor-decision-memo--house.md): 5/6 content checks, 233/300 words, 0 em dashes.

- **grounding review:** [Priya finalizes terms and signs.](../../runs/pilot-v20/minimax--minimax-m3--vendor-decision-memo--house.md:24). The source grants the CFO approval authority before signing but does not identify the signatory; Priya signing may be an unsupported role assignment.
- **Style 29:** [Rejecting Beta is a constraint decision, not a cost decision.](../../runs/pilot-v20/minimax--minimax-m3--vendor-decision-memo--house.md:27). Aphoristic mirrored landing that restates the analysis already given.
- **Style 10:** [The required capability is available on Alpha today.](../../runs/pilot-v20/minimax--minimax-m3--vendor-decision-memo--house.md:10). Repeats the preceding sentence; the SSO finding is stated four times in one paragraph.

### MiniMax / pilot-results-memo / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--pilot-results-memo--default.md): 7/7 content checks, 253/300 words, 5 em dashes.

- **Style 23:** [A matched design isolates the pilot's true effect on handling time and quality under like-for-like conditions.](../../runs/pilot-v20/minimax--minimax-m3--pilot-results-memo--default.md:18). A matched design reduces mix confounding; it does not isolate the true effect.
- **Style 21:** [MHT gap](../../runs/pilot-v20/minimax--minimax-m3--pilot-results-memo--default.md:10). Unexplained abbreviation in an executive readout.
- **Style 10:** [Hold scaling. Approve the matched-ticket follow-up. Re-decide after matched results land.](../../runs/pilot-v20/minimax--minimax-m3--pilot-results-memo--default.md:28). Repeats the bottom line and the next-decision section.

### MiniMax / pilot-results-memo / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--pilot-results-memo--house.md): 6/7 content checks, 208/300 words, 0 em dashes.

- **grounding fail:** [The pilot sits 5 points below threshold and 5 points below baseline.](../../runs/pilot-v20/minimax--minimax-m3--pilot-results-memo--house.md:11). The shortfall against the 92% threshold is 3 points, not 5. The follow-up is also described as using randomized allocation, which the source does not establish.

### MiniMax / discovery-proposal / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--discovery-proposal--default.md): 7/7 content checks, 205/350 words, 0 em dashes.

- **Style 10:** [Three artifacts will be produced:](../../runs/pilot-v20/minimax--minimax-m3--discovery-proposal--default.md:8). The Deliverables list repeats the three artifacts already named in the Purpose sentence.

### MiniMax / discovery-proposal / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--discovery-proposal--house.md): 6/7 content checks, 197/350 words, 0 em dashes.

- **grounding fail:** [A primary contact who clears access blockers within one business day](../../runs/pilot-v20/minimax--minimax-m3--discovery-proposal--house.md:28). Invents a one-business-day service level for the client contact that the source does not supply.

### MiniMax / change-order / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--change-order--default.md): 7/7 content checks, 303/300 words, 3 em dashes.

- **Style 10:** [No work, scheduling, or credential commitment will be initiated without written approval.](../../runs/pilot-v20/minimax--minimax-m3--change-order--default.md:31). Repeats the written-approval requirement stated in the preceding sentence and in section 5. The draft is also 303 words against the 300-word limit.

### MiniMax / change-order / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--change-order--house.md): 6/7 content checks, 210/300 words, 0 em dashes.

- **grounding fail:** [One validation pass against the sandbox before handoff](../../runs/pilot-v20/minimax--minimax-m3--change-order--house.md:13). Invents scope items, including authentication configuration, refresh cadence and a validation pass, that the source does not include.
- **Style 10:** [| Proposed fixed fee | $7,000 |](../../runs/pilot-v20/minimax--minimax-m3--change-order--house.md:22). The table repeats the fee already stated twice in the preceding prose.
- **Authoring placeholder:** [From: [Contractor]](../../runs/pilot-v20/minimax--minimax-m3--change-order--house.md:4). Unfilled sender placeholder in the document header.

### MiniMax / ai-strategy-slides / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--ai-strategy-slides--default.md): 6/7 content checks, 277/350 words, 8 em dashes.

- **grounding fail:** [We do not de-risk, fund, or staff a non-compliant path this quarter.](../../runs/pilot-v20/minimax--minimax-m3--ai-strategy-slides--default.md:12). Pending legal approval is not non-compliance. The deck also asserts low compliance risk and a natural-language search design that the source does not supply.
- **Style 29:** [The team can run only one pilot next quarter — discipline matters.](../../runs/pilot-v20/minimax--minimax-m3--ai-strategy-slides--default.md:9). Aphoristic tag adds nothing to the capacity fact.
- **Style 5:** [Option A converts approved documents into measurable, reusable value.](../../runs/pilot-v20/minimax--minimax-m3--ai-strategy-slides--default.md:13). Promotional claim without a defined result.

### MiniMax / ai-strategy-slides / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--ai-strategy-slides--house.md): 5/7 content checks, 159/350 words, 0 em dashes.

- **C03 fail:** [$15,000 headroom remains](../../runs/pilot-v20/minimax--minimax-m3--ai-strategy-slides--house.md:12). The remaining budget after a $30,000 pilot under a $50,000 ceiling is $20,000.
- **grounding fail:** [Option B cannot start](../../runs/pilot-v20/minimax--minimax-m3--ai-strategy-slides--house.md:16). Pending legal approval and unauthorized production use do not establish that a pilot cannot start.

### MiniMax / handoff-slides / default

[Draft](../../runs/pilot-v20/minimax--minimax-m3--handoff-slides--default.md): 7/7 content checks, 271/350 words, 6 em dashes.

- **Style 29:** [so the decision is structural, not cosmetic.](../../runs/pilot-v20/minimax--minimax-m3--handoff-slides--default.md:5). Aphoristic contrast adds no information to the ownership change it follows.

### MiniMax / handoff-slides / house

[Draft](../../runs/pilot-v20/minimax--minimax-m3--handoff-slides--house.md): 5/7 content checks, 152/350 words, 0 em dashes.

- **C02 fail:** [Pat assigns one named owner for organizing the rollback rehearsal.](../../runs/pilot-v20/minimax--minimax-m3--handoff-slides--house.md:17). The deck never states that no role currently owns the rehearsal; the gap is omitted rather than invented.
- **grounding fail:** [Lee confirms defect fixes hold through the rehearsal.](../../runs/pilot-v20/minimax--minimax-m3--handoff-slides--house.md:19). Invents a rehearsal step and attendance for Lee and Jo that the source does not assign.

## Adjudication boundaries

MiniMax passes 50/54 default and 44/54 house content checks. Default has four failures; house has nine failures and one unresolved check. Content-ready counts are 3/8 default and 0/8 house; no draft is ready without edits. The five drafts completed in pilot-v18 keep their earlier grades unchanged. Default drafts contain 28 em dashes; house drafts contain none.

Confirmed failures are invented prior conversations, week-one measurement work, delivery readiness and shipped work, contractual terms for Beta, a threshold shortfall stated as 5 points instead of 3, a one-business-day client service level, invented connector scope items, a non-compliance label for a pending approval, a $15,000 headroom figure that should be $20,000, a pilot that supposedly cannot start, an omitted rehearsal-ownership gap and an invented rehearsal step for Lee. Priya signing is unresolved because the source names no signatory.

House instructions removed every em dash but coincided with more invented detail, not less, in this sample. The vendor memo that timed out in pilot-v18 completed in pilot-v20 as a new request; the timed-out request keeps its reservation.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
