**Slide 1: Handoff Readiness — Current Status**
- Purpose: Decide if the service is ready for operational handoff
- Acceptance criteria: (1) approved runbook, (2) successful rollback rehearsal
- Runbook: ✅ Approved
- Rollback rehearsal: ❌ Not yet performed
- Conclusion: Service is **not yet ready** for acceptance

**Slide 2: Roles and Responsibilities**
- Engineering lead Lee: owns defect fixes until acceptance
- Operations lead Jo: owns incidents only after acceptance
- Sponsor Pat: can assign responsibility and approve acceptance once criteria are met
- Key issue: neither Lee nor Jo currently owns the rehearsal task

**Slide 3: The Blocking Gap**
- One acceptance criterion outstanding: rollback rehearsal
- Root cause: no role has accepted responsibility for organizing the rehearsal
- Impact: acceptance cannot proceed; ownership of incidents cannot transfer to Jo
- Until acceptance, defect responsibility remains with Lee

**Slide 4: Decision and Actions Required**
- Decision requested: Sponsor Pat to assign responsibility for organizing the rollback rehearsal
- Action 1: Assigned owner schedules and conducts the rollback rehearsal
- Action 2: On successful rehearsal, Pat approves acceptance
- Action 3: On acceptance, incident ownership transfers to Jo
- Recommendation: Do not approve handoff today; approve once rehearsal succeeds