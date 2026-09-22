# Readout criterion audit

This is an audit of benchmark design, not a replacement leaderboard. The live brief, rubric, outputs and official grades remain unchanged. No model calls were made.

## Prompt and criterion

Writer brief: Write an executive readout recommending whether to scale the pilot now. State what the results support and the next decision.

Critical C01: Handling time reduction is reported as 3 minutes or 20%, not 25% or percentage points.

The brief asks for a scaling recommendation, supporting results and a next decision. It does not directly request the derived handling-time reduction. The rubric makes that derivation a mandatory content gate. That can measure analytical completeness, but an omission must not be described as incorrect arithmetic or inability to calculate.

The supplied original rubric describes numbers integrity through arithmetic, units, baselines and forecast-versus-actual distinctions. It does not mandate this particular derived figure. C01 is a task-specific benchmark design choice.

## Effect on current uncapped comparisons

All six primary readouts from Muse, Gemini Flash and Luna give the correct endpoints and pass their other content checks. Each has C01 as its only content blocker. The following sensitivity view removes only that reviewed omission from the gate; it leaves every other finding and style decision unchanged. It is not an adopted score.

| Model | Condition | Official content ready | Hypothetical content ready | Official ready without edits | Hypothetical ready without edits |
|---|---|---:|---:|---:|---:|
| Muse | default | 7/8 | 8/8 | 4/8 | 5/8 |
| Muse | house | 7/8 | 8/8 | 5/8 | 6/8 |
| Gemini Flash | default | 5/8 | 6/8 | 0/8 | 1/8 |
| Gemini Flash | house | 4/8 | 5/8 | 3/8 | 4/8 |
| Luna | default | 5/8 | 6/8 | 2/8 | 3/8 |
| Luna | house | 6/8 | 7/8 | 4/8 | 4/8 |

The repeatability study shows this gate is sample-sensitive: Muse explicitly gave the reduction on one of three attempts and Luna on two of three. All those readouts retained the correct no-scale decision under the other frozen checks. That is a variation in completeness, not evidence of variable subtraction ability.

## Prospective repair

A proposed task-v3 file adds one sentence to the readout brief:

> Quantify the change in mean handling time in minutes or percent, and distinguish that observation from a causal claim.

The proposed file preserves every fact, check, severity, word limit and other brief. It is inactive. Validate it on fresh samples before adopting it, keep its results separate, and retain historical grades. If the intended construct is spontaneous inclusion of useful calculations, retain the natural brief and report this omission as its own completeness measure instead of presenting it as wrong arithmetic.

Readiness also includes editorial preferences. A draft blocked only on this omission can still be substantively useful; a content pass does not certify polished writing or production reliability.

## Audited evidence

- **Muse, default:** [Baseline: 200 tickets, 15 minutes mean handling time.
Pilot: 100 tickets, 12 minutes mean handling time.](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--default.md:6). Correct endpoints; no explicit derived reduction.
- **Muse, house:** [Handling time averaged 12 minutes in the pilot on 100 tickets, compared with 15 minutes at baseline on 200 tickets.](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--house.md:5). Correct endpoints; no explicit derived reduction.
- **Gemini Flash, default:** [mean handling time decreased from 15 minutes (across 200 baseline tickets) to 12 minutes (across 100 pilot tickets)](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-results-memo--default.md:10). Correct endpoints; no explicit derived reduction.
- **Gemini Flash, house:** [Mean handling time decreased from 15 minutes at baseline to 12 minutes in the pilot.](../../runs/pilot-v18/google--gemini-3.8-flash--pilot-results-memo--house.md:10). Correct endpoints; no explicit derived reduction.
- **Luna, default:** [Mean handling time fell from **15 minutes across 200 baseline tickets** to **12 minutes across 100 pilot tickets**.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--default.md:9). Correct endpoints; no explicit derived reduction.
- **Luna, house:** [The pilot reduced mean handling time from 15 minutes at baseline to 12 minutes across 100 tickets.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--house.md:3). Correct endpoints; no explicit derived reduction.

[Inactive proposed task set](../../data/proposed-tasks-v3.json), [machine-readable sensitivity](sensitivity.json), [unchanged official-file hashes](integrity.json), [repeatability study](../repeatability-v1/REPORT.md).
