## Slide 1 — Decision Required: Operational Handoff Readiness
- **Recommendation:** Do not approve operational handoff yet.
- Acceptance requires:
  - An approved runbook
  - A successful rollback rehearsal
- The runbook is approved.
- The rollback rehearsal has not happened.
- Therefore, acceptance criteria are not yet met.

## Slide 2 — Current Ownership and Readiness Position
| Area | Current position |
|---|---|
| Defect fixes | Engineering lead Lee owns defect fixes until acceptance. |
| Incidents | Operations lead Jo owns incidents only after acceptance. |
| Runbook | Approved. |
| Rollback rehearsal | Not completed. |
| Rehearsal organization | No role has accepted responsibility. |
- Operations should not assume incident ownership before acceptance.

## Slide 3 — Required Actions Before Handoff
1. Sponsor Pat assigns responsibility for organizing the rollback rehearsal.
2. The assigned responsibility holder organizes and completes the rehearsal.
3. Confirm the rehearsal is successful.
4. Verify that both acceptance criteria are satisfied:
   - Approved runbook
   - Successful rollback rehearsal
5. Keep Lee responsible for defect fixes until acceptance.
6. Keep Jo’s incident ownership beginning only after acceptance.

## Slide 4 — Steering Committee Decision and Handoff Gate
- **Decision now:** Defer operational handoff.
- **Pat’s action:** Assign responsibility for organizing the rollback rehearsal.
- **Acceptance gate:** After a successful rehearsal, Pat may approve acceptance because the runbook is already approved.
- **If acceptance is approved:** Operations lead Jo assumes incident ownership; Engineering lead Lee’s “until acceptance” ownership ends.
- **Until then:** The service is not ready for operational handoff.