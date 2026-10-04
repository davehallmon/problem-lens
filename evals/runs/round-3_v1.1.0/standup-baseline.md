# Standup Analysis: Async vs. Live

## The question is framed too narrowly

"Live standup or async updates" treats the choice as a single switch. The better question is: **which jobs is the current standup doing, and what is the cheapest way to do each one?** A daily standup usually does three different jobs:

1. **Status broadcast**: what I did and what I'm doing next. Async handles this well, often better, because it's written down and searchable.
2. **Blocker resolution and coordination**: "I'm waiting on your API change" or "we're both touching the auth module." This is the part your team is worried about. It needs fast back-and-forth between a few specific people. It rarely needs all 14.
3. **Social cohesion and visibility**: seeing faces, noticing when someone is struggling, keeping a sense of being one team across time zones. People often don't name this job, and it is usually the first thing lost when a team goes async.

If most of your 30 minutes goes to job 1, going async is an easy win. If the meeting is where jobs 2 and 3 actually get done, replacing it with written updates alone will cause the coordination problems you're expecting.

## The time savings are real but smaller than they look

- **Current cost:** 14 people × 30 min = **7 person-hours a day, about 35 a week.**
- **Async isn't free.** Writing a useful update takes 5 to 10 minutes. Reading 13 others takes another 5 to 10 if people actually read them. That's roughly 10 to 15 min per person per day, so the real saving is about **half**, not all of it.
- **Hidden costs on both sides:**
  - Live: with three time zones, someone is probably meeting at an awkward hour. A meeting in the middle of the day also breaks up focus time, so it costs more than its 30 minutes.
  - Async: blockers can take hours to surface instead of minutes, and with time-zone gaps, one missed handoff can cost a full day.

**What this tells you:** 14 people is too many for a single live standup. Most of each person's 30 minutes is spent listening to updates that don't affect their work. A large share of the waste may come from the team's size rather than the format.

## Things the team may not have said yet

- **Who is actually asking for this?** If it's the engineers in the off-hours time zone, the real issue may be fairness, not efficiency. That calls for a different fix, such as rotating the meeting time.
- **Is "coordination" a real concern or a guess?** Can someone name the last two or three times standup caught a collision or blocker that wouldn't have come up otherwise? If nobody can, the coordination value is mostly assumed. If people can, those examples show you exactly what any replacement has to preserve.
- **Async fails quietly.** Updates turn into boilerplate ("worked on ticket X, continuing"), nobody reads them, and blockers stay buried. You won't notice this the way you notice a bad meeting. You'd notice it weeks later as slipped work.
- **Are there sub-teams?** Fourteen engineers almost always split into two or three groups that coordinate mostly with each other. The org chart and the coordination pattern may not match.

## Options worth considering

| Option | Saves time | Protects coordination | Protects cohesion | Notes |
|---|---|---|---|---|
| Keep as-is | No | Yes | Yes | Default; costs ~35 person-hrs/week |
| Fully async | Moderate | At risk | At risk | Works for very independent work streams |
| **Async updates + short live sync 1–2×/week** | Good | Mostly | Mostly | Common, sensible middle ground |
| **Split into 2–3 sub-team standups (~10–15 min)** | Good | Yes, often better | Partly | Addresses the size problem directly |
| **Async by default + "blocker escalation" norm** | Good | Yes, if norm is real | No | Needs a clear rule: blockers get posted immediately and tagged, not saved for the update |
| Rotating meeting time | None | Yes | Yes | Fixes fairness, not cost |

A strong combination: **async written updates daily, an explicit blocker channel with a response-time expectation, and one or two short live syncs a week**, split by sub-team if natural groupings exist.

## How to decide without guessing: run a time-boxed experiment

1. **Before switching, write down what "hurt coordination" would look like**: missed dependencies, duplicated work, blockers that sit for more than X hours, PR review latency, sprint carryover. Measure a two-week baseline.
2. **Run the new format for 3–4 weeks.** One week is too short; the novelty effect hides problems.
3. **Make the async update structured**, not free-form, e.g.: *Blockers / Needs from someone / Changes others should know about / Progress*. Putting blockers first keeps them from getting buried.
4. **Assign an owner** to scan updates daily for collisions and blockers. Async coordination tends to fail when nobody is responsible for reading the updates.
5. **Check at the end** using the metrics plus a short anonymous pulse: "Do you know what you need to know?" "Do you feel connected to the team?"
6. **Agree in advance on the rollback condition** so reverting is a planned outcome, not a fight.

## Bottom line

Your team is right that there's waste. Your concern is also right that a plain async switch can quietly damage coordination. The 30-minute, 14-person meeting is probably the wrong format either way. Likely the best result comes from splitting the jobs: move status updates to writing, give blockers a fast dedicated channel, keep a small amount of live time for coordination and connection, and test it against measures you choose before the switch rather than against impressions afterward.
