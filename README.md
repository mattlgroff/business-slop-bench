# BusinessSlopBench

A small benchmark for the writing most of us actually ask models for at work: the client email, the vendor memo, the pilot readout, the proposal, the change order, the four-slide deck. It measures one thing above all: does the draft say only what the source facts support, or does it invent a deadline, a prior conversation, a readiness claim or an owner that was never there.

I built it, ran 25 models through it, and I am publishing it as is because I am not going to take it further myself. I am asking someone to.

## What I found

Full tables with list prices per million tokens, with and without the zero-data-retention filter:

- [Ranking](reviews/assistant-v44/RANKING.md)
- [Ranking with the zero-data-retention rule switched off](reviews/assistant-v44/RANKING-ignoring-zdr.md)
- [Every grade with its quoted evidence](reviews/assistant-v44/REPORT.md)

Plain brief, no instructions about style:

| Rank | Model | Checks passed (of 54) | Ready to send as is (of 8) | Input / output $ per M tokens |
|---:|---|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 4 | 10 / 50 |
| 2 | GPT-5.6 Terra | 52 | 3 | 2 / 12 |
| 3 | Grok 4.7 | 52 | 3 | 1.20 / 3.60 |
| 4 | Claude Opus 5.5 | 52 | 2 | 4 / 20 |
| 8 | GPT-5.6 Luna | 51 | 2 | 0.20 / 1.20 |
| 18 | Claude Opus 5 | 49 | 0 | 5 / 25 |
| 20 | Qwen 3.8 Flash | 46 | 0 | 0.15 / 0.47 |

Same brief plus my [Zero Defect](https://github.com/mattlgroff/zero-defect) anti-slop rules:

| Rank | Model | Checks passed (of 54) | Ready to send as is (of 8) | Input / output $ per M tokens |
|---:|---|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 8 | 10 / 50 |
| 2 | GPT-5.6 Sol | 53 | 4 | 4 / 20 |
| 3 | GPT-5.6 Luna | 52 | 4 | 0.20 / 1.20 |
| 8 | Claude Opus 5.5 | 51 | 3 | 4 / 20 |
| 14 | Claude Opus 5 | 49 | 3 | 5 / 25 |
| 20 | Qwen 3.8 Flash | 41 | 0 | 0.15 / 0.47 |

Three things stood out.

1. **The best model is very good and expensive.** GPT-6 Astra passed every check in both conditions, and every one of its house-rule drafts could be sent as is. A full repeat run passed every check again. GPT-5.6 Luna gets close for about forty times less per output token.
2. **Style rules fix the surface, not the substance.** Telling a model what slop sounds like removed every em dash and every editorial finding for almost every model. It did not stop the invented commitments. Across the Anthropic models, 28 of 29 failures were a claim the source never made: "the team is executing well", "confirm by Friday", "ready to launch immediately", "no legal blockers".
3. **Same price, very different output.** Claude Fable 5.1 costs what Astra costs and invented a prior discussion, a Friday deadline and a ready team on briefs where Astra invented nothing.

Five models with no zero-data-retention route on the Gateway (Muse Spark 1.3, GPT-6 Sol, GPT-6 Luna, Claude Fable 5 and 5.1) are marked disqualified in the main ranking, because that is a business requirement for me. They score well; the second ranking file shows them ranked with everyone else.

## How it works

Eight synthetic briefs, each with a small source pack of facts. Every model writes each brief once in two conditions: the plain brief, and the plain brief plus the anti-slop rules. Each draft is graded against six or seven factual checks (the fee is right, no invented start date, the right person owns the decision) plus one grounding check: every material claim traces to the source or is labeled a proposal. A draft is **content ready** if it passes every check, fits the word limit and has no residue like a `[Date]` placeholder. It is **ready without edits** if it is also free of em dashes, rhetorical negation and supported slop findings.

Every verdict quotes the exact line it rests on, and every draft is saved with its request. Open a draft, open its grade, check the quote. The long version, including the frozen protocol, the spending ledger and the retry rules, is in [docs/METHOD.md](docs/METHOD.md). The running record of every rubric decision and correction is in [IMPROVEMENTS.md](IMPROVEMENTS.md).

## Why I stopped here

I got what I needed for my own decisions, and the next steps are not a one-person job. To be a benchmark the labs would respond to, this needs:

- many more briefs, including long ones and ones that need outside knowledge
- blind grading by people who do not work for a model vendor, with published agreement between graders
- several generations per brief, so that a one-check gap means something
- a rubric that is not one person's taste

If you have the time and the standing to build that, take whatever is useful here. The code is MIT. The rubric is CC BY-SA 4.0. Open an issue or fork it; I will answer questions.

## Reproduce it

Everything in the tables reads saved files and makes no API calls:

```sh
npm ci
npm test
python3 scripts/ranking.py reviews/assistant-v44 runs/pilot-v23
python3 reviews/assistant-v44/build.py
```

Collecting new drafts needs a Vercel AI Gateway key in `AI_GATEWAY_API_KEY`:

```sh
npm run bench -- collect openai/gpt-6-astra
zsh scripts/paced-collect.sh anthropic/claude-opus-5.5
```

Reasoning effort is `low` for every model. Runs are frozen by hash; a changed brief or runner gets a new run directory rather than mixing results. Spending is capped by a ledger in `runs/budget.json`.

## Read this before quoting a number

- Each model wrote each brief once per condition. Two full repeats (Astra, Luna) kept the check scores but moved the ready counts by one or two drafts. A gap of one or two checks is within that variation.
- The grader is an AI assistant that could see the model names. Every verdict is anchored to a quote, so it can be audited. It has not been audited by an independent human.
- I wrote the briefs, the rubric and the house rules. The house condition measures compliance with my rules.
- The briefs are short and synthetic. This tests source fidelity in business documents, not long-form writing.
- Prices are Gateway list rates on the day of the run. GPT-6 Sol and Luna were billed nothing during launch pricing.

## Attribution

The anti-slop rubric is copied from [mattlgroff/zero-defect](https://github.com/mattlgroff/zero-defect) under CC BY-SA 4.0; see `sources/`. Generation goes through the [Vercel AI Gateway](https://vercel.com/ai-gateway) with the AI SDK. [SlopCodeBench](https://arxiv.org/abs/2603.24755) was the inspiration for grading quality separately from apparent task completion.
