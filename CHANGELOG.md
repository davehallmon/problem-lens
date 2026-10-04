# Changelog

All notable changes to this project are documented here.
This project follows Semantic Versioning.

## Tested With

Only models and setups that were actually recorded are listed. Blank or "not recorded" means untested or unknown, not unsupported.

| Version | Model | Setup | Not yet tested |
|---|---|---|---|
| 1.1.0 | Claude Opus 5.5 | Agents given `SKILL.md` and `references/` only (recorded examples and eval round 3) | Triggering on claude.ai and the desktop app; `AskUserQuestion` rendering |
| Draft (round 2) | Not recorded | Agents, eval round 2 | Same as above |
| 1.0.0 | Not recorded | Agents, eval round 1 | Same as above |

## [Unreleased]

### Added
- README: install steps for the Claude desktop app, a note that problem-lens is not an MCP server, and a note that Skills uploaded in claude.ai also load in Claude Code under the same account. Source: [Anthropic Help Center, "Use Skills in Claude"](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
- README: "Repo Layout" tree, a copyable "Try First" prompt, a "Security and Privacy" section, and links to the three issue templates.
- SECURITY.md: "How the Skill Handles Input", "Prompt Injection", and "Privacy" sections. Each behavior listed traces to `problem-lens/SKILL.md`. The prompt-injection section states the limit plainly instead of claiming protection.
- Examples: a "Copy This Prompt" block above each Input section. The recorded outputs are unchanged.
- CHANGELOG: "Tested With" table.

### Context
- These changes respond to an outside review of the repo (rubric drafted with Gemini, review run by DeepSeek, scored 79/100). Accepted: desktop install guidance, safety documentation, repo tree, copyable prompts, compatibility table, and issue-template links.
- Changed from the review: the review suggested pasting `SKILL.md` into Project instructions and adding a `claude_desktop_config.json` snippet. Skills are a built-in feature and problem-lens is not an MCP server, so the README points to the built-in install instead.
- Already present before the review: `SECURITY.md`, `CONTRIBUTING.md`, and issue templates for bugs, lenses, and frameworks.
- Not done yet: a demo GIF. It should be a screen recording of a real run, made by the maintainer, so it isn't added here.
- No changes to `SKILL.md`, the lenses, or the ranking frameworks.

### Changed
- New banner: "Twelve lenses. Six moves. One first step." with the OCKHAM maker mark. Removed the old `assets/banner.svg`.
- Added `assets/social-preview.png` (1280×640) for the GitHub link card.
- README: added "The Family" section linking reasoning-lens.
- GitHub Pages `index.md`: banner image and current copy.
- SECURITY.md: scope now mentions the maintainer-only checker and workflows.
- Bug report template: platform reads claude.ai / Claude Code.

## [1.1.0] — 2026-10-03

### Added
- "What's Likely Going On": two or three competing explanations, each with a check that tells them apart.
- Recommendation lines: "Do this first" and "Switch to … if".
- "Questions That Would Change the Pick", asked after the answer, not before.
- Learn more option, with one checked link per lens and framework in `references/learn-more.md`.
- `evals/`: three rounds of live runs, blind comparisons with plain Claude, and a rule checker.
- GitHub Actions: check examples against the rules, and a weekly check of Learn more links.

### Changed
- Answers right away with stated assumptions instead of asking questions first.
- Lenses are chosen by fit: within each family, the lens whose trigger best matches the problem. Lens triggers were rewritten so they do not overlap.
- The table follows the order to act. Row 1 is always "Do this first", and the anchor takes its place in that order.
- `Why This Lens` replaces `When To Use This Lens`, ties the lens to this problem, and is limited to one sentence.
- The anchor must not repeat another row.
- "Learn more" replaces "Done" in the decision prompt.
- Examples are now recorded, unedited runs.
- Moved the Skill into a `problem-lens/` folder so the install steps match the repo layout.
- Added a fifth lens family, Perspective (Cynefin, Six Thinking Hats), so five-family coverage is possible.
- Reserved Occam's Razor for the anchor.
- Renamed Cynefin's "simple" domain to "clear".
- Added a numbered-list fallback when `AskUserQuestion` is unavailable.
- Removed unfilled `{problem}` and `{background}` placeholders.
- Corrected the claude.ai install steps (ZIP upload in Customize > Skills).

### Removed
- `assets/demo` placeholder file.

## [1.0.0] — 2026-10-03

### Added
- Initial release.
- Twelve lenses: CPS, Divergent Thinking, Solution Space Exploration, TRIZ/TIPS, RCA, Cynefin, Six Thinking Hats, First Principles, Occam's Razor, Design Thinking, PDCA, OODA.
- Nine ranking frameworks: Coverage, Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.
- Six-row output table with lens tags and Occam's Razor anchor.
- Bias guards for lens bias, confirmation bias, availability bias, and option-order bias.
- Multi-select decision prompt via `AskUserQuestion`.
- Three worked examples.