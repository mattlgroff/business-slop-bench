# BusinessSlopBench owner handoff

Updated September 29, 2026. Repository: https://github.com/mattlgroff/business-slop-bench.

## Purpose

Compare single-call business writing: factual grounding, unsupported commitments, decision usefulness, and compliance with Matthew's Zero Defect anti-slop rules. Cost matters, but cheap or stylish writing is not automatically correct. Test model preferences as hypotheses. Never adjust the rubric to make a favored model win or a disliked model lose.

## Start here

- [README](README.md): overview and selected results.
- [Current primary ranking](reviews/assistant-v47/RANKING.md): 28 models, 448 primary drafts; 22 models eligible under the recorded ZDR rule, six shown separately.
- [Writing-only ranking](reviews/assistant-v47/RANKING-ignoring-zdr.md): same writing grades with ZDR eligibility ignored.
- [Current grades and evidence](reviews/assistant-v47/REPORT.md), [decisions for Sol 6.1](reviews/assistant-v47/decisions.json), and [cumulative grades](reviews/assistant-v47/grades.json).
- [Fresh Sol 6.1 versus Astra comparison](reviews/sol61-astra-low/REPORT.md): September 29 paired low-reasoning runs. Astra sample 3 is a repeat, not a replacement for its primary result.
- [Methods](docs/METHOD.md) and [decision history](IMPROVEMENTS.md).
- [Published blog](https://www.groff.dev/blog/business-slop-bench). Its source is in the separate `mattlgroff/groffdev` repository.

## Current state

The CLI uses `pilot-v27`, protocol version `0.27.0`, AI SDK `7.0.109`, `data/tasks-v2.json`, and the frozen `sources/anti-slop-reviewer.md`. There are eight synthetic briefs, with default and house-rule conditions. All models request low reasoning except the two DeepSeek models, which request none. No harness output-token cap or generation deadline is applied. The briefs still have word limits; those are evaluation requirements, not API token caps.

| Model / attempt | Condition | Checks | Content ready | Ready without edits |
|---|---|---:|---:|---:|
| Sol 6.1 primary | Default | 53/54 | 7/8 | 2/8 |
| Sol 6.1 primary | House | 54/54 | 7/8 | 4/8 |
| Astra sample 3 | Default | 54/54 | 6/8 | 2/8 |
| Astra sample 3 | House | 54/54 | 8/8 | 6/8 |

Sol ranks second in both primary tables under the existing ordering. The primary Astra house result remains 8/8 ready without edits; both full-panel repeats returned 6/8. Do not mix attempts or select the best draft from each. Sol's sixteen drafts cost $0.094556; the fresh Astra sixteen cost $0.471230. These are Gateway-reported charges, distinct from the conservative budget ledger.

The ledger is `runs/budget.json`, with a $100 ceiling and approximately $33.6304 accounted at this handoff. Read it before new calls; failed or uncertain requests can retain full reservations. It is not an invoice. There are 56 separately tracked repeat drafts, excluded from the 448 primary drafts.

## Grading contract

- Read every full draft against its source facts, task checks, and all 29 anti-slop categories. Never infer a pass from a successful API response.
- Content checks use pass, fail, or review. Review earns no point but is not a confirmed failure. API errors and incomplete outputs are ungraded, not writing failures.
- `contentReady` requires all content checks to pass, the word limit to pass, and no drafting residue.
- `readyWithoutEdits` additionally requires zero em dashes, no empty rhetorical negative parallelism, and no supported editorial findings.
- Count punctuation mechanically. Phrase scans only nominate passages; apply the lens's contextual exceptions. Necessary factual contrasts and intentional signature fields are allowed.
- Save exact quotations, offsets, line numbers, input hashes, and output hashes. Explain borderline calls. Preserve prior decisions; publish explicit corrections in a new review version.
- Review builders materialize manually authored decisions. They do not perform semantic grading. Empty override lists assert that the reviewer actually checked every criterion; do not populate them by default before reading.
- Current grades are unblinded assistant judgments without independent human gold. Do not claim independent validation, statistical superiority, or broad document-writing reliability from this panel.
- Jev paid grading is paused and disabled in the CLI. Do not resume it merely because the historical code is present.

## Reproduce without API charges

Use the existing npm lockfile and Node 22+; a working Node 26 installation was used for the latest runs. Python 3.12+ is a safe choice for the report scripts.

```sh
npm ci
npm run check
npm test
python3 scripts/coverage.py --cohort uncapped
python3 reviews/assistant-v47/build.py
python3 reviews/sol61-astra-low/build.py
python3 scripts/ranking.py reviews/assistant-v47 runs/pilot-v27
npx tsx src/draft-audit.ts pilot-v27
```

The builders regenerate saved reports from committed judgments, verifying hashes and quotations. `draft-audit` writes an audit file and covers primary outputs in the named run only; it does not audit repeat IDs. Use the comparison builder for the fresh Astra repeats. Earlier models' primary outputs remain in earlier run directories, referenced by cumulative grades. Coverage discovers compatible runs across those directories. The last code validation passed TypeScript and all 19 tests.

## Add a model or repeat a run

1. Read the current code and protocol. Check `git status`; preserve unrelated changes. Verify the exact live Gateway ID, supported reasoning, price, and routing policy from `https://ai-gateway.vercel.sh/v1/models`.
2. For a model addition, update `data/models.json` and advance both `runName` and protocol `version` in `src/cli.ts` to unused values. Any hashed runner/model change requires a new run directory. Do not edit a frozen `protocol.json` to bypass `PROTOCOL_CHANGED`.
3. Keep tasks, house instructions and reasoning unchanged for a like-for-like comparison. A task or rubric change requires a separately labeled comparison. `data/proposed-tasks-v3.json` is inactive.
4. Supply `AI_GATEWAY_API_KEY` through the environment, or point `BUSINESS_SLOP_ENV_FILE` at a local dotenv file containing that variable. No credential is committed. On Matthew's machine, the existing credential source is `/Users/deathstar/working/elios/elios-insights/apps/api-elios/.env`. Read only the required key at runtime; never print or copy that file into the benchmark.
5. Smoke-test one brief in both conditions, inspect the saved exact model identity, input, finish reason, warnings and billing, then complete the panel. For an already registered model, the syntax is:

```sh
npm run bench -- collect openai/gpt-6.1-sol pilot-client-email
npm run bench -- collect openai/gpt-6.1-sol
```

Existing primary files are reused. These commands do not rerun completed cells. For fresh repeats, use `repeat` with an explicit task, condition and unused sample number. For example, Astra sample 4 is unused at this handoff:

```sh
npm run bench -- repeat openai/gpt-6-astra pilot-client-email house 4
```

Freeze the full intended repeat panel before calls, run every planned cell, and retain every result. Do not choose tasks after inspecting output. Check existing sample IDs across all runs before choosing a number.

6. Do not introduce output caps, generation deadlines, tools, browsing, revision loops, examples, or a multi-agent writer into this single-call comparison. A different harness belongs in a separate experimental condition.
7. Keep generation sequential because the collector owns `runs/.lock` and a shared budget. Inspect 429s before retrying. `scripts/paced-collect.sh` is a historical pacing workaround for observed Anthropic account limits, not a universal provider limit. `scripts/retry-transient.py` archives an inspected failed attempt while retaining its reservation; it never makes the retry free. Do not delete failed records or zero the ledger to force progress.
8. Use `scripts/scan-review.ts`, then perform full semantic review and save a new version's explicit decisions. Preserve prior cumulative rows exactly unless making a documented correction. Verify paired inputs before claiming comparability.
9. Rebuild reports and rankings, check evidence links and scope, commit and push the authorized work. Publishing a blog update is separate work in `groffdev`; a benchmark push does not deploy the site.

The main ranking retains the existing ZDR eligibility policy. Explicitly requested non-ZDR models have been run on synthetic briefs and appear in the writing-only table. Do not confuse retention eligibility with writing quality or silently change the policy.

## Important next work

Independent calibration is unresolved. Obtain blind human labels and measure reviewer agreement before presenting this as a validated benchmark. Add more briefs and repeat runs as separate studies with a frozen plan. The existing [rubric audit](reviews/rubric-audit-v1/REPORT.md) identifies a derived handling-time reduction requested by the rubric but not explicitly by the brief; its proposed fix is not active. Do not silently rescore history under a new brief.

For another model request, a complete deliverable is: saved calls and costs, full evidence-backed review, refreshed rankings, a concise comparison with prior results, and an explicit statement of what was and was not published.

## This Mac

Current checkout: `/Volumes/DockerSSD/worktrees/businessslopbench/pilot-20260922`. Keep new worktrees, dependencies and build output on the mounted writable external SSD. Never create a replacement mount directory or fall back to internal storage if it is unavailable. Follow the user's current AGENTS instructions. Never use an em dash in authored prose. Stop temporary task-owned processes before finishing.
