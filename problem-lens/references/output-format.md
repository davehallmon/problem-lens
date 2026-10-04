# Output Format

See `SKILL.md` for the full rules. This file is a quick reference.

## Order

1. **Summary** — three sentences or fewer. Assumptions start with "Assuming".
2. **What's Likely Going On** — two or three competing explanations, each with the check that would confirm or rule it out.
3. **Recommendation** — `Do this first: Row 1 — …, because …` and `Switch to Row M if …`.
4. **Table** — six rows in the order to act. One row is the Occam's Razor anchor, marked `N · Anchor`.
5. **Ranking line** — the framework in use and the alternatives.
6. **Questions That Would Change the Pick** — up to three. Skip if none.
7. **Decision prompt** — four options.

## Table

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 · Anchor | | Occam's Razor | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

The anchor can sit at any position. `Why This Lens` is required on every row and is at most one sentence.

## Decision Prompt

Use `AskUserQuestion`. Multi-select. Options:

- Expand a solution
- Add more solutions
- Re-rank
- Learn more

If `AskUserQuestion` is not available, show the four options as a numbered list. Ask the user to reply with one or more numbers.

## Rules

- Short words.
- Active voice.
- No clichés.
- No filler.
- Teaching points are one sentence at most. More detail and links come only when the user picks Learn more, and links come only from `references/learn-more.md`.
- Never more than six rows.
