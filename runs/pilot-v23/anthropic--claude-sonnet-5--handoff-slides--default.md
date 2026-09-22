# Slide 1: Current Readiness Status
- Acceptance criteria: (1) approved runbook, (2) successful rollback rehearsal
- Runbook: **Approved** ✅
- Rollback rehearsal: **Not yet completed** ❌
- Conclusion: Service is **not ready** for operational handoff — one criterion outstanding

# Slide 2: Ownership Today (Pre-Acceptance)
| Area | Owner | Scope |
|---|---|---|
| Defect fixes | Lee (Engineering Lead) | Owns until acceptance |
| Incidents | Jo (Operations Lead) | Owns only after acceptance |
- Key gap: **No one has accepted responsibility for organizing the rollback rehearsal**
- This is a coordination gap, not a technical blocker

# Slide 3: Decision Required from Steering Committee
- The committee must decide: **who organizes the rollback rehearsal, and by when**
- Sponsor Pat holds authority to:
  - Assign rehearsal responsibility
  - Approve acceptance once both criteria are satisfied
- Until Pat assigns an owner, the rehearsal has no forcing function to occur
- Decision needed today: designate an owner (e.g., Lee or Jo) for rehearsal execution

# Slide 4: Path to Handoff — Required Actions
1. **Pat** assigns rehearsal organizing responsibility to a named owner
2. Owner schedules and executes the rollback rehearsal
3. Rehearsal outcome reported back to Pat
4. If successful, **Pat approves acceptance**
5. Upon acceptance: incident ownership transfers from Lee to Jo per defined roles
- **Recommendation:** Steering committee approve rehearsal owner assignment now to avoid handoff delay