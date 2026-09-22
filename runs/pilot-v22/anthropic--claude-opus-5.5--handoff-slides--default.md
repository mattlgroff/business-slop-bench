**Slide 1: Handoff Decision: Not Yet Ready**
- **Decision requested:** Confirm the service is not ready for operational handoff, and approve the actions needed to get there.
- **Status:** One of two acceptance criteria is met.
- **Blocker:** The rollback rehearsal has not happened, and no role owns organizing it.
- **Ask:** Sponsor Pat assigns responsibility for organizing the rehearsal.

**Slide 2: Readiness Against Acceptance Criteria**

| Criterion | Status |
|---|---|
| Approved runbook | Met |
| Successful rollback rehearsal | Not met (not yet held) |

- Acceptance requires both criteria.
- **Conclusion:** Acceptance cannot be approved today.

**Slide 3: Ownership Gap and Risk**

| Responsibility | Owner | Condition |
|---|---|---|
| Defect fixes | Engineering lead Lee | Until acceptance |
| Incidents | Operations lead Jo | Only after acceptance |
| Organizing rollback rehearsal | **Unassigned** | None |
| Assigning responsibility and approving acceptance | Sponsor Pat | Approval once criteria are met |

- Without an organizer, the rehearsal cannot be scheduled, and acceptance stays blocked.
- Until acceptance, Lee remains responsible for defect fixes, and Jo has not taken over incidents.

**Slide 4: Actions Required**
1. **Pat:** Assign a named owner to organize the rollback rehearsal.
2. **Assigned owner:** Organize and run the rehearsal, then report the outcome to the steering committee.
3. **Pat:** If the rehearsal succeeds, approve acceptance, since both criteria would then be met.
4. **On acceptance:** Incident ownership transfers to Jo, and Lee's pre-acceptance defect-fix responsibility ends.

- **Committee decision today:** Endorse "not ready" status and request that Pat make the rehearsal assignment.