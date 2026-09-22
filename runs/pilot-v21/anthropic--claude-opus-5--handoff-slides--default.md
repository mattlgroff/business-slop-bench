# Slide 1 — Decision Required

**Question for the committee:** Is the service ready for operational handoff today?

**Answer: No.** Acceptance requires two criteria: an approved runbook and a successful rollback rehearsal. Only one is met.

| Criterion | Status |
|---|---|
| Approved runbook | Met |
| Successful rollback rehearsal | Not met — rehearsal has not happened |

**Ask of the committee:** Do not approve acceptance at this meeting. Instead, close the ownership gap described on Slide 3 so acceptance can be reconsidered.

---

# Slide 2 — Current Readiness Position

**What is in place**
- The runbook is approved.

**What is outstanding**
- The rollback rehearsal has not happened, so its outcome is unknown. Readiness cannot be confirmed until a rehearsal is run and succeeds.

**Accountability today**
- Engineering lead Lee owns defect fixes until acceptance.
- Operations lead Jo owns incidents only after acceptance.

**Implication:** Until acceptance occurs, defect ownership sits with Lee and Jo does not yet own incidents. Delaying acceptance therefore keeps responsibilities where they currently sit; it does not create an unowned period for defects.

---

# Slide 3 — The Blocking Gap: Unassigned Rehearsal Ownership

**The gap:** No role has accepted responsibility for organizing the rollback rehearsal.

**Why this blocks progress:** The rehearsal is a mandatory acceptance criterion, but neither the delivery nor the operations accountability described in the source pack covers organizing it. Without an assigned owner, the outstanding criterion cannot be scheduled or completed, and acceptance remains unreachable indefinitely.

**Who can resolve it:** Sponsor Pat has the authority to assign that responsibility.

**Note on limits:** This pack does not state a rehearsal date, duration, or cost. Those should be established by the owner once assigned.

---

# Slide 4 — Actions Required

| # | Action | Owner |
|---|---|---|
| 1 | Assign responsibility for organizing the rollback rehearsal | Sponsor Pat |
| 2 | Organize and run the rollback rehearsal | Person assigned in Action 1 |
| 3 | Continue defect fixes through to acceptance | Engineering lead Lee |
| 4 | Confirm both acceptance criteria are met, then approve acceptance | Sponsor Pat |
| 5 | Assume incident ownership on acceptance | Operations lead Jo |

**Sequence:** Action 1 unblocks Action 2; Action 2 is the only outstanding acceptance criterion. Action 4 can only follow a *successful* rehearsal. Action 5 is triggered by acceptance.

**Return to committee:** Reconsider handoff readiness once the rehearsal outcome is known.