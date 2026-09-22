# Kimi K3 diagnostic screen

Same eight briefs, both conditions, low reasoning, 4,096 output-token cap, and the frozen v8 writer prompts used for Qwen. No tools, revisions, or agent loop. This is an assistant editorial read with model identity visible, not human gold or a calibrated Jev leaderboard.

## Draft observations

| Brief | Default output | House-style output |
|---|---|---|
| Pilot client email | Strong first draft: clear ask, correct scope and fee, target caveat, and explicit security prerequisite. | Preserves key facts, but exceeds the 180-word limit and adds a week-one measurement schedule not supplied by the brief. |
| Launch delay | Gives the right options and owner, but invents claims about team performance and dismisses delivery concerns without evidence. | Repeats the decision request, invents reassurance about the build, and adds preparation this week. |
| Vendor decision | Correct arithmetic, recommendation and approval path; the claim that savings purchase zero usable capability is broader than the production constraint warrants. | Clear recommendation, comparison and CFO approval before signing. Some repetition, but stronger factual restraint than the default. |
| Pilot results | Concise, useful no-scale recommendation, confounding caveat, quality threshold and named next decision. | Preserves the important decision and caveats. Opening wording credits the pilot with the improvement before the following paragraph qualifies causality. |
| Discovery proposal | Concise and commercially clear. Correct installments, exclusions, start prerequisites and acceptance. | Adds unsupported terms, including no extended acceptance process, an attached agreement, and signature-call readiness this week. |
| Change order | Clear price, approval conditions, schedule estimate and approve/decline options. No major issue identified in this editorial read. | Also clear and commercially faithful; repeats dependencies but preserves the required conditions. |
| AI strategy slides | Makes a recommendation and preserves Dana reporting; overstates pending production approval as ruling out any compliant near-term pilot. | Correct recommendation and owner, but claims credit decisions cannot enter production this quarter when no approval date is known. |
| Handoff slides | Correctly blocks acceptance and identifies the unowned rehearsal; invents Lee as the pre-acceptance incident owner. | Preserves most responsibilities, then also states incident ownership transfers from Lee to Jo without support for Lee's incident role. |

## Evidence behind the assessment

- [Pilot default](runs/pilot-v8/moonshotai--kimi-k3--pilot-client-email--default.md) explicitly requests scope and fee approval “subject to security clearance before any access to client data.” This is stronger than Qwen's house-style access-request wording.
- [Pilot house](runs/pilot-v8/moonshotai--kimi-k3--pilot-client-email--house.md) adds “begin baseline measurement in week one.” The source does not supply that delivery plan. It also has 196 words against the 180-word limit.
- [Launch default](runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--default.md) describes the change as “not a delivery concern.” The source only supplies the security timeline, not evidence ruling out delivery concerns.
- [Launch house](runs/pilot-v8/moonshotai--kimi-k3--launch-delay-email--house.md) says work continues “on schedule against the original scope.” The brief does not establish that.
- [Discovery default](runs/pilot-v8/moonshotai--kimi-k3--discovery-proposal--default.md) distinguishes signature, scheduling, kickoff payment and acceptance of delivered artifacts. This avoids Qwen house's engagement-approval/acceptance confusion.
- [Discovery house](runs/pilot-v8/moonshotai--kimi-k3--discovery-proposal--house.md) says “There is no extended acceptance process”. That new limitation is not authorized by the source.

These samples show that house-style compliance can coexist with worse length control and invented commercial detail. Positive editorial observations do not waive factual or instruction-following failures.

## Completed collection

All sixteen calls succeeded without retries. Actual successful generation charges were $0.168232 in total: $0.063224 default and $0.105008 house style. The shared conservative budget is now $2.3122 of $20. This differs from actual billing because the ledger uses conservative prices and retains failed-call reservations from earlier work.

| Mechanical observation | Qwen default | Qwen house | Kimi default | Kimi house |
|---|---:|---:|---:|---:|
| Drafts | 8 | 8 | 8 | 8 |
| Word-limit failures | 0 | 0 | 0 | 1 |
| Em dash characters | 10 | 0 | 11 | 0 |

Both models followed the explicit em dash ban in all eight house-style samples. Kimi's strong default discovery and change-order drafts are worth further testing. Its unsupported claims and one house-style length failure prevent treating this as an overall win. New task-level Jev grades are pending. These are observed samples, not a reliability ranking.

The AI strategy task itself mixes next quarter in the brief with this quarter in the facts. That source ambiguity must be corrected in a new frozen task version before temporal consistency is scored. Current drafts and input hashes remain intact; neither model is penalized here for following that conflicting quarter wording.

[Full draft audit and links](runs/pilot-v8/DRAFT_AUDIT.md)
