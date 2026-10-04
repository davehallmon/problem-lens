# Changelog

All notable changes to this project are documented here.
This project follows Semantic Versioning.

## [Unreleased]

### Changed
- New banner: "Twelve lenses. Six moves. One first step." with the OCKHAM maker mark. Removed the old `assets/banner.svg`.
- Renamed the banner to `assets/banner-v2.png` so GitHub and browsers stop serving the cached old image.
- README opening line now matches the banner byline.
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