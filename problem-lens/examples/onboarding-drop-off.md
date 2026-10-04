# Example: Onboarding Drop-Off

## Input

Problem: Our onboarding drop-off is 60% at step 3.
Background: B2B SaaS, 200 signups per week, no user interviews yet.

## Output

_Recorded run: Claude Opus 5.5, 2026-10-03, problem-lens 1.1.0. AskUserQuestion was not available, so the numbered-list prompt appears. Unedited._

**Summary.** The 60% drop-off is a symptom. The likely root is that step 3 asks for something new users can't or won't give yet, like data, access, or a colleague, before they've seen any value. Assuming the 60% counts users who reach step 3, and assuming step 3 is a setup task (integration, import, or invite) and not just a form.

**What's Likely Going On**
- Step 3 needs something the person signing up doesn't have (admin rights, data, a teammate's input). Check: whether drop-off is higher for non-admin roles and larger companies, and which field or action people stop on inside step 3.
- Step 3 is broken or slow for some users (guess). Check: error logs and load time for step 3, split by browser and device. A spike in one segment points to a bug, while an even spread across segments rules it out.
- Many signups aren't real buyers, and step 3 is the first point that asks for commitment (guess). Check: drop-off rate for signups that fit your ideal customer profile vs. those that don't, and by traffic source. If ICP-fit users finish step 3 at a much higher rate, the funnel is fine and the leads are not.

**Recommendation**
- Do this first: Row 1 — run step 3 yourself and check its error logs, because a bug is the cheapest cause to rule out and can be fixed in days.
- Switch to Row 4 if Row 2 shows the drop-off is concentrated among users who lack the access or data step 3 needs.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 · Anchor | Complete step 3 on several browsers and devices, and pull its error and timeout logs for the last 30 days. | Occam's Razor | The simplest explanation is that step 3 is broken, and that needs no theory about users. | A bug alone could explain a 60% drop, and you can check it today. | A clean result can feel like progress but only rules out one cause. |
| 2 | Break down the step 3 drop by role, company size, traffic source, and the last field touched. | Root Cause Analysis | You can see the drop, but the data doesn't yet say which users leave or why. | At about 120 drop-offs a week, two weeks of data will separate the three explanations above. | Analytics may not track field-level events yet, which adds setup time. |
| 3 | Call 6–8 users who stopped at step 3 this month and watch 3 new signups go through it live. | Design Thinking | No one has talked to users yet, so their needs at step 3 are unknown. | Interviews show the reason behind the numbers, such as "I needed IT to approve this." | A handful of calls can over-weight a few loud voices. |
| 4 | Add a "send this step to a teammate" option so the signer can hand step 3 to whoever has the access or data. | TRIZ / TIPS | Step 3 needs input to activate the account, but asking the signer for it stops them cold. | It keeps the setup step and removes the blocker of the wrong person doing it. | It helps only if the blocker is missing access, and the teammate may not act. |
| 5 | Move step 3 after the first moment of value, using sample data or defaults so users see the product working first. | First Principles | The step order is treated as fixed, but nothing says setup must come before value. | Users who have seen value are more willing to do hard setup. | Accounts with sample data may look active but never connect real data. |
| 6 | Offer a "book a 15-minute setup call" link at step 3 for ICP-fit accounts. | Six Thinking Hats | The flow is all self-serve, so the human-help view is missing. | In B2B, a short call often unblocks setup and starts a sales talk. | It doesn't scale and may hide a flow problem you should fix. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. What does step 3 ask the user to do? If it's a plain form and not a setup task, Rows 4 and 5 drop in priority and Row 2 moves to first.
2. Is the 60% measured against all signups or only against those who reach step 3? If it's against all signups, steps 1 and 2 may be part of the problem, and Row 2 should cover the whole funnel.
3. Are you sales-led or self-serve? If you're sales-led, Row 6 moves up to second, because a human-assisted path fits how you already sell.

**What next?** Reply with one or more numbers:
1. **Expand a solution:** Row 1 (logs and run-through), Row 2 (drop-off breakdown), Row 3 (user calls), Row 4 (send to a teammate), Row 5 (value before setup), Row 6 (setup call)
2. **Add more solutions:** CPS, Divergent Thinking, Solution Space Exploration, Cynefin, PDCA, OODA
3. **Re-rank:** Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay
4. **Learn more:** Occam's Razor, Root Cause Analysis, Design Thinking, TRIZ / TIPS, First Principles, Six Thinking Hats, Coverage
