# Harbor Ridge V1 — Phase D V0.2 Claude Analysis

**Scenario:** 2 (blind session — no exposure to specifications, generator, validator, Ground-Truth Answer Key, Evaluation Interpretation Protocol, or genericity-audit record)
**Session type:** Fresh Claude Code session, isolated `scenario-2` folder
**Input provided:** Executive one-liner + frozen V0.2 Discovery Procedure + Neutral Analyst Brief + `harbor_ridge_scenario2.db`
**Status:** FROZEN — first completed analysis, not revised or extended after completion.
**Intervention note:** The initial terminal display of this session's response rendered with corrupted/garbled formatting (merged words, a broken table) due to a terminal display issue, not an analytical problem. Per the Run Manifest's Intervention Rule (Section 8), a purely technical export request was made to the same session — asking it to write its own already-delivered response verbatim to a file — with no analytical content requested, changed, or added. This document reflects that clean file export.

---

## Analysis

Here's what I found after working through the database — structural mapping, aggregate baselines, then systematic decomposition across payer, channel, referral source, clinical, and financial dimensions.

### The big picture: mostly on track

Across ~3 months (May–Jul 2026):

- 1,534 acquisition touches → 738 inquiries → 582 patient opportunities → 124 admissions (21.3% admit rate)
- Admit rate is essentially flat month-over-month: 21.8% / 21.2% / 21.0%
- Payer mix (INN 55%, OON 36%, Private Pay 9%) and financial clearance rates hold steady over time
- Claims: $2.10M billed, $1.27M allowed, $943K collected from insurance, $227K from patients — denial rate is only 6/178 claims (3.4%), spread thin across payers with no payer showing a denial count large enough to be more than a coin flip
- Clinical side (length of stay, discharge disposition mix, LAMA rate ~16%, LOC transitions) looks proportionate across payer types and levels of care — no red flags
- Referral rep performance (4 reps) and reciprocation rates are all in a normal, tight band

I checked all of this specifically because a stable aggregate can hide a concentrated problem — and in every one of these areas, the categories didn't diverge from each other or from the whole in a way that survives a sample-size check.

### What stands out: one campaign has quietly broken

"Behavioral Health - Non-Brand" (a Google Ads Paid Search campaign) shows a real, sustained conversion collapse:

| Month | Touches | Conversions | Conv. rate | Cost/lead |
|---|---:|---:|---:|---:|
| May | 54 | 10 | 18.5% | $155 |
| June | 61 | 6 | 9.8% | $302 |
| July | 47 | 5 | 10.6% | $295 |

Every other Paid Search campaign either held steady or improved over the same window — this isn't a market-wide seasonality effect. A few things make this more than noise:

- **It's broad-based within the campaign** — all four ad groups and all three match types (Exact, Phrase, Broad) declined together, on the same single landing page the whole time. That points to something at the campaign level (bid strategy, budget pacing, targeting, or an account-side change around late May), not one bad keyword.
- **It's not a tracking artifact** — I checked whether the platform's conversion flag matched actual linked inquiries, and they're 1:1. The drop is real lost inquiries, not a measurement glitch.
- **Spend didn't drop** — cost stayed flat (~$1,500–1,800/mo) while output halved, so cost-per-lead roughly doubled and has stayed there for two consecutive months.

I'd call this suggestive-to-established: the pattern is persistent and internally consistent, but the monthly volumes (5–10 conversions) are individually small, so I'd treat "why" as unresolved rather than proven. It's worth someone checking the Google Ads account directly for that campaign (bid changes, budget caps, disapprovals, Quality Score) rather than concluding from this data alone.

### What I checked and ruled out

Referral volume per outreach rep (one rep, Priya Anand, has lower raw referral count, but it's spread evenly across her accounts with no single account failing — reads as normal variation, not a problem). Payer-level claim denials, discharge disposition by payer, and admit rate by acquisition channel/influence type all came back flat — no localized pattern cleared the bar.

### Bottom line

The facility's core funnel and financials look healthy and stable. The one thing worth your attention is that one paid-search campaign has been running at roughly half its earlier efficiency for two months running while spend hasn't been adjusted down — that's the one lever I'd pull on this week.

---

**End of Scenario 2 — Claude Analysis V0.2 (frozen)**
