**Summary.** Slow startup is the symptom. The likely root is that too much work runs before the first screen, so features and launch are tied together, and cutting launch work cuts features. Assuming "cold start" means time from tap to a usable home screen, and that the removed features did their work at launch.

**What's Likely Going On**
- Eager setup: SDKs and feature modules (analytics, fraud, crash reporting, feature flags, push) start on the main thread before the first frame — check: a startup trace that shows time per setup call before the first frame; if most of the 4 seconds sits there, this is it.
- Network waits: launch blocks on calls such as token refresh, remote config, or balance fetch — check: compare cold start on fast Wi-Fi vs. a throttled network; if the time moves with the network, this is it, if it stays flat, it is not.
- Security gates (guess): root or jailbreak checks, encrypted storage reads, or device checks run before any screen — check: the trace segment for security libraries, or a test build with them stubbed out.

**Recommendation**
- Do this first: Row 1 — time your app and two competitors the same way, because the 1.5-second target only matters if both numbers measure the same thing.
- Switch to Row 3 if you already have a startup trace that shows where the 4 seconds go.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 · Anchor | Time your app and two competitors on the same mid-range device, cold, from tap to a usable home screen (not splash). | Occam's Razor | The simplest step is to confirm the gap before you fix it. | If competitors show cached screens or skeletons early, the real gap may be smaller or a different shape. | Hand timing is rough, so small gaps may be noise. |
| 2 | Run a startup trace and ask "why" for each task before the first frame, and for each past fix, why it removed a feature. | Root Cause Analysis | You can see the slow start but not which tasks cause it or why fixes broke features. | It shows which explanation above is true and which features are wired into launch. | A single trace on one device may miss what slower phones see. |
| 3 | Defer every task not needed for the first screen until after it draws, and load each feature on first use. | TRIZ / TIPS | Each speed gain has cost a feature, which is a contradiction you can resolve by splitting the work in time. | Features stay; only when they load changes. | Deferred work can cause jank or a slow first tap on a feature. |
| 4 | Ask security and compliance which checks must run before any screen and which can wait until the first money action. | Six Thinking Hats, First Principles | The speed view has led so far; the risk view has not been asked what is truly required at launch. | In fintech, security gates are often a large, fixed launch cost that may not need to sit there. | Moving a check later may break a rule or a bank partner contract. |
| 5 | Show the last-known home screen from encrypted cache at once, marked as updating, then refresh in the background. | First Principles | The app treats "wait for fresh data" as the only way to start. | Users see a usable screen in about a second while live data loads. | Stale balances can confuse users or raise compliance concerns. |
| 6 | Set a startup-time budget in CI and ship each change behind a flag to a small share of users, tracking cold start and feature use. | PDCA | Each fix is a guess that can be tested in small steps. | It stops new features from slowing launch again and catches feature loss early. | Lab and field numbers can differ, so the budget may block good changes. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. Is the app native, or built with React Native or Flutter? If cross-platform, script or engine load may be the main cost, and Row 3 would center on bundle splitting.
2. Do regulators or bank partners require specific checks before any screen shows? If yes, Row 4 drops and Row 5 rises, since cache can mask fixed security time.
3. Did the removed features actually run at launch, or were they cut to shrink the app? If they did not run at launch, the coupling lies elsewhere and Row 2 moves to the top.

**What next?** Reply with one or more numbers.
1. **Expand a solution** — Row 1 (time like with like), Row 2 (startup trace), Row 3 (defer and load on use), Row 4 (move security gates), Row 5 (cached home screen), Row 6 (startup budget).
2. **Add more solutions** — CPS, Divergent Thinking, Solution Space Exploration, Cynefin, Design Thinking, OODA.
3. **Re-rank** — Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.
4. **Learn more** — Occam's Razor, Root Cause Analysis, TRIZ / TIPS, Six Thinking Hats, First Principles, PDCA, Coverage.
