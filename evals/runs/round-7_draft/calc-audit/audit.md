# Calculation Audit — Rounds 6 and 7

One auditor agent read all 22 Skill outputs from rounds 6 and 7, shuffled and renamed (`resp-NN-<problem>.md`), so it could not tell which round, and therefore which version of `SKILL.md`, produced each one. `key.json` maps each file name to its round.

For every **derived** number (a figure the response worked out, not one copied from the user), the auditor classified it as:

- **Supported:** follows from the user's numbers alone.
- **Assumed:** needs an unstated fact, and the response names that assumption next to the number.
- **Unsupported:** needs an unstated fact, and the response does not say so.
- **Wrong:** the arithmetic or reasoning is incorrect even given the stated inputs.

## Totals

| Round | Supported | Assumed | Unsupported | Wrong |
|---|---|---|---|---|
| 6 (no guard) | 10 | 5 | 9 | 0 |
| 7 (with guard) | 10 | 6 | 3 | 0 |

## Unsupported figures

| Round | File | Figure |
|---|---|---|
| 6 | resp-14-onboarding | "about 120 drop-offs" (assumes every signup reaches step 3) |
| 6 | resp-14-onboarding | "about four weeks to spot a 10-point lift" (baseline and arm size unstated) |
| 6 | resp-14-onboarding | "It takes an hour" (effort estimate not marked) |
| 6 | resp-19-revenue | "near 85% or higher" utilization benchmark, twice (not marked as a rule of thumb) |
| 6 | resp-05-receptionist | "about six slow hours a day" (assumes an unstated 8-hour day) |
| 6 | resp-09-appspeed | "It takes an hour" (effort estimate not marked) |
| 6 | resp-15-gym | "This takes an hour" (effort estimate not marked) |
| 6 | resp-01-turnover | "about one exit a month" (40-nurse assumption stated only in the Summary) |
| 7 | resp-10-receptionist | "about six hours a day outside the problem window" (unstated day length) |
| 7 | resp-16-onboarding | "It costs an hour" (effort estimate not marked) |
| 7 | resp-16-onboarding | "one afternoon of this" (effort estimate not marked) |

The auditor's counts are per figure. Its round 6 total of 9 counts the repeated 85% benchmark twice.
