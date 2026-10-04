# Onboarding Drop-off at Step 3: Analysis

## 1. First, pin down what "60% at step 3" means

Before you diagnose anything, make sure the number means what you think it does. Three readings are common, and each points to a different problem:

- **60% of users who reach step 3 never finish it.** The step itself is the problem.
- **60% of all signups are gone by step 3.** The leak is spread across steps 1–3, and step 3 is only where you happen to be counting.
- **60% leave the session at step 3 but some come back later.** That's deferral, not abandonment. In B2B this is common: people leave to get credentials, ask IT, or check with their boss.

Also check the instrumentation. A missing or misfiring event at step 3, or an SSO or redirect that breaks tracking, can produce a fake cliff. Have someone go through the flow with analytics open and confirm each event fires once.

## 2. What step 3 usually is in B2B SaaS, and why that matters

In most B2B onboarding, step 3 is where the product first asks for real effort or a dependency outside the user's control. Typical examples:

- Connecting an integration or data source (needs API keys or admin rights)
- Inviting teammates (needs social or political buy-in)
- Importing or configuring data (takes time and effort)
- Entering payment details or picking a plan

If step 3 is one of these, the drop-off probably isn't about UX polish. The step asks for **cost before the user has seen value**, or it depends on **someone who isn't in the session**.

## 3. Hypotheses, ranked by how often they explain this pattern

| # | Hypothesis | What you'd see in the data | Cheap test |
|---|---|---|---|
| 1 | **Effort before value.** Users haven't seen enough payoff to justify the work. | Drop-off is about the same across segments; time spent on step 3 is short (they bail quickly). | Let users skip or postpone step 3, or show sample or demo data first. |
| 2 | **External dependency.** They need credentials, permissions, or approval. | Long time on step, people leaving and returning, higher drop-off among non-admin roles. | Add "send this step to a colleague/admin." Measure return rate within 7 days. |
| 3 | **Wrong-fit signups.** Many signups were never going to activate. | Drop-off varies a lot by acquisition channel, company size, or email domain (gmail vs. corporate). | Segment the funnel by source and by firmographics. |
| 4 | **Confusion or a bug.** The step is unclear or broken for some users. | Errors, rage clicks, drop-off clustered by browser, device, or integration type. | Watch 20–30 session recordings. Check error logs. |
| 5 | **Sales-assisted path bypasses the funnel.** Serious buyers go through a demo instead. | Users who "drop" later show up as opportunities in the CRM. | Join product analytics with CRM data. |

These hypotheses can all be true at once. More likely, one or two dominate. You find out which by segmenting, not by guessing.

## 4. A constraint you should plan around: your volume

200 signups a week is enough to see funnel patterns. It is **not** enough for fast A/B testing of small changes.

Rough numbers: suppose about 120 users a week reach step 3, and you want to detect a 10-point improvement in completion (40% to 50%). That takes roughly 400 users per variant, which is about **6–7 weeks** for one clean test. Small tweaks like copy changes or button colors will take months to prove out, if they ever do.

What this means in practice:
- Make **big swings** (restructure, reorder, or remove the step) rather than micro-optimizations.
- Lean heavily on **qualitative evidence** to pick which swing to make.
- Accept before/after comparisons with a holdback when a full A/B test isn't practical.

## 5. The gap you named: no user interviews

This is the biggest weakness in your current position. Funnel data tells you *where* people leave. It can't tell you *why*. With your volume, you can fix this within a week:

- **Email the last 2–4 weeks of step-3 abandoners.** A short, personal note from a founder or PM ("I saw you got partway through setup. What stopped you?") typically gets a 5–15% response rate. That works out to 10–30 replies.
- **Book 5–8 calls** with responders. Offer a small incentive if needed.
- **Add a one-question exit prompt** on step 3: "What's stopping you right now?" Give a few options plus free text: *need info from someone else / not sure it's worth it / confusing / just exploring / other*.
- **Interview 3–5 users who *did* complete step 3.** Ask what made them push through. Their answers often point straight at the fix.

Ask about what happened, not opinions: "Walk me through what you were doing when you got to that screen. What did you do next?" Avoid "Would you prefer X?"

## 6. Suggested sequence (about 3 weeks to a confident decision)

**Week 1: Verify and segment**
- Confirm the metric definition and the instrumentation.
- Break down step-3 drop-off by acquisition channel, company size, role, device, and corporate vs. personal email.
- Measure how many "drop-offs" return within 7 or 14 days.
- Watch 20–30 session recordings of abandoners.

**Week 2: Talk to people**
- Run the outreach and interviews described above.
- Launch the exit-prompt question.

**Week 3: Decide and ship one structural change**
- Pick the hypothesis with the most converging evidence (quantitative and qualitative pointing the same way).
- Ship one meaningful change, for example making step 3 skippable, moving it after the first value moment, or adding "invite an admin to complete this."
- Define success up front. Measure **downstream activation and retention**, not just step-3 completion.

## 7. Two traps to avoid

- **Optimizing step 3 completion in isolation.** Making the step skippable will raise completion almost by definition. The real question is whether skipped users still activate and convert. If they don't, you've moved the cliff instead of removing it.
- **Assuming 60% is bad.** If many signups are tire-kickers or students, or if serious buyers activate through sales, a 60% drop could be partly healthy filtering. Segmenting (week 1) tells you how much of the 60% is a real problem and how much is noise you shouldn't chase.

## Bottom line

Don't redesign step 3 yet. Spend one week confirming the number and segmenting it, then one week talking to the people who left. Your volume is too low to test your way to an answer, but high enough to *ask* your way there quickly. Most likely you'll find that step 3 asks for effort or a dependency before users have seen value. If so, the fix is usually structural (reorder, defer, or delegate the step), not cosmetic.
