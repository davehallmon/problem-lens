# Analysis: Faster Cold Start Without Losing Features

## The framing is likely the problem

"Every speed fix removes features" suggests the team is treating startup time as a function of **what the app contains**. It is mostly a function of **what the app does before the first usable screen**. Those are different things.

A feature that customers use doesn't have to be initialized at launch. If removing features is the only lever that has worked, the likely cause is that features are coupled to startup: they're eagerly initialized, pulled in by the dependency graph, or blocking the first frame through synchronous calls. The useful question isn't "which features can we cut?" It's "which work has to happen before the user sees their balance, and why is everything else happening then too?"

## Assumptions worth challenging

1. **"4s vs 1.5s" is a like-for-like comparison.** Check how both numbers were measured. Is it time to first frame, or time to an interactive, authenticated screen? On what devices, and is it a P50 or a P90? Competitors may show a cached or skeleton home screen at 1.5s and finish loading after that. If yours means "fully loaded and authenticated" and theirs means "something on screen," the real gap is smaller and the fix is different.
2. **Cold start is the metric customers feel.** Find out what share of sessions are actually cold starts. If most are warm or hot resumes, cold start may matter less than resume time or the delay before biometric login.
3. **The removed features were the cause.** If removing a feature sped things up, that tells you its *initialization* was expensive. It doesn't tell you the feature itself has to cost anything at launch.
4. **All startup work is equally negotiable.** In fintech it isn't. Some of it (integrity checks, session validation) may be required by security or compliance. Separate that work early so it doesn't get treated as either untouchable or easy to cut.

## Where fintech cold starts usually lose time

- **Third-party SDK initialization**: fraud and device fingerprinting, analytics, crash reporting, attribution, push, chat support, A/B testing. These often run synchronously in `Application.onCreate` or `didFinishLaunching`, and five to ten of them can add up to more than a second.
- **Security checks run serially**: root or jailbreak detection, tamper checks, certificate pinning setup, keystore or keychain access.
- **Blocking network calls before first frame**: remote config, feature flags, session refresh, an account summary fetch.
- **Dependency injection graphs built eagerly**: every feature module gets constructed at launch whether it's needed or not.
- **Large binary or bundle size, and no baseline or startup profiles** (Android), or heavy static initializers and dylib loading (iOS).
- **Main-thread disk I/O**: encrypted database opens, migrations, large preference files.

## A way out that doesn't cut features

**1. Instrument first.** Trace a real cold start on a mid-tier device (Android Studio / Perfetto, Xcode Instruments App Launch). Attribute every millisecond to a named owner. Without this, the team is guessing, and guessing is probably how they ended up cutting features.

**2. Classify all startup work into four tiers:**

| Tier | Runs when | Examples |
|---|---|---|
| Critical path | Before first frame | Minimal UI shell, session token read |
| Pre-interaction | In parallel, before the user can act | Biometric prompt, integrity check, balance fetch |
| Deferred | After first interaction / idle | Analytics, attribution, chat SDK, marketing modules |
| On demand | When the feature is opened | Investing, card controls, statements, rewards |

Most teams find that the critical path is much smaller than what currently runs, and most "features" belong in the bottom two tiers. They stay in the app; they just stop costing anything at launch.

**3. Parallelize the work that can't be deferred.** Run security checks, the session refresh and the balance fetch concurrently instead of one after another. Show the cached last-known balance (clearly marked as stale) while the fresh one loads. This is a common pattern, but check it with compliance first.

**4. Address perceived speed separately from measured speed.** A skeleton screen that appears at 800ms and fills in by 2s *feels* closer to the competitor than a splash screen that sits for 2s. Don't use this to cover up a slow app, but don't ignore it either. Customers compare against what they experience, not against a stopwatch.

**5. Build guardrails so it doesn't regress.** Set a startup budget for each tier, enforce it in CI with automated launch benchmarks, and require that any new SDK or module say which tier it runs in before it can merge.

## The real trade-offs (some exist)

- **Security vs. speed**: Some integrity checks can run in parallel or just before sensitive actions instead of at launch. Others can't move. That decision belongs to security and compliance, not the performance team.
- **Data freshness vs. speed**: Showing a cached balance is faster, but it creates a risk of misleading the customer. You need rules about how stale it can be and how that's shown.
- **Analytics completeness**: Deferring analytics init can lose some launch events. Usually that's an acceptable cost, but product owners should agree to it explicitly.

These are the honest constraints. "Remove the feature" usually isn't one of them.

## Questions the team should answer before the next fix

- What's in the first 500ms of a trace right now, and who owns each piece?
- How exactly were the competitors' 1.5s numbers measured, and what's on screen at that point?
- Which startup steps are required by a security or regulatory obligation, and which are there out of habit?
- What share of sessions are cold starts, and on which devices?
- Which of the fixes that "removed features" could have been done as deferral instead? Revisit those first. You may be able to get the speed gains back without losing the features.

## Bottom line

A 4s to roughly 1.5–2s improvement is realistic for most fintech apps **without removing any features**, as long as the work is about *when* things initialize rather than *whether* they exist. If the team keeps finding that speed means cutting features, the cause is how startup is architected, not a real conflict between speed and features. Start with a trace and the tier classification. Most of the remaining decisions follow from those two steps.
