**Summary.** The likely root is not sync versus async but a 30-minute call where 14 people sit through updates most of them do not need. Assuming the team works in loose sub-groups and no one has measured where the 30 minutes go, find that out before you change the format. The call costs about 7 engineer-hours a day (14 × 30 minutes), so one week of logging is cheap next to it.

**What's Likely Going On**
- Too many people for one call: most updates do not concern most listeners — check: for one week, note whose update each engineer acted on; if most act on updates from only 3–5 others, size is the cause.
- The call drifts into problem-solving between two or three people while the rest wait — check: time each standup for a week; if more than half the minutes go to side discussions, format is the cause.
- Guess: the time slot is bad for one of the 3 time zones, so the cost falls unevenly and feels larger — check: count who joins outside normal hours or skips; if one zone carries most of it, timing is the cause.

**Recommendation**
- Do this first: Row 1 — log a week of standups (minutes spent on status, blockers, and side talk, and who acts on whose update), because it tells you whether the waste is in who attends or how the call runs.
- Switch to Row 3 if most engineers act on updates from only a few others.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | Log one week of standups: minutes by type, and who acted on whose update. | Root Cause Analysis | You can see the lost time but not what eats it. | It separates the size, format, and timing explanations before you commit to a change. | One person must track it for a week, and one week may not be typical. |
| 2 · Anchor | Starting tomorrow, cap the call at 15 minutes: blockers only, and move any discussion to a follow-up with just the people involved. | Occam's Razor | The fix may be a rule change, not a new system. | It halves the cost with no new tools and keeps live contact. | With 14 people, 15 minutes still leaves about one minute each, so status may creep back in. |
| 3 | Split into smaller standups by sub-team or time zone, with one person per group posting cross-group dependencies. | TRIZ / TIPS | Cutting meeting time seems to cost coordination, and splitting the group can keep both. | People hear only the updates they act on, and groups can meet at a better hour for their zone. | Work that crosses groups can slip if the dependency posts lapse. |
| 4 | Run a two-week async trial with written daily updates, and track missed handoffs and time spent blocked. | PDCA | Whether async hurts coordination is a guess you can test in a short loop. | It answers the team's worry with data instead of opinion. | Ten workdays is a small sample, and written updates often decay into filler. |
| 5 | Drop scheduled status and use a shared blocker board that people update the moment they are stuck or need someone. | First Principles | The daily meeting is treated as the only way to coordinate. | Coordination needs blockers and dependencies raised fast, not a daily recital. | It relies on people raising blockers without a prompt, which some will not do. |
| 6 | Keep one 30-minute video call a week for demos and face time, whatever the daily format. | Six Thinking Hats | The time-saving view dominates, and the social cost of losing face time is missing. | Across 3 time zones, the standup may be the only time some people see each other. | It adds back a meeting and may not fix daily coordination on its own. |

`Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.`

**Questions That Would Change the Pick**
1. Do the 14 engineers already work in distinct sub-teams or areas? If yes, Row 3 moves to first; if everyone touches the same code daily, Row 4 or Row 5 moves up.
2. Does any single meeting time fall outside normal hours for one of the zones? If yes, timing is part of the root, and Row 3 (split by zone) or Row 4 (async) beats Row 2.
3. Is the standup the main time the team sees each other? If yes, Row 6 should come with any change, not after it.

**What next?** Reply with one or more numbers:
1. **Expand a solution** — Row 1, Row 2, Row 3, Row 4, Row 5, Row 6
2. **Add more solutions** — CPS, Divergent Thinking, Solution Space Exploration, Cynefin, Design Thinking, OODA
3. **Re-rank** — Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay
4. **Learn more** — Root Cause Analysis, Occam's Razor, TRIZ / TIPS, PDCA, First Principles, Six Thinking Hats, Coverage
