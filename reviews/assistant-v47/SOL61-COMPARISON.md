# GPT-6.1 Sol, low reasoning

Tested September 29, 2026. Exact Gateway model: `openai/gpt-6.1-sol`. Eight frozen v2 briefs, default and house conditions, low reasoning, no output-token cap or generation deadline. All 16 completed with normal stops and one provider attempt each. Inputs match the existing Astra primary inputs byte for byte. The 432 earlier primary judgments remain unchanged.

| Condition | Content checks | Content ready | Ready without edits | Em dashes | Reported charge |
|---|---:|---:|---:|---:|---:|
| Plain | 53/54 | 7/8 | 2/8 | 9 | $0.021788 |
| House rules | 54/54 | 7/8 | 4/8 | 0 | $0.072768 |

Total reported generation charge: $0.094556. The saved Gateway catalog lists base rates of $2 per million input tokens and $10 per million output tokens; cache-write pricing also affects actual charges.

The plain launch email has one unresolved grounding judgment for an unsourced statement about current team focus. This receives no credit but is not a confirmed fabrication. The other 107 content checks pass. Every draft meets its word limit.

Under house rules, the pilot email, pilot readout and AI-plan deck repeat a conclusion without adding information. The handoff deck says, "The source pack does not identify an incident owner before acceptance." That is authoring residue. These four drafts need edits. The launch email, vendor memo, discovery proposal and change order have no supported edits in this review.

Content ready requires all content checks, the word limit and no authoring residue. Ready without edits additionally requires style compliance and no supported editorial findings. Passing every content check does not guarantee either readiness count.

A fresh full-panel Astra run at the same low reasoning is recorded separately in [the comparison study](../sol61-astra-low/REPORT.md), without replacing historical results.

Judgments are provisional and unblinded, with one generation per task and condition. There is no independent human gold. [Evidence and per-draft findings](REPORT.md), [decisions](decisions.json), [ranking](RANKING.md).
