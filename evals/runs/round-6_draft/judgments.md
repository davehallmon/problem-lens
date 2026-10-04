# Blind Judgments — Round 6, draft (2026-10-04)

This round tests one change aimed at Fit (using the user's stated details), the criterion where the Skill has trailed plain Claude in every round. The change adds "Use the user's details" to `SKILL.md`:

- Use at least one stated number or limit to rule out a check, size or drop an option, or change the order, and say which number did it.
- Keep every move doable with the people, money, time, and data the user described; if a move needs more, its `Risk` cell says what.

The idea came from an outside review (Gemini). It was narrowed to match where plain Claude actually wins on Fit: using a number to change the advice, not quoting it.

Method is the same as round 4: the same 11 problems (inputs in `../round-4_draft/inputs.json`), fresh agents that saw only `SKILL.md` and `references/`, and one blind judge per problem comparing Skill run 1 against the same baseline files used since round 2 (`../round-3_v1.1.0/*-baseline.md`), with the same A/B positions as round 4. Seven criteria scored 1–5, 35 maximum, totals summed from the criterion scores.

## Totals (out of 35)

| Input | Round 4 Skill | Round 6 Skill | Baseline (this round) | Winner |
|---|---|---|---|---|
| Onboarding drop-off | 30 | 29 | 30 | Baseline |
| Flat revenue | 31 | 28 | 29 | Baseline |
| Career decision | 28 | 26 | 27 | Baseline |
| Supplier bankruptcy | 28 | 31 | 31 | Tie |
| Library teens | 32 | 32 | 29 | Skill |
| Nurse turnover | 30 | 30 | 27 | Skill |
| App cold start | 30 | 28 | 29 | Baseline |
| Receptionist hire | 31 | 31 | 30 | Skill |
| Nonprofit board | 31 | 30 | 27 | Skill |
| Lapsed gym members | 28 | 29 | 28 | Skill |
| Async standup | 29 | 31 | 29 | Skill |

Result: the Skill won 6, tied 1, and lost 4. Mean total: Skill 29.5, baseline 28.7, paired gap +0.8 (round 4: +1.6).

## By criterion (mean of 11)

| Criterion | Round 4 Skill | Round 6 Skill | Baseline (this round) |
|---|---|---|---|
| Diagnosis | 4.27 | 4.00 | 4.45 |
| Option diversity | 4.09 | 4.09 | 4.09 |
| Actionability | 4.91 | 4.82 | 4.09 |
| **Fit** | **4.09** | **4.09** | **4.73** |
| Honesty | 4.55 | 4.55 | 3.64 |
| Decision support | 4.45 | 4.64 | 4.00 |
| Efficiency | 3.45 | 3.36 | 3.73 |

Fit by problem, round 4 to round 6: up on 2 (library, turnover), the same on 7, down on 2 (onboarding, career).

## What this round found

- **The rule did not move Fit.** The mean is 4.09 in both rounds, and the per-problem changes cancel out.
- **The model did follow the rule, sometimes well.** In nurse turnover it worked out that 28% on a typical unit is about 11 exits a year, too few to trust exit-interview themes, and said to pool 2–3 years of data. That judge named it the deciding insight and scored Fit 5.
- **Using numbers also led to wrong numbers.** In onboarding the run estimated an A/B test at "about four weeks." The judge worked it out at about 6–7 weeks, and noted the run assumed all 200 signups reach step 3, which the user never said. Fit dropped to 3.
- **Judges' Fit complaints are mostly about coverage, not numbers.** For example, the career run never used "8 years of experience," and the baseline did. A rule that pushes one number into the advice does not fix that.
- **Rule checks:** 11 of 11 passed. All 11 eligible lenses were used as a primary lens across the round, including OODA for the first time (supplier).
- **The usual pattern held.** The Skill led on honesty, actionability, and decision support, and trailed on fit, diagnosis, and efficiency (lens labels and the closing menu).

## How much to trust this

- The same baseline files scored an average of 1.45 points differently from round 4, about the size of any single pair's margin. The fall from +1.6 to +0.8 overall is within that noise.
- One judge per pair, and every agent is from the same model family.

## Bottom line

The change did not do what it was meant to do. Fit stayed where it was, and one run turned the rule into a confident but wrong calculation.

The maintainer kept the rule after this round. It stays in `SKILL.md` while later rounds watch Fit and the accuracy of any numbers the Skill works out.
