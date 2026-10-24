# BusinessSlopBench

A small benchmark for the writing most of us actually ask models for at work: the client email, the vendor memo, the pilot readout, the proposal, the change order, the four-slide deck. It measures one thing above all: does the draft say only what the source facts support, or does it invent a deadline, a prior conversation, a readiness claim or an owner that was never there.

I built it, tested 34 models across versioned briefs, and I am publishing it as is because I am not going to take it further myself. I am asking someone to.

**October 24: [Kimi K3.1 Pro](reviews/assistant-v53/REPORT.md)** completed the first v3 panel: 54/54 checks and 8/8 content-ready drafts in both conditions, but only 2/8 ready without edits in each. All sixteen calls cost $0.1859896. It handles the explicit signing roles correctly; repetition remains its main writing defect. The report compares the seven unchanged briefs with Astra, Muse, Sol and Kimi K3. Full v3 totals are separate from the historical v2 ranking below.

In the historical v2 panel, **Muse Wonder 1.0**, is close to Astra with the house rules: 54/54 content checks and 7/8 drafts ready without edits. Astra's original house run was 8/8; both full repeats were 6/8. Muse has one attempt per brief. [Comparison, prices and evidence](reviews/assistant-v52/MUSE-COMPARISON.md).

For another agent taking over: start with [HANDOFF.md](HANDOFF.md).

## October 13 grading correction

The vendor brief did not identify who could sign. Some models lost credit for implying a signatory while similar Astra wording passed. That inference is now retired for all models in the historical v2 panel. Seventeen verdicts change; other factual checks and style findings remain. This is a scoring correction, not new writing or proof that any guessed authority was correct. [Full correction](reviews/assistant-v52/REPORT.md).

Future runs use `data/tasks-v3.json`: Priya coordinates procurement, Alex alone signs, and CFO approval must come first. Kimi K3.1 Pro is the first model tested on that replacement. Keep future v3 results separate from this corrected v2 panel.

## What I found

[All 33 models with prices](reviews/assistant-v52/RANKING.md). Retention policy no longer affects performance ranking. [Every current grade](reviews/assistant-v52/grades.json).

Selected plain-brief results:

| Rank | Model | Checks (of 54) | Content ready | Ready without edits | Input / output $ per M |
|---:|---|---:|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 8/8 | 4/8 | 10.00 / 50.00 |
| 5 | Muse Wonder 1.0 | 53 | 7/8 | 3/8 | 4.00 / 20.00 |
| 6 | GPT-6.1 Sol | 53 | 7/8 | 2/8 | 2.00 / 10.00 |
| 7 | Claude Opus 5.5 | 53 | 4/8 | 2/8 | 4.00 / 20.00 |
| 14 | Claude Sonnet 5.5 | 51 | 3/8 | 2/8 | 2.00 / 10.00 |
| 15 | Gemini 4 Argon | 51 | 5/8 | 1/8 | 2.00 / 10.00 |
| 17 | Gemini 3.8 Flash | 51 | 5/8 | 0/8 | 0.75 / 3.75 |
| 19 | Claude Fable 5.1 | 51 | 4/8 | 0/8 | 10.00 / 50.00 |
| 20 | Claude Haiku 5.5 | 50 | 4/8 | 2/8 | 0.10 / 0.50 |
| 33 | Nemotron 3.5 Lightning Free | 45 | 1/8 | 1/8 | 0.00 / 0.00 |

Selected house-rule results:

| Rank | Model | Checks (of 54) | Content ready | Ready without edits | Input / output $ per M |
|---:|---|---:|---:|---:|---:|
| 1 | GPT-6 Astra | 54 | 8/8 | 8/8 | 10.00 / 50.00 |
| 2 | Muse Wonder 1.0 | 54 | 8/8 | 7/8 | 4.00 / 20.00 |
| 3 | GPT-6.1 Sol | 54 | 7/8 | 4/8 | 2.00 / 10.00 |
| 12 | Claude Opus 5.5 | 52 | 3/8 | 3/8 | 4.00 / 20.00 |
| 14 | Gemini 4 Argon | 51 | 5/8 | 4/8 | 2.00 / 10.00 |
| 15 | Gemini 3.8 Flash | 51 | 5/8 | 3/8 | 0.75 / 3.75 |
| 18 | Claude Fable 5.1 | 51 | 3/8 | 3/8 | 10.00 / 50.00 |
| 20 | Claude Sonnet 5.5 | 51 | 4/8 | 2/8 | 2.00 / 10.00 |
| 27 | Claude Haiku 5.5 | 49 | 2/8 | 2/8 | 0.10 / 0.50 |
| 31 | Nemotron 3.5 Lightning Free | 46 | 4/8 | 2/8 | 0.00 / 0.00 |

Muse's house run cost $0.206844 versus Astra's $0.358140. Its remaining edit is a repeated summary bullet. With plain prompts, Muse still invented pilot approval, so the house-rule result should not be read as an unqualified reliability claim. These are unblinded assistant judgments on eight short briefs.

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
python3 scripts/ranking.py reviews/assistant-v52 runs/pilot-v32
python3 reviews/assistant-v52/build.py
```

New collections use v3 tasks and do not extend the v2 leaderboard. Collecting new drafts needs a Vercel AI Gateway key in `AI_GATEWAY_API_KEY`:

```sh
npm run bench -- collect openai/gpt-6-astra
zsh scripts/paced-collect.sh anthropic/claude-opus-5.5
```

Reasoning effort is `low` except DeepSeek (`none`) and Mistral Large 4 (provider-default; configuration was ignored). Runs are frozen by hash; a changed brief or runner gets a new run directory rather than mixing results. Spending is capped by a ledger in `runs/budget.json`.

## Read this before quoting a number

- Each model wrote each brief once per condition. Two full repeats (Astra, Luna) kept the check scores but moved the ready counts by one or two drafts. A gap of one or two checks is within that variation.
- The grader is an AI assistant that could see the model names. Every verdict is anchored to a quote, so it can be audited. It has not been audited by an independent human.
- I wrote the briefs, the rubric and the house rules. The house condition measures compliance with my rules.
- The briefs are short and synthetic. This tests source fidelity in business documents, not long-form writing.
- Prices are Gateway list rates on the day of the run. GPT-6 Sol and Luna were billed nothing during launch pricing.

## Attribution

The anti-slop rubric is copied from [mattlgroff/zero-defect](https://github.com/mattlgroff/zero-defect) under CC BY-SA 4.0; see `sources/`. Generation goes through the [Vercel AI Gateway](https://vercel.com/ai-gateway) with the AI SDK. [SlopCodeBench](https://arxiv.org/abs/2603.24755) was the inspiration for grading quality separately from apparent task completion.
