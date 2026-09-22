# Steering Committee: Operational Handoff Readiness

---

## Slide 1: Acceptance Criteria Status

| Criterion | Status |
|---|---|
| Approved runbook | ✅ Complete |
| Successful rollback rehearsal | ❌ Not conducted |

**Summary:** The service is **not ready** for operational handoff. One of two required acceptance criteria remains unmet.

---

## Slide 2: Current Ownership Model

- **Pre-acceptance (now):** Engineering lead Lee owns defect fixes and service responsibility.
- **Post-acceptance:** Operations lead Jo assumes incident ownership.
- Handoff transfers accountability — it cannot occur until both criteria are satisfied.
- Lee currently carries operational risk with no defined end date due to the rehearsal gap.

---

## Slide 3: Gap — Rehearsal Ownership Unassigned

- No role has accepted responsibility for organizing the rollback rehearsal.
- Without an owner, the rehearsal will not be scheduled, and acceptance will stall indefinitely.
- This is a **governance gap**, not a technical gap — the blocker is assignment of responsibility, not capability.
- Sponsor Pat holds the authority to assign this responsibility.

---

## Slide 4: Recommended Actions

| # | Action | Owner | Dependency |
|---|---|---|---|
| 1 | Assign rollback rehearsal organizer | Pat (sponsor) | None — can decide today |
| 2 | Schedule and execute rehearsal | Assigned organizer + Lee + Jo | Action 1 |
| 3 | Confirm criteria met and approve acceptance | Pat (sponsor) | Action 2 successful |
| 4 | Transfer incident ownership to Operations | Jo | Action 3 |

**Ask of the committee:** Direct Pat to assign rehearsal ownership today so the handoff can proceed.