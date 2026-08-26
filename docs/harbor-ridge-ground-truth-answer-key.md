# Harbor Ridge V1 Ground-Truth Answer Key

**Version:** 1.0\
**Status:** Final Candidate for Human Review\
**Purpose:** Canonical answer key for evaluating independent analysis of
the two frozen Harbor Ridge V1 hidden-failure scenarios\
**Baseline:** `harbor_ridge.db`\
**Scenario 1:** `harbor_ridge_scenario1.db`\
**Scenario 2:** `harbor_ridge_scenario2.db`

------------------------------------------------------------------------

## 1. Purpose and Evaluation Rule

This document records what was intentionally embedded, what evidence a
correct analysis should recover, and what executive diagnosis that
evidence supports. It should be frozen **before** Claude or another
analytical model sees either scenario dataset.

The model under evaluation should not receive this answer key, the
scenario specifications, generator logic, validators, or validation
outputs before completing its independent analysis.

The governing discipline is:

``` text
Observed facts
→ Supported interpretation
→ Executive diagnosis
→ Bounded hypotheses / investigation
```

Actual observations below use the frozen real-seed validation results.
Theoretical values are labeled as such when needed to explain design
intent, validation anchoring, or small-sample behavior.

------------------------------------------------------------------------

# Scenario 1 --- Paid-Search Inquiry-Quality Deterioration

## 2. What Was Embedded

Scenario 1 is a localized deterioration in Google Ads non-brand inquiry
quality. The affected campaigns are:

  ID           Campaign
  ------------ -------------------------------
  `CMP-1002`   Behavioral Health - Non-Brand
  `CMP-1003`   Detox Near Me - Geo
  `CMP-1005`   Family Crisis - Non-Brand

Healthy Google comparisons are `CMP-1001` (Behavioral Health - Brand)
and `CMP-1004` (Residential Treatment - Geo). Microsoft Ads, Organic,
Professional Referral, Local, Direct, and Meta are not intentionally
degraded.

An affected opportunity is defined exactly by:

``` sql
SELECT po.*
FROM patient_opportunities po
JOIN acquisition_touches at
  ON po.originating_touch_id = at.touch_id
WHERE at.platform = 'Google Ads'
  AND at.campaign_id IN ('CMP-1002','CMP-1003','CMP-1005');
```

`arrival_channel = 'Paid Search'` alone is not sufficient.

The embedded mechanism is:

``` text
Affected Google campaigns
→ OON payer mix rises
→ financial-verification success falls
→ poor VOB / financial-clearance outcomes rise
→ Opportunity → Admission conversion falls
→ fewer downstream EHR episodes and claims
```

Top-of-funnel traffic is not intentionally collapsed. All non-financial
funnel stages remain healthy.

## 3. Scenario 1 Actual Real-Seed Evidence

`SCENARIO_1_SEED = 20260826`. Structural integrity and reproducibility
passed.

### Admission conversion

  Month     Opportunities   Admitted      Actual
  ------- --------------- ---------- -----------
  May                  25          8   **32.0%**
  June                 24          3   **12.5%**
  July                 38          3    **7.9%**

Realized May is unusually strong versus the designed healthy control of
about 22.8%, so the validator uses theoretical May as the causal anchor.
Against that anchor, June deteriorates **10.3pp** and July **14.9pp**.

### Payer drift

  Month             OON share
  ------- -------------------
  May       **52.0%** (13/25)
  June      **45.8%** (11/24)
  July      **60.5%** (23/38)

Against theoretical May OON of 35%, July is **+25.5pp**. The 60.5%
realization is 0.5pp above the specification's approximate 60% narrative
ceiling. This was reviewed and accepted as a minor seed-level
imperfection rather than retuned.

### VOB and financial quality

  Metric                        May    June        July
  ------------------------- ------- ------- -----------
  Poor VOB outcome            29.2%   40.0%   **64.0%**
  Not Financially Cleared     36.0%   58.3%   **73.7%**

July Poor VOB Outcome Rate is **+34.8pp** versus May. July Not
Financially Cleared is **+37.7pp** versus May.

These are among the strongest realized clues to the embedded failure.

### Top-of-funnel context

Affected-campaign inquiries are **32 → 31 → 50** for May, June, July.
Mean affected-campaign touch cost is **\$30.11 → \$29.05 → \$32.49**.
July is +7.9% versus May.

June's cost signal does not match its intended modest increase. It is an
accepted secondary-signal imperfection, not a separate failure.

### Internal comparisons

  Group                     May admission conversion           July    Change
  ----------------------- -------------------------- -------------- ---------
  Unaffected Google                      8.3% (n=24)   25.0% (n=20)   +16.7pp
  Microsoft Ads                         20.0% (n=15)    20.0% (n=5)     0.0pp
  Professional Referral                 19.4% (n=31)   20.0% (n=25)    +0.6pp

The cohorts are noisy but do not reproduce the engineered
affected-campaign collapse.

Large-N mechanism verification converged to the frozen design:
May/June/July Opportunity → Admission was 22.63%/18.49%/10.97%, and OON
share was 34.96%/43.17%/54.90%. These verify implementation but are
**not evidence available to an analyst examining only the database**.

## 4. Scenario 1 Evidence Trail

A correct analysis should follow:

``` text
acquisition_touches
  touch_id, platform, campaign_id, campaign_name, cost
        ↓
patient_opportunities
  originating_touch_id, payer_relationship,
  vob_outcome, admission_financial_status, admission_status
        ↓
ehr_episodes
  opportunity_id, episode_relationship, admission_datetime
        ↓
claims / claim_events
```

`inquiries` provides inquiry volume and channel context.

The critical segmentation is:

``` text
month
× campaign
× payer_relationship
× vob_outcome
× admission_financial_status
× admission_status
```

The primary evidence should emerge in `patient_opportunities` after
joining to `acquisition_touches`: affected campaigns become financially
worse and convert less often. EHR and claims are downstream
confirmation, not the source of the failure.

## 5. Scenario 1 Correct Executive Diagnosis

> **Admissions is not the primary constraint. A subset of Google Ads
> campaigns is generating progressively less financially viable Patient
> Opportunities, particularly through worsening OON mix and lower
> financial-verification success.**

Minimum passing diagnosis:

> **A campaign-specific paid-search quality problem exists upstream of
> Admissions, evidenced by deteriorating payer/financial quality and
> lower admission conversion in the affected Google campaigns.**

A response that only says "Google Ads declined" is incomplete. A
response that only says "Admissions declined" misses the hidden failure.

A correct analysis should **not** diagnose Admissions competence,
Microsoft Ads, Professional Referral, RCM, clinical operations, or
identity resolution as the primary embedded cause.

------------------------------------------------------------------------

# Scenario 2 --- Professional-Outreach Quality Deterioration

## 6. What Was Embedded

Scenario 2 is a rep-specific deterioration in professional-outreach
effectiveness centered on **Alicia Ferreira's owned portfolio of 14
professional accounts**.

Healthy internal comparison reps are Marcus Webb, Priya Anand, and Devon
Castillo.

The affected opportunity cohort is:

``` sql
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

The cohort is defined by `professional_accounts.owner_rep_id`, not
merely `outreach_activities.outreach_rep_id`.

The intended mechanism is:

``` text
Alicia-owned portfolio
→ outreach activity remains healthy
→ relationship / referral effectiveness weakens
→ referral volume remains superficially healthy
→ fewer referrals become Patient Opportunities
→ OON + Private Pay share falls
→ financial viability worsens
→ referral-derived admission conversion falls
```

## 7. Scenario 2 Actual Real-Seed Evidence

`SCENARIO_2_SEED = 20260827`. The mandatory 500,000-draw-per-month
mechanism gate passed every target within ±0.25pp before the real-seed
database was evaluated.

### Surface activity

Alicia-owned activities are **25 → 31 → 22**. Referral events are **15 →
17 → 14**.

Neither activity nor referral-event volume collapses. That is
diagnostically important.

### Reciprocity

Actual reciprocity is:

**60.0% → 71.0% → 54.5%**

This seed does **not** produce a clean monotonic decline even though the
mechanism targets 70% → 55% → 40%. The cohort is small.

Therefore, an independent analyst should **not be required to report a
perfectly monotonic reciprocity decline** to receive credit. July
weakness is a clue to be interpreted with stronger downstream evidence.

### Referral → Opportunity linkage

  Month              Link rate
  ------- --------------------
  May       **100.0%** (15/15)
  June       **76.5%** (13/17)
  July       **78.6%** (11/14)

The monthly path is noisy, but both June and July are materially below
May while referral-event volume remains broadly stable.

### Economic compatibility

OON + Private Pay among Alicia-attributable linked opportunities:

  Month     OON + Private Pay
  ------- -------------------
  May        **46.7%** (7/15)
  June       **38.5%** (5/13)
  July       **27.3%** (3/11)

This realized sequence is cleanly directional.

### Linked Opportunity → Admission

  Month     Admitted / linked   Conversion
  ------- ------------------- ------------
  May                    4/15   **26.67%**
  June                   2/13   **15.38%**
  July                   1/11    **9.09%**

Against theoretical May 22.7682%, June deterioration is **7.38pp** and
July **13.68pp**.

The pooled three-month realized rate is **17.95% (7/39)** versus a
theoretical pooled target of 18.7877%.

### Referral Event → Admission yield

  Month     Admissions / events        Yield
  ------- --------------------- ------------
  May                      4/15   **26.67%**
  June                     2/17   **11.76%**
  July                     1/14    **7.14%**

The pooled three-month realized yield is **15.22% (7/46)** versus a
theoretical pooled target of 14.7731%.

These pooled outcomes are important because Alicia's monthly cohorts are
tiny.

### Healthy comparison portfolio

Marcus + Priya + Devon:

  Metric                        May        July
  ------------------------- ------- -----------
  Reciprocity                 82.1%       67.8%
  Referral link rate          91.7%       86.8%
  OON + Private Pay           41.2%       32.4%
  Opportunity → Admission     14.7%   **20.6%**

The healthy comparison portfolio contains ordinary variation but does
not reproduce Alicia's engineered downstream admission collapse.

Other acquisition channels also remain broadly stable: Google Ads 27.5%
→ 22.2%, Microsoft Ads 25.0% → 23.1%, Organic 17.9% → 25.0%.

Large-N verification produced May/June/July link rates of
88.9710%/79.9770%/67.9420%, Linked Opportunity → Admission of
22.8445%/19.0170%/13.6322%, and Event → Admission of
20.3250%/15.2092%/9.2620%. Again, these establish implementation
fidelity but are not evidence exposed to an independent analyst.

## 8. Scenario 2 Evidence Trail

Canonical affected-opportunity path:

``` text
outreach_reps
        ↓
professional_accounts
        ↓
professional_referrals
        ↓
patient_opportunities
        ↓
ehr_episodes
        ↓
claims / claim_events
```

Canonical activity path:

``` text
outreach_reps
        ↓
professional_accounts
        ↓
outreach_activities
```

Relevant fields include:

-   `outreach_reps.rep_name`, `active_flag`
-   `professional_accounts.owner_rep_id`
-   `outreach_activities.activity_timestamp`, `reciprocated_flag`
-   `professional_referrals.professional_account_id`, `opportunity_id`,
    `referral_timestamp`
-   `patient_opportunities.originating_referral_id`,
    `payer_relationship`, `vob_outcome`, `admission_financial_status`,
    `admission_status`
-   `ehr_episodes.opportunity_id`, `episode_relationship`,
    `admission_datetime`

The critical segmentation is:

``` text
month
× professional-account owner
× activity
× reciprocity
× referral event
× opportunity linkage
× payer_relationship
× financial outcome
× admission_status
```

A correct analysis should recognize that activity remains present while
the downstream value produced by Alicia's portfolio deteriorates.

## 9. Scenario 2 Correct Executive Diagnosis

> **Professional outreach is not failing because the team stopped
> working. One rep-owned portfolio is producing less business value
> despite sustained or slightly increasing activity, indicating
> deterioration in relationship effectiveness and referral quality
> rather than an activity-volume problem or an Admissions problem.**

Core lesson:

> **Activity metrics are not necessarily outcome metrics.**

Minimum passing diagnosis:

> **A rep-specific professional-outreach effectiveness problem is
> centered on Alicia Ferreira's owned portfolio: activity remains
> present, but referral linkage, economic quality, and downstream
> admission yield deteriorate.**

The database does **not** establish that Alicia is newly hired, that she
replaced an experienced relationship manager, or that employee turnover
caused the deterioration. Those are Ground Truth/context facts not
encoded in the schema.

A responsible analysis may hypothesize a change in
relationship-management effectiveness or portfolio stewardship, but it
may not present the replacement-rep narrative as an observed fact.

------------------------------------------------------------------------

# Cross-Scenario Evaluation Standard

## 10. What a Strong Analysis Must Do

A strong analysis should:

1.  **Localize the failure correctly.** Scenario 1 resolves to specific
    Google campaigns; Scenario 2 resolves to Alicia's owned portfolio.
2.  **Distinguish volume from quality.** Neither failure is
    fundamentally a simple activity-volume collapse.
3.  **Follow relational evidence.** Upstream acquisition/referral
    evidence must be joined to Patient Opportunities and downstream
    admissions.
4.  **Use comparison groups.** Internal controls distinguish localized
    deterioration from facility-wide failure.
5.  **Identify the correct causal layer.** Scenario 1 is paid-search
    opportunity quality/financial viability. Scenario 2 is
    relationship/referral effectiveness and quality.
6.  **Respect uncertainty.** Small monthly cohorts, especially in
    Scenario 2, should not be overinterpreted.
7.  **Separate fact from hypothesis.** Unsupported organizational causes
    must not be promoted to facts.
8.  **Translate findings into executive language.** The answer should
    identify where leadership should investigate first and why.

## 11. Known Real-Seed Imperfections

### Scenario 1

Two minor accepted imperfections:

-   July OON share = **60.5%**, marginally above the approximate 60%
    narrative ceiling.
-   June mean affected-campaign cost = **-3.5% vs. May**, rather than
    the intended modest increase.

Neither changes the embedded diagnosis.

### Scenario 2

Small-cohort noise creates non-monotonic monthly surface signals:

-   Reciprocity: **60.0% → 71.0% → 54.5%**
-   Referral linkage: **100.0% → 76.5% → 78.6%**

These do not invalidate the scenario. Pooled outcomes and large-N
verification confirm the intended mechanism. An analyst should be
rewarded for recognizing uncertainty rather than forced to overstate
noisy monthly trends.

## 12. Canonical Scenario Signatures

Scenario 1:

``` text
Specific Google campaigns
→ OON-heavy opportunity mix
→ worse VOB / financial clearance
→ lower admission conversion
→ fewer downstream episodes / claims
```

Scenario 2:

``` text
Alicia-owned professional portfolio
→ activity remains present
→ referral effectiveness weakens
→ economic compatibility deteriorates
→ referral-derived admission yield falls
```

## 13. Freeze Rule

Once reviewed and approved:

1.  save this as the canonical Ground Truth artifact;
2.  commit it to the repository;
3.  do not revise it merely because Claude later discovers or misses
    something;
4.  run Claude without exposing this answer key;
5.  compare Claude's independent findings against this frozen document
    afterward.

The benchmark must not move after the answer is known.

## 14. Source-of-Truth Hierarchy

1.  `docs/harbor-ridge-scenario-1-specification.md`
2.  `docs/harbor-ridge-scenario-2-specification.md`
3.  `scenario1_validation_results.txt`
4.  `scenario2_validation_results.txt`
5.  frozen baseline schema and generation rules

Where theoretical specification targets and realized values differ, the
**realized database value is the observation**. Theoretical values are
labeled separately when needed for design or validation context.

------------------------------------------------------------------------

**End of Harbor Ridge V1 Ground-Truth Answer Key --- Version 1.0**
