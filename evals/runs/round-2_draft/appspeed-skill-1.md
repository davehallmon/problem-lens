**Summary.** The trade-off between speed and features is likely a symptom: the root is that the app does all its feature setup before the first screen appears, so every speed fix has to cut something. Assuming the 4 seconds is measured to the first usable screen, and assuming past fixes removed or stripped features rather than delaying them. The goal is to change *when* work runs, not *whether* it runs.

**Recommendation.**
- Do this first: Row 1 — trace the cold start and assign every millisecond to a task, because each other fix is a guess until you know where the 4 seconds go.
- Switch to Row 4 if the trace shows most of the time is a required server call (login, balance fetch) that no client change can remove.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | Run a startup trace on a mid-range phone and list each task, its time, and whether the first screen needs it. | Root Cause Analysis | You can see the 4 seconds but not what fills them. | Most cold starts are a few heavy tasks, and fixes chosen without this data tend to hit features instead of waste. | The trace takes days to set up well, and a test phone may not match what customers use. |
| 2 | Load only what the first screen needs, then start each other feature in the background or when the user first opens it. | TRIZ / TIPS | Making launch faster has made features worse. | This resolves the conflict by splitting work in time, so features stay and launch gets shorter. | The first tap on a delayed feature may feel slow unless it is warmed up in the background. |
| 3 | Cut the cost of loading the same code: precompile startup paths, merge or drop dynamic libraries, and shrink the app binary. | First Principles | The team assumes launch cost grows with feature count. | Launch time comes from code loaded and work done, and build-level changes speed both without touching any feature. | Gains vary by platform and may stall at a few hundred milliseconds. |
| 4 | Show the last known balance and screen layout from local cache at once, then refresh in place. | Six Thinking Hats | The engineering view of speed dominates; the customer's sense of speed is missing. | Customers judge speed by when they see something useful, not by when every task ends. | Stale balances in a fintech app can mislead users, so the cached state must be clearly marked. |
| 5 | Put each startup change behind a flag, ship it to a small share of users, and check both launch time and feature use before widening it. | PDCA | Each speed fix is a guess that can be tested in small steps. | This catches any change that hurts feature use before it reaches all customers. | Slow rollouts can stretch the timeline while competitors keep their lead. |
| Anchor | Time your app and the top two competitors today on the same phone, same network, to the same point (first usable screen). | Occam's Razor | The 1.5-second target is the one claim no one has checked. | This confirms the gap is real and defines what "started" means before you spend on fixes. | It tells you how far you are behind but not why. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. Is most of the 4 seconds spent on the phone, or waiting on your servers? If servers, Row 4 moves to first and the fix shifts to backend and caching.
2. Do the competitors' 1.5 seconds measure the same point as your 4 seconds? If they time a splash screen and you time a usable home screen, the gap is smaller and the Anchor becomes the first move.
3. Must any security or compliance check (device checks, login, fraud screening) finish before the first screen? If yes, Row 2 can defer less, and moving those checks to run alongside the UI becomes the main work.

**What next?** Reply with one or more numbers.
1. **Expand a solution** — Row 1 (startup trace), Row 2 (defer feature loading), Row 3 (build-level speedups), Row 4 (cached first screen), Row 5 (flagged rollout), Anchor (side-by-side timing)
2. **Add more solutions** — CPS, Divergent Thinking, Solution Space Exploration, Cynefin, Design Thinking, OODA
3. **Re-rank** — Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay
4. **Learn more** — Root Cause Analysis, TRIZ / TIPS, First Principles, Six Thinking Hats, PDCA, Occam's Razor, Coverage
