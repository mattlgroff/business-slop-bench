### Slide 1 — Handoff Decision
- **Decision: The service is not ready for operational handoff.**
- Acceptance is incomplete: the runbook is approved, but the required rollback rehearsal has not happened.
- Handoff should proceed only after acceptance.

### Slide 2 — Readiness Against Acceptance Criteria
- **Approved runbook:** Met.
- **Successful rollback rehearsal:** Not met; the rehearsal has not occurred.
- Both criteria are required for acceptance, so acceptance cannot yet be approved.

### Slide 3 — Ownership and Accountability
- Engineering lead Lee owns defect fixes until acceptance.
- Operations lead Jo owns incidents only after acceptance.
- No role has accepted responsibility for organizing the rehearsal.
- Sponsor Pat can assign that responsibility and approve acceptance once the criteria are met.

### Slide 4 — Required Actions and Committee Direction
1. Pat assigns responsibility for organizing the rollback rehearsal.
2. The assigned organizer ensures the rehearsal takes place and is successful.
3. With the runbook approved and rehearsal successful, Pat approves acceptance.
4. After acceptance, operational incident ownership passes to Jo.
- **Committee direction:** Withhold handoff approval pending these actions; Lee retains defect-fix ownership until acceptance.