# Harbor Ridge V1 — Phase D V0.2 Claude Analysis

**Scenario:** 1 (blind session — no exposure to specifications, generator, validator, Ground-Truth Answer Key, Evaluation Interpretation Protocol, or genericity-audit record)
**Session type:** Fresh Claude Code session, isolated `scenario-1` folder
**Input provided:** Executive one-liner + frozen V0.2 Discovery Procedure + Neutral Analyst Brief + `harbor_ridge_scenario1.db`
**Status:** FROZEN — first completed analysis, not revised or extended after completion. The session's closing offer to extend the analysis further was not accepted, per the Run Manifest's no-post-freeze-extension rule.

---

## Analysis

Ran a full structural, aggregate, and dimensional decomposition pass on the database (874 contacts, 530 patient opportunities, 152 EHR episodes, 173 claims, ~3 months of data, May–Jul 2026 with claims runoff into Aug). Here's what actually holds up versus what's just noise.

### Bottom line

Nothing in the core business is on fire. Aggregate admissions, payer mix, financial collections, and authorization management all look like normal operating variation. But there's one specific, well-corroborated personnel finding, and a couple of small-sample payer signals worth watching but not acting on yet.

### Established finding: Marcus Webb (outreach rep) is underperforming on two independent measures

- **Outreach engagement:** His reciprocated-contact rate is 60.0% (45/75 activities) vs. 73.8–76.7% for the other three reps. This holds up across all three months, both inbound and outbound activity, and every activity type (call, email, meeting, lunch, tour, presentation) — it's not one bad week or one bad channel.
- **Referral conversion:** Referrals from professional accounts he owns convert to admission at 12.0% (3/25 matched referrals) vs. 19.4–39.3% for peers — and it's spread across 7 of his 10 accounts (not one problem account dragging the average).
- **Ruled out as confounds:** his account portfolio mix (professional type: social workers, interventionists, etc.) closely matches Devon Castillo's, who's a top performer; his activity volume and referral volume are in line with peers; his data-quality mix (human-entered vs. system-observed) matches everyone else.

Two independent measures, same direction, same person, persistent over time, no confound found — this clears the bar for a real finding, not noise. Worth a direct conversation with him or a look at what he's doing differently in the field.

### Suggestive, not established: two payers with rough numbers, but samples too small to act on

- **Keystone Wellness Plan:** lowest admit rate of any payer (9.7%, 3/31) and 2 of those 3 admitted patients left AMA (67%).
- **Redwood Mutual:** admit rate 15.6% (5/32), and 4 of 7 admitted patients left AMA (57%).

Both are directionally consistent (low admit + high AMA among the few who do get in), but the AMA numerator sits on a subset of only 3 and 7 patients respectively — well under the ~30 needed to trust a rate. Worth tracking as these payers accumulate more volume, not worth restructuring anything around yet.

### Checked and came back clean (the useful negatives)

- **Authorization management:** zero episodes ran past their insurance authorization end date, out of 142 checked. No hidden write-off risk there.
- **Claim denials:** only 6 of 173 claims denied, spread thin across payers with no concentration.
- **Financially-cleared-but-not-admitted leak** (180 of 289 cleared opportunities didn't admit): this looked like a big number at first, but the ~35–44% conversion rate is essentially flat across month, payer type, and lead source — it's a structural funnel rate, not a localized problem to fix.
- **Detox vs. Residential length of stay** (5.0 vs 22.3 days) and discharge disposition mix look internally consistent, no red flags by payer or month.
- **Weekly admission volume** is choppy (as expected for a 32-bed facility) but shows no declining trend — the apparent "zero-admit weeks" in a naive week-by-created-date cut turned out to be a timing artifact (opportunity creation date vs. actual admission date aren't the same event), not a real pattern.

### What I'd actually watch going forward

1. Marcus Webb's numbers — this is the one lever with real, actionable signal.
2. Keystone and Redwood volumes — once each has 30+ admitted patients, re-check the AMA rate.
3. Nothing else in this dataset currently clears the bar for concern.

---

**End of Scenario 1 — Claude Analysis V0.2 (frozen)**
