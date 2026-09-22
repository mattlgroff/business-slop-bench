**Slide 1 — Decision Requested**
- Question for the committee: Is the service ready for operational handoff?
- Recommendation: Not yet. One acceptance criterion remains unmet.
- Decision needed today: Assign an owner for the rollback rehearsal so acceptance can proceed.

**Slide 2 — Acceptance Criteria Status**

| Criterion | Status | Evidence |
|---|---|---|
| Approved runbook | Met | Runbook is approved |
| Successful rollback rehearsal | Not met | Rehearsal has not happened |

- Readiness verdict: Acceptance cannot be granted until the rehearsal is completed successfully.

**Slide 3 — Ownership Gap and Risk**
- Current responsibilities:
  - Lee (Engineering lead) owns defect fixes until acceptance.
  - Jo (Operations lead) owns incidents only after acceptance.
  - Pat (Sponsor) can assign responsibility and approve acceptance once criteria are met.
- Gap: No role has accepted responsibility for organizing the rollback rehearsal.
- Risk: Without an assigned owner, the rehearsal will not be scheduled, acceptance stalls, and the handoff date remains undefined.

**Slide 4 — Actions Required**

| # | Action | Owner | Dependency |
|---|---|---|---|
| 1 | Assign responsibility for organizing the rollback rehearsal | Pat | Committee decision today |
| 2 | Plan and conduct the rollback rehearsal | Assignee (per Action 1) | Action 1 |
| 3 | Confirm rehearsal result against acceptance criterion | Assignee reports to Pat | Action 2 |
| 4 | Approve acceptance; incident ownership transfers to Jo | Pat | Action 3 successful |

- Until acceptance: Lee continues to own defect fixes.
- Ask of the committee: Endorse Pat assigning the rehearsal owner now and reconvene once the rehearsal result is available.