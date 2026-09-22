# Uncapped comparison: Muse and Gemini Flash

Provisional assistant-authored grades, not human gold or independent benchmark validation. Same eight corrected briefs and both conditions, one generation per cell. Model identities visible; no Jev calls.

## Uncapped results

| Model | Condition | Completed briefs | Content checks | Failed | Unresolved | Content ready | Ready without edits | Generation cost |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Muse | default | 8/8 | 53/54 | 1 | 0 | 7/8 | 4/8 | $0.03816 |
| Muse | house | 8/8 | 53/54 | 1 | 0 | 7/8 | 5/8 | $0.05720 |
| Gemini Flash | default | 8/8 | 51/54 | 2 | 1 | 5/8 | 0/8 | $0.01866 |
| Gemini Flash | house | 8/8 | 50/54 | 3 | 1 | 4/8 | 3/8 | $0.02418 |
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Muse and Gemini Flash are new generations on all attempted cells. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### Muse / pilot-client-email / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-client-email--default.md): 7/7 content checks, 86/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / pilot-client-email / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-client-email--house.md): 7/7 content checks, 89/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / launch-delay-email / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--launch-delay-email--default.md): 6/6 content checks, 83/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / launch-delay-email / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--launch-delay-email--house.md): 6/6 content checks, 83/180 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / vendor-decision-memo / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--vendor-decision-memo--default.md): 6/6 content checks, 147/300 words, 0 em dashes.

- **Style 10:** [Conclusion: Select Alpha. It is the only vendor satisfying budget and mandatory SSO.](../../runs/pilot-v18/meta--muse-spark-1.3--vendor-decision-memo--default.md:18). Repeats the opening recommendation and the immediately preceding eligibility analysis without adding a next action.

### Muse / vendor-decision-memo / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--vendor-decision-memo--house.md): 6/6 content checks, 125/300 words, 0 em dashes.

- **Style 10:** [Alpha costs $72,000 subscription plus $20,000 setup.](../../runs/pilot-v18/meta--muse-spark-1.3--vendor-decision-memo--house.md:8). The prose repeats subscription and setup amounts also given in the table; the same duplication occurs for Beta. Retain the SSO analysis while presenting prices once.

### Muse / pilot-results-memo / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--default.md): 6/7 content checks, 111/300 words, 0 em dashes.

- **C01 fail:** [Baseline: 200 tickets, 15 minutes mean handling time.
Pilot: 100 tickets, 12 minutes mean handling time.](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--default.md:6). Reports endpoints but omits the required explicit 3-minute or 20% reduction.

### Muse / pilot-results-memo / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--house.md): 6/7 content checks, 87/300 words, 0 em dashes.

- **C01 fail:** [Handling time averaged 12 minutes in the pilot on 100 tickets, compared with 15 minutes at baseline on 200 tickets.](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--house.md:5). Reports endpoints but omits the required explicit 3-minute or 20% reduction.

### Muse / discovery-proposal / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--discovery-proposal--default.md): 7/7 content checks, 107/350 words, 0 em dashes.

- **Style 10:** [Upon signature and named client contact, the start date will be agreed.](../../runs/pilot-v18/meta--muse-spark-1.3--discovery-proposal--default.md:27). Repeats the start-date prerequisite already stated under client requirements and the immediately preceding signing/contact steps.

### Muse / discovery-proposal / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--discovery-proposal--house.md): 7/7 content checks, 98/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / change-order / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--change-order--default.md): 7/7 content checks, 119/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / change-order / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--change-order--house.md): 7/7 content checks, 113/300 words, 0 em dashes.

- **Style 10:** [This timing is an estimate.](../../runs/pilot-v18/meta--muse-spark-1.3--change-order--house.md:13). Repeats the immediately preceding description of the two weeks as estimated.

### Muse / ai-strategy-slides / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--ai-strategy-slides--default.md): 7/7 content checks, 107/350 words, 3 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / ai-strategy-slides / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--ai-strategy-slides--house.md): 7/7 content checks, 110/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / handoff-slides / default

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--handoff-slides--default.md): 7/7 content checks, 114/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Muse / handoff-slides / house

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--handoff-slides--house.md): 7/7 content checks, 134/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / pilot-client-email / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-client-email--default.md): 7/7 content checks, 110/180 words, 0 em dashes.

- **Style 2:** [I am writing to propose our pilot to assess invoice handling.](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-client-email--default.md:5). Announces the proposal instead of starting with the scope and fee.

### Gemini Flash / pilot-client-email / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-client-email--house.md): 7/7 content checks, 121/180 words, 0 em dashes.

- **Style 21:** [assess our invoice handling](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-client-email--house.md:5). The client-facing email calls the invoice handling ours, making the sender/client relationship unclear; the source describes the client's process.

### Gemini Flash / launch-delay-email / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--launch-delay-email--default.md): 5/6 content checks, 111/180 words, 0 em dashes.

- **grounding review:** [Our team remains completely focused on delivering a successful, secure release.](../../runs/pilot-v18/google--gemini-3.8-flash--launch-delay-email--default.md:5). Current team focus is not supplied; this may be routine reassurance rather than a material status claim, consistently with earlier reviews.
- **Style 2:** [I am writing to update you on our launch position.](../../runs/pilot-v18/google--gemini-3.8-flash--launch-delay-email--default.md:3). Announces the update before the actual changed timeline.

### Gemini Flash / launch-delay-email / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--launch-delay-email--house.md): 5/6 content checks, 102/180 words, 0 em dashes.

- **grounding fail:** [Our team remains fully prepared to proceed as planned with our scheduled activities.](../../runs/pilot-v18/google--gemini-3.8-flash--launch-delay-email--house.md:5). Asserts full preparedness across scheduled activities, beyond the supported availability of a staging demo.

### Gemini Flash / vendor-decision-memo / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--vendor-decision-memo--default.md): 6/6 content checks, 182/300 words, 0 em dashes.

- **Style 2:** [To evaluate Vendor Alpha and Vendor Beta against our year-one constraints and obtain your required approval before signing.](../../runs/pilot-v18/google--gemini-3.8-flash--vendor-decision-memo--default.md:8). Purpose preamble delays the decision and repeats the subject and closing approval request.

### Gemini Flash / vendor-decision-memo / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--vendor-decision-memo--house.md): 5/6 content checks, 161/300 words, 0 em dashes.

- **grounding review:** [Your signature is required to authorize the contract with Alpha.](../../runs/pilot-v18/google--gemini-3.8-flash--vendor-decision-memo--house.md:20). The source requires CFO approval but does not specify a signature. This could request written authorization or invent a signing requirement; the source does not resolve which.
- **Style 10:** [Beta fails the mandatory condition for production deployment. Alpha meets all technical requirements, includes SSO, and remains within the authorized budget.](../../runs/pilot-v18/google--gemini-3.8-flash--vendor-decision-memo--house.md:18). Repeats the eligibility findings already stated in the vendor evaluation and opening recommendation.

### Gemini Flash / pilot-results-memo / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-results-memo--default.md): 6/7 content checks, 153/300 words, 0 em dashes.

- **C01 fail:** [mean handling time decreased from 15 minutes (across 200 baseline tickets) to 12 minutes (across 100 pilot tickets)](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-results-memo--default.md:10). Reports endpoints but omits the required explicit 3-minute or 20% reduction.

### Gemini Flash / pilot-results-memo / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-results-memo--house.md): 6/7 content checks, 152/300 words, 0 em dashes.

- **C01 fail:** [Mean handling time decreased from 15 minutes at baseline to 12 minutes in the pilot.](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-results-memo--house.md:10). Reports endpoints but omits the required explicit 3-minute or 20% reduction.

### Gemini Flash / discovery-proposal / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--discovery-proposal--default.md): 7/7 content checks, 197/350 words, 0 em dashes.

- **Style 27:** [Please note that](../../runs/pilot-v18/google--gemini-3.8-flash--discovery-proposal--default.md:33). Unnecessary reader coaching before the start-date prerequisite.

### Gemini Flash / discovery-proposal / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--discovery-proposal--house.md): 7/7 content checks, 134/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / change-order / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--change-order--default.md): 7/7 content checks, 123/300 words, 0 em dashes.

- **Style 27:** [Please note that](../../runs/pilot-v18/google--gemini-3.8-flash--change-order--default.md:13). Unnecessary reader coaching before the schedule qualification.

### Gemini Flash / change-order / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--change-order--house.md): 7/7 content checks, 158/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / ai-strategy-slides / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--ai-strategy-slides--default.md): 6/7 content checks, 235/350 words, 0 em dashes.

- **grounding fail:** [Fully funded with a $30,000 investment](../../runs/pilot-v18/google--gemini-3.8-flash--ai-strategy-slides--default.md:21). A pilot cost within a budget ceiling does not establish that its funding has been approved. The COO still needs to select the pilot.

### Gemini Flash / ai-strategy-slides / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--ai-strategy-slides--house.md): 7/7 content checks, 182/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### Gemini Flash / handoff-slides / default

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--handoff-slides--default.md): 7/7 content checks, 275/350 words, 0 em dashes.

- **Style 21:** [Operational ownership remains in limbo](../../runs/pilot-v18/google--gemini-3.8-flash--handoff-slides--default.md:31). Vague metaphor adds no precision to the ownership boundaries and missing rehearsal organizer already stated.

### Gemini Flash / handoff-slides / house

[Draft](../../runs/pilot-v18/google--gemini-3.8-flash--handoff-slides--house.md): 6/7 content checks, 172/350 words, 0 em dashes.

- **grounding fail:** [The rollback rehearsal remains unscheduled and unexecuted.](../../runs/pilot-v18/google--gemini-3.8-flash--handoff-slides--house.md:18). The source says the rehearsal has not happened and has no accepted organizer; it does not establish whether a tentative date has been scheduled.
- **Style 10:** [- Jo does not manage incidents under current conditions.
- Lee remains responsible for defect fixes today.](../../runs/pilot-v18/google--gemini-3.8-flash--handoff-slides--house.md:13). Repeats the two ownership rules already stated in the same slide.

## Adjudication boundaries

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
