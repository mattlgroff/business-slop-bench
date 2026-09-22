## Slide 1: Decision requested

- Decide whether the service is ready for operational handoff.
- Current recommendation: defer handoff.
- Acceptance requires both:
  - An approved runbook
  - A successful rollback rehearsal
- The runbook is approved. The rollback rehearsal has not happened.

## Slide 2: Readiness status

| Acceptance requirement | Status |
|---|---|
| Approved runbook | Complete |
| Successful rollback rehearsal | Outstanding |
| Operational handoff | Not ready for acceptance |

- The service has not met all acceptance criteria.
- Operations lead Jo owns incidents only after acceptance.
- Engineering lead Lee owns defect fixes until acceptance.

## Slide 3: Decision blocker and authority

- No role has accepted responsibility for organizing the rollback rehearsal.
- Sponsor Pat can assign responsibility for the rehearsal.
- Sponsor Pat can approve acceptance after both criteria are met.
- Until acceptance, Lee retains ownership of defect fixes.

## Slide 4: Actions required

1. Pat assigns a responsible role to organize the rollback rehearsal.
2. The assigned role organizes and completes the rehearsal.
3. The steering committee confirms that the rehearsal was successful.
4. Pat approves acceptance once the approved runbook and successful rehearsal are confirmed.
5. After acceptance, Jo assumes incident ownership and the service can proceed to operational handoff.