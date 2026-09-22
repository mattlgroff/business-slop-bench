# Qwen Flash: eight-brief diagnostic screen

This is an assistant editorial read of one draft per condition and brief. The reviewer knows the model identity. These observations are not human gold, Jev scores, or estimates of model reliability. The v7 grades for the first email remain separate. New v8 drafts are ungraded pending judge validation.

## Findings from the drafts

| Brief | Default output | House-style output |
|---|---|---|
| Pilot client email | Clear commercial outline, but invents prior discussions and an initial risk mitigation strategy. | Short and easy to scan; omits security approval as a prerequisite to accessing data. |
| Launch delay | Offers the right next decision, then invents evidence of team efficiency and review thoroughness. | Clear action for Avery, but says the team is fully prepared without supporting facts. |
| Vendor decision | Correct totals and useful constraint table; incorrectly turns an uncommitted SSO date into certainty that production is impossible within year one. | Correct comparison, but closes with signing rather than explicitly preserving CFO approval before signing. Repeats costs already shown in the table. |
| Pilot results | Clear no-scale recommendation; later says failure to meet the quality threshold would mean failure on both speed and quality, which does not follow. | Concise and actionable; promises random allocation in the follow-up although the source only says matched-ticket. |
| Discovery proposal | Clear offer, but offers email approval as an alternative to signature while subsequently requiring signature. The approval path is inconsistent. | Concise offer, but confuses engagement approval with acceptance of delivered artifacts. |
| Change order | Explains price and dependencies, but contains unfilled date/author placeholders and adds testing/handover detail that needs scope review. | The strongest proposal in this read: concise, correct fee, explicit approval and credential conditions, and a clear approve/decline action. |

| AI strategy slides | Useful option comparison and correct budget arithmetic; describes knowledge search as low risk without supplied risk evidence. | Omits a specific recommendation and assigns results reporting to the COO instead of Dana. |
| Handoff slides | Makes the blocker, owner gap and next decision clear; adds unsupported certainty that no further criteria exist. | Clear readiness and responsibility structure; invents Lee as runbook owner in its summary table. |

## Representative passages

- [Launch default](runs/pilot-v8/alibaba--qwen3.8-flash--launch-delay-email--default.md): “The team is moving efficiently.” No delivery-performance evidence was supplied.
- [Launch house](runs/pilot-v8/alibaba--qwen3.8-flash--launch-delay-email--house.md): “The team is fully prepared and remains confident in the quality of the release.” Neither assertion appears in the source pack.
- [Vendor default](runs/pilot-v8/alibaba--qwen3.8-flash--vendor-decision-memo--default.md): “cannot reach production within year one under any planned timeline.” No committed delivery date does not establish impossibility throughout year one.
- [Pilot results house](runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--house.md): “This test will control for ticket mix and randomize allocation”. A matched-ticket follow-up does not by itself authorize random allocation.
- [Discovery house](runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--house.md): “You approve the engagement by confirming delivery of the three listed artifacts.” Approval to start and acceptance of completed work are different decisions.
- [Change order house](runs/pilot-v8/alibaba--qwen3.8-flash--change-order--house.md): “The two-week duration begins after we receive your written approval and sandbox credentials.” This preserves both required conditions without adding an invented date.

- [AI strategy house](runs/pilot-v8/alibaba--qwen3.8-flash--ai-strategy-slides--house.md): “COO selects the pilot and reports results before expansion.” The source assigns reporting to Dana.
- [Handoff house](runs/pilot-v8/alibaba--qwen3.8-flash--handoff-slides--house.md): its table lists Lee as owner of the approved runbook. The source only assigns Lee defect fixes until acceptance.

## Collection and mechanical checks

All 16 drafts are saved. Two first-brief outputs were reused with matching input hashes; 14 were newly generated. All fit their word limits. Default outputs contain ten em dashes across six briefs; all eight house-style outputs contain zero. This is evidence of compliance with that character ban in this sample, not overall quality.

New successful generation charges total $0.009630, about 0.96 cents. The larger change in conservative budget accounting is not the billed generation cost. See the [audit and individual drafts](runs/pilot-v8/DRAFT_AUDIT.md).

## What this changes in the benchmark

These examples separate three questions: does the draft help the reader decide, are its claims and obligations faithful to the brief, and does its language violate the house style? Clear structure can coexist with unsupported claims. A clean style result cannot stand in for overall quality. The next judge validation should cover these natural failure modes and matched counterexamples, without treating this already inspected sample as a blind test set.
