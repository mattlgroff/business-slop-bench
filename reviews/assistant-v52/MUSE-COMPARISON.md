# Muse Wonder is close to Astra on this writing panel

October 13, 2026. These are the corrected legacy v2 scores from assistant-v52. The vendor signatory inference was retired for every model, not just Muse. The replacement v3 task has not been run.

## House rules: the closest comparison

| Model / attempt | Checks | Content ready | Ready without edits | Input / output per 1M tokens | Charge for 8 drafts |
|---|---:|---:|---:|---:|---:|
| GPT-6 Astra primary | 54/54 | 8/8 | 8/8 | $10 / $50 | $0.358140 |
| Muse Wonder 1.0 primary | 54/54 | 8/8 | 7/8 | $4 / $20 | $0.206844 |
| GPT-6.1 Sol primary | 54/54 | 7/8 | 4/8 | $2 / $10 | $0.072768 |
| GPT-6 Astra repeat, sample 3 | 54/54 | 8/8 | 6/8 | $10 / $50 | $0.358840 |

Muse ranks second under the existing order: content checks, ready without edits, content ready, fewer failures. It is almost as good as Astra on the primary house-rule panel. Its one remaining editorial finding is a repeated summary bullet in the AI strategy deck. Both full Astra repeats produced 6/8 ready without edits. Muse has only one attempt per brief, so these results do not establish a reliable gap or statistical equivalence.

Muse's house run cost about 42% less than Astra's primary house run. All sixteen Muse calls cost $0.378520, versus $0.470180 for Astra's original sixteen. Muse's plain run cost more than Astra's plain run; cheaper token rates do not guarantee a cheaper document.

With the plain brief, Muse passed 53/54, with 7/8 content-ready and 3/8 ready without edits. Its strategy deck called the pilot approved and ready when the source only approved the internal documents. That unsupported approval claim remains a failure. Astra's primary plain result was 54/54, 8/8 content-ready and 4/8 ready without edits.

## Other requested models

| Model | Plain checks | Plain content ready / no edits | House checks | House content ready / no edits | Charge for 16 drafts |
|---|---:|---:|---:|---:|---:|
| Gemini 4 Argon | 51/54 | 5/8 / 1/8 | 51/54 | 5/8 / 4/8 | $0.097468 |
| Nemotron 3.5 Lightning Free | 45/54 | 1/8 / 1/8 | 46/54 | 4/8 / 2/8 | $0 reported |
| Gemini 3.8 Flash, saved primary | 51/54 | 5/8 / 0/8 | 51/54 | 5/8 / 3/8 | $0.0428445 |

Argon and Nemotron still have substantive grounding and task-completeness failures. Gemini 3.8 Flash was not regenerated for this comparison. Its saved grades receive the same signatory correction as the other models.

## Evidence and boundaries

- Forty-eight fresh calls: sixteen Argon under pilot-v31, sixteen Nemotron and sixteen Muse under pilot-v32. Every call finished normally, with no warnings, harness output cap, generation deadline or retry. All requested low reasoning. Saved input verification matches the earlier Sol v2 prompts exactly.
- Muse exact ID: `meta/muse-wonder-1.0`. Saved responses verify the requested model, response model and Gateway canonical slug.
- List prices come from the saved pilot-v32 Gateway catalog, captured October 13 local time. Observed charges are saved Gateway billing, not estimates from list rates.
- [Corrected grades and boundary](REPORT.md), [all rankings](RANKING.md), [before/after decisions](corrections.json), [Muse and Nemotron original review](../assistant-v51/REPORT.md), [Argon original review](../assistant-v50/REPORT.md), [Astra sample 3](../sol61-astra-low/REPORT.md).
- All 33 models are ranked on writing performance. Retention metadata no longer excludes a model. Primary attempts and repeats remain separate; no best-of selection.
- The assistant could see model identities. There is no independent human gold or validated judge agreement. This is a small, provisional writing panel.
