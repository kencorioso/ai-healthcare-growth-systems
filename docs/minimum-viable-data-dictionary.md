Harbor Ridge V1 Minimum Viable Data Dictionary
Version: 1.0  
Status: Corrected Final Candidate for Human Review  
Target: SQLite  
Scope: Minimum relational schema required to construct and test the Harbor Ridge V1 synthetic dataset
---
1. Purpose
The Harbor Ridge V1 Minimum Viable Data Dictionary translates the finalized Source-System Map into the smallest relational structure required to build the canonical synthetic SQLite dataset.
This document defines:
table names,
column names,
SQLite data types,
primary keys,
foreign keys,
nullability,
constrained values,
conditional integrity rules,
and the minimum provenance / confidence fields required by Harbor Ridge V1.
Every table and field must trace back to the finalized Source-System Map or completed source-system interviews.
If a proposed field cannot be traced to an established V1 requirement, it does not enter this schema.
This is not a production healthcare data warehouse design.
---
2. Minimum Relational Model
Harbor Ridge V1 uses the following minimum relational structure:
```text
                         outreach_reps
                          /         \
                         ↓           ↓
              professional_accounts  outreach_activities
                         ↓
              professional_referrals
                         ↓
contacts → inquiries → patient_opportunities → ehr_episodes → claims → claim_events
              ↑                 ↑
              │                 │
      acquisition_touches       │
                                │
                    professional_referrals
```
The core acquisition-to-revenue Golden Thread is:
```text
acquisition_touches
        ↓
inquiries
        ↓
patient_opportunities
        ↓
ehr_episodes
        ↓
claims
        ↓
claim_events
```
Professional referral influence joins through:
```text
outreach_reps
        ↓
professional_accounts
        ↓
professional_referrals
        ↓
patient_opportunities
```
---
3. Table: `contacts`
Purpose: Represent the synthetic human beings interacting with Harbor Ridge.
Contact identity remains separate from Patient Opportunity identity because a patient, loved one, and professional referral source may all participate in the same underlying opportunity.
Column	SQLite Type	Constraint	Definition
`contact_id`	TEXT	PK, NOT NULL	Synthetic unique contact identifier
`first_name`	TEXT	NOT NULL	Synthetic first name
`last_name`	TEXT	NOT NULL	Synthetic last name
`phone`	TEXT	NULL	Synthetic phone number
`email`	TEXT	NULL	Synthetic email address
`date_of_birth`	TEXT	NULL	ISO date; primarily populated for patients
`created_at`	TEXT	NOT NULL	ISO timestamp when contact enters dataset
Example:
```text
contact_id: CNT-000241
first_name: Susan
last_name: Miller
phone: 555-010-8821
email: susan.miller@example.test
date_of_birth: NULL
created_at: 2026-06-03T14:22:00
```
V1 restraint: No address, SSN, gender, detailed demographics, or production identity attributes unless later testing proves them necessary.
---
4. Table: `patient_opportunities`
Purpose: Represent the central commercial opportunity.
Multiple inquiries may resolve to one Patient Opportunity.
Canonical identifier:
```text
HRO-######
```
Example:
```text
HRO-000184
```
Column	SQLite Type	Constraint	Definition
`opportunity_id`	TEXT	PK, NOT NULL	Canonical Harbor Ridge Opportunity ID
`patient_contact_id`	TEXT	FK → `contacts.contact_id`, NULL	Contact believed to represent the prospective patient
`created_at`	TEXT	NOT NULL	Opportunity creation timestamp
`vob_submitted_flag`	INTEGER	NOT NULL	Whether a VOB was submitted; 0 = no, 1 = yes
`vob_outcome`	TEXT	NULL	Current VOB outcome; conditionally nullable
`payer`	TEXT	NULL	Payer / insurance carrier; may be NULL for Private Pay
`payer_relationship`	TEXT	NOT NULL	Harbor Ridge payer relationship: INN, OON, or Private Pay
`admission_financial_status`	TEXT	NOT NULL	Financial clearance state
`admission_status`	TEXT	NOT NULL	Current / final admission state
`originating_influence_type`	TEXT	NOT NULL	Paid, Organic, Professional Referral, Direct, or Unknown
`originating_touch_id`	TEXT	FK → `acquisition_touches.touch_id`, NULL	Digital touch supporting originating influence
`originating_referral_id`	TEXT	FK → `professional_referrals.referral_id`, NULL	Professional referral supporting originating influence
`attribution_confidence`	TEXT	NOT NULL	Confidence in originating-influence assignment
4.1 `vob_submitted_flag`
Allowed values:
```text
0
1
```
Constraint:
```text
vob_submitted_flag IN (0, 1)
```
4.2 `vob_outcome`
This column is nullable.
Allowed non-NULL values:
```text
Pending
Viable
Non-Viable
Unable to Verify
```
Conditional rule:
```text
IF vob_submitted_flag = 0
    vob_outcome MUST be NULL

IF vob_submitted_flag = 1
    vob_outcome MUST be NOT NULL
    AND vob_outcome MUST be one of:
        Pending
        Viable
        Non-Viable
        Unable to Verify
```
This preserves the distinction between whether a VOB occurred and what its result was.
4.3 `payer_relationship`
Allowed values:
```text
INN
OON
Private Pay
```
This field is required because payer-network relationship is a core economic dimension in the Harbor Ridge business scenario and planned diagnostic logic.
4.4 `admission_financial_status`
Allowed values:
```text
Financially Cleared
At-Risk Admission
Not Financially Cleared
```
No additional financial status values enter V1 unless later testing demonstrates a requirement.
4.5 `admission_status`
Allowed minimum V1 values:
```text
Open
Admitted
Not Admitted
```
Detailed loss-reason taxonomy is intentionally deferred.
4.6 `attribution_confidence`
Allowed values:
```text
Confirmed
Probable
Possible
Unmatched
```
---
5. Table: `inquiries`
Purpose: Store each actual inbound human interaction.
Calls and web forms remain distinct inquiry mechanisms.
Column	SQLite Type	Constraint	Definition
`inquiry_id`	TEXT	PK, NOT NULL	Unique inbound inquiry identifier
`opportunity_id`	TEXT	FK → `patient_opportunities.opportunity_id`, NULL	Resolved Patient Opportunity
`contact_id`	TEXT	FK → `contacts.contact_id`, NOT NULL	Person making the inquiry
`inquiry_timestamp`	TEXT	NOT NULL	ISO timestamp
`contact_role`	TEXT	NOT NULL	Patient, Loved One, or Professional Referral Source
`inquiry_method`	TEXT	NOT NULL	Call or Web Form
`arrival_channel`	TEXT	NOT NULL	Paid Search, Organic, Local, Professional Referral, Direct, Other, or Unknown
`source_platform`	TEXT	NULL	Google Ads, Microsoft Ads, Google Organic, GBP, Meta, etc.
`tracking_number`	TEXT	NULL	Phone tracking number where applicable
`call_duration_seconds`	INTEGER	NULL	Call duration in seconds
`landing_page`	TEXT	NULL	Landing / submission page for digital inquiries
`match_confidence`	TEXT	NOT NULL	Confirmed, Probable, Possible, or Unmatched
`source_system`	TEXT	NOT NULL	CRM, Call Tracking, Web Form, etc.
`evidence_class`	TEXT	NOT NULL	System-Observed, Human-Entered, or Derived / Analytical
5.1 Identity Resolution
Allowed `match_confidence` values:
```text
Confirmed
Probable
Possible
Unmatched
```
`opportunity_id` is intentionally nullable.
This allows Harbor Ridge V1 to represent:
```text
Inquiry exists
        ↓
Identity resolution is incomplete
        ↓
No defensible Patient Opportunity link yet
```
without creating an invalid foreign-key reference.
---
6. Table: `acquisition_touches`
Purpose: Preserve observable digital acquisition activity separately from CRM inquiry creation.
This allows Harbor Ridge to reconcile platform-observed activity against real inquiries and downstream outcomes.
Column	SQLite Type	Constraint	Definition
`touch_id`	TEXT	PK, NOT NULL	Unique acquisition-touch identifier
`inquiry_id`	TEXT	FK → `inquiries.inquiry_id`, NULL	Inquiry resulting from the touch, if known
`touch_timestamp`	TEXT	NOT NULL	Touch timestamp
`channel`	TEXT	NOT NULL	Paid Search, Paid Social, Organic, Local, or Direct
`platform`	TEXT	NULL	Google Ads, Microsoft Ads, Meta, Google Organic, GBP
`campaign_id`	TEXT	NULL	Platform campaign identifier
`campaign_name`	TEXT	NULL	Human-readable campaign name
`ad_group`	TEXT	NULL	Ad Group / Ad Set
`keyword`	TEXT	NULL	Purchased / bid keyword
`search_term`	TEXT	NULL	Observed search query where available
`match_type`	TEXT	NULL	Exact, Phrase, or Broad
`landing_page`	TEXT	NULL	Page reached by visitor
`geography`	TEXT	NULL	State / market used for V1 analysis
`cost`	REAL	NULL	Cost attributable to the touch / click
`platform_conversion`	INTEGER	NOT NULL	SQLite boolean; 0 = no, 1 = yes
`source_system`	TEXT	NOT NULL	Original digital source system
`evidence_class`	TEXT	NOT NULL	Generally System-Observed
6.1 `platform_conversion`
Constraint:
```text
platform_conversion IN (0, 1)
```
Deliberately omitted for V1: Quality Score, impression share, creative assets, Meta frequency, video quartiles, complete GSC metric sets, and full change-history tables.
---
7. Table: `outreach_reps`
Purpose: Identify the professional-referral representative who owns or works a professional account.
Column	SQLite Type	Constraint	Definition
`outreach_rep_id`	TEXT	PK, NOT NULL	Synthetic outreach representative ID
`rep_name`	TEXT	NOT NULL	Synthetic representative name
`active_flag`	INTEGER	NOT NULL	SQLite boolean; 0 = inactive, 1 = active
Constraint:
```text
active_flag IN (0, 1)
```
---
8. Table: `professional_accounts`
Purpose: Represent professional referral relationships.
Column	SQLite Type	Constraint	Definition
`professional_account_id`	TEXT	PK, NOT NULL	Unique professional / practice identifier
`professional_name`	TEXT	NOT NULL	Synthetic referring-professional name
`organization_name`	TEXT	NULL	Practice / organization
`professional_type`	TEXT	NOT NULL	Therapist, Psychiatrist, Hospital, Interventionist, etc.
`owner_rep_id`	TEXT	FK → `outreach_reps.outreach_rep_id`, NULL	Primary relationship owner
`created_at`	TEXT	NOT NULL	Account creation timestamp
Deliberately omitted: NPI, license numbers, full address, specialty taxonomy, and other production CRM attributes.
---
9. Table: `professional_referrals`
Purpose: Represent the referral event connecting a professional account to a Patient Opportunity.
Column	SQLite Type	Constraint	Definition
`referral_id`	TEXT	PK, NOT NULL	Unique professional-referral event
`professional_account_id`	TEXT	FK → `professional_accounts.professional_account_id`, NOT NULL	Referring professional account
`opportunity_id`	TEXT	FK → `patient_opportunities.opportunity_id`, NULL	Resulting Patient Opportunity, if successfully linked
`referral_timestamp`	TEXT	NOT NULL	Referral timestamp
`referral_channel`	TEXT	NOT NULL	Call, Email/Text Coordination, Patient Told to Call, or Other
`source_system`	TEXT	NOT NULL	CRM, intake record, etc.
`evidence_class`	TEXT	NOT NULL	System-Observed or Human-Entered
`attribution_confidence`	TEXT	NOT NULL	Confidence that the referral generated the opportunity
`opportunity_id` is intentionally nullable so V1 can represent referral attribution loss.
Allowed `attribution_confidence` values:
```text
Confirmed
Probable
Possible
Unmatched
```
---
10. Table: `outreach_activities`
Purpose: Store the minimum relationship activity required to evaluate professional-referral performance and relationship decay.
Column	SQLite Type	Constraint	Definition
`activity_id`	TEXT	PK, NOT NULL	Unique outreach activity
`professional_account_id`	TEXT	FK → `professional_accounts.professional_account_id`, NOT NULL	Professional account contacted
`outreach_rep_id`	TEXT	FK → `outreach_reps.outreach_rep_id`, NOT NULL	Representative performing the activity
`activity_timestamp`	TEXT	NOT NULL	Activity timestamp
`activity_type`	TEXT	NOT NULL	Call, Email, Meeting, Lunch, Presentation, or Tour
`direction`	TEXT	NOT NULL	Outbound or Inbound
`reciprocated_flag`	INTEGER	NOT NULL	Whether meaningful reciprocal engagement occurred
`evidence_class`	TEXT	NOT NULL	System-Observed or Human-Entered
10.1 `reciprocated_flag`
Constraint:
```text
reciprocated_flag IN (0, 1)
```
This table remains intentionally smaller than a production BD CRM.
---
11. Table: `ehr_episodes`
Purpose: Represent admitted clinical episodes.
One Patient Opportunity may produce one or more EHR episodes.
Column	SQLite Type	Constraint	Definition
`episode_id`	TEXT	PK, NOT NULL	EHR Episode ID
`opportunity_id`	TEXT	FK → `patient_opportunities.opportunity_id`, NULL	Parent Patient Opportunity
`prior_episode_id`	TEXT	Self-FK → `ehr_episodes.episode_id`, NULL / conditionally required	Prior episode when current episode is a transition or administrative re-admit
`episode_relationship`	TEXT	NOT NULL	Initial, LOC Transition, or Administrative Re-Admit
`admission_datetime`	TEXT	NOT NULL	System-recorded admission timestamp
`discharge_datetime`	TEXT	NULL	Discharge timestamp
`level_of_care`	TEXT	NOT NULL	Detox or Residential for V1
`payer`	TEXT	NULL	Payer associated with episode
`authorization_start`	TEXT	NULL	Authorized period start
`authorization_end`	TEXT	NULL	Authorized period end
`discharge_disposition`	TEXT	NULL	Recorded discharge disposition
`source_system`	TEXT	NOT NULL	EHR
`evidence_class`	TEXT	NOT NULL	System-Observed / Human-Entered depending on field context
11.1 `episode_relationship`
Allowed values:
```text
Initial
LOC Transition
Administrative Re-Admit
```
11.2 `prior_episode_id`
`prior_episode_id` is a nullable self-referencing foreign key, but its nullability is controlled by `episode_relationship`.
Conditional rule:
```text
IF episode_relationship = 'Initial'
    prior_episode_id MUST be NULL

IF episode_relationship IN ('LOC Transition', 'Administrative Re-Admit')
    prior_episode_id MUST be NOT NULL
```
Examples:
Valid:
```text
episode_id = KIPU-000101
episode_relationship = Initial
prior_episode_id = NULL
```
Valid:
```text
episode_id = KIPU-000102
episode_relationship = LOC Transition
prior_episode_id = KIPU-000101
```
Invalid:
```text
episode_relationship = LOC Transition
prior_episode_id = NULL
```
Invalid:
```text
episode_relationship = Initial
prior_episode_id = KIPU-000099
```
This rule ensures that Harbor Ridge can distinguish a level-of-care transition or administrative re-admit from an unrelated episode.
11.3 Opportunity Linkage
`opportunity_id` remains nullable so V1 can represent Outcome-Linkage Loss where an EHR episode exists but cannot be connected to its CRM opportunity.
---
12. Table: `claims`
Purpose: Represent financial claims generated from clinical episodes.
Column	SQLite Type	Constraint	Definition
`claim_id`	TEXT	PK, NOT NULL	RCM claim identifier
`episode_id`	TEXT	FK → `ehr_episodes.episode_id`, NULL	Parent clinical episode
`service_start_date`	TEXT	NOT NULL	First date of service
`service_end_date`	TEXT	NOT NULL	Last date of service
`payer`	TEXT	NOT NULL	Claim payer
`billed_amount`	REAL	NOT NULL	Submitted charges
`allowed_amount`	REAL	NULL	Payer allowed amount
`patient_responsibility`	REAL	NULL	Deductible / coinsurance responsibility
`claim_status`	TEXT	NOT NULL	Submitted, Pending, Paid, Denied, Appealed, or Closed
`source_system`	TEXT	NOT NULL	RCM
`evidence_class`	TEXT	NOT NULL	System-Observed
`episode_id` remains nullable so V1 can represent an EHR-to-RCM linkage failure without inserting an invalid foreign-key reference.
---
13. Table: `claim_events`
Purpose: Represent the one-to-many financial events occurring after a claim is created.
`claim_events` is used instead of a simple payment table because Harbor Ridge V1 must represent payments, adjustments, write-offs, denials, and appeals.
Column	SQLite Type	Constraint	Definition
`claim_event_id`	TEXT	PK, NOT NULL	Unique financial event
`claim_id`	TEXT	FK → `claims.claim_id`, NULL	Associated claim
`event_date`	TEXT	NOT NULL	Financial-event date
`event_type`	TEXT	NOT NULL	Insurance Payment, Patient Payment, Adjustment, Write-Off, Denial, or Appeal
`amount`	REAL	NULL	Dollar value where applicable
`source_system`	TEXT	NOT NULL	RCM / Financial Ledger
`evidence_class`	TEXT	NOT NULL	System-Observed / Human-Entered as applicable
`claim_id` is nullable so V1 can represent a payment or adjustment record that exists but has lost its deterministic link to the originating claim.
13.1 Actual Cash Collected
Actual cash collected is derived rather than stored as a standalone revenue field:
```text
SUM(amount)
WHERE event_type IN ('Insurance Payment', 'Patient Payment')
```
for the appropriate claim, episode, opportunity, acquisition source, or mature cohort.
---
14. Minimum Evidence and Confidence Taxonomy
14.1 `evidence_class`
Allowed values:
```text
System-Observed
Human-Entered
Derived / Analytical
```
14.2 Identity / Attribution Confidence
Allowed values:
```text
Confirmed
Probable
Possible
Unmatched
```
For V1, the same four confidence values are reused wherever an explicit identity or attribution confidence state is required.
---
15. Final Constraint Audit for Corrected Fields
The following constraints are explicitly locked before SQLite implementation.
Table	Column	Final Constraint
`patient_opportunities`	`payer_relationship`	NOT NULL; `INN`, `OON`, or `Private Pay`
`patient_opportunities`	`vob_submitted_flag`	NOT NULL; 0 or 1
`patient_opportunities`	`vob_outcome`	NULLABLE; conditionally required when VOB is submitted
`patient_opportunities`	`admission_financial_status`	NOT NULL; exactly 3 approved V1 values
`ehr_episodes`	`episode_relationship`	NOT NULL; exactly 3 approved V1 values
`ehr_episodes`	`prior_episode_id`	Self-FK; NULL only for `Initial`; required for transition / administrative re-admit
15.1 VOB Conditional Integrity Rule
```text
(vob_submitted_flag = 0 AND vob_outcome IS NULL)

OR

(vob_submitted_flag = 1
 AND vob_outcome IN ('Pending', 'Viable', 'Non-Viable', 'Unable to Verify'))
```
15.2 Episode Conditional Integrity Rule
```text
(episode_relationship = 'Initial'
 AND prior_episode_id IS NULL)

OR

(episode_relationship IN ('LOC Transition', 'Administrative Re-Admit')
 AND prior_episode_id IS NOT NULL)
```
These rules must be reflected both in this dictionary and later in `schema.sql`.
---
16. Key Relationships
SQLite should enforce the following relational skeleton:
```text
contacts.contact_id
        ↓
inquiries.contact_id

patient_opportunities.opportunity_id
        ↓
inquiries.opportunity_id

patient_opportunities.opportunity_id
        ↓
professional_referrals.opportunity_id

patient_opportunities.opportunity_id
        ↓
ehr_episodes.opportunity_id

professional_accounts.professional_account_id
        ↓
professional_referrals.professional_account_id

professional_accounts.professional_account_id
        ↓
outreach_activities.professional_account_id

outreach_reps.outreach_rep_id
        ↓
professional_accounts.owner_rep_id

outreach_reps.outreach_rep_id
        ↓
outreach_activities.outreach_rep_id

inquiries.inquiry_id
        ↓
acquisition_touches.inquiry_id

ehr_episodes.episode_id
        ↓
ehr_episodes.prior_episode_id

ehr_episodes.episode_id
        ↓
claims.episode_id

claims.claim_id
        ↓
claim_events.claim_id
```
Acquisition-to-Revenue Golden Thread
```text
acquisition_touches
        ↓
inquiries
        ↓
patient_opportunities
        ↓
ehr_episodes
        ↓
claims
        ↓
claim_events
```
Professional Referral Influence
```text
outreach_reps
        ↓
professional_accounts
        ↓
professional_referrals
        ↓
patient_opportunities
```
---
17. SQLite Conventions
17.1 IDs
Use `TEXT`.
Examples:
```text
CNT-000001
INQ-000001
HRO-000001
TOUCH-000001
REP-000001
PRO-000001
REF-000001
ACT-000001
KIPU-000001
CLM-000001
CEV-000001
```
17.2 Dates and Timestamps
Use ISO-8601 `TEXT`.
```text
2026-06-14
2026-06-14T19:42:18
```
17.3 Currency
Use `REAL` for Harbor Ridge V1 synthetic analytics.
Production-grade decimal-accounting machinery is outside V1 scope unless implementation demonstrates a need.
17.4 Booleans
Use `INTEGER`.
```text
0 = false
1 = true
```
Boolean fields should use `CHECK` constraints limiting values to 0 or 1.
17.5 Foreign Keys
Foreign keys should be enabled and enforced wherever a relationship is known to exist.
Nullable foreign keys are used when the source-system relationship itself is legitimately missing or unresolved.
---
18. Modeling Data Degradation Without Corrupting the Database
Harbor Ridge V1 must represent realistic broken lineage while preserving relational integrity.
Example:
```text
ehr_episodes.opportunity_id = NULL
```
means:
> The EHR episode exists, but its Patient Opportunity relationship is missing.
That is different from:
```text
ehr_episodes.opportunity_id = HRO-999999
```
when `HRO-999999` does not exist.
The latter would mean the relational database itself contains an invalid reference.
Likewise:
```text
claims.episode_id = NULL
```
can represent a missing EHR-to-RCM bridge.
And:
```text
claim_events.claim_id = NULL
```
can represent a financial event whose deterministic claim linkage was lost.
V1 principle: Simulate broken healthcare lineage without building a broken database.
---
19. Deliberately Excluded from V1
The following are intentionally excluded from the Minimum Viable Data Dictionary:
Payer master tables
Facilities table
Beds table
Clinical diagnoses table
Clinician table
Separate authorizations table
Claim-line table
Remittance table
Separate appeals table
Attribution-history table
Website-pages table
Campaign master table
Keyword master table
Geographic master table
Google Ads change-history table
Full GA4 events table
Full GSC performance table
EHR notes
Call transcripts
AI summaries
Dashboard tables
SQL aggregate tables
Production identity-resolution tables
Enterprise master-patient-index structures
These may eventually become legitimate additions, but they are not required to construct and test the Harbor Ridge V1 synthetic dataset.
---
20. V1 Scope Rule
Every table and field in Harbor Ridge V1 must trace back to the finalized Source-System Map or completed source-system interviews.
If a proposed field cannot be traced to an established project requirement, it does not enter V1.
Architecture and schema refinement should occur only when implementation or Claude testing demonstrates that a missing element prevents Harbor Ridge V1 from answering one of its defined executive diagnostic questions.
---
21. Governing Principle
> The Minimum Viable Data Dictionary exists to make the Harbor Ridge V1 SQLite synthetic dataset possible. It is not an attempt to model a production healthcare enterprise.
The schema should preserve enough relational integrity, identity, attribution, provenance, uncertainty, clinical linkage, payer economics, and financial linkage for an executive or AI system to reconstruct the Harbor Ridge patient-acquisition-to-revenue journey and diagnose deliberately embedded business failures.
---
End of Harbor Ridge V1 Minimum Viable Data Dictionary — Version 1.0
