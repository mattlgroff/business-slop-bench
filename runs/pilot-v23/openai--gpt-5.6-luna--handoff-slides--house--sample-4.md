## Slide 1: Readiness decision

- **Recommendation:** Do not hand off to Operations yet.
- Acceptance requires:
  - An approved runbook
  - A successful rollback rehearsal
- The runbook is approved.
- The rollback rehearsal has not happened.
- The service is therefore not ready for operational handoff.

## Slide 2: Current ownership

| Area | Current owner | Boundary |
|---|---|---|
| Defect fixes | Engineering lead Lee | Until acceptance |
| Incidents | Operations lead Jo | After acceptance |
| Acceptance authority | Sponsor Pat | Once criteria are met |

- No role has accepted responsibility for organizing the rollback rehearsal.
- Operations does not own incidents until acceptance.

## Slide 3: Action required before handoff

- Sponsor Pat assigns responsibility for organizing the rollback rehearsal.
- The assigned role coordinates and completes the rehearsal.
- The rehearsal must be successful.
- The approved runbook remains part of the acceptance evidence.
- Lee continues to own defect fixes until acceptance.

## Slide 4: Committee decision and handoff gate

- **Decision requested:** Confirm that handoff is pending completion of the rollback rehearsal.
- After a successful rehearsal, Pat can approve acceptance.
- Once Pat approves acceptance:
  - Jo assumes incident ownership.
  - Lee’s defect-fix ownership under the pre-acceptance arrangement ends.
- Until then, keep the service with Engineering ownership for defect fixes and do not transfer incident ownership to Operations.