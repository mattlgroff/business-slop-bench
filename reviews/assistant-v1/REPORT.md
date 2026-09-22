# Assistant grading: Qwen Flash and Kimi K3

Provisional assistant-authored grades, not human gold or independent benchmark validation. Model identities were visible. Same eight briefs, default and house-style conditions, one output per cell. No Jev calls were used for these decisions.

## Summary

Content checks are the existing task-specific rubric, not an invented overall quality score. Unresolved checks receive no credit and are reported separately. A high check fraction can coexist with a critical failure. Counts of overlapping checks are not independent observations.

| Model | Condition | Content checks passed | Failed | Unresolved | Content ready | Style gate pass | Ready without edits |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen Flash | default | 47/54 | 6 | 1 | 1/8 | 2/8 | 0/8 |
| Qwen Flash | house | 40/54 | 13 | 1 | 1/8 | 8/8 | 1/8 |
| Kimi K3 | default | 50/54 | 3 | 1 | 4/8 | 4/8 | 4/8 |
| Kimi K3 | house | 48/54 | 6 | 0 | 3/8 | 8/8 | 1/8 |

Content ready requires all content checks to pass, within the word limit, with no placeholders. Ready without edits also requires the house style gate and no recorded editorial findings. Default style scores describe house-style fit without having supplied the house-style instructions. They are not instruction-following failures.

## Per-draft results

| Model | Brief | Condition | Content checks | Main reason to edit |
|---|---|---|---:|---|
| Qwen Flash | [pilot-client-email](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-client-email--default.md) | default | 6/7 | Invents prior discussions and an initial risk mitigation strategy absent from the source. |
| Qwen Flash | [pilot-client-email](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-client-email--house.md) | house | 4/7 | Submitting an access request does not explicitly require granted approval before data access. |
| Qwen Flash | [launch-delay-email](../../runs/pilot-v8/alibaba--qwen3.8-flash--launch-delay-email--default.md) | default | 5/6 | Invents team performance, review quality and present readiness. |
| Qwen Flash | [launch-delay-email](../../runs/pilot-v8/alibaba--qwen3.8-flash--launch-delay-email--house.md) | house | 5/6 | Readiness and confidence are asserted without evidence in the source. |
| Qwen Flash | [vendor-decision-memo](../../runs/pilot-v8/alibaba--qwen3.8-flash--vendor-decision-memo--default.md) | default | 5/6 | An uncommitted SSO date does not prove impossibility throughout year one. |
| Qwen Flash | [vendor-decision-memo](../../runs/pilot-v8/alibaba--qwen3.8-flash--vendor-decision-memo--house.md) | house | 5/6 | Names Priya in the sender line but does not explicitly preserve CFO approval before signing. |
| Qwen Flash | [pilot-results-memo](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--default.md) | default | 6/7 | Failure of a quality threshold does not establish a failure of speed; also attributes a proposed design to Sam without source support. |
| Qwen Flash | [pilot-results-memo](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--house.md) | house | 4/7 | Reports endpoints but not the requested reduction of 3 minutes or 20%. |
| Qwen Flash | [discovery-proposal](../../runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--default.md) | default | 5/7 | Offers email confirmation as an alternative to signature, conflicting with the signature prerequisite later in the draft. |
| Qwen Flash | [discovery-proposal](../../runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--house.md) | house | 5/7 | Confuses approval to engage with acceptance of completed deliverables. |
| Qwen Flash | [change-order](../../runs/pilot-v8/alibaba--qwen3.8-flash--change-order--default.md) | default | 7/7 | Unfilled placeholders. |
| Qwen Flash | [change-order](../../runs/pilot-v8/alibaba--qwen3.8-flash--change-order--house.md) | house | 7/7 | No supported edits found in this review. |
| Qwen Flash | [ai-strategy-slides](../../runs/pilot-v8/alibaba--qwen3.8-flash--ai-strategy-slides--default.md) | default | 6/7 | Low risk and ready go beyond the given facts, but may be read as recommendation rationale rather than a verified status. |
| Qwen Flash | [ai-strategy-slides](../../runs/pilot-v8/alibaba--qwen3.8-flash--ai-strategy-slides--house.md) | house | 4/7 | Lists options and a metric but never recommends choosing knowledge search. |
| Qwen Flash | [handoff-slides](../../runs/pilot-v8/alibaba--qwen3.8-flash--handoff-slides--default.md) | default | 7/7 | Abstract restatement adds no information beyond the explicit unassigned rehearsal organizer. |
| Qwen Flash | [handoff-slides](../../runs/pilot-v8/alibaba--qwen3.8-flash--handoff-slides--house.md) | house | 6/7 | Source assigns Lee defect fixes, not ownership of the approved runbook. |
| Kimi K3 | [pilot-client-email](../../runs/pilot-v8/moonshotai--kimi-k3--pilot-client-email--default.md) | default | 7/7 | No supported edits found in this review. |
| Kimi K3 | [pilot-client-email](../../runs/pilot-v8/moonshotai--kimi-k3--pilot-client-email--house.md) | house | 6/7 | Adds a definite delivery sequence not supplied or labelled as a proposed plan. |
| Kimi K3 | [launch-delay-email](../../runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--default.md) | default | 5/6 | Rules out delivery concerns and asserts team performance without evidence. |
| Kimi K3 | [launch-delay-email](../../runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--house.md) | house | 5/6 | Invents delivery status and separately promises preparation this week. |
| Kimi K3 | [vendor-decision-memo](../../runs/pilot-v8/moonshotai--kimi-k3--vendor-decision-memo--default.md) | default | 5/6 | The brief blocks production without SSO, but does not establish that every capability is unusable. The sentence may be intended to refer only to production value. |
| Kimi K3 | [vendor-decision-memo](../../runs/pilot-v8/moonshotai--kimi-k3--vendor-decision-memo--house.md) | house | 6/6 | Third request for Alpha approval after Recommendation and Decision sections. |
| Kimi K3 | [pilot-results-memo](../../runs/pilot-v8/moonshotai--kimi-k3--pilot-results-memo--default.md) | default | 7/7 | No supported edits found in this review. |
| Kimi K3 | [pilot-results-memo](../../runs/pilot-v8/moonshotai--kimi-k3--pilot-results-memo--house.md) | house | 7/7 | Manufactured phrasing repeats the already explicit 89% versus 92% result. |
| Kimi K3 | [discovery-proposal](../../runs/pilot-v8/moonshotai--kimi-k3--discovery-proposal--default.md) | default | 7/7 | No supported edits found in this review. |
| Kimi K3 | [discovery-proposal](../../runs/pilot-v8/moonshotai--kimi-k3--discovery-proposal--house.md) | house | 5/7 | A later statement treats delivery itself as closing acceptance rather than preserving sponsor confirmation. |
| Kimi K3 | [change-order](../../runs/pilot-v8/moonshotai--kimi-k3--change-order--default.md) | default | 7/7 | No supported edits found in this review. |
| Kimi K3 | [change-order](../../runs/pilot-v8/moonshotai--kimi-k3--change-order--house.md) | house | 7/7 | No supported edits found in this review. |
| Kimi K3 | [ai-strategy-slides](../../runs/pilot-v8/moonshotai--kimi-k3--ai-strategy-slides--default.md) | default | 6/7 | Pending production authorization does not establish that every pilot is impermissible. |
| Kimi K3 | [ai-strategy-slides](../../runs/pilot-v8/moonshotai--kimi-k3--ai-strategy-slides--house.md) | house | 6/7 | No approval date is known. A current authorization gap does not establish impossibility for the whole quarter. This is not a penalty for the brief's next/this-quarter ambiguity. |
| Kimi K3 | [handoff-slides](../../runs/pilot-v8/moonshotai--kimi-k3--handoff-slides--default.md) | default | 6/7 | Invents Lee as pre-acceptance incident owner. Source only assigns Lee defect fixes. |
| Kimi K3 | [handoff-slides](../../runs/pilot-v8/moonshotai--kimi-k3--handoff-slides--house.md) | house | 6/7 | Invents Lee as pre-acceptance incident owner. Source only assigns Lee defect fixes. |

## Evidence and repairs

### Qwen Flash / pilot-client-email / default

- **grounding fail:** [Following recent discussions](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-client-email--default.md:5). Invents prior discussions and an initial risk mitigation strategy absent from the source.
- **Style 16:** [This pilot offers a low-risk opportunity to validate efficiency gains before committing to broader implementation.](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-client-email--default.md:13). Generic reassurance repeats the bounded-pilot rationale without adding decision information.

### Qwen Flash / pilot-client-email / house

- **C04 fail:** [I will submit the access request for security clearance once you reply.](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-client-email--house.md:17). Submitting an access request does not explicitly require granted approval before data access.
- **C06 fail:** [Please confirm acceptance of the scope and fee.](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-client-email--house.md:17). The requested approval is not explicitly conditional on security clearance.
- **grounding review:** [production rollout and specific dates remain out of scope until we review the pilot's results.](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-client-email--house.md:15). Unclear whether specific dates means rollout dates or all scheduling; the latter adds an unsupported dependency.

### Qwen Flash / launch-delay-email / default

- **grounding fail:** [The team is moving efficiently. Nia's review is thorough, and the demo path is ready now.](../../runs/pilot-v8/alibaba--qwen3.8-flash--launch-delay-email--default.md:13). Invents team performance, review quality and present readiness.

### Qwen Flash / launch-delay-email / house

- **grounding fail:** [The team is fully prepared and remains confident in the quality of the release.](../../runs/pilot-v8/alibaba--qwen3.8-flash--launch-delay-email--house.md:3). Readiness and confidence are asserted without evidence in the source.

### Qwen Flash / vendor-decision-memo / default

- **grounding fail:** [the platform cannot reach production within year one under any planned timeline.](../../runs/pilot-v8/alibaba--qwen3.8-flash--vendor-decision-memo--default.md:21). An uncommitted SSO date does not prove impossibility throughout year one.
- **Style 14:** [✅](../../runs/pilot-v8/alibaba--qwen3.8-flash--vendor-decision-memo--default.md:15). Emojis used as professional decision-table structural markers.

### Qwen Flash / vendor-decision-memo / house

- **C05 fail:** [Sign with Alpha.](../../runs/pilot-v8/alibaba--qwen3.8-flash--vendor-decision-memo--house.md:22). Names Priya in the sender line but does not explicitly preserve CFO approval before signing.
- **Style 16:** [Beta offers a $70,000 first-year cost](../../runs/pilot-v8/alibaba--qwen3.8-flash--vendor-decision-memo--house.md:16). Repeats both vendor totals immediately after a table already displaying them.

### Qwen Flash / pilot-results-memo / default

- **grounding fail:** [the scaling threshold fails on both speed and quality grounds](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--default.md:27). Failure of a quality threshold does not establish a failure of speed; also attributes a proposed design to Sam without source support.
- **Style 10:** [### Summary](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--default.md:29). Final summary repeats the recommendation, caveat, quality gate and savings status already stated.

### Qwen Flash / pilot-results-memo / house

- **C01 fail:** [from 15 to 12 minutes](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--house.md:3). Reports endpoints but not the requested reduction of 3 minutes or 20%.
- **C02 fail:** [The pass rate fell to 89%, below the required 92%.](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--house.md:5). Omits the required 94% baseline quality rate.
- **grounding fail:** [This test will control for ticket mix and randomize allocation](../../runs/pilot-v8/alibaba--qwen3.8-flash--pilot-results-memo--house.md:9). Adds a definite randomization commitment to a source that only authorizes a matched-ticket follow-up.

### Qwen Flash / discovery-proposal / default

- **C05 fail:** [Sign** this proposal (or reply confirming approval via email).](../../runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--default.md:38). Offers email confirmation as an alternative to signature, conflicting with the signature prerequisite later in the draft.
- **grounding fail:** [or reply confirming approval via email](../../runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--default.md:38). Adds an unsupported approval alternative.
- **Style 20:** [designed to de-risk a larger investment by separating discovery from delivery.](../../runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--default.md:45). Generic consulting close repeats the discovery-only scope.

### Qwen Flash / discovery-proposal / house

- **C06 fail:** [You approve the engagement by confirming delivery of the three listed artifacts.](../../runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--house.md:23). Confuses approval to engage with acceptance of completed deliverables.
- **grounding fail:** [You approve the engagement by confirming delivery](../../runs/pilot-v8/alibaba--qwen3.8-flash--discovery-proposal--house.md:23). Changes the meaning and timing of the approval step.

### Qwen Flash / change-order / default

- **Style 13:** [[Insert Date]](../../runs/pilot-v8/alibaba--qwen3.8-flash--change-order--default.md:3). Unfilled template placeholders in a requested finished proposal; [Project Lead] is also unfilled.

### Qwen Flash / ai-strategy-slides / default

- **grounding review:** [Option A is ready: approved source documents, defined IT owner, low risk](../../runs/pilot-v8/alibaba--qwen3.8-flash--ai-strategy-slides--default.md:17). Low risk and ready go beyond the given facts, but may be read as recommendation rationale rather than a verified status.

### Qwen Flash / ai-strategy-slides / house

- **C01 fail:** [Slide 4: Evaluation Criteria and Success Threshold](../../runs/pilot-v8/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:18). Lists options and a metric but never recommends choosing knowledge search.
- **C05 fail:** [COO selects the pilot and reports results before expansion.](../../runs/pilot-v8/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:4). Source assigns selection to COO and reporting to Dana.
- **grounding fail:** [COO selects the pilot and reports results before expansion.](../../runs/pilot-v8/alibaba--qwen3.8-flash--ai-strategy-slides--house.md:4). Misassigns reporting responsibility.

### Qwen Flash / handoff-slides / default

- **Style 29:** [The gap is structural: the handoff boundary creates a zone of unowned work.](../../runs/pilot-v8/alibaba--qwen3.8-flash--handoff-slides--default.md:21). Abstract restatement adds no information beyond the explicit unassigned rehearsal organizer.

### Qwen Flash / handoff-slides / house

- **grounding fail:** [| Runbook approved | Lee | Done |](../../runs/pilot-v8/alibaba--qwen3.8-flash--handoff-slides--house.md:41). Source assigns Lee defect fixes, not ownership of the approved runbook.

### Kimi K3 / pilot-client-email / house

- **grounding fail:** [begin baseline measurement in week one](../../runs/pilot-v8/moonshotai--kimi-k3--pilot-client-email--house.md:13). Adds a definite delivery sequence not supplied or labelled as a proposed plan.
- **Style 16:** [Over the six weeks we will establish a handling-time baseline](../../runs/pilot-v8/moonshotai--kimi-k3--pilot-client-email--house.md:7). Overlong email repeats the pilot rationale and approval request across several paragraphs; exceeds the explicit limit.

### Kimi K3 / launch-delay-email / default

- **grounding fail:** [not a delivery concern](../../runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--default.md:11). Rules out delivery concerns and asserts team performance without evidence.
- **Style 2:** [A quick update on where we stand with the launch.](../../runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--default.md:5). Throat clearing before the actual launch update.

### Kimi K3 / launch-delay-email / house

- **grounding fail:** [Work continues on schedule against the original scope](../../runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--house.md:9). Invents delivery status and separately promises preparation this week.
- **Style 10:** [Action needed from you:](../../runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--house.md:11). Repeats the staging-demo decision already requested earlier in the email.

### Kimi K3 / vendor-decision-memo / default

- **grounding review:** [the savings purchase zero usable capability.](../../runs/pilot-v8/moonshotai--kimi-k3--vendor-decision-memo--default.md:32). The brief blocks production without SSO, but does not establish that every capability is unusable. The sentence may be intended to refer only to production value.
- **Style 16:** [Alpha totals $92,000; Beta totals $70,000.](../../runs/pilot-v8/moonshotai--kimi-k3--vendor-decision-memo--default.md:24). Repeats the table values, then repeats Alpha cost and headroom again in the recommendation.

### Kimi K3 / vendor-decision-memo / house

- **Style 10:** [## Requested action](../../runs/pilot-v8/moonshotai--kimi-k3--vendor-decision-memo--house.md:32). Third request for Alpha approval after Recommendation and Decision sections.

### Kimi K3 / pilot-results-memo / house

- **Style 29:** [a clear bar it did not clear](../../runs/pilot-v8/moonshotai--kimi-k3--pilot-results-memo--house.md:16). Manufactured phrasing repeats the already explicit 89% versus 92% result.

### Kimi K3 / discovery-proposal / house

- **C06 fail:** [delivery of the artifacts closes the engagement](../../runs/pilot-v8/moonshotai--kimi-k3--discovery-proposal--house.md:44). A later statement treats delivery itself as closing acceptance rather than preserving sponsor confirmation.
- **grounding fail:** [There is no extended acceptance process](../../runs/pilot-v8/moonshotai--kimi-k3--discovery-proposal--house.md:44). Adds an unauthorized acceptance limitation; also claims an attached agreement and scheduling availability not provided.
- **Style 10:** [Discovery ends with delivery of the process map, backlog, and recommendation](../../runs/pilot-v8/moonshotai--kimi-k3--discovery-proposal--house.md:56). Repeats the deliverables and payment sequence after describing both in prior sections.

### Kimi K3 / ai-strategy-slides / default

- **grounding fail:** [Cannot be the compliant near-term pilot](../../runs/pilot-v8/moonshotai--kimi-k3--ai-strategy-slides--default.md:20). Pending production authorization does not establish that every pilot is impermissible.

### Kimi K3 / ai-strategy-slides / house

- **grounding fail:** [Option B cannot enter production this quarter.](../../runs/pilot-v8/moonshotai--kimi-k3--ai-strategy-slides--house.md:13). No approval date is known. A current authorization gap does not establish impossibility for the whole quarter. This is not a penalty for the brief's next/this-quarter ambiguity.

### Kimi K3 / handoff-slides / default

- **grounding fail:** [incident ownership moves from Lee to Jo](../../runs/pilot-v8/moonshotai--kimi-k3--handoff-slides--default.md:34). Invents Lee as pre-acceptance incident owner. Source only assigns Lee defect fixes.

### Kimi K3 / handoff-slides / house

- **grounding fail:** [Incident ownership transfers from Lee to Jo](../../runs/pilot-v8/moonshotai--kimi-k3--handoff-slides--house.md:15). Invents Lee as pre-acceptance incident owner. Source only assigns Lee defect fixes.

## Limits and preserved decisions

- Do not score this/next-quarter inconsistency introduced by the AI strategy brief itself.
- Handoff default Qwen: No further criteria exist is accepted as referring to the two supplied acceptance criteria, not unknown external policy. This revises the earlier tentative editorial concern.
- Matched-ticket randomization is treated as a new delivery commitment when asserted as what the test will do, rather than labelled as a proposed design.
- C01 for results requires the stated delta (3 minutes or 20%), not just endpoints from which a reader could calculate it.

All quoted findings are checked against the saved text and carry line/offset anchors in [grades.json](grades.json). Missing content is assessed against the full draft; an excerpt is context, not proof of absence. No statistical model ranking is justified by eight briefs and a single unblinded assistant reviewer.
