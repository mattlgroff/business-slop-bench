# Slide 1: Readiness Verdict — Not Yet Ready

- **Status:** The service is NOT ready for operational handoff.
- **Criteria met:** Runbook is approved. ✅
- **Criteria not met:** Rollback rehearsal has not happened. ❌
- **Ownership boundary:** Engineering lead Lee owns defect fixes until acceptance; Operations lead Jo owns incidents only after acceptance.
- **Consequence of proceeding now:** Acceptance criteria would be unmet, so the handoff boundary between Lee and Jo cannot take effect.

# Slide 2: The Blocking Gap

- **Acceptance requires two things:** an approved runbook AND a successful rollback rehearsal.
- **One of two criteria is complete:** the runbook is approved.
- **The blocker:** the rollback rehearsal has not occurred.
- **Root cause:** no role has accepted responsibility for organizing the rehearsal.
- **Risk:** without an owner, the rehearsal cannot be scheduled or completed, leaving the second acceptance criterion permanently open.

# Slide 3: Actions Required to Reach Readiness

| # | Action | Owner / Actor |
|---|--------|---------------|
| 1 | Assign responsibility for organizing the rollback rehearsal | Sponsor Pat |
| 2 | Organize and conduct the rehearsal; confirm it is successful | Assigned role (per Pat's assignment) |
| 3 | Verify both acceptance criteria are met: approved runbook + successful rehearsal | Sponsor Pat |
| 4 | Approve acceptance once criteria are met | Sponsor Pat |
| 5 | Complete handoff: Lee's defect-fix ownership ends; Jo's incident ownership begins | Per acceptance approval |

# Slide 4: Decision Requested from the Steering Committee

- **Decide today:** whether to direct Sponsor Pat to assign rehearsal responsibility now.
- **Why Pat:** Pat can assign that responsibility AND approve acceptance once criteria are met — the authority needed to close the gap.
- **Recommended path:**
  1. Direct Pat to assign the rehearsal organizer.
  2. Require the rehearsal to be completed successfully.
  3. Require Pat to confirm criteria and approve acceptance before handoff.
- **Readiness restated:** the service becomes ready only when the rollback rehearsal succeeds and Pat approves acceptance — not before.
- **Upon approval:** handoff takes effect, transferring incident ownership to Jo.