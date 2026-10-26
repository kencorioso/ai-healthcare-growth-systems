# Harbor Ridge V1 — Phase D Neutral Analyst Brief

**Version:** 1.0  
**Status:** FROZEN  
**Use:** Identical supporting document for both Phase D V0.1 blind-analysis sessions  
**Purpose:** Business context, field vocabulary, and plain relational structure only

---

## 1. Business Setting

Harbor Ridge is a fictional 32-bed dual-diagnosis behavioral health treatment facility.

The facility has:

- 8 detox beds
- 24 residential beds

Harbor Ridge serves patients using commercial:

- in-network insurance coverage,
- out-of-network insurance coverage,
- and private-pay arrangements.

The SQLite database represents approximately three months of synthetic Harbor Ridge activity across patient acquisition, admissions, professional referrals, treatment episodes, claims, and financial events.

This brief provides no expected performance levels, benchmark values, target rates, or definitions of healthy or unhealthy behavior.

---

## 2. Database Contents

The database contains 11 tables:

1. `contacts`
2. `patient_opportunities`
3. `inquiries`
4. `acquisition_touches`
5. `outreach_reps`
6. `professional_accounts`
7. `professional_referrals`
8. `outreach_activities`
9. `ehr_episodes`
10. `claims`
11. `claim_events`

The definitions below describe what each stored field represents.

They do not identify which fields are analytically important.

---

## 3. `contacts`

Represents synthetic people appearing in Harbor Ridge records.

| Column | Plain-English Meaning |
|---|---|
| `contact_id` | Unique identifier for a contact. |
| `first_name` | Synthetic first name. |
| `last_name` | Synthetic last name. |
| `phone` | Synthetic phone number, when present. |
| `email` | Synthetic email address, when present. |
| `date_of_birth` | Synthetic date of birth, when present. |
| `created_at` | Timestamp when the contact record was created. |

---

## 4. `patient_opportunities`

Represents a Harbor Ridge Patient Opportunity record.

| Column | Plain-English Meaning |
|---|---|
| `opportunity_id` | Unique identifier for the Patient Opportunity. |
| `patient_contact_id` | Contact identifier associated with the prospective patient, when present. |
| `created_at` | Timestamp when the Patient Opportunity was created. |
| `vob_submitted_flag` | Stored 0/1 indicator of whether a verification-of-benefits submission was recorded. |
| `vob_outcome` | Stored verification-of-benefits outcome, when present. |
| `payer` | Insurance carrier or payer name, when present. |
| `payer_relationship` | Harbor Ridge's stored payer relationship. |
| `admission_financial_status` | Stored financial status associated with the opportunity. |
| `admission_status` | Stored admission state associated with the opportunity. |
| `originating_influence_type` | Stored category describing the originating influence assigned to the opportunity. |
| `originating_touch_id` | Acquisition-touch identifier associated with the opportunity, when present. |
| `originating_referral_id` | Professional-referral identifier associated with the opportunity, when present. |
| `attribution_confidence` | Stored categorical value associated with the originating-influence assignment. |

Stored `payer_relationship` values may include:

- `INN`
- `OON`
- `Private Pay`

Stored `vob_outcome` values may include:

- `Pending`
- `Viable`
- `Non-Viable`
- `Unable to Verify`

Stored `admission_financial_status` values may include:

- `Financially Cleared`
- `At-Risk Admission`
- `Not Financially Cleared`

Stored `admission_status` values may include:

- `Open`
- `Admitted`
- `Not Admitted`

Stored `originating_influence_type` values may include:

- `Paid`
- `Organic`
- `Professional Referral`
- `Direct`
- `Unknown`

Stored `attribution_confidence` values may include:

- `Confirmed`
- `Probable`
- `Possible`
- `Unmatched`

---

## 5. `inquiries`

Represents inbound inquiry records.

| Column | Plain-English Meaning |
|---|---|
| `inquiry_id` | Unique identifier for an inquiry. |
| `opportunity_id` | Patient Opportunity identifier associated with the inquiry, when present. |
| `contact_id` | Contact identifier associated with the inquiry. |
| `inquiry_timestamp` | Timestamp of the inquiry. |
| `contact_role` | Stored role of the contact on the inquiry. |
| `inquiry_method` | Stored inquiry method. |
| `arrival_channel` | Stored channel through which the inquiry arrived. |
| `source_platform` | Named source platform, when present. |
| `tracking_number` | Phone tracking number, when present. |
| `call_duration_seconds` | Recorded call duration in seconds, when present. |
| `landing_page` | Recorded landing or submission page, when present. |
| `match_confidence` | Stored categorical value associated with the inquiry-to-opportunity match. |
| `source_system` | Named source system recorded on the inquiry. |
| `evidence_class` | Stored categorical value present on the inquiry record. |

Stored `contact_role` values may include:

- `Patient`
- `Loved One`
- `Professional Referral Source`

Stored `inquiry_method` values may include:

- `Call`
- `Web Form`

Stored `arrival_channel` values may include:

- `Paid Search`
- `Organic`
- `Local`
- `Professional Referral`
- `Direct`
- `Other`
- `Unknown`

Stored `match_confidence` values may include:

- `Confirmed`
- `Probable`
- `Possible`
- `Unmatched`

---

## 6. `acquisition_touches`

Represents recorded digital acquisition activity.

| Column | Plain-English Meaning |
|---|---|
| `touch_id` | Unique identifier for an acquisition touch. |
| `inquiry_id` | Inquiry identifier associated with the touch, when present. |
| `touch_timestamp` | Timestamp of the acquisition touch. |
| `channel` | Stored acquisition channel. |
| `platform` | Named acquisition platform, when present. |
| `campaign_id` | Platform campaign identifier, when present. |
| `campaign_name` | Human-readable campaign name, when present. |
| `ad_group` | Ad group or ad-set name, when present. |
| `keyword` | Recorded purchased or bid keyword, when present. |
| `search_term` | Recorded search query, when present. |
| `match_type` | Stored keyword match type, when present. |
| `landing_page` | Recorded landing page, when present. |
| `geography` | Stored geographic label, when present. |
| `cost` | Recorded cost associated with the touch, when present. |
| `platform_conversion` | Stored 0/1 platform-conversion indicator. |
| `source_system` | Named source system recorded on the touch. |
| `evidence_class` | Stored categorical value present on the touch record. |

Stored `channel` values may include:

- `Paid Search`
- `Paid Social`
- `Organic`
- `Local`
- `Direct`

Stored `match_type` values may include:

- `Exact`
- `Phrase`
- `Broad`

---

## 7. `outreach_reps`

Represents professional-outreach representatives.

| Column | Plain-English Meaning |
|---|---|
| `outreach_rep_id` | Unique identifier for an outreach representative. |
| `rep_name` | Synthetic representative name. |
| `active_flag` | Stored 0/1 indicator showing whether the representative record is marked active. |

---

## 8. `professional_accounts`

Represents professional referral accounts.

| Column | Plain-English Meaning |
|---|---|
| `professional_account_id` | Unique identifier for a professional account. |
| `professional_name` | Synthetic referring-professional name. |
| `organization_name` | Synthetic organization or practice name, when present. |
| `professional_type` | Stored professional category. |
| `owner_rep_id` | Outreach-representative identifier stored as the account owner, when present. |
| `created_at` | Timestamp when the professional-account record was created. |

Stored `professional_type` values may include:

- `Therapist`
- `Psychiatrist`
- `Hospital`
- `Interventionist`
- `Primary Care Physician`
- `Psychologist`
- `Social Worker`

---

## 9. `professional_referrals`

Represents professional-referral events.

| Column | Plain-English Meaning |
|---|---|
| `referral_id` | Unique identifier for a referral event. |
| `professional_account_id` | Professional-account identifier associated with the referral. |
| `opportunity_id` | Patient Opportunity identifier associated with the referral, when present. |
| `referral_timestamp` | Timestamp of the referral event. |
| `referral_channel` | Stored referral channel. |
| `source_system` | Named source system recorded on the referral. |
| `evidence_class` | Stored categorical value present on the referral record. |
| `attribution_confidence` | Stored categorical value associated with the referral-to-opportunity attribution. |

Stored `referral_channel` values may include:

- `Call`
- `Email/Text Coordination`
- `Patient Told to Call`
- `Other`

Stored `attribution_confidence` values may include:

- `Confirmed`
- `Probable`
- `Possible`
- `Unmatched`

---

## 10. `outreach_activities`

Represents recorded professional-outreach activities.

| Column | Plain-English Meaning |
|---|---|
| `activity_id` | Unique identifier for an outreach activity. |
| `professional_account_id` | Professional-account identifier associated with the activity. |
| `outreach_rep_id` | Outreach-representative identifier associated with the activity. |
| `activity_timestamp` | Timestamp of the activity. |
| `activity_type` | Stored activity type. |
| `direction` | Stored activity direction. |
| `reciprocated_flag` | Stored 0/1 reciprocated indicator. |
| `evidence_class` | Stored categorical value present on the activity record. |

Stored `activity_type` values may include:

- `Call`
- `Email`
- `Meeting`
- `Lunch`
- `Presentation`
- `Tour`

Stored `direction` values may include:

- `Outbound`
- `Inbound`

---

## 11. `ehr_episodes`

Represents recorded EHR treatment episodes.

| Column | Plain-English Meaning |
|---|---|
| `episode_id` | Unique identifier for an EHR episode. |
| `opportunity_id` | Patient Opportunity identifier associated with the episode, when present. |
| `prior_episode_id` | Identifier of another EHR episode referenced by this episode, when present. |
| `episode_relationship` | Stored relationship category for the episode. |
| `admission_datetime` | Recorded admission timestamp. |
| `discharge_datetime` | Recorded discharge timestamp, when present. |
| `level_of_care` | Stored level of care. |
| `payer` | Payer associated with the episode, when present. |
| `authorization_start` | Recorded authorization start date, when present. |
| `authorization_end` | Recorded authorization end date, when present. |
| `discharge_disposition` | Recorded discharge disposition, when present. |
| `source_system` | Named source system recorded on the episode. |
| `evidence_class` | Stored categorical value present on the episode record. |

Stored `episode_relationship` values may include:

- `Initial`
- `LOC Transition`
- `Administrative Re-Admit`

Stored `level_of_care` values may include:

- `Detox`
- `Residential`

---

## 12. `claims`

Represents financial claims associated with treatment episodes.

| Column | Plain-English Meaning |
|---|---|
| `claim_id` | Unique identifier for a claim. |
| `episode_id` | EHR Episode identifier associated with the claim, when present. |
| `service_start_date` | First recorded date of service for the claim. |
| `service_end_date` | Last recorded date of service for the claim. |
| `payer` | Payer recorded on the claim. |
| `billed_amount` | Recorded billed amount. |
| `allowed_amount` | Recorded allowed amount, when present. |
| `patient_responsibility` | Recorded patient-responsibility amount, when present. |
| `claim_status` | Stored claim status. |
| `source_system` | Named source system recorded on the claim. |
| `evidence_class` | Stored categorical value present on the claim record. |

Stored `claim_status` values may include:

- `Submitted`
- `Pending`
- `Paid`
- `Denied`
- `Appealed`
- `Closed`

---

## 13. `claim_events`

Represents financial events associated with claims.

| Column | Plain-English Meaning |
|---|---|
| `claim_event_id` | Unique identifier for a claim event. |
| `claim_id` | Claim identifier associated with the event, when present. |
| `event_date` | Recorded date of the event. |
| `event_type` | Stored financial-event type. |
| `amount` | Recorded dollar amount for the event, when present. |
| `source_system` | Named source system recorded on the event. |
| `evidence_class` | Stored categorical value present on the event record. |

Stored `event_type` values may include:

- `Insurance Payment`
- `Patient Payment`
- `Adjustment`
- `Write-Off`
- `Denial`
- `Appeal`

---

## 14. Plain Structural Relationships

The following statements describe database structure only.

- A `contact` may be referenced by one or more `inquiries`.
- A `patient_opportunity` may be associated with more than one `inquiry`.
- An `inquiry` may be associated with an `acquisition_touch`.
- An `acquisition_touch` may exist without a linked `inquiry`.
- A `patient_opportunity` may reference an originating acquisition touch.
- A `patient_opportunity` may reference an originating professional referral.
- A `professional_account` may be associated with multiple `professional_referrals`.
- A `professional_account` may be associated with multiple `outreach_activities`.
- An `outreach_rep` may be referenced as the owner of multiple `professional_accounts`.
- An `outreach_rep` may be associated with multiple `outreach_activities`.
- A `professional_referral` may be associated with a Patient Opportunity.
- A `professional_referral` may exist without an associated Patient Opportunity.
- A `patient_opportunity` may be associated with one or more `ehr_episodes`.
- An `ehr_episode` may reference another EHR episode through `prior_episode_id`.
- An `ehr_episode` may be associated with one or more `claims`.
- A `claim` may be associated with one or more `claim_events`.

These statements describe how records can relate.

They do not imply that any relationship should occur at a particular frequency.

---

## 15. Storage Conventions

These are literal storage conventions only.

- IDs are stored as text.
- Dates and timestamps are stored as ISO-8601 text.
- Currency-like values are stored as SQLite `REAL`.
- Boolean-style values are stored as integers where `0` means false and `1` means true.
- Some relationship fields can be `NULL`.

This brief supplies no analytical rule for interpreting the frequency or significance of missing relationships.

---

## 16. Explicitly Not Provided

This brief intentionally does **not** provide:

- expected admission volume,
- expected conversion rates,
- expected payer mix,
- expected channel mix,
- expected campaign performance,
- expected representative performance,
- expected outreach activity,
- expected reciprocity,
- expected referral linkage,
- expected VOB outcomes,
- expected claim outcomes,
- definitions of healthy or unhealthy behavior,
- scenario names or scenario descriptions,
- affected campaigns,
- affected representatives,
- affected accounts,
- affected cohorts,
- conditional integrity rules,
- validation logic,
- generator logic,
- source-system hierarchy,
- evidence-provenance or trust-tier interpretation,
- degradation or failure-type frameworks,
- Ground-Truth conclusions,
- recommendations about which tables or fields to prioritize.

The analyst must determine relevance from the database itself.

---

## 17. Borderline Items — Final Review Record

The following items were explicitly reviewed before freeze.

### 17.1 `evidence_class`

The field remains listed because it physically exists in the database.

Its interpretation, taxonomy, provenance implications, and any relative trust hierarchy are intentionally omitted.

**Decision:** Keep as-is.

### 17.2 `match_confidence` and `attribution_confidence`

The literal stored values remain listed:

- `Confirmed`
- `Probable`
- `Possible`
- `Unmatched`

No instructions are provided for how these values should affect analysis.

**Decision:** Keep as-is.

### 17.3 `originating_influence_type`

The field and literal stored values remain listed.

No guidance is supplied about which influence type matters or how it should be analyzed.

**Decision:** Keep as-is.

### 17.4 `prior_episode_id` and `episode_relationship`

The brief describes the literal cross-record relationship and lists stored relationship values, while omitting all conditional integrity logic.

**Decision:** Keep as-is.

### 17.5 `reciprocated_flag`

The field is defined only as:

> `Stored 0/1 reciprocated indicator.`

No quality, engagement, or effectiveness interpretation is attached.

**Decision:** Keep with this stricter wording.

### 17.6 `professional_type` value list

The literal value `Interventionist` is retained because it is a stored professional-account category and does not identify, privilege, or hint at either scenario's affected cohort or mechanism.

**Decision:** Keep the full literal `professional_type` value list as-is.

---

## 18. Blind-Test Use

This exact document must be copied unchanged into both isolated analysis environments.

Scenario 1 and Scenario 2 must receive the identical brief.

No scenario-specific annotation, filename change, explanatory note, or added field guidance may be introduced between the two runs.

**Approved blind-test locations:**

```text
harbor-ridge-blind-test/scenario-1/
harbor-ridge-blind-test/scenario-2/
```

**Status: FROZEN — ready for blind-test use.**

**End of Harbor Ridge V1 — Phase D Neutral Analyst Brief**
