# Targeted repeatability diagnostic

Targeted repeatability diagnostic on two previously inspected briefs. Not a random or representative reliability sample.

Two new house-style calls per model and brief, plus the existing uncapped sample. Prompts, source facts, reasoning settings and routing policy match. All 12 generation IDs are distinct; the eight new calls imported no saved outputs. Grades are unblinded assistant decisions under the frozen criteria.

| Model | Brief | Content checks passed, attempts 1 / 2 / 3 | Ready without edits, attempts 1 / 2 / 3 |
|---|---|---|---|
| Muse | pilot-results-memo | 6 / 7 / 6 out of 7 | no / yes / no |
| Muse | handoff-slides | 7 / 7 / 7 out of 7 | yes / yes / yes |
| Luna | pilot-results-memo | 6 / 7 / 7 out of 7 | no / yes / yes |
| Luna | handoff-slides | 7 / 7 / 7 out of 7 | no / no / no |

Both models omitted the required reduction calculation on attempt 1. Muse included it on attempt 2 and omitted it again on attempt 3; Luna included it on attempts 2 and 3. All handoff content checks passed on all attempts. Luna handoff repetition remained an editorial defect on every attempt.

The eight new calls cost $0.03742557. Baseline charges are excluded from that amount. Results are not selected by best score or merged into the primary leaderboard. Three attempts on two selected briefs do not estimate general reliability or prove one model better. The calculation criterion measures whether the reduction is explicitly written, not whether a model can subtract.

## Evidence by attempt

### Muse / pilot-results-memo / attempt 1

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--house.md): 6/7 content checks; 87/300 words.

- **C01 fail:** [Handling time averaged 12 minutes in the pilot on 100 tickets, compared with 15 minutes at baseline on 200 tickets.](../../runs/pilot-v18/meta--muse-spark-1.3--pilot-results-memo--house.md:5). Reports endpoints but omits the required explicit 3-minute or 20% reduction.

### Muse / pilot-results-memo / attempt 2

[Draft](../../runs/pilot-v19/meta--muse-spark-1.3--pilot-results-memo--house--sample-2.md): 7/7 content checks; 92/300 words.

No supported content or editorial finding in this review.

### Muse / pilot-results-memo / attempt 3

[Draft](../../runs/pilot-v19/meta--muse-spark-1.3--pilot-results-memo--house--sample-3.md): 6/7 content checks; 107/300 words.

- **C01 fail:** [Mean handling time was 15 minutes across 200 baseline tickets and 12 minutes across 100 pilot tickets.](../../runs/pilot-v19/meta--muse-spark-1.3--pilot-results-memo--house--sample-3.md:7). Reports endpoints but omits the required explicit 3-minute or 20% reduction.

### Muse / handoff-slides / attempt 1

[Draft](../../runs/pilot-v18/meta--muse-spark-1.3--handoff-slides--house.md): 7/7 content checks; 134/350 words.

No supported content or editorial finding in this review.

### Muse / handoff-slides / attempt 2

[Draft](../../runs/pilot-v19/meta--muse-spark-1.3--handoff-slides--house--sample-2.md): 7/7 content checks; 124/350 words.

No supported content or editorial finding in this review.

### Muse / handoff-slides / attempt 3

[Draft](../../runs/pilot-v19/meta--muse-spark-1.3--handoff-slides--house--sample-3.md): 7/7 content checks; 102/350 words.

No supported content or editorial finding in this review.

### Luna / pilot-results-memo / attempt 1

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--house.md): 6/7 content checks; 151/300 words.

- **C01 fail:** [The pilot reduced mean handling time from 15 minutes at baseline to 12 minutes across 100 tickets.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--house.md:3). Reports endpoints but omits the required explicit 3-minute or 20% reduction.
- **Style 10:** [The pilot provides an efficiency signal, but the quality result is below threshold and the evidence is not causal.](../../runs/pilot-v18/openai--gpt-5.6-luna--pilot-results-memo--house.md:9). Repeats the handling-time caveat and failed quality threshold already explained in the two preceding paragraphs.

### Luna / pilot-results-memo / attempt 2

[Draft](../../runs/pilot-v19/openai--gpt-5.6-luna--pilot-results-memo--house--sample-2.md): 7/7 content checks; 149/300 words.

No supported content or editorial finding in this review.

### Luna / pilot-results-memo / attempt 3

[Draft](../../runs/pilot-v19/openai--gpt-5.6-luna--pilot-results-memo--house--sample-3.md): 7/7 content checks; 177/300 words.

No supported content or editorial finding in this review.

### Luna / handoff-slides / attempt 1

[Draft](../../runs/pilot-v18/openai--gpt-5.6-luna--handoff-slides--house.md): 7/7 content checks; 167/350 words.

- **Style 10:** [- **Now:** Pat assigns the rehearsal responsibility.
- **Next:** The assigned owner completes a successful rollback rehearsal.](../../runs/pilot-v18/openai--gpt-5.6-luna--handoff-slides--house.md:24). Repeats the assignment and execution steps from the preceding slide without adding an action or condition.

### Luna / handoff-slides / attempt 2

[Draft](../../runs/pilot-v19/openai--gpt-5.6-luna--handoff-slides--house--sample-2.md): 7/7 content checks; 184/350 words.

- **Style 10:** [The rehearsal therefore has no assigned organizer.](../../runs/pilot-v19/openai--gpt-5.6-luna--handoff-slides--house--sample-2.md:15). Repeats the preceding bullet that no role has accepted responsibility for organizing the rehearsal.

### Luna / handoff-slides / attempt 3

[Draft](../../runs/pilot-v19/openai--gpt-5.6-luna--handoff-slides--house--sample-3.md): 7/7 content checks; 215/350 words.

- **Style 10:** [Until acceptance, Lee retains ownership of defect fixes.](../../runs/pilot-v19/openai--gpt-5.6-luna--handoff-slides--house--sample-3.md:27). Repeats the same ownership rule already stated on the preceding slide.
