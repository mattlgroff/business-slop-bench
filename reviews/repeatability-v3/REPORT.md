# Luna full-panel repeat

Fresh full-panel Luna repeat for comparison with the Astra repeat; no best-of selection.

The plan was frozen before new calls. All 16 writer inputs match the baseline exactly; task/lens hashes and the selected ZDR policy also match. All 32 generation IDs are distinct. Every new full-panel draft is retained separately, with no best-of replacement. Grades are unblinded assistant judgments.

| Condition | Round | Content checks | Content ready | Ready without edits | Em dashes |
|---|---:|---:|---:|---:|---:|
| default | 1 | 51/54 | 5/8 | 2/8 | 8 |
| default | 2 | 52/54 | 6/8 | 1/8 | 8 |
| house | 1 | 52/54 | 6/8 | 4/8 | 0 |
| house | 2 | 52/54 | 6/8 | 3/8 | 0 |

Round 1 is the primary sample; round 2 is the new full-panel repeat. The two previously repeated house briefs use sample ID 4; all other new files use sample ID 2. Existing diagnostic outputs were not reused or overwritten.

New reported generation charges: $0.011698. Primary charges are excluded. The primary leaderboard remains unchanged. This is a small, fixed-panel, unblinded same-reviewer study, not a population reliability estimate.

## New-round findings

### pilot-client-email / default

- **21:** [with a client hope of achieving a 20% reduction.](../../runs/pilot-v23/openai--gpt-5.6-luna--pilot-client-email--default--sample-2.md:5). Awkward third-person client reference in an email addressed directly to Morgan.

### pilot-client-email / house

- **21:** [The client’s target](../../runs/pilot-v23/openai--gpt-5.6-luna--pilot-client-email--house--sample-2.md:7). Third-person client reference in an email addressed directly to Morgan.

### launch-delay-email / default

- **grounding:** [The team remains focused and confident in its ability to support the review, address any required remediation, and keep progress moving.](../../runs/pilot-v23/openai--gpt-5.6-luna--launch-delay-email--default--sample-2.md:7). The source does not report current team focus. This may be general reassurance rather than a material unsupported status claim.

### launch-delay-email / house

- **grounding:** [The team remains focused on completing the release work and responding to any review findings.](../../runs/pilot-v23/openai--gpt-5.6-luna--launch-delay-email--house--sample-2.md:7). The source does not report current team focus. This may be general reassurance rather than a material unsupported status claim.

### vendor-decision-memo / default

- **10:** [Select **Alpha**. The additional cost is necessary to meet the mandatory SSO requirement and enable production.](../../runs/pilot-v23/openai--gpt-5.6-luna--vendor-decision-memo--default--sample-2.md:27). Repeats the opening recommendation and the SSO-versus-cost reasoning already stated in the evaluation.

### pilot-results-memo / default

- **C01:** [Mean handling time declined from **15 minutes at baseline** to **12 minutes during the pilot**](../../runs/pilot-v23/openai--gpt-5.6-luna--pilot-results-memo--default--sample-2.md:9). Correct endpoints but no explicit 3-minute or 20% reduction, as required by the frozen criterion. This is omission, not incorrect arithmetic.
- **10:** [The pilot suggests a potential handling-time improvement, but it does not establish that the pilot caused the improvement. More importantly, observed quality is below the threshold required for scaling. The evidence therefore does not support immediate expansion.](../../runs/pilot-v23/openai--gpt-5.6-luna--pilot-results-memo--default--sample-2.md:16). The separate rationale paragraph repeats the preceding result caveats and no-scale recommendation.

### discovery-proposal / default

- **10:** [The engagement will be considered accepted when the sponsor confirms delivery of:

- The current-state process map
- The prioritized backlog
- The implementation recommendation](../../runs/pilot-v23/openai--gpt-5.6-luna--discovery-proposal--default--sample-2.md:40). Repeats the entire deliverables list rather than referring to the three artifacts already named.

### change-order / house

- **10:** [The proposed change fee is $7,000.](../../runs/pilot-v23/openai--gpt-5.6-luna--change-order--house--sample-2.md:15). Immediately repeats the fixed fee already stated in the table.

### ai-strategy-slides / default

- **21:** [Select One Q Next-Quarter AI Pilot](../../runs/pilot-v23/openai--gpt-5.6-luna--ai-strategy-slides--default--sample-2.md:1). Stray Q makes the heading awkward; the next-quarter period is already named.

### ai-strategy-slides / house

- **grounding:** [Option A is ready for next-quarter execution](../../runs/pilot-v23/openai--gpt-5.6-luna--ai-strategy-slides--house--sample-2.md:9). Approved policy documents do not establish overall pilot readiness. The source provides no readiness-to-execute finding.
- **10:** [Decide on any expansion after Dana reports the results.](../../runs/pilot-v23/openai--gpt-5.6-luna--ai-strategy-slides--house--sample-2.md:34). The reporting prerequisite is repeated on slides 1, 3 and 4 without a new decision condition.

### handoff-slides / house

- **10:** [Until then, keep the service with Engineering ownership for defect fixes and do not transfer incident ownership to Operations.](../../runs/pilot-v23/openai--gpt-5.6-luna--handoff-slides--house--sample-4.md:37). The closing bullet repeats the before/after ownership boundaries already stated in the table and several preceding bullets.

## Comparison with Astra repeats

Luna house remains at 52/54 content checks, but the failure moves: the new readout includes the reduction, while the new strategy deck asserts execution readiness. Default improves from 51/54 to 52/54 because the earlier strategy grounding failure is absent. Both launch reassurances remain unresolved.

Ready without edits changes from 2/8 to 1/8 default and 4/8 to 3/8 house. The Astra full-panel repeat retains 54/54 content checks in each condition and 6/8 house drafts ready without edits, versus Luna at 3/8. The new Luna calls cost $0.011698 versus Astra at $0.475830. This is a fixed-panel observation, not a cost-adjusted model ranking or a population reliability estimate.

[Astra full-panel repeat](../repeatability-v2/REPORT.md).

[Frozen plan](plan.json), [explicit decisions](decisions.json), [all grades](grades.json), and [output hashes](output-hashes.json). Mechanical em dash findings are preserved in the grades; phrase candidates are not automatically defects.
