### Slide 1: Operational handoff decision

- Recommendation: Defer acceptance. The service is not ready for operational handoff.
- Acceptance requires two items: an approved runbook and a successful rollback rehearsal.
- One criterion remains unmet because the rollback rehearsal has not happened.

### Slide 2: Readiness status and ownership gap

- Runbook status: Approved.
- Rollback rehearsal status: Not completed.
- Blocker: No role has accepted responsibility for organizing the rollback rehearsal.
- Sponsor Pat holds the authority to assign this responsibility.

### Slide 3: Support ownership before and after acceptance

- Current state: Engineering lead Lee owns defect fixes until acceptance.
- Post-handoff state: Operations lead Jo owns incidents only after acceptance.
- Consequence: Deferring acceptance keeps defect resolution with Engineering while the team completes the missing rehearsal.

### Slide 4: Required actions to complete handoff

- Decision today: Defer operational handoff.
- Action 1: Sponsor Pat assigns an owner to organize the rollback rehearsal.
- Action 2: The assigned owner schedules and executes a successful rollback rehearsal.
- Action 3: Sponsor Pat approves acceptance once the rehearsal succeeds, transferring incident ownership from Lee to Jo.