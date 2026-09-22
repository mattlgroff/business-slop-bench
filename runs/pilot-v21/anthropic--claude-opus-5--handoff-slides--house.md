## Slide 1: Decision requested

Pat decides today whether to approve operational handoff. Recommendation: do not approve yet. One acceptance criterion is unmet.

- Acceptance requires two things: an approved runbook and a successful rollback rehearsal.
- The runbook is approved.
- The rollback rehearsal has not happened.
- Pat holds authority to approve acceptance once both criteria are met.

## Slide 2: Current readiness against criteria

| Criterion | Status | Owner |
|---|---|---|
| Runbook approved | Met | Lee |
| Rollback rehearsal completed successfully | Not met | Unassigned |

No role has accepted responsibility for organizing the rehearsal. That absence, not a failed test, is why the service sits short of acceptance.

## Slide 3: Who owns what before and after acceptance

- Lee, engineering lead, owns defect fixes until acceptance.
- Jo, operations lead, owns incidents only after acceptance.
- Between now and acceptance, incidents fall outside Jo's remit. Approving handoff without the rehearsal would move incident ownership to Jo while the rollback path remains untested.
- Pat can assign rehearsal responsibility to a named person.

## Slide 4: Actions required

1. Pat assigns rehearsal ownership to a named individual at this meeting. Without that assignment the gap persists, since neither Lee's nor Jo's current remit covers it.
2. The assigned owner schedules and runs the rollback rehearsal and reports the result to Pat.
3. Lee continues defect fixes until acceptance.
4. Pat approves acceptance once the rehearsal succeeds, at which point Jo takes incident ownership.

Bring the rehearsal result back to this committee for the acceptance decision.