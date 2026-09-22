## Slide 1 — Decision: Not Ready for Operational Handoff
- **Acceptance requires:** an approved runbook and a successful rollback rehearsal.
- **Current status:** the runbook is approved; the rollback rehearsal has not happened.
- **Readiness conclusion:** acceptance criteria are not yet met.
- **Recommended decision:** defer operational handoff until the rehearsal succeeds and Sponsor Pat approves acceptance.

## Slide 2 — Readiness Evidence and Open Gap
| Requirement | Status | Required action |
|---|---|---|
| Approved runbook | Met | No further action identified in the source pack |
| Successful rollback rehearsal | Not met: rehearsal has not happened | Organize and successfully complete the rehearsal |
| Rehearsal organizer | Unassigned: no role has accepted responsibility | Sponsor Pat assigns responsibility |

- **Key blocker:** the required rehearsal remains outstanding, with no accepted organizer.

## Slide 3 — Accountability Before and After Acceptance
- **Engineering lead Lee:** owns defect fixes until acceptance.
- **Operations lead Jo:** owns incidents only after acceptance.
- **Sponsor Pat:** can assign responsibility for organizing the rehearsal and approve acceptance once criteria are met.
- **Required clarification:** explicitly assign rehearsal organization; neither Lee’s defect ownership nor Jo’s post-acceptance incident ownership establishes that responsibility.

## Slide 4 — Actions and Acceptance Gate
1. **Assign:** Sponsor Pat assigns responsibility for organizing the rollback rehearsal.
2. **Rehearse:** the assigned organizer arranges the rehearsal; it must complete successfully.
3. **Confirm criteria:** verify that the runbook is approved and the rollback rehearsal was successful.
4. **Approve:** Sponsor Pat approves acceptance once both criteria are met.
5. **Handoff:** Jo’s incident ownership begins after acceptance; Lee’s defect-fix ownership applies until acceptance.

**Steering committee decision requested:** defer handoff now and request Pat’s assignment of rehearsal responsibility.