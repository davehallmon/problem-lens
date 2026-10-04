# Example: Business Strategy

## Copy This Prompt

```
Analyze this problem: revenue is flat for three quarters.

Background: B2B services firm, 40 staff, no marketing team.
```

## Input

Problem: Revenue is flat for three quarters.
Background: B2B services firm, 40 staff, no marketing team.

## Output

_Recorded run: Claude Opus 5.5, 2026-10-03, problem-lens 1.1.0. AskUserQuestion was not available, so the numbered-list prompt appears. Unedited._

**Summary**
Flat revenue is a symptom, not the problem. Assuming most new work comes from referrals and senior staff both sell and deliver, the likely root is either no steady way to win new clients or a cap on how much work 40 people can bill. Find out which one it is before you spend on marketing.

**What's Likely Going On**
- **Capacity ceiling:** staff are fully booked, so revenue can't grow without more people or higher rates — check: billable utilization and average rate per hour for the last six quarters. High, flat utilization points here. Low utilization rules it out.
- **New-client pipeline has slowed:** referrals have thinned out, and existing clients are only replacing what you lose — check: revenue split into new clients and existing clients by quarter, plus the number of proposals sent. A falling share from new clients points here.
- **A large client shrank, hidden by small gains** (guess) — check: revenue from your top 10 clients for each of the last six quarters. One or two big drops with steady totals elsewhere point here.

**Recommendation**
- Do this first: Row 1 — split the last six quarters of revenue by source, because it tells you which of the three causes is real for about a day of work.
- Switch to Row 5 if utilization is above about 85%. If so, the limit is capacity, not demand.

| Priority | Solution | Lens | Why This Lens | Rationale | Risk |
|---|---|---|---|---|---|
| 1 | Break the last six quarters of revenue into new clients, growth in existing clients, lost clients, utilization, and rate. | Root Cause Analysis | You can see the flat line, but not what is causing it. | Each cause calls for a different fix, so this decides the rest of the order. | Messy billing data may take longer to sort than expected. |
| 2 · Anchor | Call your top 10 clients this month. Ask what is changing in their plans and what else they need. | Occam's Razor | The simplest source of new revenue is clients who already trust you. | It costs nothing, starts today, and may surface work or warning signs right away. | Calls that sound like a sales pitch can strain client relationships. |
| 3 | Ask delivery staff to flag client needs they see on the job, and pay a bonus for leads that close. | Six Thinking Hats | Leadership's view dominates, and the view of staff who talk to clients every day is missing. | With no marketing team, your 40 staff are the widest channel you already have. | Staff may push work on clients who don't need it, which hurts trust. |
| 4 | Run a 90-day outbound test: pick one niche where you have strong past results, contact 50 similar firms, and review results every month. | PDCA | No one knows yet which channel works, so test small before you commit. | Monthly checks show quickly whether outbound sales can work for you. | 90 days may be too short for long B2B sales cycles. |
| 5 | Turn your most common job into a fixed-price package or monthly retainer, and raise rates on new work. | First Principles | Billing by the hour is treated as the only way, which caps revenue at hours worked. | If staff are fully booked, price and packaging are the only levers that don't need new hires. | Clients may reject the new prices, or a fixed scope may lose money. |
| 6 | Free one senior person to spend half their time on sales, and move their client work to more junior staff. | TRIZ / TIPS | The people best placed to sell are also the ones billing, so more selling means less billing. | It splits the two roles so selling happens on a schedule, not only when there is spare time. | Delivery quality may drop, and the senior person may not like or be good at selling. |

Ranked by: Coverage (default). Other options: Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.

**Questions That Would Change the Pick**
1. Is billable utilization above about 85%? If yes, Row 5 moves to first, and the sales rows (3, 4, 6) drop because you couldn't deliver more work anyway.
2. Did you lose or shrink a major client in the last year? If yes, the anchor moves to first: win back that work or replace it.
3. Do you want growth, or would flat revenue with better margins be fine? If margins are the goal, the pick shifts toward Row 5 and away from the sales rows.

**What next?** Reply with one or more numbers.
1. **Expand a solution** — Row 1 (revenue breakdown), Row 2 (top-10 client calls), Row 3 (staff lead bonus), Row 4 (90-day outbound test), Row 5 (packages and rates), Row 6 (senior person on sales).
2. **Add more solutions** — CPS, Divergent Thinking, Solution Space Exploration, Cynefin, Design Thinking, OODA.
3. **Re-rank** — Impact vs. Effort, Confidence vs. Reversibility, ICE, RICE, Eisenhower, Regret Minimization, Optionality, Cost of Delay.
4. **Learn more** — Root Cause Analysis, Occam's Razor, Six Thinking Hats, PDCA, First Principles, TRIZ / TIPS, Coverage.
