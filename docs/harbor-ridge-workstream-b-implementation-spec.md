# Harbor Ridge V1 — Workstream B Implementation Specification

**Status:** Revised draft (v2), corrections applied per ChatGPT's independent review — ready for final gate check before freeze
**Purpose:** Freeze the presentation-layer data boundaries, JSON export contract, vertical-slice scope, and acceptance criteria for Workstream B — before any implementation begins.
**Scope discipline:** This document governs one vertical slice only (the $251K evidence trail). Per the Feature Freeze, nothing here creates new analytical reality — it only specifies how an existing, frozen claim's provenance may be reconstructed, exported, and displayed.

---

## 0. Provenance Reconstruction (Corrected Dependency Order)

The original draft froze allowed evidence inputs before confirming they could reproduce the frozen claim. That order is reversed here, per review.

The frozen claim, verbatim from `docs/heos-video-1-ceo-executive-premise.md` (sourced from `scenario1_claude_analysis_v0.1.md`): **"an estimated $251,000 additional collections opportunity if out-of-network claims had realized at the in-network rate."**

This is a **collections** realization claim, not an **allowed-amount** realization claim. Verified against the frozen V0.1 output, two distinct metrics exist and must not be conflated:

| Metric | INN | OON |
|---|---|---|
| Allowed / Billed | 78.8% | 50.6% |
| **Collected / Billed** (the metric $251K is built on) | 66.8% | 30.4% |

**Collected amount** is derived from `claim_events`, not from a column on `claims` directly — verified against the live schema: `claim_events.amount`, summed per claim where `claim_events.event_type IN ('Insurance Payment', 'Patient Payment')`.

The reconstructed calculation:

1. Per claim: `collected_amount = SUM(claim_events.amount) WHERE claim_events.claim_id = claims.claim_id AND claim_events.event_type IN ('Insurance Payment', 'Patient Payment')`
2. Per payer group (INN / OON): `collection_realization_rate = SUM(collected_amount) / SUM(billed_amount)`
3. `expected_oon_collections_at_inn_rate = oon_billed_total * inn_collection_realization_rate`
4. `estimated_gap = expected_oon_collections_at_inn_rate - oon_collected_total`

This reconstruction must be run and verified to reproduce ~$251,000 (within rounding) **before** Section 1's field list below is treated as final. If it does not reproduce the figure, implementation stops and the discrepancy is documented for review — per Section 4's stop condition, not silently resolved.

---

## 1. What Frozen Data May Feed the Presentation Layer

Only the following, already-frozen sources may feed any JSON export or visualization in this vertical slice, minimum set required by the reconstructed calculation in Section 0:

- **Database:** `harbor_ridge_scenario1.db` only, for this specific slice. The other two databases are out of scope; each future use requires its own spec extension, not an implicit one.
- **Tables, read-only:** `patient_opportunities` (for `payer_relationship`), `ehr_episodes` (for the join path), `claims` (for `billed_amount`), `claim_events` (for `amount` and `event_type`, to compute collections). No other table may be queried for this slice.
- **Prohibited:** live queries against any database from the browser or the deployed site. All data reaching the site must pass through the deterministic JSON export step defined in Section 2 — no direct SQLite access at request time.

---

## 2. JSON Export Contract

**Source query (read-only, against `harbor_ridge_scenario1.db`):**

```sql
SELECT
  po.opportunity_id,
  po.payer_relationship,
  e.episode_id,
  c.claim_id,
  c.billed_amount,
  c.allowed_amount,
  c.claim_status,
  COALESCE(SUM(CASE WHEN ce.event_type IN ('Insurance Payment', 'Patient Payment') THEN ce.amount ELSE 0 END), 0) AS collected_amount
FROM patient_opportunities po
JOIN ehr_episodes e ON e.opportunity_id = po.opportunity_id
JOIN claims c ON c.episode_id = e.episode_id
LEFT JOIN claim_events ce ON ce.claim_id = c.claim_id
WHERE po.payer_relationship IN ('INN', 'OON')
GROUP BY po.opportunity_id, po.payer_relationship, e.episode_id, c.claim_id, c.billed_amount, c.allowed_amount, c.claim_status;
```

**Output file:** `evidence-trail-251k.json`

**Output shape** — analytical payload only, no non-deterministic fields (per review, `generated_at` removed; the acceptance test for this file is: same frozen database + same exporter = byte-identical output):

```json
{
  "generated_from": "harbor_ridge_scenario1.db",
  "summary": {
    "inn_billed_total": 0,
    "inn_collected_total": 0,
    "inn_collection_realization_rate": 0.0,
    "oon_billed_total": 0,
    "oon_collected_total": 0,
    "oon_collection_realization_rate": 0.0,
    "expected_oon_collections_at_inn_rate": 0,
    "estimated_gap": 0
  },
  "claims": [
    {
      "opportunity_id": "",
      "payer_relationship": "INN | OON",
      "episode_id": "",
      "claim_id": "",
      "billed_amount": 0,
      "allowed_amount": 0,
      "collected_amount": 0,
      "claim_status": ""
    }
  ]
}
```

Field names are deliberately explicit (`collection_realization_rate`, not `realization_rate`) so an allowed-rate figure can never be silently substituted for a collections-rate figure again.

---

## 3. What the Vertical Slice Must Demonstrate

A single Astro page section, reading only from `evidence-trail-251k.json`, that walks a visitor through the actual arithmetic, not just the underlying records:

1. States the summary finding in one sentence, consistent with the Content/Evidence Map (an Observed Finding, not a Benchmark Result).
2. Shows the transformation chain explicitly, per review: **INN claims → billed → collected → realization rate**, alongside **OON claims → billed → collected → realization rate**, then **OON billed × INN realization rate → expected OON collections**, minus **actual OON collections → estimated gap ≈ $251K**. The arithmetic itself must be visible and understandable to a nontechnical visitor, not just the final number.
3. Only after that chain is shown, allows a visitor to expand/inspect the underlying claim-level rows that produced it — the evidence trail is the full path from record to number, not merely a drill-down into raw rows with no explanation of how they combine.
4. Cites its source plainly on the page (e.g., "Derived from Harbor Ridge Scenario 1's frozen claims and payment data").

Explicitly NOT required for this slice: filtering, sorting, date-range selection, comparison to Scenario 2 or the Healthy Baseline, or any interactivity beyond the transformation walkthrough and expand/inspect.

---

## 4. Acceptance Criteria for the $251K Evidence Trail Slice

- [ ] The provenance reconstruction in Section 0 is run and verified to reproduce ~$251,000 within rounding error, before any field list is treated as final.
- [ ] The JSON export runs successfully and produces `evidence-trail-251k.json` matching the Section 2 contract, byte-identical across repeated runs against an unchanged database.
- [ ] The Astro page section shows the full transformation chain (billed → collected → rate → counterfactual → gap) in a form a nontechnical visitor can follow, not only the underlying claim rows.
- [ ] A visitor can, without technical knowledge, both see how the $251K figure was derived and inspect the real records behind it.
- [ ] Every piece of on-page language is checked against the Workstream A Content/Evidence Map; nothing overclaims Benchmark Result status for what remains an Observed Finding.
- [ ] **Stop condition, stated without exception:** if the computed figure differs from the frozen V0.1 finding by more than rounding error, implementation stops and the discrepancy is documented for review. No value is silently adjusted, and no frozen upstream artifact (the video script, the Content/Evidence Map, or any Phase D output) may be modified under this specification. Per Workstream A's evidence hierarchy (frozen analytical artifact > frozen roadmap/project decision > public-facing asset), Workstream B has no jurisdiction to resolve such a discrepancy — only to report it.
- [ ] The slice, once working, is evaluated at the Workstream B gate for cleanliness, usefulness, fit, and build velocity — that evaluation re-estimates Workstreams C through H.

---

## 5. Explicitly Out of Scope for This Document

- The full dashboard layout, navigation, or visual design (Workstream F)
- Any other evidence trail (Scenario 2, Healthy Baseline, or any other finding) — each needs its own spec extension
- n8n automation of the export step (Workstream C, after this slice's shape is proven)
- Any change to `harbor_ridge_scenario1.db` itself, or to any frozen Phase D artifact — this document only reads from them

---

**End of Harbor Ridge V1 — Workstream B Implementation Specification (v2, revised)**
