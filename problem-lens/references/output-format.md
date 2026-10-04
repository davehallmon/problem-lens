# Output Format

See `SKILL.md` for the full rules. This file is a quick reference.

## Order

1. **Summary** — three sentences or fewer. Assumptions start with "Assuming".
2. **Recommendation** — `Do this first: Row N — …, because …` and `Switch to Row M if …`.
3. **Table** — five solution rows plus the Occam's Razor anchor.
4. **Ranking line** — the framework in use and the alternatives.
5. **Questions That Would Change the Pick** — up to three. Skip if none.
6. **Decision prompt** — four options.

## Table

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| Anchor | | Occam's Razor | | | |

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
- No links unless the user picks Learn more, and then only links from `references/learn-more.md`.
- Never more than six rows.
