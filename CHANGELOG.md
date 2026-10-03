# Changelog

All notable changes to this project are documented here.
This project follows Semantic Versioning.

## [Unreleased]

### Changed
- Moved the Skill into a `problem-lens/` folder so the install steps match the repo layout.
- Added a fifth lens family, Perspective (Cynefin, Six Thinking Hats), so five-family coverage is possible.
- Defined a primary lens per row and how Coverage orders rows 1–5.
- Reserved Occam's Razor for the anchor and clarified the anchor-match rule.
- `When To Use This Lens` now names when the lens fits, not when the solution fits.
- Redefined Six Thinking Hats to find solutions from missing views.
- Renamed Cynefin's "simple" domain to "clear".
- Added a numbered-list fallback when `AskUserQuestion` is unavailable.
- Removed unfilled `{problem}` and `{background}` placeholders.
- Corrected all three examples to follow the table rules. Renamed `software-bug.md` to `onboarding-drop-off.md`.
- Corrected the claude.ai install steps (ZIP upload in Customize > Skills).
- Replaced the demo placeholder with a link to a worked example.

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