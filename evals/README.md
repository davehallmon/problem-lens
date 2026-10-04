# Evaluations

Recorded live runs of the Skill, a rule checker, and a no-Skill baseline comparison. Nothing in this folder is part of the installed Skill.

## Run: 2026-10-03

- **Skill version:** `main` at commit `2d3e21a`.
- **Model:** Claude Opus 5.5, run through fresh agents. Each agent saw only `SKILL.md` and `references/`. None saw the examples.
- **Inputs:** the three example problems (onboarding drop-off, flat revenue, career decision).
- **Skill runs:** 3 per input, 9 in total.
- **Baseline:** 1 run per input, using the same model and the same user message, with no Skill.
- **Judging:** one blind judge per input compared Skill run 1 against the baseline, with A/B order randomized.

### Test conditions

- The user was not available for follow-up. When the Skill asked Turn 1 questions, the harness replied "No more information. Go ahead."
- `AskUserQuestion` was not available, so these runs exercised the numbered-list fallback.

### Results

**Rule compliance:** 8 of 9 runs passed every structural rule. One run had a 5-sentence summary; the limit is 3. See [`runs/2026-10-03/check-output.txt`](runs/2026-10-03/check-output.txt).

| Behavior | Count |
|---|---|
| Five distinct primary families | 9 / 9 |
| `When To Use This Lens` matches the lens | 9 / 9 |
| Numbered fallback used | 9 / 9 |
| Asked Turn 1 questions before answering | 9 / 9 |
| Anchor marked `Matches row N` (adds no new option) | 5 / 9 |
| Root Cause Analysis as row 1 | 9 / 9 |
| Distinct lenses used as primary (of 12) | 6 |

Primary lens counts across the 9 runs (45 rows):
- Root Cause Analysis 9
- First Principles 9
- TRIZ / TIPS 9
- Six Thinking Hats 9
- PDCA 5
- Design Thinking 4

These six lenses were never primary: CPS, Divergent Thinking, Solution Space Exploration, Cynefin, OODA, Occam's Razor. Occam's Razor is reserved for the anchor by design.

**Skill vs. baseline:** the baseline won all three blind judgments, 32–23, 32–25, and 29–27. The Skill tied or beat the baseline on option diversity, actionability, and honesty, and lost on decision support every time. See [`runs/2026-10-03/judgments.md`](runs/2026-10-03/judgments.md).

### Limits of this run

- Small sample: three inputs, one judged pair per input, one judge each.
- Generator, judges, and baseline are all the same model family.
- The baseline had no length limit and ran about 1.7 times longer than the Skill output.
- The judges could tell the formats apart, so the "blind" applies to labels only, not to style.
- These runs do not test whether the Skill triggers on claude.ai or how `AskUserQuestion` renders there.

## Reproduce

Check any output file against the table rules:

```
python3 evals/check_rules.py evals/runs/2026-10-03/*-skill-*.md
python3 evals/check_rules.py problem-lens/examples/*.md
```

The checker tests structure only. It cannot tell you whether the solutions are good. The baseline comparison is what measures that.
