## Slide 1 — Readiness Decision
- **The service is not ready for operational handoff.**
- Acceptance requires both an approved runbook and a successful rollback rehearsal.
- The runbook is approved, but the rollback rehearsal has not happened.
- **Recommended decision:** Defer acceptance until the rehearsal succeeds.

## Slide 2 — Acceptance Criteria and Evidence
| Criterion | Current status | Required action |
|---|---|---|
| Approved runbook | Met: runbook approved | No further action required for this criterion |
| Successful rollback rehearsal | Not met: rehearsal has not happened | Organize and successfully complete the rehearsal |

- Readiness depends on meeting both criteria; runbook approval alone is insufficient.

## Slide 3 — Ownership Before and After Acceptance
- **Before acceptance:** Engineering lead Lee owns defect fixes.
- **After acceptance:** Operations lead Jo owns incidents.
- **Unresolved responsibility:** No role has accepted responsibility for organizing the rollback rehearsal.
- **Required action:** Sponsor Pat assigns responsibility for organizing the rehearsal.
- Do not treat Jo’s post-acceptance incident ownership as ownership of rehearsal organization.

## Slide 4 — Required Actions and Approval Gate
1. **Pat assigns rehearsal responsibility** to close the ownership gap.
2. **The assigned owner organizes the rollback rehearsal.**
3. **Complete the rehearsal successfully** to satisfy the outstanding acceptance criterion.
4. **Pat approves acceptance once both criteria are met.**

- **Steering committee decision requested:** Defer handoff now and endorse the action sequence above.
- **Handoff gate:** Approved runbook plus successful rollback rehearsal, followed by Pat’s acceptance approval.