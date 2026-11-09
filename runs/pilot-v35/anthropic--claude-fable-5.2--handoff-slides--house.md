# Slide 1: The service is not ready for operational handoff

- Acceptance requires two things: an approved runbook and a successful rollback rehearsal.
- The runbook is approved.
- The rollback rehearsal has not happened, and no role has accepted responsibility for organizing it.
- Recommendation: withhold acceptance today and have Sponsor Pat assign responsibility for the rehearsal.

# Slide 2: Status against the acceptance criteria

| Criterion | Status | Owner |
|---|---|---|
| Approved runbook | Met | No action needed |
| Successful rollback rehearsal | Not met, not yet held | Unassigned |

- Pat can approve acceptance once both criteria are met.

# Slide 3: Who owns what until acceptance

- Engineering lead Lee owns defect fixes until acceptance.
- Operations lead Jo owns incidents only after acceptance.
- Both arrangements stay as they are while the rehearsal is outstanding. Lee's defect-fix ownership continues, and Jo's incident ownership has not started.
- Organizing the rehearsal sits with neither role today. Pat has the authority to assign it.

# Slide 4: Actions required

1. Pat assigns responsibility for organizing the rollback rehearsal to a named role. Pat can make this assignment in this meeting.
2. The assigned owner sets a rehearsal date, holds the rehearsal, and reports the result to Pat.
3. If the rehearsal succeeds, Pat approves acceptance. Jo then owns incidents, and Lee's defect-fix ownership ends.
4. If the rehearsal fails, the acceptance criterion stays unmet, the service stays with engineering, and the rehearsal must be repeated successfully before Pat can approve acceptance.

Decision requested from the committee: confirm that handoff waits for a successful rehearsal, and ask Pat to name the rehearsal owner.