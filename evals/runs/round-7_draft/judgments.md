# Blind Judgments — Round 7, draft (2026-10-04)

This round tests one change: a guard added to the "Use the user's details" section of `SKILL.md`, after round 6 found a confident but unsupported A/B test estimate.

> Only work out a number from facts you have. If a figure you derive (a duration, a sample size, a cost, a count) depends on a fact the user did not give, either name that assumption next to the figure, or do not calculate it and say what fact would let you. Never present a derived figure as known.

Method is the same as rounds 4 and 6: the same 11 problems (inputs in `../round-4_draft/inputs.json`), fresh agents that saw only `SKILL.md` and `references/`, one blind judge per problem against the same baseline files used since round 2, the same A/B positions, and seven criteria scored 1–5.

This round adds a **calculation audit**: one agent classified every derived number in the 22 Skill outputs from rounds 6 and 7, shuffled and unlabeled. See `calc-audit/audit.md`.

## Calculation audit (the guard's target)

| Round | Supported | Assumed | Unsupported | Wrong |
|---|---|---|---|---|
| 6 (no guard) | 10 | 5 | 9 | 0 |
| 7 (with guard) | 10 | 6 | 3 | 0 |

Unsupported figures fell from 9 to 3. Two of the remaining three are effort estimates such as "it costs an hour." The third is "about six hours a day," which assumes an unstated 8-hour day. The round 6 onboarding A/B estimate now reads "about 4 weeks… assuming about 100 users per version per week," so a reader can check its premise.

## Totals (out of 35)

| Input | Round 6 Skill | Round 7 Skill | Baseline (this round) | Winner |
|---|---|---|---|---|
| Onboarding drop-off | 29 | 28 | 29 | Baseline |
| Flat revenue | 28 | 31 | 29 | Skill |
| Career decision | 26 | 25 | 27 | Baseline |
| Supplier bankruptcy | 31 | 28 | 30 | Baseline |
| Library teens | 32 | 32 | 28 | Skill |
| Nurse turnover | 30 | 29 | 30 | Baseline |
| App cold start | 28 | 30 | 27 | Skill |
| Receptionist hire | 31 | 31 | 32 | Baseline |
| Nonprofit board | 30 | 29 | 30 | Baseline |
| Lapsed gym members | 29 | 31 | 31 | Tie |
| Async standup | 31 | 30 | 31 | Baseline |

Result: the Skill won 3, tied 1, and lost 7. Mean total: Skill 29.5, baseline 29.5, paired gap 0.0 (round 6: +0.8; round 4: +1.6).

## By criterion (mean of 11)

| Criterion | Round 4 Skill | Round 6 Skill | Round 7 Skill | Baseline (this round) |
|---|---|---|---|---|
| Diagnosis | 4.27 | 4.00 | 4.09 | 4.55 |
| Option diversity | 4.09 | 4.09 | 4.09 | 4.09 |
| Actionability | 4.91 | 4.82 | 4.64 | 4.36 |
| Fit | 4.09 | 4.09 | 4.18 | 4.73 |
| Honesty | 4.55 | 4.55 | 4.73 | 3.64 |
| Decision support | 4.45 | 4.64 | 4.27 | 4.27 |
| Efficiency | 3.45 | 3.36 | 3.45 | 3.82 |

## What this round found

- **The guard did what it was for.** Unsupported derived numbers fell from 9 to 3, with no arithmetic errors in either round. Honesty reached 4.73, its highest so far.
- **The overall result is level, not a win.** The Skill's mean total is unchanged from round 6 (29.5). The gap closed to 0.0 because the same baseline files scored 0.8 higher on average this time, and five of the seven losses were by one point (the other two by two). The same baseline files moved 1.64 points per pair between rounds 6 and 7, the noisiest round so far.
- **Fit moved a little:** 4.18, up from 4.09, still behind plain Claude's 4.73.
- **Rule checks:** 10 of 11 passed. The receptionist run's Summary had four sentences. Lens rotation: 10 of 11 eligible lenses were used as a primary lens (OODA was not).
- **Judges kept making the same points:** lens labels and the closing menu cost reading time. The baseline catches more field-specific risks, such as tracking errors in onboarding and health insurance in the career decision.

## How much to trust this

- One judge per pair, every agent from the same model family, and the auditor is a single agent.
- Round-to-round judge noise (1.45–1.64 points per pair) is larger than the overall changes in rounds 6 and 7.
