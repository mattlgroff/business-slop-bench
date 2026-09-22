Slide 1: Readiness status
Acceptance requires two things: an approved runbook and a successful rollback rehearsal. The runbook is approved. The rollback rehearsal has not happened. The service is therefore not ready for operational handoff.

| Criterion | Status |
|---|---|
| Approved runbook | Met |
| Successful rollback rehearsal | Not met |

Slide 2: Why the rehearsal has stalled
No role has accepted responsibility for organizing the rehearsal. Engineering lead Lee owns defect fixes until acceptance. Operations lead Jo owns incidents only after acceptance. Neither ownership covers the rehearsal, so nobody has scheduled it.

Slide 3: What acceptance changes
Until acceptance, Lee owns defect fixes and Jo has no incident responsibility. After acceptance, Jo owns incidents. Handing over before the rehearsal would move incident ownership to Jo without a tested rollback path.

Slide 4: Decisions requested from the committee
1. Ask Sponsor Pat to assign responsibility for organizing the rollback rehearsal to a named role.
2. That role schedules and runs the rehearsal and reports the result to Pat.
3. Once the rehearsal succeeds, Pat approves acceptance; incident ownership then passes from Lee's defect-fix scope to Jo.
4. Defer the handoff decision until Pat confirms both criteria are met.