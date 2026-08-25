Harbor Ridge V1 Scenario 1 Specification
Paid-Search Inquiry-Quality Deterioration
Version: Final Candidate for Review Scenario database: harbor_ridge_scenario1.db Baseline control: harbor_ridge.db Scenario seed: SCENARIO_1_SEED = 20260826 Implementation model: Scenario-aware generation, not post-hoc mutation


1. Scenario Objective
Scenario 1 models a localized deterioration in Google Ads non-brand inquiry quality.

Top-of-funnel paid-search activity remains broadly healthy, but a subset of Google Ads campaigns progressively generates a less financially viable Patient Opportunity mix. That deterioration flows through VOB and financial-clearance outcomes and ultimately lowers admissions.

The intended executive diagnosis is:

Admissions is not the primary constraint. A subset of Google Ads campaigns is generating progressively less financially viable Patient Opportunities, particularly through worsening OON mix and lower financial-verification success.

The scenario must require relational analysis to find. No single field should announce the failure.


2. Affected Campaigns
Scenario 1 applies only to these Google Ads campaigns:

Campaign ID
Campaign Name
CMP-1002
Behavioral Health - Non-Brand
CMP-1003
Detox Near Me - Geo
CMP-1005
Family Crisis - Non-Brand


The following Google Ads campaigns remain healthy and serve as internal comparison groups:

Campaign ID
Campaign Name
CMP-1001
Behavioral Health - Brand
CMP-1004
Residential Treatment - Geo


Microsoft Ads, Organic, Professional Referral, Local, Direct, and Meta remain unaffected by Scenario 1.


3. Definition of an Attributable Opportunity
For Scenario 1, an affected attributable opportunity is defined strictly as:

A patient_opportunities row whose originating_touch_id references an acquisition_touches row where platform = 'Google Ads' and campaign_id belongs to the Scenario 1 affected-campaign set.

Canonical SQL definition:

SELECT po.*

FROM patient_opportunities po

JOIN acquisition_touches at

  ON po.originating_touch_id = at.touch_id

WHERE at.platform = 'Google Ads'

  AND at.campaign_id IN ('CMP-1002', 'CMP-1003', 'CMP-1005');

This same definition must be used by both:

Scenario generation logic
Scenario validation logic

arrival_channel = 'Paid Search' alone is not sufficient to define Scenario 1 attribution.


4. Scenario Timeframe
The degradation is staged across the three-month operating window.
May 2026
Healthy control

Scenario 1 applies no degradation.
June 2026
Emerging deterioration

Payer quality and financial-verification performance begin to weaken, but the problem remains plausible as normal variation without deeper analysis.
July 2026
Established deterioration

The signal becomes materially detectable through campaign-level payer, VOB, financial-clearance, and admission analysis.

The intended pattern is:

May = healthy control

June = emerging signal

July = established failure


5. Revised Payer-Mix Parameters
For affected attributable opportunities only:

Month
INN
OON
Private Pay
May
55%
35%
10%
June
47%
43%
10%
July
35%
55%
10%


Interpretation:

May matches healthy baseline.
June begins shifting toward OON.
July reaches a material but still plausible OON-heavy mix.
OON never exceeds the approximately 60% upper bound established for avoiding an overly obvious synthetic failure.


6. Revised Financial-Verification Pass Rates
For affected attributable opportunities only:

Month
INN
OON
Private Pay
May
70%
64%
68%
June
60%
48%
62%
July
45%
22%
50%


These rates replace the previous Scenario 1 values.

All other funnel-stage pass rates remain exactly at healthy-baseline values.


7. Unchanged Funnel Stages
Scenario 1 must not alter the following seven stages:

Stage
Pass Rate
Clinical / Safety
88%
Readiness
78%
Admission Decision
90%
Scheduling / Contact
88%
Logistics
88%
Arrival
74%
Paperwork
95%


Their combined pass-through factor is:

0.88 × 0.78 × 0.90 × 0.88 × 0.88 × 0.74 × 0.95 = 0.3363105208

or approximately:

33.63%

Therefore:

Projected Opportunity → Admission

    = Weighted Financial Verification Pass Rate × 33.63%

This dilution factor must be preserved in implementation.


8. Full Scenario Funnel Math
8.1 May Control
Payer mix: 55% INN / 35% OON / 10% Private Pay Financial-verification pass rates: INN 70%, OON 64%, Private Pay 68%

Weighted financial-verification pass rate: (0.55 × 0.70) + (0.35 × 0.64) + (0.10 × 0.68) = 0.385 + 0.224 + 0.068 = 0.677

Weighted financial pass = 67.7%

Apply unchanged downstream factor: 0.677 × 0.3363105208 = 0.227682

Projected May Opportunity → Admission: 22.77% ≈ 22.8%

This aligns closely with the validated healthy baseline near 23%. May therefore functions as Scenario 1's internal control.
8.2 June Emerging Deterioration
Payer mix: 47% INN / 43% OON / 10% Private Pay Financial-verification pass rates: INN 60%, OON 48%, Private Pay 62%

Weighted financial-verification pass rate: (0.47 × 0.60) + (0.43 × 0.48) + (0.10 × 0.62) = 0.282 + 0.2064 + 0.062 = 0.5504

Weighted financial pass = 55.04%

Apply unchanged downstream factor: 0.5504 × 0.3363105208 = 0.185105

Projected June Opportunity → Admission: 18.51% ≈ 18.5%

Difference from May: 22.77% − 18.51% = 4.26 percentage points
June result
Projected deterioration: −4.3pp

This satisfies the Scenario 1 acceptance requirement that June be 4–12 percentage points below May. It also preserves the intended behavior of June as an emerging rather than catastrophic failure.
8.3 July Established Deterioration
Payer mix: 35% INN / 55% OON / 10% Private Pay Financial-verification pass rates: INN 45%, OON 22%, Private Pay 50%

Weighted financial-verification pass rate: (0.35 × 0.45) + (0.55 × 0.22) + (0.10 × 0.50) = 0.1575 + 0.121 + 0.050 = 0.3285

Weighted financial pass = 32.85%

Apply unchanged downstream factor: 0.3285 × 0.3363105208 = 0.110478

Projected July Opportunity → Admission: 11.05% ≈ 11.0%

Difference from May: 22.77% − 11.05% = 11.72 percentage points
July result
Projected deterioration: −11.7pp

This satisfies the Scenario 1 acceptance requirement that July be 10–15 percentage points below May.


9. Mathematical Summary
Month
Weighted Financial Pass
Downstream Factor
Projected Admission Conversion
Change vs. May
May
67.70%
33.63%
22.77%
Control
June
55.04%
33.63%
18.51%
−4.26pp
July
32.85%
33.63%
11.05%
−11.72pp


The revised parameters therefore mathematically satisfy the intended Scenario 1 conversion bands before coding begins.


10. Cost Pressure
Affected Google Ads campaigns receive only modest cost inflation:

Month
Cost Multiplier
May
1.00x
June
1.05x
July
1.10x


This applies to Scenario 1 affected-campaign acquisition-touch costs.

The purpose is to add secondary economic pressure without turning CPC into the primary diagnostic signal.

CPC / touch cost should not exceed approximately +20% versus May under Scenario 1.


11. Top-of-Funnel Behavior
Affected-campaign inquiry volume must remain broadly stable.

For the three affected campaigns combined:

June inquiry volume: within ±10% of May
July inquiry volume: within ±10% of May

The scenario must not be produced by simply eliminating traffic. The intended surface-level impression remains: Google is still producing inquiries.


12. Evidence Trail
Scenario 1 should leave a distributed evidence trail across the relational model.
12.1 acquisition_touches
Relevant fields: touch_id, inquiry_id, platform, campaign_id, campaign_name, cost, platform_conversion

Tell: Affected campaign traffic remains present, platform conversions remain materially represented, and costs rise only modestly. This table alone should not reveal the diagnosis.
12.2 inquiries
Relevant fields: inquiry_id, opportunity_id, inquiry_timestamp, arrival_channel, source_platform

Tell: Google / Paid Search inquiry volume remains broadly stable. A marketer looking only at lead volume should not immediately identify the failure.
12.3 patient_opportunities
Relevant fields: opportunity_id, originating_touch_id, payer_relationship, vob_submitted_flag, vob_outcome, admission_financial_status, admission_status

Tell: Affected campaigns increasingly generate OON opportunities, poor VOB outcomes, Not Financially Cleared opportunities, and fewer admissions. The key causal pattern should become visible here.
12.4 ehr_episodes
Relevant fields: opportunity_id, episode_relationship, admission_datetime

Tell: Fewer affected-campaign opportunities eventually generate Initial EHR episodes. Clinical episode mechanics themselves remain healthy.
12.5 claims and claim_events
These are downstream confirmation only. Relevant fields include episode_id, claim_status, event_type, amount.

There should naturally be fewer downstream claims from affected campaigns because fewer attributable opportunities admit. RCM mechanics themselves must not deteriorate.


13. What Must Stay Unaffected
Scenario isolation is mandatory.
13.1 Admissions competence
For opportunities that remain clinically appropriate, financially viable or acceptable-risk, ready, scheduled, logistically capable, and present for admission, Admissions continues operating at healthy-baseline rates. Do not degrade Admissions performance.
13.2 Unaffected Google campaigns
Keep healthy: CMP-1001, CMP-1004. Their July Opportunity → Admission conversion should remain within ±5pp of May.
13.3 Microsoft Ads
No Scenario 1 mutation. July Opportunity → Admission must remain within ±5pp of May.
13.4 Professional Referral
No Scenario 1 deterioration in referral volume, referral payer quality, outreach activity, reciprocity, or rep behavior. July Opportunity → Admission must remain within ±5pp of May.
13.5 Organic / Local / Direct / Meta
No intentional Scenario 1 degradation.
13.6 Identity resolution
Do not alter Confirmed / Probable / Possible / Unmatched distributions beyond normal seeded variation. No new identity fragmentation.
13.7 EHR behavior
Do not alter Detox/Residential mix, LOS assumptions, LOC transition probability, transition-link integrity, or discharge mechanics.
13.8 RCM behavior
Do not alter denial probabilities, appeal mechanics, claim-processing timing, payment timing, write-off mechanics, or allowed-amount logic. Any financial decline attributable to Scenario 1 should originate upstream from degraded opportunity quality, not a separate billing failure.


14. Code-Defined Scenario Architecture
Scenario 1 must not be implemented as a mutation of an already completed relational dataset. The baseline remains harbor_ridge.db and must never be changed in place. Scenario 1 must instead be generated independently through scenario-aware funnel logic.

Conceptual architecture:

Frozen schema

      │

      ├── Baseline mode

      │   SEED = 20260825

      │       ↓

      │   harbor_ridge.db

      │

      └── Scenario 1 mode

          SCENARIO_1_SEED = 20260826

          Scenario 1 config

              ↓

          harbor_ridge_scenario1.db

The opportunity-building pipeline should determine, in order:

Channel

↓

Platform

↓

Campaign

↓

Month

↓

Scenario eligibility

↓

Scenario-specific payer mix

↓

Scenario-specific financial-verification pass rate

↓

Funnel decision

↓

Admission status

↓

EHR episodes

↓

Claims

↓

Claim events

This ensures downstream records are generated only after the Scenario 1 admission outcome has already been decided. No patient ever needs to be "un-admitted."


15. Scenario Seed
Use:

SCENARIO_1_SEED = 20260826

Requirements:

fixed
documented
distinct from baseline SEED
used specifically for Scenario 1 generation
reproducible within the same Python process
reproducible across separate database builds

Changing Scenario 1 parameters must not alter the frozen baseline seed or baseline database.


16. Scenario 1 Acceptance Criteria
A. Structural Integrity
Scenario 1 must pass: PRAGMA foreign_key_check = 0; PRAGMA integrity_check = ok; all 11 tables populated where appropriate; VOB conditional rule; episode relationship conditional rule; no dangling prior_episode_id; same-process reproducibility; database-to-database reproducibility using SCENARIO_1_SEED.

Scenario effects do not excuse structural defects.
B. Affected-Campaign Payer Drift
For affected attributable opportunities:

May OON share — Target: 35% — Acceptable: 32–38%
June OON share — Target: 43% — Acceptable: 39–47%
July OON share — Target: 55% — Acceptable: 50–60%

Also require: July OON Share − May OON Share ≥ 15pp. The OON share must not exceed approximately 60%.
C. Affected-Campaign Admission Deterioration
Opportunity → Admission = Admitted attributable opportunities ÷ All attributable opportunities, for the three affected campaigns combined.

May — Healthy internal control. Theoretical value: ~22.8%
June — Must be 4–12pp below May. Theoretical target: −4.3pp
July — Must be 10–15pp below May. Theoretical target: −11.7pp
Too-obvious ceiling — July must not deteriorate by more than 18pp below May.
D. Healthy Comparison Groups Remain Stable
Unaffected Google campaigns (CMP-1001 + CMP-1004): July within ±5pp of May
Microsoft Ads: July within ±5pp of May
Professional Referral: July within ±5pp of May

The validator should fail Scenario 1 if these comparison groups materially collapse.
E. Top-of-Funnel Stability
For affected campaigns combined:

Inquiry volume: June vs. May within ±10%; July vs. May within ±10%
Cost: June mean affected-campaign cost approximately +5% ±3pp; July approximately +10% ±3pp. Neither month may exceed approximately +20% versus May.
F. VOB / Financial-Quality Deterioration
Poor VOB Outcome Rate — defined as Non-Viable + Unable to Verify among insured attributable opportunities with submitted VOBs. July must exceed May by at least 10 percentage points. Scenario 1 must not produce anything resembling 100% VOB failure.

Not Financially Cleared Rate — July affected-campaign rate must exceed May by at least 8 percentage points.


17. Detectable but Not Cartoonishly Obvious
Too subtle
Scenario 1 is too subtle if: July conversion falls <10pp below May; OON mix shifts <15pp; poor VOB outcomes barely increase; affected and unaffected Google campaigns behave similarly; segmentation does not materially improve visibility.
Too obvious
Scenario 1 is too obvious if: July conversion deteriorates >18pp below May; OON exceeds ~60%; Google inquiry volume collapses >15%; CPC/touch cost increases >20%; VOB failure approaches 100%; all Google campaigns deteriorate; Microsoft deteriorates; professional referral deteriorates; facility-wide admissions collapse.

None of those should occur.


18. Target Analytical Difficulty
A basic review of Google inquiry volume, acquisition-touch volume, and platform conversions should not produce the diagnosis.

A careful analysis joining and segmenting month × campaign × payer_relationship × vob_outcome × admission_financial_status × admission_status should reveal it.

The intended chain is:

Affected Google campaigns

        ↓

OON payer mix rises

        ↓

Financial-verification success falls

        ↓

Poor VOB / financial-clearance outcomes rise

        ↓

Opportunity → Admission conversion falls

        ↓

Fewer downstream EHR episodes and claims

Meanwhile: inquiry volume remains healthy; unaffected Google campaigns remain healthy; Microsoft remains healthy; professional referrals remain healthy; Admissions competence remains healthy; RCM remains healthy.

That is the Scenario 1 signature.


19. Too-Obvious Ceiling Confirmation
The revised intensified parameters remain inside the established ceiling.

July conversion: May theoretical 22.77%; July theoretical 11.05%; difference −11.72pp. This is greater than the 10pp minimum, less than the 15pp preferred upper target, and well below the 18pp "too obvious" ceiling.

July OON: 55%, remaining below the approximately 60% ceiling.

VOB behavior: The scenario lowers financial-verification success but does not require all insured opportunities to fail or all VOBs to become Non-Viable.

Comparison groups: Unaffected Google campaigns, Microsoft Ads, Professional Referral, Organic, and other channels remain governed by healthy-baseline parameters.

Top of funnel: Affected inquiry volume remains within ±10% of May, preventing the scenario from announcing itself through traffic collapse.

Therefore, the intensified parameters survive the 33.63% funnel dilution without crossing into cartoonishly obvious territory.


20. Scenario 1 Output
Scenario database: harbor_ridge_scenario1.db The frozen baseline remains: harbor_ridge.db

Scenario 1 should be reproducibly generated from code, independently validated, and never produced through manual row editing or post-hoc database mutation.


Final Candidate Status
This Scenario 1 specification now includes: calibrated payer-mix deterioration; calibrated financial-verification deterioration; full month-by-month funnel math; explicit downstream dilution; affected and unaffected campaign groups; unambiguous attribution logic; independent Scenario 1 seed; scenario-aware generation architecture; structural acceptance criteria; domain acceptance criteria; top-of-funnel stability criteria; financial-quality criteria; comparison-group safeguards; explicit too-subtle and too-obvious bounds.

