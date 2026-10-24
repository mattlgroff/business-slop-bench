## Slide 1: Readiness assessment
- Recommendation: the service is not ready for operational handoff.
- Acceptance requires an approved runbook and a successful rollback rehearsal.
- The runbook is approved, but the rollback rehearsal has not happened. Acceptance criteria are therefore unmet.

## Slide 2: Ownership and the remaining gap
- Engineering lead Lee owns defect fixes until acceptance.
- Operations lead Jo owns incidents only after acceptance.
- No role has accepted responsibility for organizing the rollback rehearsal.
- The remaining acceptance activity has no accepted organizer, and incident ownership cannot transfer to Jo before acceptance.

## Slide 3: Actions required
- Sponsor Pat assigns responsibility for organizing the rollback rehearsal.
- The assigned organizer organizes the rehearsal.
- The service completes a successful rollback rehearsal to meet the outstanding acceptance criterion.
- Lee continues to own defect fixes until acceptance.
- Pat approves acceptance only after both criteria are met.

## Slide 4: Steering committee decision
- Decide that operational handoff should wait for acceptance.
- Ask Pat to assign the rehearsal organizer.
- Treat a successful rollback rehearsal, together with the approved runbook, as the basis for Pat’s acceptance decision.
- After acceptance, Jo owns incidents and operational handoff can proceed.
- If the rehearsal is unsuccessful, acceptance remains pending: Lee retains defect-fix ownership and Jo does not yet own incidents.