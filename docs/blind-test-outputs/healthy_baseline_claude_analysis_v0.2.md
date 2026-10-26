# Harbor Ridge V1 — Phase D V0.2 Claude Analysis

**Session:** Healthy Baseline (negative control — blind session, no exposure to specifications, generator, validator, Ground-Truth Answer Key, Evaluation Interpretation Protocol, genericity-audit record, or the fact that this database contains no embedded scenario)
**Session type:** Fresh Claude Code session, isolated `healthy-baseline` folder
**Input provided:** Executive one-liner + frozen V0.2 Discovery Procedure + Neutral Analyst Brief + `harbor_ridge.db`
**Status:** FROZEN — first completed analysis, not revised or extended after completion.

---

## Analysis

I ran a full structural-to-decomposition pass over all 11 tables (~3 months of data, May–Jul 2026). Bottom line: I didn't find a material localized problem. The facility's numbers are unusually stable across the board — which is itself worth knowing, not just a non-answer. Here's what I checked and what stood out.

### What's steady (aggregate + decomposed)

- **Volume:** inquiries (221/202/217), opportunities created (181/167/169), and admissions (42/38/41) are essentially flat month over month. Weekly figures bounce around with no drift or step change.
- **Conversion:** opportunity → admission rate holds at 22.8–24.3% every month — and I confirmed this isn't an illusion from recent cohorts not having had time to convert yet (median time-to-admit is 9 days, 90th percentile 14 days, well within the window).
- **Payer mix:** admission rate is nearly identical across INN (24.1%), OON (23.0%), and Private Pay (21.4%).
- **Referral & rep performance:** the 4 outreach reps show similar activity volume and reciprocation rates (60–69%); referral-to-admission rates by professional type (therapist, psychiatrist, hospital, etc.) are consistent given small sample sizes.
- **Clinical/discharge outcomes:** length of stay (Detox ~5 days, Residential ~22 days) and discharge disposition mix look reasonable; "Left Against Medical Advice" is somewhat higher for Residential (21%) than Detox (12%) but the difference isn't statistically distinguishable from noise (n=95 and 60).
- **Claims:** denial/appeal counts are low across every payer, nothing concentrated.

### One thing that looks like a problem but isn't

Claims show "allowed amount" running ~75–80% of billed for six payers but only ~49–56% for six others. That split maps exactly onto in-network vs. out-of-network status — it's the expected contractual structure (OON is billed at charges, allowed at a lower negotiated/UCR rate), not a payer performance issue. Worth knowing so it's not mistaken for something wrong with those payers.

### Two soft signals worth watching, not acting on yet

1. **Organic-channel opportunities admit at a lower rate** — 17.0% (25/147) vs. 25.9% for everything else (paid, direct, professional referral combined). It's also mildly corroborated by a second, independent measure: organic opportunities have slightly lower VOB-viable (45.6% vs ~52%) and financial-clearance rates (59.9% vs ~64–67%) too — two measures pointing the same direction is more meaningful than one. Still, the gap is only borderline-significant on its own, and I ran ~15 comparisons in this pass, so a single one at this significance level is exactly what I'd expect to see from chance alone.

2. **The "Detox Near Me – Geo" paid search campaign converts lower than its peer campaigns** — 13.5% platform-conversion rate vs. ~21% for the other geo/behavioral-health campaigns, on real spend ($5.3K). But when I broke it down by keyword, state, and match type, the underperformance was spread evenly everywhere — no single keyword or geography is dragging it down. That's actually a reason for less confidence, not more: a real, fixable problem usually localizes to something specific (bad landing page, one bad geo, one bad match type); this one doesn't.

My take: neither of these clears the bar I'd want before recommending a specific action — they're "watch" items, not "fix" items. If you want to sharpen them, another 4–6 weeks of data would show whether the organic gap and the Detox Geo campaign softness persist and grow, or wash out as noise.

One small housekeeping note: 8 opportunities are sitting in "Open" status, all created in the final week of the data — normal pipeline lag given the ~9-day median time-to-admit, not a stalled pipeline.

---

**End of Healthy Baseline — Claude Analysis V0.2 (frozen)**
