**Slide 1: Decision Requested**
Steering committee must decide whether to approve operational handoff. Acceptance requires two criteria: an approved runbook and a successful rollback rehearsal. Current status: runbook approved; rollback rehearsal not performed. Therefore the service is not ready for operational handoff. Decision: do not accept until rehearsal succeeds.

**Slide 2: Readiness Assessment**
| Criterion | Status | Evidence |
|---|---|---|
| Approved runbook | Met | Runbook is approved. |
| Successful rollback rehearsal | Not met | Rehearsal has not happened. |
| Ownership clarity | Gap | No role has accepted responsibility for organizing the rehearsal. |

Readiness fails on the rehearsal criterion. Engineering lead Lee owns defect fixes until acceptance. Operations lead Jo owns incidents only after acceptance. Neither owns organizing the rehearsal.

**Slide 3: Required Actions**
1. Sponsor Pat assigns responsibility for organizing the rollback rehearsal.
2. Assigned role organizes and conducts the rehearsal.
3. Rehearsal must succeed.
4. Pat approves acceptance once criteria are met.
5. Lee retains defect-fix ownership until acceptance.
6. Jo assumes incident ownership only after acceptance.

Action owner: Pat for assignment and approval. Rehearsal organizer: to be assigned. No other role currently owns this.

**Slide 4: Decision Options and Recommendation**
Option A: Accept now. Rejected—rehearsal criterion unmet; Jo would not own incidents.
Option B: Defer acceptance, assign rehearsal responsibility, rehearse, then decide. Recommended.
Option C: Reject handoff permanently. Not supported—gap is addressable by Pat.

Recommendation: Defer acceptance. Pat assigns rehearsal responsibility. Once rehearsal succeeds and runbook remains approved, Pat may approve acceptance. Then Lee hands off defect fixes; Jo assumes incidents.