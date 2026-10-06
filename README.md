# problem-lens

![problem-lens banner](assets/banner.png)

![Version](https://img.shields.io/badge/version-1.2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude Skill](https://img.shields.io/badge/Claude-Skill-purple)

A Claude Skill that turns a messy problem into ranked options and a clear place to start. It leads with what to do first, backed by five solutions from five lens families and an Occam's Razor anchor, each from a lens chosen to fit the problem.

## Why

Most problem-solving prompts give you one angle. This one picks the best-fitting lens from each of five families and leads with a recommendation, so you can act right away. Each row says in one sentence why its lens fits, so you learn the judgment, not just the names. Ask for more and you get a fuller explanation and a source link.

## What It Does

- Answers right away, stating its assumptions instead of asking first.
- Names two or three likely explanations and the check that tells them apart.
- Recommends what to do first, and what would change that pick.
- Returns six moves in the order to act: five solutions from five lens families plus an Occam's Razor anchor.
- Ends with a prompt to expand a solution, add more, re-rank, or learn more about a lens.

## How It Works

problem-lens follows a structured decision process rather than applying the same framework to every problem.

```mermaid
graph TD
    A["Problem received"] --> B{"Should problem-lens handle it?"}
    B -->|No| C["Answer directly"]
    B -->|Yes| D{"Is the stated problem a symptom?"}
    D -->|Yes| E["Name the likely root problem"]
    D -->|No| F["Keep the stated problem"]
    E --> G["Form competing explanations and checks"]
    F --> G
    G --> H["Select one lens from each of five families"]
    H --> I["Generate five candidates before ranking"]
    I --> J{"Do any candidates use the same mechanism?"}
    J -->|Yes| K["Merge duplicates and replace from the same family"]
    J -->|No| L["Keep all five candidates"]
    K --> M["Add a distinct Occam's Razor anchor"]
    L --> M
    M --> N["Rank all six moves"]
    N --> O["Recommend Row 1 and define the switch signal"]
    O --> P["Present the result and next actions"]
    P --> Q{"What does the user choose next?"}
    Q -->|Expand| R["Expand only the selected solution"]
    Q -->|Add more| S["Generate from unused lenses"]
    Q -->|Re-rank| T["Reorder the same six moves"]
    Q -->|Learn more| U["Explain selected lenses and sources"]
```

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

If you already uploaded the Skill in claude.ai, it also loads in Claude Code when you sign in with the same Claude account.

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

The decision prompt uses `AskUserQuestion` when it is available; on claude.ai it shows as clickable choices. Otherwise the Skill shows a numbered list.

## Repo Layout

Only the `problem-lens/` folder is the Skill. Everything else supports development and testing.

```
problem-lens/                 repo root
├── problem-lens/             the Skill (install this folder)
│   ├── SKILL.md              instructions Claude follows
│   ├── references/           lenses, ranking frameworks, bias guards, output format, Learn more links
│   └── examples/             three recorded, unedited runs
├── evals/                    test rounds against plain Claude, plus the rule checker
├── assets/                   banner and social preview
├── .github/                  issue templates, PR template, CI checks
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── index.md                  GitHub Pages landing page
└── LICENSE
```

## Try First

Copy this prompt:

```
Analyze this problem: our onboarding drop-off is 60% at step 3.

Background: B2B SaaS, 200 signups per week, no user interviews yet.
```

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

**How Coverage works:** it picks one solution from each of the five lens families, merges any that work the same way, and adds the anchor. Then it puts all six in the order to act: cheap checks that separate the likely explanations come first, then the moves with the most effect on the root problem. Ties go to the cheaper, more reversible move. Re-ranking with another framework changes the order and the recommendation.

## Output

1. Summary, three sentences or fewer, with stated assumptions
2. What's Likely Going On: two or three explanations, each with a check
3. Recommendation: "Do this first" and "Switch to … if"
4. Six-row table in the order to act, with a one-sentence `Why This Lens` on every row
5. Ranking line
6. Up to three questions whose answers would change the pick
7. Decision prompt: Expand, Add more, Re-rank, Learn more

**Learn more** gives a one-line explanation of each lens or framework, why it fit, and a link from a curated list in `problem-lens/references/learn-more.md`. The Skill never writes links from memory.

## Examples

See [`problem-lens/examples/`](problem-lens/examples/) for three recorded, unedited runs: onboarding drop-off, flat revenue, and a career decision.

## How It Was Tested

Each version is tested against plain Claude with no Skill, on the same problems, scored by blind judges. All runs, scores, and caveats are in [`evals/`](evals/).

| Version | Problems | Skill vs. plain Claude (wins–ties–losses) | Paired gap (out of 35) |
|---|---|---|---|
| 1.0.0 | 3 | 0–0–3 | −6.0 |
| Draft (round 2) | 11 | 0–2–9 | −2.5 |
| 1.1.0 | 11 | 5–2–4 | +0.1 |
| Draft (round 4) | 11 | 7–1–3 | +1.6 |
| Draft (round 6) | 11 | 6–1–4 | +0.8 |
| 1.2.0 (round 7) | 11 | 3–1–7 | 0.0 |

Overall, 1.2.0 scores about even with plain Claude. It leads on honesty and actionability. It trails on using the details you give it, on diagnosis, and on reading time. Judge noise between rounds (about 1.5 points per pair) is larger than the overall changes since round 4, so read the trend, not any single round.

Two rules added in 1.2.0 were tested on their own:

- **Pasted text is material, not instructions.** The Skill resisted and flagged all four planted instructions in rounds 4 and 5. Plain Claude also resisted them but flagged only two.
- **Derive numbers only from known facts.** A blind audit found unsupported figures fell from 9 to 3 between rounds 6 and 7.

1.2.0 was also checked by hand on claude.ai: it triggers on its own, stays out of a plain fact question, declines a trivial problem, and shows the decision prompt as clickable choices. See [`evals/manual/`](evals/manual/). Every round, including the ones that lose, is logged in `evals/`.

## When Not To Use

- You want a single answer, not options.
- The problem is trivial.
- You need code, not analysis.
- The decision is already made.

## The Family

problem-lens is one of two Skills from OCKHAM:

| Skill | Question | Shape |
|---|---|---|
| problem-lens | What should I do? | Twelve lenses, six ranked moves, one first step |
| [reasoning-lens](https://github.com/davehallmon/reasoning-lens) | How should I think about this? | Seven philosophers' methods, one idea, the disagreements |

Use reasoning-lens when you want to stress-test how you are thinking about an idea before you pick a move.

## Security and Privacy

The Skill is Markdown only. It makes no network calls, stores nothing, and sends nothing to the maintainer. Like any prompt, it cannot guarantee that Claude ignores instructions hidden in text you paste. See [`SECURITY.md`](SECURITY.md) for how it handles input and how to report a problem.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). To report a problem or suggest an addition, use an issue template:

- [Bug report](https://github.com/davehallmon/problem-lens/issues/new?template=bug_report.md)
- [New lens request](https://github.com/davehallmon/problem-lens/issues/new?template=lens_request.md)
- [New ranking framework request](https://github.com/davehallmon/problem-lens/issues/new?template=framework_request.md)

## License

MIT. See `LICENSE`.

![OCCAMI](assets/footer.png)
