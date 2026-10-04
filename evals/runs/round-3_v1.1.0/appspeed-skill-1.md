**Summary**
"Speed or features" is likely a false choice. The likely root is that the app does all its work before the first screen (loads every feature, SDK, and API call up front), so cutting startup time means cutting features. Assuming the 4 seconds is time to first usable screen and the competitor figure is measured the same way.

**What's Likely Going On**
- Eager setup: every feature and third-party SDK (analytics, fraud, crash, marketing) starts before the first screen — check: a startup trace shows most of the 4 seconds spent in feature and SDK setup on the main thread.
- Network wait: the first screen waits on several API calls in a row (login, config, balance) — check: the trace shows long idle gaps waiting on the network, and startup drops sharply with responses cached.
- Unfair comparison (guess): competitors show a cached or partial screen at 1.5 seconds and finish loading later, or were timed on a faster device — check: time both apps to first usable screen on the same mid-range phone, cold, on the same network.

**Recommendation**
- Do this first: Row 1 — trace one cold start and sort the time by cause, because it tells you which fix to make instead of cutting features by guess.
- Switch to Row 4 if the trace shows the first screen waits mostly on the network, not on code setup.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | Trace a cold start on a mid-range phone and list each task over 100 ms with its owner. | Root Cause Analysis | You can see the slow start but not what causes it. | Past fixes cut features because no one knew which work cost the time. | One trace on one device may miss what real users' phones show. |
| 2 · Anchor | Time your app and the top two competitors to first usable screen on the same phone, cold, today. | Occam's Razor | The gap may be smaller or different than the 4 vs. 1.5 numbers suggest. | It confirms the target before anyone spends weeks on it. | It may show the gap is real, adding a step without changing the plan. |
| 3 | Keep every feature but start each one only when the user first opens it, after the first screen shows. | TRIZ / TIPS | Speed and features pull against each other, and splitting them in time removes the clash. | Customers keep all features, and the first screen pays only for what it shows. | The first tap into a deferred feature may feel slow unless it preloads in the background. |
| 4 | Show the last known balance and home screen from secure local storage at once, then refresh from the server. | First Principles | The rule that the first screen must wait for fresh server data is assumed, not required. | It takes network wait out of startup without removing anything. | Stale balances in a fintech app can confuse users unless they are clearly marked as updating. |
| 5 | Ship each change behind a flag to 5% of users and compare startup time and feature use before rolling out. | PDCA | Each fix is a guess about what is safe to defer, and you can test it in small steps. | It catches any fix that quietly hurts feature use before all customers see it. | Slower rollout, and small groups may hide rare-device problems. |
| 6 | Set a startup time budget per team and SDK, checked in each build, with security, marketing, and product at the table. | Six Thinking Hats | Engineering has owned speed alone, while the teams adding SDKs and checks are missing from the room. | It stops new features and SDKs from pushing startup back to 4 seconds. | Teams may resist a hard limit if security or compliance checks must run first. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. Were the removed features on the first screen or elsewhere in the app? If elsewhere, Row 3 moves to first, since deferring them is near-certain to help. If on the first screen, Row 4 matters more.
2. Must any security or fraud checks finish before the first screen by rule? If yes, Row 6 moves up, because the fix becomes running them in parallel and agreeing on what can wait.
3. Is the 4 seconds from real users' phones or a test device? If from a fast test device, real users likely see worse, and Row 1 should trace on low-end phones first.

**What next?** Reply with one or more numbers:
1. **Expand a solution** — Row 1 (cold start trace), Row 2 (side-by-side timing), Row 3 (start features on first use), Row 4 (cached first screen), Row 5 (flagged rollout), Row 6 (startup budget).
2. **Add more solutions** — CPS, Divergent Thinking, Solution Space Exploration, Cynefin, Design Thinking, OODA.
3. **Re-rank** — Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.
4. **Learn more** — Root Cause Analysis, Occam's Razor, TRIZ / TIPS, First Principles, PDCA, Six Thinking Hats, Coverage.
