# Opus 5 retry and separate Opus 4.6 comparison

Exact model IDs were checked against the requested model, returned model ID and Gateway canonical slug in each saved response. No 4.6 output is labelled as Opus 5.

| Model | Brief | Condition | Content checks | Words / limit | Em dashes | Successful charge |
|---|---|---|---:|---:|---:|---:|
| Opus 5 | launch-delay-email | house | 5/6 | 197/180 | 0 | $0.032225 |
| Opus 4.6 | pilot-client-email | default | 5/7 | 178/180 | 2 | $0.007960 |
| Opus 4.6 | pilot-client-email | house | 6/7 | 164/180 | 0 | $0.021570 |

Provisional, unblinded assistant grades. Opus 4.6 house has one unresolved grounding check, not a confirmed grounding failure. Neither partial model sample supports an eight-brief ranking.

## Findings

### Opus 5 / launch-delay-email / house

[Saved draft](../../runs/pilot-v14/anthropic--claude-opus-5--launch-delay-email--house.md)

- **grounding fail:** [Nia's team has kept the review on a clear schedule and has flagged each step early](../../runs/pilot-v14/anthropic--claude-opus-5--launch-delay-email--house.md:9). Invents a record of team performance and early warnings not provided in the source.
- **Length:** 197 words exceeds the 180-word limit.

### Opus 4.6 / pilot-client-email / default

[Saved draft](../../runs/pilot-v15/anthropic--claude-opus-4.6--pilot-client-email--default.md)

- **C04 fail:** [We initiate security clearance for client data access.](../../runs/pilot-v15/anthropic--claude-opus-4.6--pilot-client-email--default.md:20). Initiating clearance does not explicitly require granted approval before data access.
- **grounding fail:** [every week of delay is unquantified cost](../../runs/pilot-v15/anthropic--claude-opus-4.6--pilot-client-email--default.md:15). Asserts a cost of delay without supplied evidence; also invents prior discussions.
- **Style 2:** [I'm writing to formally propose](../../runs/pilot-v15/anthropic--claude-opus-4.6--pilot-client-email--default.md:5). Delays the proposal with an unnecessary announcement of writing it.

### Opus 4.6 / pilot-client-email / house

[Saved draft](../../runs/pilot-v15/anthropic--claude-opus-4.6--pilot-client-email--house.md)

- **grounding review:** [measure actual improvement against it](../../runs/pilot-v15/anthropic--claude-opus-4.6--pilot-client-email--house.md:7). May imply improvement will exist or an intervention beyond assessment, but could mean measuring whether improvement occurs. The source does not resolve that reading.
- **Style 2:** [Below is the summary.](../../runs/pilot-v15/anthropic--claude-opus-4.6--pilot-client-email--house.md:5). Unnecessary preamble inside the requested finished email.

[Model identity receipts](model-verification.json) preserve routing provider and generation IDs without credential details. Opus 5 used vertexAnthropic; Opus 4.6 used anthropic. The prior Opus 5 failures remain charged at their conservative reservations. Their cause is still not established by the generic 429 message.

Opus 4.6 increases the requested roster to 22 models and the full target to 352 drafts. Earlier 21-model protocols remain intact. [Earlier complete comparisons](../assistant-v6/REPORT.md).
