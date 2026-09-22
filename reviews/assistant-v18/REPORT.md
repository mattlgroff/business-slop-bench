# Uncapped comparison: GLM Flash added

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
| GLM Flash | default | 8/8 | 48/54 | 4 | 2 | 3/8 | 1/8 | $0.00187 |
| GLM Flash | house | 8/8 | 48/54 | 6 | 0 | 3/8 | 2/8 | $0.00459 |
| MiniMax | default | 3/8 | 16/19 | 3 | 0 | 0/3 | 0/3 | $0.01102 |
| MiniMax | house | 2/8 | 11/13 | 2 | 0 | 0/2 | 0/2 | $0.00580 |

Content checks overlap and are not independent trials. Unresolved checks receive no credit. Content ready requires every task check, the word limit and no authoring residue; ready without edits additionally requires the style gate and no supported editorial findings. Default style measures fit without the explicit house instructions.

These samples use no harness output-token cap or generation deadline. They are not pooled with the earlier capped cohort. The same briefs, word limits and grading criteria apply. Qwen Flash and GLM Flash are new uncapped generations on each attempted cell. MiniMax retains partial coverage after its transport timeout.

## New review evidence

### GLM Flash / pilot-client-email / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--pilot-client-email--default.md): 7/7 content checks, 169/180 words, 1 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM Flash / pilot-client-email / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--pilot-client-email--house.md): 6/7 content checks, 182/180 words, 0 em dashes.

- **grounding fail:** [I'll send the security review package and proposed schedule the same week.](../../runs/pilot-v19/zai--glm-5.3-flash--pilot-client-email--house.md:13). Invents a security review package deliverable and a same-week delivery deadline; the source authorizes neither. The draft is also 182 words against the 180-word limit.

### GLM Flash / launch-delay-email / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--launch-delay-email--default.md): 5/6 content checks, 168/180 words, 2 em dashes.

- **grounding fail:** [this is a standard gate, not a setback in quality or readiness.](../../runs/pilot-v19/zai--glm-5.3-flash--launch-delay-email--default.md:12). Asserts no readiness setback while the source says the review may require remediation and no production date is authorized.
- **Style 29:** [Two things worth noting:](../../runs/pilot-v19/zai--glm-5.3-flash--launch-delay-email--default.md:7). Prefatory importance pointer that can be removed without information loss.

### GLM Flash / launch-delay-email / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--launch-delay-email--house.md): 5/6 content checks, 137/180 words, 0 em dashes.

- **grounding fail:** [The team's execution has been solid](../../runs/pilot-v19/zai--glm-5.3-flash--launch-delay-email--house.md:9). Asserts favorable past team performance that the source pack does not supply; confidence in the team can be expressed without an unsupported performance claim.

### GLM Flash / vendor-decision-memo / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--vendor-decision-memo--default.md): 4/6 content checks, 262/300 words, 1 em dashes.

- **C03 fail:** [leaving $30,000 vs. $8,000 of headroom respectively](../../runs/pilot-v19/zai--glm-5.3-flash--vendor-decision-memo--default.md:23). Reverses the headroom figures: Vendor A leaves $8,000 and Vendor B $30,000. The recommendation later states $8,000 correctly, so the memo contains conflicting calculations.
- **grounding review:** [**Re:** Vendor A vs. Vendor B, Year One](../../runs/pilot-v19/zai--glm-5.3-flash--vendor-decision-memo--default.md:5). Renames Alpha and Beta as Vendor A and Vendor B throughout. The mapping is inferable from the figures but never stated, so whether the CFO can identify the recommended vendor is unresolved. The statement that Priya signs may also imply an unsupported signatory role.
- **Style 10:** [Vendor B is cheaper by $22,000 in year one and is within budget, but the mandatory SSO requirement is a hard gate, and Vendor B offers no delivery date.](../../runs/pilot-v19/zai--glm-5.3-flash--vendor-decision-memo--default.md:32). Restates the SSO gate and budget analysis already given in the Analysis section.

### GLM Flash / vendor-decision-memo / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--vendor-decision-memo--house.md): 6/6 content checks, 202/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM Flash / pilot-results-memo / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--pilot-results-memo--default.md): 7/7 content checks, 164/300 words, 1 em dashes.

- **Style 10:** [**Bottom line:** Results support continued investigation, not scaling. Next decision gate: COO authorization of the matched-ticket follow-up.](../../runs/pilot-v19/zai--glm-5.3-flash--pilot-results-memo--default.md:13). Repeats the recommendation and next decision already stated at the top and in the preceding paragraph.

### GLM Flash / pilot-results-memo / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--pilot-results-memo--house.md): 7/7 content checks, 234/300 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM Flash / discovery-proposal / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--default.md): 6/7 content checks, 263/350 words, 0 em dashes.

- **grounding fail:** [The remaining $8,000 is invoiced on delivery and acceptance of the artifacts.](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--default.md:41). Adds acceptance as a condition of the second payment; the source specifies payment on delivery.
- **Style 21:** [## commencement](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--default.md:29). A lowercase heading among title-case headings reads as an unfinished draft.
- **Style 10:** [(current-state process map, prioritized backlog, and implementation recommendation)](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--default.md:33). Repeats the three artifacts already listed in the Objective section.
- **Style 28:** [We look forward to your approval and to delivering a clear, actionable basis for your next steps.](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--default.md:43). Closing promises a clear, actionable basis without adding a decision, owner or condition.

### GLM Flash / discovery-proposal / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--house.md): 5/7 content checks, 257/350 words, 0 em dashes.

- **C05 fail:** [we can begin within two weeks of receipt](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--house.md:36). Commits to a start within two weeks of signature; the source agrees a start date only after signature and a named contact.
- **grounding fail:** [we can begin within two weeks of receipt](../../runs/pilot-v19/zai--glm-5.3-flash--discovery-proposal--house.md:36). Invents a two-week start commitment. The purpose statement also promises a costed recommendation, which the source does not include.

### GLM Flash / change-order / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--change-order--default.md): 6/7 content checks, 258/300 words, 3 em dashes.

- **grounding review:** [all amounts, hours, and durations above are estimates per the stated basis](../../runs/pilot-v19/zai--glm-5.3-flash--change-order--default.md:58). The footer calls every amount an estimate while the fee is presented as fixed, so whether the $7,000 fee is fixed is left ambiguous. The reference to governing terms is also unsupported.
- **Style 10:** [The connector schedule cannot start until they are received alongside written approval.](../../runs/pilot-v19/zai--glm-5.3-flash--change-order--default.md:36). Repeats the schedule condition stated in the preceding section.
- **Authoring placeholder:** [**From:** [Vendor]](../../runs/pilot-v19/zai--glm-5.3-flash--change-order--default.md:4). Unfilled sender placeholder in the document header.
- **Authoring placeholder:** [**Date:** [Date]](../../runs/pilot-v19/zai--glm-5.3-flash--change-order--default.md:4). Unfilled document-preparation date; the sponsor signature block fields are intentional form fields.

### GLM Flash / change-order / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--change-order--house.md): 7/7 content checks, 236/300 words, 0 em dashes.

- **Style 10:** [| Change | Additional CRM connector |](../../runs/pilot-v19/zai--glm-5.3-flash--change-order--house.md:25). The closing table repeats every item already stated in the preceding prose.

### GLM Flash / ai-strategy-slides / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--ai-strategy-slides--default.md): 6/7 content checks, 254/350 words, 6 em dashes.

- **grounding fail:** [No legal blockers; ready to launch immediately](../../runs/pilot-v19/zai--glm-5.3-flash--ai-strategy-slides--default.md:16). Approved policy documents do not establish immediate launch readiness. The deck also invents present urgency to secure resources and a stranded-investment outcome for the alternative.
- **Style 29:** [**One pilot. One choice. Next quarter.**](../../runs/pilot-v19/zai--glm-5.3-flash--ai-strategy-slides--default.md:2). Dramatic fragmentation manufactures emphasis for a fact stated in the next bullet.

### GLM Flash / ai-strategy-slides / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--ai-strategy-slides--house.md): 6/7 content checks, 255/350 words, 0 em dashes.

- **grounding fail:** [The pilot cannot move to production even if it performs well this quarter](../../runs/pilot-v19/zai--glm-5.3-flash--ai-strategy-slides--house.md:20). Pending legal approval does not establish that authorization cannot arrive this quarter. The deck also calls both options funded and says Option A starts immediately, neither of which the source supports.
- **Style 10:** [Decision requested: COO approves Option A, with Dana reporting results before any expansion](../../runs/pilot-v19/zai--glm-5.3-flash--ai-strategy-slides--house.md:30). Repeats the selection and reporting rules already stated on slide 1 and the cost and target already stated on slide 2.

### GLM Flash / handoff-slides / default

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--handoff-slides--default.md): 7/7 content checks, 142/350 words, 0 em dashes.

No supported content or editorial finding in this review; any em dash violations remain separate.

### GLM Flash / handoff-slides / house

[Draft](../../runs/pilot-v19/zai--glm-5.3-flash--handoff-slides--house.md): 6/7 content checks, 230/350 words, 0 em dashes.

- **grounding fail:** [| Approved runbook | Sponsor Pat approves | Met |](../../runs/pilot-v19/zai--glm-5.3-flash--handoff-slides--house.md:11). Assigns runbook approval to Pat; the source says only that the runbook is approved and that Pat approves acceptance.
- **Style 21:** [Today, no defect-free handoff path exists for incidents.](../../runs/pilot-v19/zai--glm-5.3-flash--handoff-slides--house.md:14). The sentence has no clear literal meaning; the source states only that Jo owns incidents after acceptance.

## Adjudication boundaries

GLM Flash has three content-ready default drafts and three house drafts, but only one default and two house drafts are ready without edits. Default drafts contain 14 em dashes across six briefs; house drafts contain none. The house pilot email also exceeds the word limit by two words, which would block readiness even without its grounding failure.

Two default checks are unresolved rather than failed. The vendor memo names the vendors only as Vendor A and Vendor B; the figures identify them, but the memo never says so. The change-order footer calls every amount an estimate while presenting the fee as fixed. Neither is treated as a confirmed false claim.

Both readouts state the reduction explicitly, so the calculation-omission gate does not affect this model. Reassurance about team performance is failed here because it asserts past execution quality, unlike the present-focus statements left unresolved in the Luna review. The default vendor memo reverses the headroom figures in one sentence and states them correctly later; that is recorded as a conflicting calculation.

- Provider-native limits still apply; catalog capacity is used only to reserve spending.
- Prior capped outcomes and canceled requests are retained as execution evidence and excluded from this writing comparison.

[All decisions](grades.json) and [summary](summary.json) retain exact output hashes for the uncapped cohort. Historical capped grades remain in assistant-v13 and earlier reports. Costs are successful reported charges for represented outputs, excluding failed requests and earlier diagnostic calls.
