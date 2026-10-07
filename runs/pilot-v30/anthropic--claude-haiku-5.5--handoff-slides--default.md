Slide 1: Readiness Decision Requested
- Decision: Is the service ready for operational handoff to Operations (Jo)?
- Current status: Not yet ready. Handoff requires acceptance, and acceptance has two criteria.
- Criteria check:
  - Approved runbook: Met
  - Successful rollback rehearsal: Not met (has not happened)

Slide 2: Current Ownership and Gap
- Engineering (Lee): owns defect fixes until acceptance
- Operations (Jo): owns incidents only after acceptance
- Gap: No role has accepted responsibility for organizing the rollback rehearsal
- Implication: Until the rehearsal is organized and passed, the service cannot move to Operations, and incident ownership stays with Engineering.

Slide 3: Actions Required to Close the Gap
- Sponsor Pat assigns a named owner to organize the rollback rehearsal
- Assigned owner schedules and runs the rehearsal
- Rehearsal result is reported against the success criterion
- Engineering (Lee) continues defect fixes until acceptance

Slide 4: Recommendation and Decision
- Recommendation: Do not approve handoff today; direct Pat to assign the rehearsal owner now
- Re-review trigger: Successful rollback rehearsal reported
- Once both criteria are met, Pat approves acceptance and handoff to Operations (Jo) proceeds
- Decision for committee: Confirm the recommendation and set the re-review date