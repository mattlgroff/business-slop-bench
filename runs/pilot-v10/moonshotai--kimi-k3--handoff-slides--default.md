# Slide 1: Purpose — Operational Handoff Readiness Decision

**Objective:** Steering committee to decide whether the service is ready for handoff to Operations.

**Decision framing:**
- Handoff transfers incident ownership from Engineering (Lee) to Operations (Jo).
- Jo owns incidents **only after acceptance** is granted.
- Until acceptance, Lee owns defect fixes.

**Question for the committee:** Have the acceptance criteria been met, and if not, what actions close the gap?

---

# Slide 2: Readiness Assessment Against Acceptance Criteria

Acceptance requires two conditions:

| Criterion | Status |
|---|---|
| Approved runbook | ✅ Complete |
| Successful rollback rehearsal | ❌ Not yet held |

**Conclusion:** The service is **not ready** for operational handoff. One of two acceptance criteria is unmet.

**Blocking gap:** No role has accepted responsibility for organizing the rollback rehearsal — it is unowned, not merely unscheduled.

---

# Slide 3: Actions Required Before Handoff

1. **Assign rehearsal ownership.** The rehearsal has no organizer; this accountability gap must be closed first.
2. **Conduct a successful rollback rehearsal.**
3. **Grant acceptance** once both criteria (approved runbook + successful rehearsal) are satisfied.
4. **Execute handoff:** incident ownership moves from Lee to Jo upon acceptance; Lee's defect-fix responsibility ends at that point.

**Sequencing note:** Steps are dependent — acceptance cannot occur before the rehearsal succeeds, and the rehearsal cannot proceed reliably without a named owner.

---

# Slide 4: Decision Requested and Authority

**Recommendation:** Defer handoff. Acceptance criteria are not yet met.

**Decision for the committee:**
- Confirm the service is not yet ready for operational handoff.
- Direct Sponsor Pat to **assign responsibility for organizing the rollback rehearsal** — Pat holds this assignment authority.
- Authorize Pat to **approve acceptance** once the runbook criterion (already met) and the rollback rehearsal criterion are both satisfied.

**Outcome after approval:** Operations lead Jo assumes incident ownership; Engineering lead Lee's pre-acceptance defect-fix duty concludes.