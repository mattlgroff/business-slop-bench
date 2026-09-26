

## Slide 1: Handoff Readiness Status

Acceptance requires two criteria: an approved runbook and a successful rollback rehearsal. The runbook is approved. The rollback rehearsal has not occurred. One of two criteria is met. The service is not ready for operational handoff.

## Slide 2: Ownership Gaps

| Role | Responsibility | Active now? |
|------|---------------|-------------|
| Lee (Engineering Lead) | Defect fixes | Yes, until acceptance |
| Jo (Operations Lead) | Incident response | No, only after acceptance |

Neither Lee nor Jo has accepted responsibility for organizing the rollback rehearsal. Jo's ownership begins only after acceptance, which the rehearsal gates. Lee's scope covers defect fixes, not rehearsal coordination. No role currently covers this task.

## Slide 3: Action Required

Sponsor Pat holds two authorities: assigning the rehearsal coordination responsibility and approving acceptance once both criteria are met.

Pat must assign a named person to organize and execute the rollback rehearsal. Until that assignment is made, the rehearsal cannot happen, acceptance cannot proceed, and Jo's operational ownership cannot begin.

## Slide 4: Path to Decision

1. Pat assigns rehearsal coordination to a named individual.
2. That individual schedules and completes the rollback rehearsal.
3. Pat verifies both criteria are met and approves acceptance.
4. Jo assumes incident ownership.
5. Lee's defect-fix obligation closes.

The committee can decide today if Pat assigns the rehearsal owner and sets a completion date. Without that assignment, the remaining steps have no start.