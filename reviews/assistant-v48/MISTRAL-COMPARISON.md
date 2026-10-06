# Mistral Large 4: an échec on this writing panel

October 6, 2026. Sixteen completed drafts, eight synthetic briefs, plain and house-rule conditions. These are provisional, unblinded assistant grades.

| Model | Plain checks | Plain ready without edits | House checks | House ready without edits | House cost, eight drafts |
|---|---:|---:|---:|---:|---:|
| Mistral Large 4 | 46/54 | 0/8 | 48/54 | 1/8 | $0.01974 |
| GLM 5.3 Flash | 49/54 | 1/8 | 48/54 | 2/8 | $0.0046 |
| DeepSeek V4.1 Flash | 52/54 | 0/8 | 50/54 | 0/8 | $0.0084 |
| Qwen 3.8 Max | 49/54 | 1/8 | 52/54 | 3/8 | $0.0866 |

Mistral placed 22nd of 23 eligible models on the plain brief and 20th with house rules. Its only house-rule draft ready without edits was the change order. All drafts met the word limits, but the house-rule readout still contained three em dashes. The failures went beyond style: invented prior discussions, team readiness, signing authority, approval status, and a five-business-day scheduling commitment.

GLM Flash matched the house content score, produced twice as many drafts ready without edits, and cost less. DeepSeek Flash passed more checks in both conditions but still needed editing on every draft. Qwen Max exceeded Mistral on both checks and ready-without-edits counts. Qwen Flash and MiniMax did worse than Mistral with house rules, so this is not a claim that every Chinese model won.

These were Gateway-hosted calls. No local hardware, quantization or laptop inference was tested.

Reasoning limits the comparison: Mistral's low request failed with HTTP 400. The successful requests used none, but Gateway warned that reasoning configuration was ignored. Treat Mistral as provider-default reasoning. GLM Flash and Qwen Max requested low; DeepSeek Flash requested none. Do not present this as a controlled comparison at one reasoning level.

Successful Mistral calls cost $0.02496809 in total. The failed low-request reservation remains separately accounted in the budget. No completed draft was retried or replaced.

[Full findings and quotes](REPORT.md), [saved decisions](decisions.json), [ranking](RANKING.md), [input verification](input-verification.json).
