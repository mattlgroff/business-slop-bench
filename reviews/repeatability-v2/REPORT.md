# Astra full-panel repeat

Repeat the entire Astra task panel once to check the strong primary result without selecting favorable tasks or outputs.

The plan was frozen before new calls. All 16 writer inputs match the baseline exactly; task/lens hashes and the selected ZDR policy also match. All 32 generation IDs are distinct. Every second attempt is retained separately, with no best-of replacement. Grades are unblinded assistant judgments.

| Condition | Attempt | Content checks | Content ready | Ready without edits | Em dashes |
|---|---:|---:|---:|---:|---:|
| default | 1 | 54/54 | 8/8 | 4/8 | 11 |
| default | 2 | 54/54 | 7/8 | 3/8 | 13 |
| house | 1 | 54/54 | 8/8 | 8/8 | 0 |
| house | 2 | 54/54 | 8/8 | 6/8 | 0 |

All task-specific content checks pass on both attempts. The second default handoff contains an internal source-pack reference, blocking content readiness under the same residue rule applied to other models. Two second-attempt house drafts add editorial findings: a generic pilot-email closing and a repeated vendor recommendation. The original house result was 8/8 ready without edits; the repeat is 6/8.

New reported generation charges: $0.475830. Original charges are excluded. The primary leaderboard and grades file are unchanged. Two attempts across this fixed eight-brief panel do not establish broad reliability, independent judging accuracy or a population failure rate.

## Second-attempt findings

### pilot-client-email / default

- **28:** [Your approval would give us a clear scope and commercial basis for moving forward while preserving the required security gate.](../../runs/pilot-v23/openai--gpt-6-astra--pilot-client-email--default--sample-2.md:11). Generic closing restates what approving the scope and fee means without adding a next action.

### pilot-client-email / house

- **28:** [That is the next decision needed to move the proposal forward.](../../runs/pilot-v23/openai--gpt-6-astra--pilot-client-email--house--sample-2.md:11). Generic closing after the explicit approval request adds no action or information.

### vendor-decision-memo / default

- **10:** [Alpha is therefore the only option that can meet the stated production requirements within the budget ceiling. SSO must be in place before production.](../../runs/pilot-v23/openai--gpt-6-astra--vendor-decision-memo--default--sample-2.md:23). Repeats the recommendation and mandatory SSO condition already stated above.

### vendor-decision-memo / house

- **10:** [Alpha is the only vendor that can satisfy all stated requirements within the year-one budget. Its $22,000 premium over Beta buys access to a mandatory capability.](../../runs/pilot-v23/openai--gpt-6-astra--vendor-decision-memo--house--sample-2.md:18). Repeats the opening recommendation, budget qualification and SSO-versus-price comparison already given above.

### handoff-slides / default

- **10:** [**Key blocker:** the required rehearsal remains outstanding, with no accepted organizer.](../../runs/pilot-v23/openai--gpt-6-astra--handoff-slides--default--sample-2.md:14). Immediately repeats the preceding table rows describing the outstanding rehearsal and unassigned organizer.
- **Authoring residue:** [No further action identified in the source pack](../../runs/pilot-v23/openai--gpt-6-astra--handoff-slides--default--sample-2.md:10). Refers to the internal source pack inside the finished committee deck. This is authoring residue under the same rule applied to other models.

[Frozen plan](plan.json), [explicit decisions](decisions.json), [all grades](grades.json), and [output hashes](output-hashes.json). Mechanical em dash findings are preserved in the grades; phrase candidates are not automatically defects.
