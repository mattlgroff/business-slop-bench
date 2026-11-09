# Slide 1: Readiness Decision

**Headline:** The service is not ready for operational handoff.

- Acceptance requires two things: an approved runbook and a successful rollback rehearsal.
- The runbook is approved.
- The rollback rehearsal has not happened.
- No role has accepted responsibility for organizing the rehearsal.

**Committee takeaway:** One criterion is met, one is open, and the open one has no owner.

# Slide 2: Status Against Acceptance Criteria

| Criterion | Status | Owner |
|---|---|---|
| Approved runbook | Met | n/a |
| Successful rollback rehearsal | Not met; rehearsal not yet held | None assigned |

- Until acceptance, responsibilities stay as they are:
  - Engineering lead Lee owns defect fixes.
  - Operations lead Jo does not yet own incidents; that begins only after acceptance.

**Committee takeaway:** Handoff cannot occur until the rehearsal succeeds.

# Slide 3: The Ownership Gap

**Headline:** The rehearsal is blocked by missing ownership.

- Lee's defined responsibility is defect fixes until acceptance.
- Jo's defined responsibility is incidents after acceptance.
- Neither role's remit covers organizing the rehearsal, and no one has accepted it.
- Sponsor Pat has the authority to assign that responsibility.

**Committee takeaway:** Without an assignment from Pat, the remaining criterion has no route to completion.

# Slide 4: Actions Required

| # | Action | Who | Trigger |
|---|---|---|---|
| 1 | Assign responsibility for organizing the rollback rehearsal | Sponsor Pat | Now |
| 2 | Organize and hold the rollback rehearsal | Assigned owner | After action 1 |
| 3 | Approve acceptance | Sponsor Pat | Once the rehearsal succeeds and both criteria are met |
| 4 | Take ownership of incidents | Operations lead Jo | On acceptance |

- Lee continues to own defect fixes until action 3 is complete.
- If the rehearsal is unsuccessful, acceptance stays open and current responsibilities continue.

**Decision requested today:** Confirm the service is not yet ready for handoff, and ask Pat to name a rehearsal owner.