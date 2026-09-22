## Slide 1 — Readiness Decision: Not Ready for Operational Handoff
- Acceptance requires both an approved runbook and a successful rollback rehearsal.
- The runbook is approved, but the rollback rehearsal has not happened.
- **Recommended decision:** Defer operational handoff until the rehearsal succeeds and Sponsor Pat approves acceptance.

## Slide 2 — Acceptance Criteria and Current Evidence
| Criterion | Current status | Required action |
|---|---|---|
| Approved runbook | Met | No further action identified in the source pack |
| Successful rollback rehearsal | Not met: rehearsal has not happened | Organize and successfully complete the rehearsal |

- Runbook approval alone does not satisfy acceptance.
- Rehearsal completion must be successful to meet the remaining criterion.

## Slide 3 — Ownership Gap and Required Assignment
- **Current gap:** No role has accepted responsibility for organizing the rollback rehearsal.
- **Authority:** Sponsor Pat can assign that responsibility.
- **Required action:** Pat assigns a rehearsal organizer.
- **Proposed organizer actions:** Coordinate the rehearsal and present its outcome for the acceptance decision.
- Do not assume that either Engineering or Operations already owns rehearsal organization.

## Slide 4 — Handoff Sequence and Accountability
1. **Pat assigns responsibility** for organizing the rollback rehearsal.
2. **The assigned organizer coordinates the rehearsal;** a successful outcome is required.
3. **Pat approves acceptance** once both acceptance criteria are met.
4. **Ownership follows the acceptance boundary:**
   - Engineering lead Lee owns defect fixes until acceptance.
   - Operations lead Jo owns incidents only after acceptance.

**Steering committee action requested:** Endorse deferral of handoff and request Pat’s assignment of rehearsal responsibility.