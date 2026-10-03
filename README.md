# problem-lens

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude Skill](https://img.shields.io/badge/Claude-Skill-purple)

A Claude Skill that analyzes any problem through twelve lenses and returns five diverse solutions plus an Occam's Razor anchor.

## Why

Most problem-solving prompts give you one angle. This one gives you twelve, then filters to the five that differ most. It also teaches the user which lens they missed.

## What It Does

- Runs your problem through twelve lenses.
- Returns five diverse solutions plus an Occam's Razor anchor.
- Ranks by Coverage, Impact vs. Effort, Confidence vs. Reversibility, or another framework you pick.
- Ends with a decision prompt so you choose the next move.
- Teaches problem-solving judgment along the way.

## Demo

Comming Soon

## Install

### Claude Projects

1. Clone this repo.
2. Copy `problem-lens/` into `.claude/skills/` in your project.
3. Restart Claude.
4. Ask: "Analyze this problem: ..."

### Claude Code (personal)

1. Clone this repo.
2. Copy `problem-lens/` into `~/.claude/skills/`.
3. Restart Claude Code.
4. Ask: "Analyze this problem: ..."

### Claude Code (project)

1. Clone this repo.
2. Copy `problem-lens/` into `.claude/skills/` in your project repo.
3. Restart Claude Code.
4. Ask: "Analyze this problem: ..."

## Try First

Analyze this problem: our onboarding drop-off is 60% at step 3.

Background: B2B SaaS, 200 signups per week, no user interviews yet.


## Lenses

CPS, Divergent Thinking, Solution Space Exploration, TRIZ/TIPS, Root Cause Analysis, Cynefin, Six Thinking Hats, First Principles, Occam's Razor, Design Thinking, PDCA, OODA.

## Ranking Frameworks

Coverage (default), Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

## Output

- 3-sentence summary
- 6-row table (5 solutions + anchor)
- Ranking line
- Multi-select decision prompt

## Examples

See `examples/` for three worked problems.

## When Not To Use

- You want a single answer, not options.
- The problem is trivial.
- You need code, not analysis.
- The decision is already made.

## Contributing

See `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
