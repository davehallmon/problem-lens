# Evaluations

Every version of problem-lens is tested against plain Claude, with no Skill, on the same problems. Nothing in this folder is part of the installed Skill.

## Method

- **Skill runs:** fresh agents saw only `SKILL.md` and `references/`, never the examples. `AskUserQuestion` was not available, so runs use the numbered-list fallback.
- **Baseline:** the same model and the same user message, with no Skill.
- **Judging:** one blind judge per problem compared Skill run 1 with the baseline. A/B order was alternated. Seven criteria were scored 1–5, for a maximum of 35.
- **Rule checks:** `check_rules.py` tests structure only. It does not judge whether the advice is good.

## Results

| Round | Version | Problems | Skill wins–ties–losses | Mean Skill | Paired gap |
|---|---|---|---|---|---|
| 1 | 1.0.0 | 3 | 0–0–3 | 25.0 | −6.0 |
| 2 | draft | 11 | 0–2–9 | 27.3 | −2.5 |
| 3 | 1.1.0 | 11 | 5–2–4 | 29.0 | +0.1 |
| 4 | draft (pasted-text rule) | 11 | 7–1–3 | 29.8 | +1.6 |

Round 4 also ran four injection problems, where the background includes pasted text with an instruction aimed at AI tools. The Skill and plain Claude both resisted all four. The Skill told the user about the instruction in 4 of 4 runs, plain Claude in 2 of 4. In 2 of the 4 Skill runs, the warning pushed the summary past its three-sentence limit. Details are in `runs/round-4_draft/judgments.md`.

Round 3, mean score by criterion:

| Criterion | Skill 1.1.0 | Plain Claude |
|---|---|---|
| Diagnosis | 4.09 | 4.55 |
| Option diversity | 4.18 | 3.73 |
| Actionability | 4.64 | 4.18 |
| Fit to the user's details | 3.73 | 4.64 |
| Honesty | 4.55 | 3.73 |
| Decision support | 4.45 | 4.27 |
| Efficiency | 3.36 | 3.82 |

Other checks in round 3:
- **Rule compliance:** 11 of 11 runs passed `check_rules.py`.
- **Lens rotation:** 10 of 11 eligible lenses were used as a primary lens. OODA was not.
- **Trivial problems:** a trivial problem was correctly declined and answered directly.

## Caveats

- **Judge noise is real.** The same baseline files scored about 1.4 points differently between rounds 2 and 3. Treat any single comparison as noisy. The trend is clearer: the Skill improved on 10 of 11 problems from round 2 to round 3.
- **Same model family.** Generator, baseline, and judges are all the same model family, with one judge per pair.
- **Not tested here:** whether the Skill triggers on claude.ai, and how `AskUserQuestion` renders there.

## Next

Future releases will explore fixes for the weak spots: fit to the user's details, reading time, OODA never being chosen, and lens labels that judges called forced. Every round will be logged here, including rounds that lose.

Two fixes came out of round 4: say where the injection warning goes so it doesn't break the summary limit, and stop `check_rules.py` from misreading numbered section headings.

## Files

- `runs/round-1_v1.0.0/`, `runs/round-2_draft/`, `runs/round-3_v1.1.0/`, `runs/round-4_draft/`: raw outputs, baselines, `judgments.md`, and `check-output.txt`. Rounds 1 and 2 were checked with the rules of their time. Round 4 also has `inputs.json`, the exact user messages for its 15 problems.
- `check_rules.py`: run `python3 evals/check_rules.py problem-lens/examples/*.md`
