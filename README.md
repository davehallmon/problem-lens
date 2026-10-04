# problem-lens

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude Skill](https://img.shields.io/badge/Claude-Skill-purple)

A Claude Skill that analyzes a problem through twelve lenses and returns five diverse solutions plus an Occam's Razor anchor.

## Why

Most problem-solving prompts give you one angle. This one runs twelve, then keeps one solution from each of five lens families. A `When To Use This Lens` column shows when each lens fits, so you learn the judgment, not just the names.

## What It Does

- Runs your problem through twelve lenses in five families.
- Returns five diverse solutions plus an Occam's Razor anchor.
- Ranks by Coverage, Impact vs. Effort, Confidence vs. Reversibility, or another framework you pick.
- Ends with a decision prompt so you choose the next move.

## Sample Output

See [`problem-lens/examples/onboarding-drop-off.md`](problem-lens/examples/onboarding-drop-off.md) for a full run on the "Try First" problem below.

## Install

The Skill lives in the `problem-lens/` folder of this repo. Install that folder, not the whole repo.

### claude.ai

1. Clone this repo.
2. From the repo root, zip the Skill folder: `zip -r problem-lens.zip problem-lens`
3. In claude.ai, turn on code execution in Settings.
4. Go to **Customize > Skills**, click **+**, choose **Create skill**, then **Upload a skill**. Upload `problem-lens.zip`.
5. Ask: "Analyze this problem: ..."

Uploaded Skills apply to your account, not to a single Project.

### Claude Code (personal)

1. Clone this repo.
2. Copy the `problem-lens/` folder into `~/.claude/skills/`.
3. Restart Claude Code.
4. Ask: "Analyze this problem: ..."

### Claude Code (project)

1. Clone this repo.
2. Copy the `problem-lens/` folder into `.claude/skills/` in your project repo.
3. Restart Claude Code.
4. Ask: "Analyze this problem: ..."

## Requirements

- **Claude access** with Skills support:
  - claude.ai, with code execution on
  - Claude Code (CLI)
- **A problem to analyze.** The Skill needs a problem statement and background context.
- **No dependencies.** The Skill in `problem-lens/` is Markdown-only. No scripts, no packages, no API keys. The `evals/` folder holds a maintainer-only checker script that is not part of the install.

### Supported Platforms

| Platform | How to install |
|---|---|
| claude.ai | Upload `problem-lens.zip` in **Customize > Skills** |
| Claude Code (personal) | `~/.claude/skills/problem-lens/` |
| Claude Code (project) | `.claude/skills/problem-lens/` |

The decision prompt uses `AskUserQuestion` when it is available. Otherwise the Skill shows a numbered list.

## Try First

Analyze this problem: our onboarding drop-off is 60% at step 3.

Background: B2B SaaS, 200 signups per week, no user interviews yet.

## Lenses

| Family | Lenses |
|---|---|
| Generation | CPS, Divergent Thinking, Solution Space Exploration, TRIZ / TIPS |
| Diagnosis | Root Cause Analysis |
| Perspective | Cynefin, Six Thinking Hats |
| Fundamentals | First Principles, Occam's Razor (anchor only) |
| Process | Design Thinking, PDCA, OODA |

## Ranking Frameworks

Coverage (default), Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**How Coverage works:** it picks one solution from each of the five lens families, merges any that work the same way, then orders the five by expected effect on the root problem. Ties go to the cheaper, more reversible move. The other frameworks re-order those same five rows.

## Output

- 3-sentence summary
- 6-row table (5 solutions + anchor)
- Ranking line
- Multi-select decision prompt

## Examples

See [`problem-lens/examples/`](problem-lens/examples/) for three worked problems: onboarding drop-off, flat revenue, and a career decision.

## When Not To Use

- You want a single answer, not options.
- The problem is trivial.
- You need code, not analysis.
- The decision is already made.

## Contributing

See `CONTRIBUTING.md`.

## License

MIT. See `LICENSE`.
