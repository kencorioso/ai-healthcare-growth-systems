# Harbor Ridge V1 Scenario 2 Specification
## Professional-Outreach Quality Deterioration

**Version:** 1.0  
**Status:** Frozen Specification  
**Scenario database:** `harbor_ridge_scenario2.db`  
**Baseline control:** `harbor_ridge.db`  
**Scenario seed:** `SCENARIO_2_SEED = 20260827`  
**Implementation model:** Scenario-aware causal generation, not post-hoc mutation

---

## 1. Scenario Objective

Scenario 2 models a rep-specific deterioration in professional-outreach effectiveness.

A replacement relationship manager continues generating healthy-looking outreach activity, but the portfolio progressively produces:

- weaker reciprocal professional relationships,
- fewer referral events that become legitimate Patient Opportunities,
- fewer economically attractive OON / Private Pay opportunities,
- poorer financial-verification performance,
- fewer completed admissions.

The intended executive diagnosis is:

> **Professional outreach is not failing because the team stopped working. One rep-owned portfolio is producing less business value despite sustained or slightly increasing activity, indicating deterioration in relationship effectiveness and referral quality rather than an activity-volume problem or an Admissions problem.**

The core lesson is:

> **Activity metrics are not necessarily outcome metrics.**

No single field should announce the failure. The diagnosis must emerge from relational analysis across outreach activity, professional relationships, referral events, Patient Opportunities, financial verification, and admissions.

---

## 2. Affected and Unaffected Split

### 2.1 Affected Rep

**Alicia Ferreira** is the Scenario 2 affected rep.

In the frozen healthy-baseline realization, Alicia owns the largest professional-account portfolio:

| Rep | Professional Accounts |
|---|---:|
| Alicia Ferreira | 14 |
| Priya Anand | 13 |
| Devon Castillo | 11 |
| Marcus Webb | 2 |

Her portfolio also produces the largest number of linked professional referrals in the current healthy-baseline realization.

Alicia is therefore the preferred Scenario 2 affected rep for two reasons:

1. **Adequate sample size.** Her portfolio is the largest available rep-owned cohort.
2. **Isolation.** She represents only part of professional outreach, leaving the majority of professional accounts under healthy internal comparison reps.

Scenario Ground Truth will treat Alicia as the replacement relationship manager who inherited a mature relationship portfolio after an experienced relationship manager departed.

The frozen schema contains no hire-date, tenure, predecessor, or replacement-status field.

Therefore, an analytical system may observe deterioration in Alicia's portfolio, but it may not claim from the database alone that she is a replacement employee.

That organizational-history explanation belongs in Ground Truth/context, not in the observed data.

### 2.2 Healthy Internal Comparison Group

The healthy comparison group is the pooled portfolio owned by:

- **Marcus Webb**
- **Priya Anand**
- **Devon Castillo**

All three remain governed by healthy-baseline behavior throughout May, June, and July.

Their:

- outreach activity,
- reciprocity,
- referral-event effectiveness,
- payer composition,
- financial-verification behavior,
- referral-to-admission performance

remain unchanged except for normal seeded variation.

The canonical internal comparison is therefore:

```text
Alicia Ferreira-owned accounts
              vs.
Marcus + Priya + Devon-owned accounts
```

This provides the same analytical control that the unaffected Google campaigns provided in Scenario 1:

> **Is the deterioration facility-wide, channel-wide, or localized to a particular rep-owned portfolio?**

Because Marcus owns only two accounts, the pooled three-rep cohort is the canonical healthy comparison group. Individual-rep views may still be used for exploratory analysis.

---

## 3. Exact Definition of the Affected Cohort

Scenario 2 is defined at the **professional-account owner level**.

An affected attributable Patient Opportunity is:

> A `patient_opportunities` row whose `originating_referral_id` references a `professional_referrals` row whose `professional_account_id` references a `professional_accounts` row owned by Alicia Ferreira.

Canonical SQL:

```sql
SELECT po.*
FROM patient_opportunities po
JOIN professional_referrals pr
  ON po.originating_referral_id = pr.referral_id
JOIN professional_accounts pa
  ON pr.professional_account_id = pa.professional_account_id
JOIN outreach_reps r
  ON pa.owner_rep_id = r.outreach_rep_id
WHERE r.rep_name = 'Alicia Ferreira';
```

This definition is authoritative for both Scenario 2 generation and validation.

It is intentionally based on:

```text
professional_accounts.owner_rep_id
```

rather than:

```text
outreach_activities.outreach_rep_id
```

because the affected object is Alicia's owned relationship portfolio, not merely activities personally logged by Alicia.

If another rep records an activity against an Alicia-owned account, that account remains part of the affected cohort.

### Canonical Affected Activity Cohort

```sql
SELECT oa.*
FROM outreach_activities oa
JOIN professional_accounts pa
  ON oa.professional_account_id = pa.professional_account_id
JOIN outreach_reps r
  ON pa.owner_rep_id = r.outreach_rep_id
WHERE r.rep_name = 'Alicia Ferreira';
```

---

## 4. Scenario Timeframe

### May 2026

**Healthy control**

Alicia's portfolio behaves according to healthy-baseline parameters.

### June 2026

**Emerging deterioration**

Activity remains healthy, but:

- reciprocity begins weakening,
- fewer referral events become captured Patient Opportunities,
- OON / Private Pay mix declines,
- financial viability begins weakening.

### July 2026

**Established deterioration**

The portfolio continues to look active at the surface, but downstream relationship and referral value have materially deteriorated.

The intended temporal pattern is:

```text
May
Healthy relationship portfolio
        ↓
June
Activity still healthy
Reciprocity and referral effectiveness weakening
        ↓
July
Activity still healthy
Relationship quality materially weaker
Fewer viable referral opportunities
Fewer admissions
```

---

## 5. Outreach Activity Parameters

The healthy generator produces approximately 3–10 outreach activities per account over the three-month period, averaging approximately 2.2 activities per account-month, with a healthy reciprocity probability near 70%.

Scenario 2 makes the affected portfolio's monthly behavior explicit:

| Month | Target Activities / Account | Relative Activity | Reciprocity |
|---|---:|---:|---:|
| May | 2.20 | 1.00x | 70% |
| June | 2.30 | 1.05x | 55% |
| July | 2.40 | 1.10x | 40% |

The contrast is intentional:

> **Activity slightly increases while reciprocity materially declines.**

Other outreach-activity behavior remains healthy:

- Direction remains approximately 70% Outbound / 30% Inbound.
- Activity-type distribution remains unchanged.
- Evidence-class behavior remains unchanged.
- Alicia remains `active_flag = 1`.

There is no synthetic field such as `bad_rep_flag`, `relationship_quality_score`, or equivalent shortcut.

---

## 6. Referral-Event Volume and Opportunity-Linkage Parameters

Scenario 2 explicitly separates:

**referral activity volume**

from:

**referral effectiveness**.

This distinction is central to the hidden-failure design.

### 6.1 Referral-Event Intensity

For Alicia-owned accounts:

| Month | Referral Events / Account |
|---|---:|
| May | 0.90 |
| June | 0.95 |
| July | 1.00 |

Surface referral-event volume therefore remains stable to slightly increasing.

The scenario must not be created through an obvious referral-count collapse.

### 6.2 Referral Event → Patient Opportunity Link Rate

Not every professional referral event resolves into a legitimate captured Patient Opportunity. The frozen schema permits `professional_referrals.opportunity_id = NULL`.

Scenario 2 uses:

| Month | Referral → Opportunity Link Rate |
|---|---:|
| May | 89% |
| June | 80% |
| July | 68% |

Expected linked Patient Opportunities per affected account:

#### May

\[
0.90 \times 0.89 = 0.801
\]

#### June

\[
0.95 \times 0.80 = 0.760
\]

#### July

\[
1.00 \times 0.68 = 0.680
\]

Therefore, surface referral events increase modestly:

```text
0.90 → 0.95 → 1.00
```

while productive linked-opportunity yield declines:

```text
0.801 → 0.760 → 0.680
```

Across Alicia's 14 accounts, the theoretical monthly linked-opportunity counts are approximately:

| Month | Expected Linked Opportunities |
|---|---:|
| May | 11.21 |
| June | 10.64 |
| July | 9.52 |

This small affected cohort is explicitly accounted for in the Scenario 2 validation methodology.

---

## 7. Referral Payer-Mix Parameters

Scenario 2 represents deterioration in the economic compatibility of professional referrals by progressively reducing the proportion of OON and Private Pay opportunities.

For Alicia-attributable linked Patient Opportunities:

| Month | INN | OON | Private Pay | OON + Private Pay |
|---|---:|---:|---:|---:|
| May | 55% | 35% | 10% | **45%** |
| June | 62% | 30% | 8% | **38%** |
| July | 70% | 24% | 6% | **30%** |

The intended signal is:

> **The affected professional portfolio progressively produces fewer OON / Private Pay opportunities, consistent with declining economic compatibility of professional referrals.**

This deliberately differs from Scenario 1, where affected paid-search traffic became increasingly OON-heavy.

---

## 8. Financial-Verification Parameters

For Alicia-attributable opportunities only:

| Month | INN | OON | Private Pay |
|---|---:|---:|---:|
| May | 70% | 64% | 68% |
| June | 60% | 50% | 55% |
| July | 45% | 30% | 40% |

These rates represent deterioration within payer categories in addition to the changing payer composition.

All non-financial funnel stages remain at healthy-baseline rates.

---

## 9. Unchanged Funnel Stages

Scenario 2 must not alter the following seven funnel stages:

| Stage | Pass Rate |
|---|---:|
| Clinical / Safety | 88% |
| Readiness | 78% |
| Admission Decision | 90% |
| Scheduling / Contact | 88% |
| Logistics | 88% |
| Arrival | 74% |
| Paperwork | 95% |

Their combined downstream pass-through factor is:

\[
0.88 \times 0.78 \times 0.90 \times 0.88 \times 0.88 \times 0.74 \times 0.95
\]

\[
= 0.3363105208
\]

or approximately:

**33.63%**

Therefore:

\[
\text{Linked Opportunity → Admission}
=
\text{Weighted Financial-Verification Pass Rate}
\times
33.63\%
\]

---

## 10. Full Funnel Math

### 10.1 May Control

Payer mix:

- INN: 55%
- OON: 35%
- Private Pay: 10%

Financial-verification pass rates:

- INN: 70%
- OON: 64%
- Private Pay: 68%

Weighted financial-verification pass rate:

\[
(0.55 \times 0.70)
+
(0.35 \times 0.64)
+
(0.10 \times 0.68)
\]

\[
=0.385+0.224+0.068
\]

\[
=0.677
\]

**Weighted financial pass = 67.70%**

Apply unchanged downstream factor:

\[
0.677 \times 0.3363105208
=
0.227682
\]

### May Linked Opportunity → Admission

**22.7682%**

Now include referral linkage:

\[
0.89 \times 0.227682
=
0.202637
\]

### May Referral Event → Admission Yield

**20.2637%**

---

### 10.2 June Emerging Deterioration

Payer mix:

- INN: 62%
- OON: 30%
- Private Pay: 8%

Financial-verification pass rates:

- INN: 60%
- OON: 50%
- Private Pay: 55%

Weighted financial-verification pass rate:

\[
(0.62 \times 0.60)
+
(0.30 \times 0.50)
+
(0.08 \times 0.55)
\]

\[
=0.372+0.150+0.044
\]

\[
=0.566
\]

**Weighted financial pass = 56.60%**

Apply unchanged downstream factor:

\[
0.566 \times 0.3363105208
=
0.190352
\]

### June Linked Opportunity → Admission

**19.0352%**

Difference from May:

\[
22.7682\%-19.0352\%
=
3.7330pp
\]

Now include referral linkage:

\[
0.80 \times 0.190352
=
0.152282
\]

### June Referral Event → Admission Yield

**15.2282%**

Difference from May:

\[
20.2637\%-15.2282\%
=
5.0355pp
\]

---

### 10.3 July Established Deterioration

Payer mix:

- INN: 70%
- OON: 24%
- Private Pay: 6%

Financial-verification pass rates:

- INN: 45%
- OON: 30%
- Private Pay: 40%

Weighted financial-verification pass rate:

\[
(0.70 \times 0.45)
+
(0.24 \times 0.30)
+
(0.06 \times 0.40)
\]

\[
=0.315+0.072+0.024
\]

\[
=0.411
\]

**Weighted financial pass = 41.10%**

Apply unchanged downstream factor:

\[
0.411 \times 0.3363105208
=
0.138224
\]

### July Linked Opportunity → Admission

**13.8224%**

Difference from May:

\[
22.7682\%-13.8224\%
=
8.9458pp
\]

Now include referral linkage:

\[
0.68 \times 0.138224
=
0.093992
\]

### July Referral Event → Admission Yield

**9.3992%**

Difference from May:

\[
20.2637\%-9.3992\%
=
10.8645pp
\]

---

## 11. Mathematical Summary

| Month | Referral → Opportunity | Weighted Financial Pass | Linked Opp → Admission | Event → Admission | Opp Conversion Δ vs. May |
|---|---:|---:|---:|---:|---:|
| May | 89% | 67.70% | **22.7682%** | **20.2637%** | Control |
| June | 80% | 56.60% | **19.0352%** | **15.2282%** | **−3.7330pp** |
| July | 68% | 41.10% | **13.8224%** | **9.3992%** | **−8.9458pp** |

Scenario 2 therefore contains multiple related deterioration signals:

```text
Reciprocity declines
        +
Referral → Opportunity linkage declines
        +
Economic / financial quality declines
        ↓
Referral-derived admissions decline
```

while activity and referral-event volume remain superficially healthy.

---

## 12. Three-Month Pooled Outcome Math

Because Alicia owns only 14 professional accounts, the expected linked-opportunity cohort is approximately 9–11 records per month.

Monthly admission-conversion results are therefore inherently noisy.

Scenario 2 must validate Sections G and H using pooled three-month checks **in addition to**, not instead of, the monthly theoretical trend checks.

### 12.1 Pooled Linked Opportunity → Admission

Expected linked-opportunity exposure per affected account:

| Month | Expected Linked Opportunities / Account |
|---|---:|
| May | 0.801 |
| June | 0.760 |
| July | 0.680 |

The pooled conversion is weighted by expected linked-opportunity exposure:

\[
\frac{
(0.801 \times 0.227682)
+
(0.760 \times 0.190352)
+
(0.680 \times 0.138224)
}{
0.801+0.760+0.680
}
\]

Numerator:

\[
0.182374+0.144668+0.093992
=
0.421034
\]

Denominator:

\[
0.801+0.760+0.680
=
2.241
\]

Therefore:

\[
0.421034 / 2.241
=
0.187877
\]

### Pooled Theoretical Linked Opportunity → Admission

**18.7877%**

This is the canonical three-month mechanism target for the pooled Section G check.

---

### 12.2 Pooled Referral Event → Admission Yield

Monthly referral-event intensity:

| Month | Referral Events / Account |
|---|---:|
| May | 0.90 |
| June | 0.95 |
| July | 1.00 |

The pooled yield is weighted by monthly referral-event intensity:

\[
\frac{
(0.90 \times 0.202637)
+
(0.95 \times 0.152282)
+
(1.00 \times 0.093992)
}{
0.90+0.95+1.00
}
\]

Numerator:

\[
0.182373+0.144668+0.093992
=
0.421033
\]

Denominator:

\[
2.85
\]

Therefore:

\[
0.421033 / 2.85
=
0.147731
\]

### Pooled Theoretical Referral Event → Admission Yield

**14.7731%**

This is the canonical three-month mechanism target for the pooled Section H check.

The near-identical numerators in Sections 12.1 and 12.2 are expected because both calculations represent the same expected admissions. Their denominators differ because one measures admissions per linked opportunity and the other measures admissions per referral event.

---

## 13. Evidence Trail

Scenario 2 must leave a distributed relational evidence trail.

### 13.1 `outreach_reps`

Relevant fields:

- `outreach_rep_id`
- `rep_name`
- `active_flag`

#### Tell

Alicia remains active.

This table alone does not reveal the failure.

---

### 13.2 `professional_accounts`

Relevant fields:

- `professional_account_id`
- `owner_rep_id`
- `professional_type`

#### Tell

Establishes portfolio ownership and permits comparison between Alicia-owned accounts and the healthy pooled portfolio.

No deterioration is visible here by itself.

---

### 13.3 `outreach_activities`

Relevant fields:

- `professional_account_id`
- `outreach_rep_id`
- `activity_timestamp`
- `activity_type`
- `direction`
- `reciprocated_flag`

#### Tell

Activity counts remain stable or increase.

At the same time, `reciprocated_flag` progressively deteriorates across Alicia-owned accounts.

This creates the first meaningful clue:

> **Effort is no longer translating into equivalent relationship engagement.**

---

### 13.4 `professional_referrals`

Relevant fields:

- `referral_id`
- `professional_account_id`
- `opportunity_id`
- `referral_timestamp`
- `attribution_confidence`

#### Tell

Referral-event volume remains superficially healthy, but an increasing share of affected referral events does not resolve to a Patient Opportunity.

The analyst should compare:

```text
all referral events
        vs.
referrals with opportunity_id IS NOT NULL
```

---

### 13.5 `patient_opportunities`

Relevant fields:

- `originating_referral_id`
- `payer_relationship`
- `vob_submitted_flag`
- `vob_outcome`
- `admission_financial_status`
- `admission_status`

#### Tell

Among Alicia-attributable opportunities:

- OON + Private Pay share falls,
- financial-verification outcomes worsen,
- Not Financially Cleared opportunities increase,
- completed-admission conversion falls.

---

### 13.6 `ehr_episodes`

Relevant fields:

- `opportunity_id`
- `episode_relationship`
- `admission_datetime`

#### Tell

Fewer Alicia-attributable referrals ultimately generate Initial EHR episodes.

EHR mechanics themselves remain healthy.

---

### 13.7 `claims` and `claim_events`

These tables provide downstream confirmation only.

There should naturally be fewer claims attributable to Alicia's deteriorating portfolio because fewer referred patients admit.

RCM mechanics themselves must not deteriorate.

---

## 14. What Must Stay Unaffected

Scenario isolation is mandatory.

### 14.1 Healthy Outreach Portfolios

Marcus Webb, Priya Anand, and Devon Castillo remain healthy.

Their:

- activity levels,
- reciprocity,
- referral linkage,
- payer mix,
- financial verification,
- admission conversion

remain governed by healthy-baseline parameters.

---

### 14.2 Digital Acquisition

Do not intentionally mutate:

- Google Ads
- Microsoft Ads
- Meta
- Organic
- Local
- Direct

Scenario 1's paid-search deterioration must **not** be embedded into Scenario 2.

Scenario 2 represents professional-outreach deterioration independently.

---

### 14.3 Admissions Competence

Admissions remains healthy once supplied with an appropriate, financially viable or acceptable-risk, ready patient.

Do not degrade:

- readiness,
- admission decision,
- scheduling,
- logistics,
- arrival,
- paperwork.

---

### 14.4 Identity Resolution

Do not introduce Scenario 2 identity-resolution deterioration.

---

### 14.5 EHR / Clinical Operations

Do not alter:

- Detox / Residential mix,
- LOS assumptions,
- LOC-transition probability,
- transition-link integrity,
- discharge mechanics.

---

### 14.6 RCM

Do not alter:

- denial probability,
- appeal mechanics,
- claim-processing timing,
- payment timing,
- allowed-amount logic,
- write-off mechanics.

Any downstream financial decline attributable to Scenario 2 must originate upstream from deteriorating professional-referral effectiveness and quality.

---

### 14.7 Attribution Confidence

Do not intentionally degrade professional-referral attribution confidence.

Otherwise Scenario 2 would combine:

**Outreach Quality Loss**

with:

**Attribution Loss**

which would violate scenario isolation.

---

## 15. Code-Defined Generation Architecture

Scenario 2 must not be implemented through post-hoc mutation of completed baseline rows.

The generation sequence must preserve causal consistency.

Canonical conceptual architecture:

```text
Generate Outreach Reps
        ↓
Generate Professional Accounts
        ↓
Identify Alicia-owned affected portfolio
        ↓
For each month
        ↓
Generate outreach activity
using activity + reciprocity parameters
        ↓
Generate professional referral events
using monthly referral-event intensity
        ↓
Determine whether each referral event
resolves to a Patient Opportunity
using referral-linkage rate
        ↓
For linked referral events
assign Scenario 2 payer mix
        ↓
Apply Scenario 2 financial-verification rates
        ↓
Run unchanged remainder of funnel
        ↓
Finalize admission_status
        ↓
Generate EHR episodes only for actual admissions
        ↓
Generate claims and claim events
```

Non-professional opportunities must be generated independently using healthy-baseline logic.

Nothing should need to be "un-admitted" or repaired after downstream records have already been generated.

This ensures that relational consistency is preserved by construction.

---

## 16. Scenario Seed

Use:

```python
SCENARIO_2_SEED = 20260827
```

Requirements:

- fixed,
- documented,
- distinct from baseline `SEED`,
- distinct from `SCENARIO_1_SEED`,
- used specifically for Scenario 2 generation,
- reproducible within the same Python process,
- reproducible across independent SQLite builds.

Scenario output:

```text
harbor_ridge_scenario2.db
```

Scenario CSV export directory:

```text
data/csv_export_scenario2/
```

Changing Scenario 2 parameters must not alter the frozen baseline database or Scenario 1 database.

---

## 17. Scenario 2 Acceptance Criteria

Scenario 2 uses the sample-size-aware validation methodology established during Scenario 1.

For statistically sampled quantities:

> **Acceptance tolerance = max(specification tolerance floor, 2 × standard error).**

Sample-size adjustment may widen statistical acceptance bands where the realized cohort cannot support a tighter estimate.

It may **never** widen fixed narrative "too subtle" or "too obvious" ceilings.

### A. Structural Integrity and Reproducibility

Scenario 2 must pass:

- `PRAGMA foreign_key_check = 0`
- `PRAGMA integrity_check = ok`
- all 11 tables populated where appropriate
- VOB conditional integrity
- episode-relationship conditional integrity
- no dangling `prior_episode_id`
- same-process reproducibility
- independent database-to-database reproducibility using `SCENARIO_2_SEED`

Scenario effects do not excuse structural defects.

---

### B. Outreach Activity Remains Healthy

Affected portfolio targets:

| Month | Activities / Account |
|---|---:|
| May | 2.20 |
| June | 2.30 |
| July | 2.40 |

Acceptance:

- June total activity must be no more than **10% below May**.
- July total activity must be no more than **10% below May**.
- Neither June nor July may exceed **25% above May**.

Hard narrative ceiling:

> **Affected outreach activity may not collapse by more than 15%.**

---

### C. Reciprocity Deteriorates

Affected portfolio targets:

| Month | Reciprocity |
|---|---:|
| May | 70% |
| June | 55% |
| July | 40% |

Acceptance uses sample-size-aware bands around these targets.

Hard directional requirements:

- June reciprocity must be at least **8pp below theoretical May**.
- July reciprocity must be at least **20pp below theoretical May**.

Hard too-obvious floor:

- July reciprocity must remain **≥30%**.

The affected professional relationships must deteriorate materially without becoming virtually nonexistent.

---

### D. Referral Volume Looks Superficially Healthy

Affected portfolio referral-event intensity:

| Month | Events / Account |
|---|---:|
| May | 0.90 |
| June | 0.95 |
| July | 1.00 |

June and July referral-event counts should remain within a sample-size-aware band approximately equivalent to:

**±15% of May**

with a hard rule that neither month may fall more than:

**20% below May**

A major referral-count collapse would make Scenario 2 too easy to diagnose.

---

### E. Referral → Opportunity Effectiveness Deteriorates

Targets:

| Month | Link Rate |
|---|---:|
| May | 89% |
| June | 80% |
| July | 68% |

Acceptance uses sample-size-aware bands.

Hard directional requirements:

- June must be at least **5pp below theoretical May**.
- July must be at least **15pp below theoretical May**.

Hard too-obvious floor:

- July link rate must remain **≥55%**.

---

### F. Economic Compatibility Deteriorates

Affected Opportunity OON + Private Pay share:

| Month | Target |
|---|---:|
| May | 45% |
| June | 38% |
| July | 30% |

Acceptance uses sample-size-aware target bands.

Hard directional requirement:

- July OON + Private Pay share must be at least **10pp below theoretical May**.

Hard too-obvious floor:

- July OON + Private Pay share must remain **≥25%**.

Scenario 2 must not eliminate economically attractive professional referrals entirely.

---

### G. Linked Opportunity → Admission Deterioration

Theoretical monthly rates:

| Month | Theoretical Conversion | Deterioration vs. May |
|---|---:|---:|
| May | **22.7682%** | Control |
| June | **19.0352%** | **−3.7330pp** |
| July | **13.8224%** | **−8.9458pp** |

The exact theoretical deterioration centers are:

- June: **3.7330pp**
- July: **8.9458pp**

These exact values are the canonical band centers.

Per-month database checks must remain sample-size-aware and anchored to theoretical May.

Because the affected linked-opportunity cohort is expected to contain only approximately 9–11 records per month, monthly realization is **not sufficient on its own** to determine whether Scenario 2 is correctly implemented.

#### G.1 Pooled Three-Month Check

Expected linked-opportunity exposure per affected account:

- May: 0.801
- June: 0.760
- July: 0.680

The pooled theoretical Linked Opportunity → Admission rate is:

**18.7877%**

The realized three-month affected linked-opportunity cohort must be evaluated against this pooled target using a sample-size-aware tolerance.

This pooled check is **additional to**, not a replacement for, the monthly trend checks.

#### G.2 Hard Narrative Bounds

- July theoretical deterioration must remain **≥6pp** to avoid becoming too subtle.
- July theoretical deterioration must remain **≤15pp** to avoid becoming too obvious.

These mechanism-level difficulty bounds are fixed and may not be widened for sample size.

---

### H. Referral Event → Admission Yield

Theoretical monthly yields:

| Month | Event → Admission Yield | Deterioration vs. May |
|---|---:|---:|
| May | **20.2637%** | Control |
| June | **15.2282%** | **−5.0355pp** |
| July | **9.3992%** | **−10.8645pp** |

#### H.1 Pooled Three-Month Check

Monthly referral-event intensity:

- May: 0.90/account
- June: 0.95/account
- July: 1.00/account

The pooled theoretical Referral Event → Admission Yield is:

**14.7731%**

The realized three-month affected referral-event cohort must be evaluated against this pooled target using a sample-size-aware tolerance.

This pooled check is **additional to**, not a replacement for, the monthly trend checks.

#### H.2 Hard Narrative Bounds

- July deterioration **<7pp** = too subtle.
- July deterioration **>15pp** = too obvious.

These bounds are fixed and may not be widened for sample size.

---

### I. Healthy Comparison Portfolios Remain Stable

The pooled Marcus + Priya + Devon portfolio must remain healthy.

At minimum:

- reciprocity remains within sample-size-adjusted healthy tolerance of May,
- referral-link rate remains stable,
- OON + Private Pay share remains stable,
- Opportunity → Admission remains stable.

No engineered Scenario 2 deterioration may appear in the healthy comparison pool.

---

### J. Other Acquisition Channels Remain Stable

At minimum:

- Google Ads,
- Microsoft Ads,
- Organic

must show no intentionally engineered Scenario 2 deterioration.

Scenario 1 behavior must not appear in Scenario 2.

These channels provide cross-channel evidence that the failure is not a facility-wide Admissions problem.

---

### K. Large-N Mechanism Verification Must Pass Before Database Validation

Before the realized `SCENARIO_2_SEED` database is treated as authoritative evidence that Scenario 2 is implemented correctly, the Scenario 2 generator logic must pass an independent large-N convergence test.

This test is mandatory.

Use:

- an unrelated verification seed,
- **200,000–500,000 synthetic draws per month**,
- Scenario 2 payer-mix parameters,
- Scenario 2 financial-verification parameters,
- Scenario 2 referral-link probabilities,
- unchanged downstream funnel stages.

The purpose is to distinguish implementation defects from small-sample noise.

#### K.1 Referral → Opportunity Linkage Targets

| Month | Theoretical Target | Required Large-N Tolerance |
|---|---:|---:|
| May | 89.00% | ±0.25pp |
| June | 80.00% | ±0.25pp |
| July | 68.00% | ±0.25pp |

---

#### K.2 Linked Opportunity → Admission Targets

| Month | Theoretical Target | Required Large-N Tolerance |
|---|---:|---:|
| May | 22.7682% | ±0.25pp |
| June | 19.0352% | ±0.25pp |
| July | 13.8224% | ±0.25pp |

---

#### K.3 Referral Event → Admission Targets

| Month | Theoretical Target | Required Large-N Tolerance |
|---|---:|---:|
| May | 20.2637% | ±0.25pp |
| June | 15.2282% | ±0.25pp |
| July | 9.3992% | ±0.25pp |

---

#### K.4 Payer-Composition Targets

The large-N realization must converge to the following Scenario 2 payer composition:

| Month | INN | OON | Private Pay |
|---|---:|---:|---:|
| May | 55.00% | 35.00% | 10.00% |
| June | 62.00% | 30.00% | 8.00% |
| July | 70.00% | 24.00% | 6.00% |

**Every individual payer-share target must converge within ±0.25 percentage points.**

Therefore:

- May INN: 55.00% ±0.25pp
- May OON: 35.00% ±0.25pp
- May Private Pay: 10.00% ±0.25pp
- June INN: 62.00% ±0.25pp
- June OON: 30.00% ±0.25pp
- June Private Pay: 8.00% ±0.25pp
- July INN: 70.00% ±0.25pp
- July OON: 24.00% ±0.25pp
- July Private Pay: 6.00% ±0.25pp

No payer-composition target may be validated using a vague "close to target" standard.

---

#### K.5 Pooled Three-Month Targets

| Metric | Theoretical Target | Required Large-N Tolerance |
|---|---:|---:|
| Pooled Linked Opportunity → Admission | **18.7877%** | ±0.25pp |
| Pooled Referral Event → Admission | **14.7731%** | ±0.25pp |

---

#### K.6 Mechanism-Verification Rule

All major modeled rates, yields, pooled rates, and individual payer-composition shares listed in Section K must converge within:

**±0.25 percentage points**

of their theoretical targets.

If the large-N simulation does not converge within these tolerances, the implementation is incorrect.

The required response is:

> **Fix the generator before evaluating any realized Scenario 2 database seed.**

No:

- seed search,
- tolerance widening,
- small-sample explanation,
- validator exception,
- or manual database adjustment

may substitute for failure at the mechanism-verification stage.

The governing distinction is:

```text
Large-N failure
= implementation defect

Single-seed small-cohort deviation
= potentially sampling noise
```

---

## 18. Required Validation Order

Scenario 2 validation must proceed in the following order:

1. **Large-N mechanism verification**
2. **Structural integrity**
3. **Reproducibility**
4. **Surface activity and reciprocity checks**
5. **Referral linkage and payer-quality checks**
6. **Per-month linked-opportunity outcome checks**
7. **Pooled three-month Section G check**
8. **Pooled three-month Section H check**
9. **Healthy comparison-group checks**
10. **Hard too-subtle / too-obvious ceiling checks**

This order is intentional.

A noisy single-month realization involving approximately ten linked opportunities must not be treated as more authoritative than the mathematically verified underlying mechanism.

Large-N verification establishes that the generator is correct.

The realized database then establishes that the chosen Scenario 2 seed produces a usable, structurally sound, analytically detectable scenario.

---

## 19. Detectable but Not Cartoonishly Obvious

### Too Subtle

Scenario 2 is too subtle if:

- reciprocity moves less than approximately 10pp,
- referral linkage falls less than approximately 10pp,
- OON + Private Pay share falls less than approximately 10pp,
- July Linked Opportunity → Admission deterioration is less than 6pp,
- July Referral Event → Admission deterioration is less than 7pp,
- affected and healthy portfolios are analytically indistinguishable.

At that point, random variation can plausibly explain too much of the apparent failure.

### Too Obvious

Scenario 2 is too obvious if:

- outreach activity falls more than 15%,
- referral-event volume collapses more than 20%,
- reciprocity falls below 30%,
- referral → opportunity linkage falls below 55%,
- OON + Private Pay share falls below 25%,
- July Linked Opportunity → Admission deteriorates by more than 15pp,
- July Referral Event → Admission deteriorates by more than 15pp,
- healthy comparison reps deteriorate simultaneously.

That would turn the scenario into an obvious "bad rep" story rather than a hidden operational failure.

---

## 20. Target Analytical Difficulty

A superficial management review of:

```text
calls
meetings
lunches
visits
presentations
total outreach activities
total referral events
```

should reasonably suggest:

> **Professional outreach is still active.**

A careful analyst should need to examine:

```text
month
× professional-account owner
× outreach activity
× reciprocated_flag
× referral event
× opportunity linkage
× payer_relationship
× vob_outcome
× admission_financial_status
× admission_status
```

to identify the failure.

The intended analytical chain is:

```text
Alicia-owned portfolio
        ↓
Activity remains healthy / increases
        ↓
Reciprocity falls
        ↓
Referral events remain superficially healthy
        ↓
Fewer referral events become Patient Opportunities
        ↓
OON + Private Pay share falls
        ↓
Financial viability worsens
        ↓
Referral-derived admission conversion falls
```

Meanwhile:

```text
Marcus / Priya / Devon remain healthy
Digital acquisition remains healthy
Admissions remains healthy
Identity resolution remains healthy
EHR remains healthy
RCM remains healthy
```

That is the Scenario 2 signature.

---

## 21. Too-Obvious Ceiling Confirmation

The frozen parameters remain inside the intended difficulty envelope.

### Outreach Activity

May → July:

```text
2.20 → 2.40 activities/account
```

Activity increases slightly rather than collapsing.

### Reciprocity

```text
70% → 40%
```

This is a material 30pp deterioration but remains above the 30% hard lower bound.

### Referral → Opportunity Linkage

```text
89% → 68%
```

This is a 21pp deterioration but remains well above the 55% hard lower bound.

### Economic Payer Mix

OON + Private Pay:

```text
45% → 30%
```

This is a 15pp deterioration without eliminating economically attractive referrals.

### Linked Opportunity → Admission

```text
22.7682% → 13.8224%
```

Difference:

**−8.9458pp**

This remains below the 15pp too-obvious ceiling.

### Referral Event → Admission

```text
20.2637% → 9.3992%
```

Difference:

**−10.8645pp**

This is large enough to matter but remains distributed across several causal mechanisms.

No single parameter alone explains the full decline.

---

## 22. Output and Ground-Truth Boundary

Scenario 2 output:

```text
harbor_ridge_scenario2.db
```

Scenario 2 CSV exports:

```text
data/csv_export_scenario2/
```

The frozen healthy baseline remains:

```text
harbor_ridge.db
```

Scenario 1 remains independently generated as:

```text
harbor_ridge_scenario1.db
```

Scenario 2 must not contain Scenario 1's paid-search deterioration.

### Ground-Truth Boundary

Scenario Ground Truth may know that Alicia represents a replacement relationship manager following the loss of experienced professional-outreach personnel.

The analytical system may responsibly conclude from the data:

> **Alicia-owned professional accounts show deteriorating reciprocal engagement, referral effectiveness, economic compatibility, and downstream admission yield despite sustained outreach activity.**

It may reasonably hypothesize:

> **A change in relationship-management effectiveness or portfolio stewardship may explain the deterioration.**

But unless organizational-history context is separately supplied, the analytical system may not state as an observed fact that:

- Alicia is newly hired,
- Alicia replaced an experienced employee,
- experienced relationship managers departed,
- staffing turnover caused the deterioration.

Those facts are not encoded in the frozen relational schema.

This preserves the Harbor Ridge evidence discipline:

```text
Facts
→ Hypotheses
→ Investigations
→ Not Established
```

---

## 23. Freeze Status

Scenario 2 is frozen as:

**Professional-Outreach Quality Deterioration**

The specification now includes:

- one explicitly affected rep,
- three pooled healthy comparison reps,
- exact SQL attribution,
- staged May / June / July deterioration,
- explicit outreach-activity parameters,
- explicit reciprocity parameters,
- explicit referral-event parameters,
- explicit referral → opportunity linkage parameters,
- explicit payer-quality deterioration,
- explicit financial-verification deterioration,
- full downstream funnel math,
- exact monthly conversion and deterioration values,
- pooled three-month Section G mathematics,
- pooled three-month Section H mathematics,
- independent `SCENARIO_2_SEED`,
- code-defined causal generation architecture,
- distributed evidence trail,
- isolation requirements,
- sample-size-aware validation methodology,
- mandatory large-N mechanism verification,
- explicit ±0.25pp convergence tolerance for every large-N rate, yield, pooled metric, and payer-composition target,
- revised 10-step validation order,
- fixed too-subtle / too-obvious bounds,
- explicit Ground-Truth boundary.

**Canonical filename:**

`docs/harbor-ridge-scenario-2-specification.md`

**Status: FROZEN — ready for implementation.**
