# Example: Software Bug

## Input

Problem: Our onboarding drop-off is 60% at step 3.
Background: B2B SaaS, 200 signups per week, no user interviews yet.

## Output

Summary: The drop-off may be a symptom, not the problem. Test the step-3 flow with five users before optimizing. If the flow is fine, the problem is expectations, not design.

| Priority | Solution | Lens Tags | When To Use This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | Watch five users complete step 3 | Design Thinking, Root Cause Analysis | User behavior is unknown | Direct observation finds the real cause faster than guessing | Small sample may not represent all users |
| 2 | Split the flow into two shorter steps | Divergent Thinking, Occam's Razor | The step is too dense | Fewer fields per screen lift completion | Adds a screen and may slow power users |
| 3 | Add a progress bar and save-and-resume | CPS, Solution Space Exploration | Users feel lost or rushed | Reduces perceived effort and lets users return | Cosmetic fix if the cause is deeper |
| 4 | Offer a skip option with a default | TRIZ, Six Thinking Hats | The step is mandatory but low-value | Removes the contradiction between required and unwanted data | Skips may reduce data quality |
| 5 | Move step 3 to after first value | First Principles, PDCA | Users have not seen value yet | Ask for effort after the user sees a payoff | Delays setup and may create later friction |
| Anchor | Ask why users drop at step 3 | Occam's Razor | The cause is unknown | One question may reveal the answer | Users may not know or may not say |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

## Decision Prompt

- Expand a solution
- Add more solutions
- Re-rank
- Done
