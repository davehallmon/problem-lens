**Summary**
The 60% drop is a symptom. The likely root is that step 3 asks for effort or trust before users see value, though a bug or poor-fit signups could cause the same number. Assuming step 3 asks for setup work such as connecting data, inviting teammates, or entering billing, and assuming the 60% is measured among users who reach step 3.

**What's Likely Going On**
- Step 3 is broken or confusing (an error, a dead button, an unclear field) — check: error logs and step 3 completion by browser and device; a bug shows as error spikes or one device with near-zero completion. *(Guess.)*
- Step 3 asks for costly effort before value (data access, IT approval, teammates) — check: time spent on step 3 and how many leavers come back within a week; effort shows as long stays and later returns, a bug as fast exits. *(Guess, and the most common pattern in B2B setup steps.)*
- Many signups are poor fit and would never have activated — check: drop-off split by signup source and company size; if good-fit accounts finish step 3 at a much higher rate, the problem is who signs up, not the step. *(Guess.)*

**Recommendation**
- Do this first: Row 1 — complete step 3 yourself on a fresh account and read the error logs, because a bug would make every other fix moot and you can rule it out in an hour.
- Switch to Row 6 if the segment split in Row 2 shows good-fit accounts also stall on step 3 for a long time.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 · Anchor | Sign up as a new user on two or three browsers, complete step 3, and check the error logs for that step. | Occam's Razor | "It's broken" is the explanation with the fewest assumptions, so test it before the costly ones. | A bug is cheap to find and fix and would explain a sharp drop at one step. | Finding no bug can feel like progress while the real cause goes unchecked. |
| 2 | Split step 3 drop-off by source, company size, device, and time on step, then ask "why" down each branch. | Root Cause Analysis | You can see where users leave but not why, and the three explanations predict different splits. | The data you already have can tell the three explanations apart within a day or two. | 200 signups a week gives thin slices, so small segments may mislead. |
| 3 | Run a short session where sales and support name the fears and doubts buyers voice about what step 3 asks for. | Six Thinking Hats | The only view in hand is funnel data; the feelings and risks buyers voice to your front line are missing. | People who talk to buyers often know the objection already, at no cost. | Front-line stories reflect the loudest buyers, not the typical one. |
| 4 | Interview five to eight users who stopped at step 3 and watch two new users try it live. | Design Thinking | You have no interviews, so the needs of the people stalling are not yet understood. | Watching users hit step 3 shows what the data cannot, such as who they had to ask for access. | Users who left may not respond, and the ones who do may not be typical. |
| 5 | Offer good-fit signups a 15-minute setup call to complete step 3 with them. | First Principles | Self-serve setup is treated as the only path, but at 200 signups a week a human can cover the good-fit share. | It gets high-value accounts past the step now while you learn what blocks them. | It does not scale and can hide a product problem behind human effort. |
| 6 | Let users skip or defer step 3 and reach a first result with sample data, then ask for setup once they see value. | TRIZ / TIPS | You need step 3's setup for the product to work, yet asking for it early drives users away. | Moving the ask after the first result resolves the conflict instead of trading one side for the other. | Users who skip may never return to finish setup, which moves the drop to a later step. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. What does step 3 ask the user to do? If it needs IT approval or another person, Rows 5 and 6 move up; if it is a plain form, Rows 1 and 4 stay on top.
2. Is the 60% of users who reach step 3, or of all signups? If it is of all signups, the loss may be spread across steps 1 to 3 and Row 2 should look at the whole funnel first.
3. How much is a won account worth, and do you have sales or success staff? A high deal size with staff in place moves Row 5 to second; low deal size with no staff drops it to last.

**What next?** Reply with one or more numbers:
1. **Expand a solution** — Row 1 (test step 3 yourself), Row 2 (segment and ask why), Row 3 (sales and support session), Row 4 (interviews), Row 5 (setup call), Row 6 (skip or defer step 3).
2. **Add more solutions** — CPS, Divergent Thinking, Solution Space Exploration, Cynefin, PDCA, OODA.
3. **Re-rank** — Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.
4. **Learn more** — Occam's Razor, Root Cause Analysis, Six Thinking Hats, Design Thinking, First Principles, TRIZ / TIPS, Coverage.
