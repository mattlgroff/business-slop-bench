Slide 1: Decision
The service is not ready for operational handoff.
Acceptance is incomplete. The runbook is approved, and the rollback rehearsal has not happened.
Sponsor Pat should not approve acceptance until both criteria are met.

Slide 2: Readiness against acceptance criteria
Acceptance requires an approved runbook and a successful rollback rehearsal.
Current status:
- Runbook: approved
- Rollback rehearsal: not done
- Organizer: no role has accepted responsibility
One criterion is met. The second is open, so the service fails acceptance.

Slide 3: Ownership before and after acceptance
Engineering lead Lee owns defect fixes until acceptance.
Operations lead Jo owns incidents only after acceptance.
Jo does not own incidents now. Handoff before acceptance would leave incident ownership unassigned under the stated rule.
Lee remains responsible for defect fixes until Pat approves acceptance.

Slide 4: Actions required
Pat assigns one role responsibility for organizing the rollback rehearsal.
That role runs the rehearsal and records whether it succeeded.
If the rehearsal succeeds, both acceptance criteria are met. Pat can then approve acceptance.
After that approval, Jo owns incidents and Lee’s defect-fix ownership ends.
If the rehearsal does not succeed, Pat withholds acceptance and the service stays with Lee for defect fixes.