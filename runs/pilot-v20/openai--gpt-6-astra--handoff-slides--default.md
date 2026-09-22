### Slide 1 — Readiness Decision: Not Ready for Handoff
- **Acceptance requires:** an approved runbook and a successful rollback rehearsal.
- **Current status:** the runbook is approved; the rollback rehearsal has not happened.
- **Decision requested:** defer operational handoff until the rehearsal succeeds and Sponsor Pat approves acceptance.

### Slide 2 — Ownership Before and After Acceptance
| Responsibility | Owner | Boundary |
|---|---|---|
| Defect fixes | Engineering lead Lee | Until acceptance |
| Incidents | Operations lead Jo | Only after acceptance |
| Organizing the rollback rehearsal | No role has accepted responsibility | Assignment needed |
| Assigning rehearsal responsibility and approving acceptance | Sponsor Pat | Acceptance approval once criteria are met |

- **Implication:** do not treat Jo’s incident ownership as active before acceptance.

### Slide 3 — Actions Required to Close the Gap
1. **Pat:** assign responsibility for organizing the rollback rehearsal.
2. **Assigned organizer:** arrange the rehearsal.
3. **Rehearsal:** complete successfully to satisfy the outstanding acceptance criterion.
4. **Pat:** approve acceptance once both criteria are met.

- **Recommended control:** make the organizer’s acceptance of responsibility explicit so the current ownership gap is closed.

### Slide 4 — Steering Committee Decision and Release Gate
- **Recommended decision now:** service is not ready for operational handoff.
- **Required intervention:** ask Pat to assign rehearsal-organizing responsibility.
- **Acceptance gate:**
  - Approved runbook — **met**.
  - Successful rollback rehearsal — **not met**.
- **Handoff trigger:** Pat’s acceptance approval after the criteria are met.
- **Ownership transition:** Lee owns defect fixes until acceptance; Jo owns incidents only after acceptance.