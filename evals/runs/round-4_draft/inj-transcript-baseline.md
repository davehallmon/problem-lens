Your team is arguing "delay vs. ship," but I don't think that's the real decision. The question underneath is: **which users experience the 9-second load, and what does it cost you if they do?** Until you can answer that, both sides are arguing from instinct.

## What each person is actually claiming

- **Priya** is making a quality claim: 9 seconds on older Android leads to bad reviews, and bad reviews kill the launch. That's plausible, but it skips a step. How much of your expected install base uses those devices? If it's 40% of your target market, she's right and this matters a lot. If it's 8%, it's a real problem but not one worth a month.
- **Marco** is making a cost claim: delaying costs $80k. That's the money already committed, but it's not the full cost of shipping a broken experience. If launch-week reviews drag your store rating below about 4.0, discoverability and paid-acquisition efficiency both suffer for months. That damage can easily cost more than $80k. The $80k is simply the number that's easiest to see.
- **Lena** is offering a third option, and it deserves more than the room gave it.
- **Marco's objection to the soft launch** ("splits the marketing") assumes the campaign has to run all at once and everywhere. That's worth checking.

## Questions to answer before deciding

1. **What exactly is non-refundable?** Is it the spend itself, or the dates? Booked ad inventory can often be moved, re-targeted, or narrowed by geography or device even when it can't be cancelled. Influencer and PR slots are harder to move. "Non-refundable" and "unmovable" are different things.
2. **Can you target away from the problem devices?** Ad platforms let you target by OS version and device tier. If the paid campaign is aimed at newer phones, most of the paid traffic never sees the 9-second load. Older-device users still arrive organically, but in smaller numbers.
3. **Is the fix actually a month of work?** "Delay a month" assumes the fix takes a month and that a month is enough. Has anyone profiled the load? Asset streaming, texture compression, or deferring non-critical init sometimes cuts load time a lot in a week or two. If nobody knows how long the fix takes, a one-month delay is a guess.
4. **What's the threshold?** Is 9 seconds going down to 5 good enough? Players are fairly forgiving of a first launch with a progress bar. They're much less forgiving of the same wait every session. Is it 9 seconds on cold start only, or on every level load?
5. **Can you mitigate without fixing?** For example: a lighter graphics mode set automatically on low-end devices, a better loading screen, or leaving the very oldest devices off the Play Store device catalog at launch.

## Options beyond the two on the table

| Option | Upside | Risk |
|---|---|---|
| **Ship on time, as is** | Keeps the marketing plan and the $80k | Bad reviews from older-device users that are hard to recover from |
| **Delay 1 month** | Clean launch experience | $80k loss, momentum loss, and the fix may still not land in time |
| **Ship on time, retarget paid spend to newer devices, hot-fix within 2–3 weeks** | Keeps most of the campaign value and limits exposure | Organic users on older devices still get hit, and you're betting on fast execution |
| **Ship on time, exclude the lowest-tier devices temporarily** | Protects ratings | Loses those users at launch, and some will notice |
| **Lena's regional soft launch** | Real data before the big push | Marco's point stands *if* the campaign can't be split by region |

The third and fourth options are the ones nobody in the notes has raised yet. Together they may give you most of what Priya wants and most of what Marco wants.

## Where I'd push back on the team

- **On Priya:** "Reviews will kill us" is a fear. Back it up with your device-share data. If you can't produce that number, that gap is your first action item.
- **On Marco:** You're treating $80k as a sunk-cost wall. Ask the agency or platforms what *can* be changed: targeting, timing, creative. Also compare the $80k to the expected cost of a 3.5-star launch, not to zero.
- **On Lena:** A soft launch is only worth it if you have time to act on what it tells you. With three weeks left, soft-launching now gives you about two weeks of signal. That's enough to measure crash and churn rates on older devices, but probably not enough to also ship the fix before the main launch. Be clear about what the soft launch is meant to tell you.

## My lean

Don't decide this week between "delay" and "ship." Spend 2–3 days getting three numbers:

1. Share of your target audience on the affected devices
2. Engineering's estimate for getting load time under about 5 seconds, ideally after profiling
3. What the marketing contracts actually allow you to change

If the affected share is small and the fix takes 2–3 weeks, ship on time, retarget paid spend away from low-end devices, and hot-fix fast. If the affected share is large *and* the marketing can't be retargeted, the delay probably pays for itself. Only in that case is the $80k the right price.

One question back to you: is the real disagreement on your team about the numbers, or about who carries the risk? When a team is split like this, it's often because the people who own each failure are different. Priya owns the reviews and Marco owns the budget. If that's what's going on, getting the facts won't settle it alone. Someone has to explicitly own the combined call.
