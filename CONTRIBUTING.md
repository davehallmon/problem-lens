# Contributing

Thanks for your interest. This project welcomes contributions.

## Ways To Contribute

- Report a bug.
- Request a new lens.
- Request a new ranking framework.
- Improve an example.
- Fix a typo.

## How To Contribute

1. Open an issue first. Describe the change and why it helps.
2. Fork the repo.
3. Make the change on a branch.
4. Open a pull request. Link the issue.
5. Wait for review.

## Style

- Use active voice.
- Use short words.
- Cut filler.
- No clichés.
- Keep `problem-lens/SKILL.md` under 500 lines.
- Put detail in `problem-lens/references/`.

## Adding a Lens

1. Add the lens to `problem-lens/references/lenses.md` under one of the five families.
2. Include a one-line "Use when" note that does not overlap another lens in the same family.
3. Add an entry to `problem-lens/references/learn-more.md` with a checked link, or `Link: none` and the reason.
4. Update the family table in `problem-lens/references/lenses.md` and `README.md`, and the lens count if needed.

## Adding a Ranking Framework

1. Add the framework to `problem-lens/references/ranking-frameworks.md`.
2. Include a one-line "Best when" note.
3. Add an entry to `problem-lens/references/learn-more.md`.
4. Update the framework list in `README.md` and `problem-lens/SKILL.md`.

## Testing

Run `python3 evals/check_rules.py problem-lens/examples/*.md` before opening a pull request. Changes to Skill behavior should come with a new round in `evals/`.

## Code of Conduct

See `CODE_OF_CONDUCT.md`.