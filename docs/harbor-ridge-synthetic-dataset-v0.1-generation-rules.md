# Harbor Ridge Synthetic Dataset V0.1 Generation Rules

**Version:** 1.0  
**Status:** Final / Approved  
**Canonical format:** SQLite  
**Period modeled:** 3 months  
**Generator:** Seeded Python script  
**Purpose:** Produce a healthy baseline Harbor Ridge operating dataset before any diagnostic scenario is embedded.

> **Design principle:** These rules distinguish canonical Harbor Ridge assumptions already established in the project from V0.1 generator assumptions chosen for implementation. Synthetic design choices must not quietly become represented as industry facts.

---

## 1. Time Window

Recommended operating period:

**May 1, 2026 through July 31, 2026**

Financial events may continue through:

**August 31, 2026**

This provides three complete operating months while allowing May, June, and July claims to have different degrees of financial maturity.

Use a fixed observation date:

`2026-08-31`

---

## 2. Reproducibility

Use one fixed random seed for V0.1:

`SEED = 20260825`

Running the generator twice with the same seed should produce the **same database**.

Later scenario variants can use the same baseline seed plus explicit scenario parameters. This distinguishes changes caused by scenarios from random noise.

---

## 3. Baseline Operating Volume and Funnel Attrition

Harbor Ridge's domain-realism target is approximately **40 completed admissions per month**.

Recommended V0.1 baseline:

| Measure | Monthly Target | 3-Month Target |
|---|---:|---:|
| Inquiries | ~210 | ~630 |
| Patient Opportunities | ~175 | ~525 |
| Completed Admissions | ~40 | ~120 |

This yields approximately:

- **83% Inquiry → Patient Opportunity**
- **23% Patient Opportunity → Completed Admission**
- **19% Inquiry → Completed Admission**

These inquiry/opportunity volumes are **generator assumptions**, not industry benchmarks. They are chosen so the synthetic funnel reflects the multiple documented attrition points in the Harbor Ridge operating model rather than forcing an unrealistically clean conversion rate.

Allow approximately **±5–10% random variation** in inquiries and opportunities month-to-month.

Completed admissions should remain tighter:

**38–42 per month**, centered on 40.

### 3.1 Inquiry → Patient Opportunity

The reduction from approximately 210 inquiries to 175 Patient Opportunities reflects pre-admissions factors such as:

- Multiple family-member contacts resolving to one Patient Opportunity
- Duplicate or repeated inquiries
- Non-patient inquiries
- Contacts that never become a legitimate Patient Opportunity

This is distinct from downstream clinical/admissions attrition.

### 3.2 Patient Opportunity → Completed Admission

A plausible monthly opportunity cohort is:

| Stage | Approx. Pass Rate | Remaining from 175 | Representative Attrition |
|---|---:|---:|---|
| Patient Opportunity created | — | 175 | Starting cohort |
| Clinical / Safety fit | 88% | 154 | Clinically inappropriate; higher/lower LOC required |
| Financial Verification | 68% | 105 | Financially infeasible; non-viable coverage |
| Readiness | 78% | 82 | Patient unwilling / not ready |
| Admission Decision | 90% | 74 | Not accepted / alternate disposition |
| Scheduling / Contact | 88% | 65 | Unable to contact; delayed decision |
| Logistics | 88% | 57 | Transportation / family / logistical failure |
| Arrival | 74% | 42 | Went elsewhere; no-show; changed mind |
| Paperwork / Completed Admission | 95% | ~40 | Final refusal / incomplete intake |

This produces approximately:

**40 admissions ÷ 175 opportunities ≈ 23% Opportunity → Admission**

and:

**40 admissions ÷ 210 inquiries ≈ 19% Inquiry → Admission**

The generator should allow natural month-to-month variation rather than forcing exactly 40 admissions every month.

---

## 4. Payer Mix

Target admitted payer mix:

- **55% INN Commercial**
- **35% OON Commercial**
- **10% Private Pay**

Enforce this most tightly at the **completed-admission cohort**, because that is the population actually occupying Harbor Ridge.

For approximately 40 monthly admissions:

- 22 INN
- 14 OON
- 4 Private Pay

Opportunity-level payer mix may fluctuate modestly around the same baseline.

**Tolerance:** ±3 percentage points across the full three-month admitted cohort.

Use entirely fictitious carrier names.

### 4.1 Healthy-Baseline Payer Behavior

Harbor Ridge V0.1 intentionally keeps **INN, OON, and Private Pay admission-conversion rates within a relatively narrow range** so payer relationship does not become an embedded failure in the healthy baseline.

This is deliberate.

The `payer_relationship` field remains analytically active in V0.1 because it should affect:

- Payer-mix reporting
- VOB behavior
- Financial-clearance behavior
- Allowed-amount variability
- Collection timing
- Financial maturity

Similar baseline conversion rates do **not** mean the payer categories behave identically.

Recommended directional differences:

- **INN:** more predictable VOB and collection behavior
- **OON:** somewhat more VOB uncertainty, more At-Risk Admissions, and greater reimbursement / collection variability
- **Private Pay:** no VOB, different financial-clearance behavior, and generally shorter collection timing

More pronounced payer-driven conversion deterioration is reserved for the later diagnostic scenario layer rather than being embedded in the healthy baseline.

**Baseline payer differences should be economically visible but not operationally pathological.**

---

## 5. Acquisition Behavior

The canonical acquisition environment includes:

- Google Ads
- Organic / SEO
- Professional referrals
- Hospital / crisis referrals
- Alumni / patient referrals
- Interventionists
- Microsoft Ads
- Direct / Brand
- Meta

For V0.1, map these into the **existing frozen schema**, not new channel structures.

Recommended baseline inquiry mix:

- Paid Search: ~35%
- Organic: ~20%
- Professional Referral: ~20%
- Local: ~10%
- Direct: ~10%
- Other: ~5%

This is a **generator assumption**, not the marketing-budget allocation.

Within Paid Search:

- ~90% Google Ads
- ~10% Microsoft Ads

Within Paid Social:

- Meta only

Organic and Local should remain distinct where the schema allows it.

---

## 6. Marketing Budget

Canonical healthy controllable allocation:

- 45% Google Ads
- 20% Professional Outreach / BD
- 15% SEO / Organic Content
- 10% Events / Community / Referral Development
- 5% Microsoft Ads
- 5% Meta

### V0.1 Implementation Note

The frozen database does not contain one common cross-channel marketing-spend table. `acquisition_touches.cost` can store digital costs, but `outreach_activities` does not contain a cost field, and Events / Community spending is not separately represented.

**Do not reopen the schema solely for this reason.**

For V0.1, treat the 45/20/15/10/5/5 allocation as a **generator configuration and validation benchmark**, reported in the generator's summary/manifest. Digital spend lives in SQLite where the existing schema supports it.

If later implementation demonstrates that full cross-channel spend must exist inside SQLite to answer the defined executive question, that may qualify as a genuine implementation-discovered schema gap.

---

## 7. Calls vs. Web Forms

Calls and web forms must remain distinct.

Baseline generator assumption:

- **60% Call**
- **40% Web Form**

Allow modest channel-specific variation.

Phone inquiries may populate:

- Tracking number
- Call duration

Web forms may populate:

- Landing page

Do not populate irrelevant fields merely to avoid `NULL`.

---

## 8. Inquiry Initiators and Identity

Recommended baseline:

- Patient: ~55%
- Loved One: ~40%
- Professional Referral Source: ~5%

Most opportunities should have one inquiry.

A meaningful minority should have multiple inquiries:

- ~15% have 2 inquiries
- ~3–5% have 3 inquiries

Example:

`Mom → Dad → Patient → one HRO`

Baseline identity resolution should generally work:

- Confirmed: ~85–90%
- Probable: ~7–10%
- Possible: small minority
- Unmatched: rare

The explicit Identity Loss scenario comes later.

**Do not deliberately degrade identity resolution in the baseline.**

---

## 9. VOB Behavior

For insured opportunities:

- Most should receive a VOB
- Some opportunities should terminate before VOB
- VOB viability should be materially better in the healthy baseline than it becomes under the later paid-search failure scenario

Private Pay normally uses:

`vob_submitted_flag = 0`

`vob_outcome = NULL`

while still being eligible for:

`Financially Cleared`

The frozen conditional VOB constraints must never be violated.

The generator should generate valid business states intentionally rather than relying on SQLite to reject invalid combinations after insertion.

---

## 10. Admission Logic

The baseline must preserve the canonical control condition:

> Admissions remains reasonably effective when supplied with clinically appropriate, financially viable or acceptable-risk, ready patients.

Because the frozen schema does not explicitly store every clinical-fit/readiness stage, encode this condition through the observable outcomes already available.

Completed admissions should overwhelmingly originate from:

- `Financially Cleared`
- A smaller share of `At-Risk Admission`

and essentially never from:

- `Not Financially Cleared`

Do not create a baseline where every channel has wildly different downstream conversion performance.

Healthy baseline channel behavior should be fairly stable.

Later scenarios should change **input quality**, not admissions competence.

---

## 11. EHR Episode Generation

Harbor Ridge has:

- 8 Detox beds
- 24 Residential beds

Supported pathways include:

- Detox → Residential → Discharge
- Detox → External Discharge
- Residential → Discharge

Recommended V0.1 generator assumptions:

- ~50% of admitted patients begin in Detox
- ~50% admit directly to Residential
- ~60% of Detox admissions transition to Residential

For approximately 40 admissions, this might create:

- 20 Detox initial episodes
- 20 Residential initial episodes
- 12 Residential LOC-transition episodes

or approximately **52 EHR episodes per month**.

These percentages are generator assumptions.

Every transition must obey:

`episode_relationship = LOC Transition`

and carry a valid:

`prior_episode_id`

Initial episodes must have:

`prior_episode_id = NULL`

---

## 12. Length of Stay

Create plausible variation rather than fixed lengths.

### Detox

- Typical: 3–7 days

### Residential

- Typical: 14–30 days

Include occasional shorter stays and early dispositions, but do not turn V0.1 into a clinical-outcomes simulation.

The purpose is to provide enough variation to support census, episode, claim, and revenue reasoning.

---

## 13. Claims

Every admitted EHR episode should normally generate at least one claim.

To prove the one-to-many architecture:

- ~85% of episodes → 1 claim
- ~15% → 2 claims

The split-claim minority gives SQL and later AI analysis genuinely relational data to reconstruct without making the entire dataset unnecessarily complex.

Claims must obey existing foreign-key constraints unless a later diagnostic scenario deliberately embeds Outcome-Linkage Loss.

---

## 14. Claim Events and Collections

Claims should generate realistic event histories.

Example simple paid claim:

`Submitted → Insurance Payment`

Example more complex claim:

`Submitted → Denial → Appeal → Insurance Payment`

Example patient-responsibility sequence:

`Insurance Payment → Patient Payment`

Example adjustment case:

`Insurance Payment → Adjustment`

Amounts and delays should contain variation.

Baseline financial behavior should differ directionally:

- INN: more predictable
- OON: greater reimbursement and collection variability
- Private Pay: generally shorter collection timing

Dollar values are **synthetic design assumptions**, not industry benchmarks.

---

## 15. Financial Maturity

Use the observation date to create natural maturity differences:

- **May admissions:** relatively mature
- **June admissions:** partially mature
- **July admissions:** materially less mature

Do not artificially force every July claim to be paid by August 31.

Pending claims are useful data, not generator failures.

---

## 16. Professional Referral Baseline

Before introducing referral deterioration, the professional pipeline should be healthy.

Recommended V0.1 assumptions:

- 4 active outreach reps
- ~40 professional accounts
- Several activities per rep/account over the three months
- Referral volume somewhat concentrated among stronger accounts, but not excessively
- Meaningful reciprocal activity
- Financially compatible referral mix

These counts are V0.1 generator assumptions.

The later diagnostic scenario may introduce replacement reps, superficially healthy activity, lower reciprocity/referral quality, and deteriorating payer compatibility.

---

## 17. Baseline Stability Rule

**V0.1 baseline must not already contain the hidden failures.**

Across May, June, and July before scenario mutation:

- Inquiry volume roughly stable
- Admission volume roughly stable
- Payer mix roughly stable
- Google inquiry quality roughly stable
- Professional referral quality roughly stable
- Admissions conversion among viable opportunities roughly stable

**Random noise: yes.**

**Intentional trend: no.**

This provides a clean substrate on which diagnostic scenarios can later be introduced deliberately.

---

## 18. Synthetic Identity / Privacy Rules

Everything must be fictional.

Use:

- Fabricated names
- `555` phone numbers
- `.example.test` email addresses/domains
- Fictional payer names
- Fictional professional practices
- No copied real patient records
- No actual PHI

The database must be unmistakably synthetic.

---

## 19. ID Generation

Use deterministic sequential IDs consistent with the frozen dictionary:

`CNT-000001`  
`INQ-000001`  
`HRO-000001`  
`TOUCH-000001`  
`REP-000001`  
`PRO-000001`  
`REF-000001`  
`ACT-000001`  
`KIPU-000001`  
`CLM-000001`  
`CEV-000001`

No UUID complexity for V1.

---

## 20. Insert Order

Because the model contains a legitimate circular attribution relationship, use the already-tested insertion strategy:

```text
Contacts
↓
Outreach Reps
↓
Professional Accounts
↓
Patient Opportunities
   originating IDs initially NULL
↓
Inquiries
↓
Acquisition Touches / Professional Referrals
↓
Update Patient Opportunities
   with originating_touch_id / originating_referral_id
↓
Outreach Activities
↓
EHR Episodes
↓
Claims
↓
Claim Events
```

This mirrors the Golden Thread insertion strategy already validated against the frozen SQLite schema.

---

# V0.1 Baseline Acceptance Criteria

Before declaring the generated baseline successful, require all of the following:

- Database generated successfully from a clean start
- Same seed produces the same dataset
- All 11 tables populated where appropriate
- `PRAGMA foreign_key_check` returns **zero violations**
- Existing schema constraints remain satisfied
- Approximately **40 admissions per month**
- Approximately **23% Patient Opportunity → Completed Admission**
- Approximately **19% Inquiry → Completed Admission**
- Three-month admitted payer mix approximately **55% INN / 35% OON / 10% Private Pay**
- Calls and forms both materially represented
- Multiple-inquiry opportunities exist
- Both Detox and Residential pathways exist
- LOC transitions exist and link correctly
- Multi-claim episodes exist
- Payment / adjustment histories exist
- Financial maturity differs naturally by cohort month
- Healthy baseline does **not** contain an intentional downward trend
- Synthetic-only identity conventions are respected

---

## V0.1 Scope Note

The full **45/20/15/10/5/5 controllable-marketing allocation** is a generator-level validation assumption for V0.1 because the frozen schema does not currently store all categories of non-digital spend in a common relational structure.

This limitation does **not** justify reopening the frozen schema unless implementation demonstrates that full cross-channel spend must exist relationally to answer the defined Harbor Ridge V1 executive question.

---

## Next Step

Once these rules are frozen and committed, proceed to:

**Step 2 — Build the baseline Python generator (`generate_synthetic_data.py`)**

The generator should implement this specification against the frozen Harbor Ridge SQLite schema without adding new fields or expanding V1 scope.

---

**End of Harbor Ridge Synthetic Dataset V0.1 Generation Rules — Version 1.0**
