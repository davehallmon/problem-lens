**Summary**
"Async vs. video" is a choice of fix, but the likely root is that one 30-minute meeting for 14 people in 3 time zones does not fit how the work is split. Assuming the 14 engineers work in two or three streams that rarely depend on each other, most of each standup is updates that most people do not need. Assuming at least one time zone joins at an awkward local hour, that cost is real even if it goes unspoken.

**What's Likely Going On**
- The group is too big for one standup: most updates matter to only a few listeners — check: map who depends on whom this sprint; if the links cluster into separate groups, size is the cause.
- The standup turns into problem-solving, and the talks run long — check: time one week of standups and split the minutes into status and discussion; if discussion is more than a third, the format is the cause, not the medium.
- (Guess) The time-zone spread is the real pain, and "save time" stands in for "this hour is bad for some of us" — check: ask each zone, privately, their local start time and whether they would keep the meeting.

**Recommendation**
- Do this first: Row 1 — time one week of standups and map who depends on whom, because it tells you which of the three causes you are fixing before you change anything.
- Switch to Row 3 if the dependency map shows two or three groups that rarely need each other.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | Log one week: minutes on status vs. discussion, who speaks to whom, and who depends on whom. | Root Cause Analysis | You can see the symptom (time cost) but not yet the cause. | One week of data tells the three explanations apart at almost no cost. | The team may act differently while it knows it is being timed. |
| 2 · Anchor | Keep the meeting but cap it at 15 minutes; move any discussion to a follow-up with only the people involved. | Occam's Razor | The simplest change cuts time without touching how the team coordinates. | It halves the cost for most people starting tomorrow, with no new tools. | If size is the root, a shorter meeting stays mostly irrelevant to most people. |
| 3 | Split into two or three standups of 4–6 people by work stream, each at a time that suits its members. | First Principles | One meeting for all 14 is treated as the only way to coordinate. | Coordination only needs to happen between people who depend on each other. | Work that crosses streams can fall through the gaps between groups. |
| 4 | Run a two-week async trial with set measures (time to clear a blocker, missed handoffs), then compare with the meeting. | PDCA | "Async will hurt coordination" is a guess you can test in a short loop. | It turns the team's worry into numbers you can check and undo. | Two weeks may be too short to show slow coordination losses. |
| 5 | Make written updates the daily default, and hold a call only on days someone flags a blocker that needs more than one person. | TRIZ / TIPS | Saving time and keeping coordination pull against each other. | It keeps live talk for the cases that need it and drops it on the days that don't. | People may hold back blockers to avoid calling a meeting. |
| 6 | Sort current work into routine and uncertain; handle routine work async and keep live check-ins only for uncertain, tightly linked work. | Cynefin | One method is used for all work, whether routine or uncertain. | Routine work needs status; uncertain work needs live talk, and the two need different formats. | Work labels can drift, and the sorting itself takes upkeep. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. Do the 14 engineers work on one product or on separate streams? Separate streams would move Row 3 to the top, ahead of the time log.
2. What is the local start time for each time zone? If one group joins before 8 a.m. or after 6 p.m., async (Rows 4 and 5) moves up.
3. Does the team keep a shared board or tracker that is current each day? If yes, async carries less coordination risk and Row 5 moves up; if no, async updates would have little to anchor them.

**What next? Reply with one or more numbers.**
1. **Expand a solution** — Row 1 (time log), Row 2 (15-minute cap), Row 3 (split by stream), Row 4 (async trial), Row 5 (blocker-only calls), Row 6 (routine vs. uncertain work)
2. **Add more solutions** — CPS, Divergent Thinking, Solution Space Exploration, Six Thinking Hats, Design Thinking, OODA
3. **Re-rank** — Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay
4. **Learn more** — Root Cause Analysis, Occam's Razor, First Principles, PDCA, TRIZ / TIPS, Cynefin, Coverage
