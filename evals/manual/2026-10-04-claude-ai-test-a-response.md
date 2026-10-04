I'll load the problem-lens skill and run your onboarding drop-off through it.

**Summary**
Assuming the 60% counts all signups (about 120 people a week) and step 3 is where users must do real work, such as connecting data or inviting a teammate, the likely root is that step 3 asks for more effort, access, or trust than a new user can give in one sitting. The 60% is a symptom until someone confirms the tracking is right and looks at what step 3 actually asks. With no user interviews, every cause below is a guess.

**What's Likely Going On**
- **The number is wrong or distorted** (a tracking bug, bots, or signups who were never a fit) — check: compare step-3 events with backend records, then split the drop-off by company email vs. free email. Guess.
- **Step 3 asks too much** (an integration, a data upload, an invite, payment, or approval from someone else, which is common in B2B) — check: find the last action before exit, and see whether leavers come back days later. Guess.
- **Expectation mismatch** (the signup promise and step 3 don't match, or one channel brings the wrong people) — check: compare step-3 drop-off by acquisition channel. Guess.

**Recommendation**
- **Do this first:** Row 1 — walk through step 3 yourself as a new customer, because it takes about an hour, needs nothing you lack, and shows whether step 3 is broken or only demanding.
- **Switch to Row 2 if** step 3 works and feels easy, or if the drop began on a specific date. Then tracking, a release, or a change in who signs up is the more likely cause.

**Table**

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 · Anchor | Sign up on a clean account and do onboarding yourself on laptop and phone, timing step 3 and noting every point of friction. | Occam's Razor | Dashboards and theories are piling up before anyone has used step 3 as a new user. | It costs about an hour and shows a bug or a heavy ask directly. | You know the product too well to feel what a new user feels, so also watch a colleague who has never seen it try. |
| 2 | Confirm the tracking is right, then split step-3 drop-off by channel, email domain, device, and last action before exit, pooling the last four weeks. | Root Cause Analysis | The drop is visible but the cause is not. | One week gives about 120 leavers, too few to split several ways, while four weeks (about 480, assuming a steady rate) is enough to compare groups. | It needs event-level analytics, and if you only have funnel totals this waits on added tracking. |
| 3 | Ask sales, support, or customer success what trial users say about step 3, and read last month's support tickets that mention it. | Six Thinking Hats | Only the dashboard view is in the room, and the people who talk to customers are missing. | It brings in user-side facts within a day, before any interview is arranged. | If no one talks to trial users, this returns nothing and the row drops out. |
| 4 | Email people who left at step 3 within 48 hours and offer a 15-minute call, aiming for five calls in two weeks. | Design Thinking | No one has heard from the users this fix is for. | Assuming about 1 in 20 of the roughly 120 weekly leavers agree to talk (a guess), you reach about 6 a week, enough to hear repeated reasons. | Leavers often ignore email, so you may need a small incentive, and you haven't said whether there is budget for one. |
| 5 | List what a user must do to reach first value, then make step 3 skippable or move it after that point for all new signups and compare with the prior four weeks. | First Principles | Step 3 may be in the flow only because it has always been there. | If step 3 isn't needed for first value, removing it is the cheapest fix, and a large effect shows within a few weeks. | A before-and-after comparison can be skewed by a change in who signs up, and an A/B test would need about 4 weeks to see a 10-point lift (assuming 40% to 50%, 80% power, an even split of all 200 weekly signups). |
| 6 | If step 3 collects data or setup the product needs, keep it but cut the effort: offer sample data for a first result, pre-fill what you know, or let the user hand the task to a teammate or your team. | TRIZ / TIPS | You need step 3's input to deliver value, but asking for it is what pushes people out. | Separating getting value from supplying real input removes the conflict instead of trading one side for the other. | It takes build time and only applies if step 3 is a data or setup task, which you haven't said. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. **What does step 3 ask the user to do?** If it is an integration, upload, invite, or payment, Rows 6 and 5 move up. If it is a short form, Rows 1 and 2 stay on top.
2. **Is the 60% share of people who reach step 3, or of all signups, and did it change on a known date?** A recent jump makes Row 2 the first move, along with a check of the release log.
3. **Does anyone on your team talk to trial users today?** If not, Row 3 drops out and Row 4 moves up.

**Occam's Razor.** Prefer the explanation that needs the fewest assumptions.
- *Why it fit:* Before anyone chased theories, the simplest cause (step 3 is hard or broken) could be checked in an hour.
- Link: https://www.britannica.com/topic/Occams-razor

**Root Cause Analysis.** Tools such as 5 Whys and Fishbone diagrams that trace a symptom back to its cause.
- *Why it fit:* A 60% drop shows the symptom but not the cause, and the data split in Row 2 is how you find it.
- Link: https://asq.org/quality-resources/root-cause-analysis

**Six Thinking Hats.** Edward de Bono's method for looking at a problem from six separate views, one at a time.
- *Why it fit:* Right now only the dashboard view is in the room, and sales, support, and customer success hold the missing user-side view.
- Link: https://www.debonogroup.com/services/core-programs/six-thinking-hats/

**Design Thinking.** A human-centered process: understand the people you serve, then prototype and test.
- *Why it fit:* You have no user interviews, so you don't yet know what the people leaving step 3 need.
- Link: https://www.ideou.com/blogs/inspiration/what-is-design-thinking

**First Principles.** Reasoning from basic truths instead of from how things are usually done.
- *Why it fit:* Step 3 may exist only because it has always been in the flow, and asking what first value requires tests that.
- Link: https://en.wikipedia.org/wiki/First_principle

**TRIZ / TIPS.** Genrich Altshuller's method for solving problems by resolving contradictions with patterns from past inventions.
- *Why it fit:* You may need step 3's input to deliver value, yet asking for it is what drives users away, which is a contradiction to resolve.
- Link: https://en.wikipedia.org/wiki/TRIZ

**Coverage (ranking).** Pick one solution from each of five lens families, then order by expected effect on the root problem.
- *Why it fit:* With no data on the cause yet, it put cheap checks ahead of costly fixes while keeping five different kinds of move in view.
- Link: none (defined by this Skill)

I can also expand a row, add solutions from the unused lenses, re-rank, or update the pick once you answer the three questions.