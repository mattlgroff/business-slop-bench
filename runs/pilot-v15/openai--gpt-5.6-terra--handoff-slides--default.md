### Slide 1 — Operational Handoff Readiness Decision
- **Decision:** Service is **not ready** for operational handoff.
- Acceptance requires:
  - An approved runbook.
  - A successful rollback rehearsal.
- Current status:
  - Runbook is approved.
  - Rollback rehearsal has not happened.

### Slide 2 — Readiness Assessment
| Acceptance criterion | Status | Readiness implication |
|---|---|---|
| Approved runbook | Complete | Criterion met |
| Successful rollback rehearsal | Not complete | Criterion not met |
| Acceptance approval | Not available until criteria are met | Handoff cannot proceed |

- The service cannot be accepted until the rollback rehearsal is successful.

### Slide 3 — Ownership and Current Gap
- Engineering lead **Lee** owns defect fixes until acceptance.
- Operations lead **Jo** owns incidents only after acceptance.
- No role has accepted responsibility for organizing the rollback rehearsal.
- This ownership gap prevents completion of the remaining acceptance criterion.

### Slide 4 — Required Actions and Steering Committee Decision
- Sponsor **Pat** should assign responsibility for organizing the rollback rehearsal.
- The assigned role should organize and complete the rehearsal.
- A successful rehearsal is required before acceptance.
- Once both criteria are met, Sponsor **Pat** can approve acceptance.
- After acceptance, Operations lead **Jo** owns incidents.