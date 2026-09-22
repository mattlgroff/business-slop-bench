# Operational Handoff Readiness

## Slide 1: Decision requested

The committee decides whether the service is ready for handoff from Engineering to Operations. Acceptance requires two criteria: an approved runbook and a successful rollback rehearsal. One criterion is met, one is not. The service is not ready today. The committee should approve a plan to close the remaining gap and set a date to confirm acceptance.

## Slide 2: Current status

| Criterion | Status | Owner |
|---|---|---|
| Approved runbook | Met | Lee |
| Successful rollback rehearsal | Not met | Unassigned |

The runbook is approved. The rollback rehearsal has not happened. No role has accepted responsibility for organizing the rehearsal, so the second acceptance criterion has no path to completion until someone is assigned.

## Slide 3: Readiness assessment

The service is partially ready. Engineering lead Lee owns defect fixes until acceptance, and operations lead Jo owns incidents only after acceptance. Until acceptance, Jo cannot take incidents and Lee retains defect responsibility. The longer the rehearsal stays unowned, the longer this split arrangement runs. The gap is narrow and specific: schedule and run one rehearsal, then record the result.

## Slide 4: Required actions

1. Sponsor Pat assigns responsibility for organizing the rollback rehearsal to a named owner.
2. That owner schedules and runs the rehearsal.
3. Once the rehearsal succeeds, Pat approves acceptance.
4. On acceptance, Jo takes ownership of incidents; Lee's defect-fix responsibility ends.

The committee's decision today: confirm action 1 with Pat and agree the review date for confirming acceptance.