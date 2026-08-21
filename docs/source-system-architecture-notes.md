# Harbor Ridge V1 — Source-System Architecture Notes

## Purpose

This document records architectural decisions established during the Harbor Ridge V1 domain-expert interview.

The goal is to define how acquisition, admissions, telephony, CRM, EHR, and other source-system evidence should eventually connect within the Patient Acquisition & Executive Insight Engine.

These notes represent the current architecture and will inform the Source-System Map, Canonical Data Model, Data Dictionary, Measurement Specification, and synthetic dataset.

---

## Core Journey Model

The emerging Harbor Ridge journey is:

Acquisition Touch  
→ Contact Method  
→ Inquiry Record  
→ Patient Opportunity  
→ Clinical Qualification  
→ Verification of Benefits (VOB)  
→ Financial Fit  
→ Readiness  
→ Admission Candidate  
→ Logistics  
→ Arrival  
→ Completed Admission  
→ EHR / Treatment Outcome

A single Patient Opportunity may contain multiple acquisition touches, inquiry records, callers, and source-system identifiers.

---

## Acquisition Architecture

Acquisition should not be represented as a single flat source field.

The architecture distinguishes:

**Acquisition Channel**  
→ **Acquisition Source**  
→ **Source Detail**  
→ **Contact Method**  
→ **Inquiry Record**  
→ **Patient Opportunity**

Examples include:

- Paid Search → Google Ads → Campaign / Ad Group / Keyword → Phone Call
- Paid Search → Google Ads → Campaign / Ad Group / Keyword → Web Form
- Paid Search → Microsoft Ads → Campaign / Ad Group / Keyword → Phone Call or Web Form
- Paid Social → Meta Ads → Campaign / Ad Set / Ad → Phone Call or Web Form
- Organic Search → Google Organic → Landing Page / Content → Phone Call or Web Form
- Healthcare Directory → Psychology Today → Listing / Profile → Phone Call or Web Form
- Professional Referral → Therapist / Psychiatrist → Individual or Practice → Phone Call
- Hospital / Clinical Referral → Hospital / Crisis Center → Facility / Department → Phone Call
- Alumni / Patient Referral → Alumni → Referral Relationship → Phone Call or Web Form
- Direct / Brand → Direct → Phone or Web
- Other → Other Identifiable Source

### Healthcare Directories

Healthcare Directory should exist as a distinct acquisition category rather than treating individual directory sites as equivalent to paid-media platforms.

A directory may generate inquiries through a free listing, paid listing, paid placement, or other relationship.

---

## Calls and Web Forms

Calls and web forms must remain analytically distinct contact methods.

They should not be collapsed into a generic conversion event.

This distinction allows executives to ask questions such as:

> How are web-form leads performing versus calls this month?

or:

> Are calls converting to viable VOBs at a higher rate than web forms?

The two contact methods may originate from the same acquisition source while producing substantially different downstream behavior.

---

## Patient Opportunity vs. Inquiry

An Inquiry Record is not necessarily equivalent to a Patient Opportunity.

One prospective patient may generate:

- multiple calls
- multiple web forms
- calls from different family members
- a professional referral
- repeat contacts over several days
- duplicate CRM records

These interactions should ultimately resolve to a canonical Patient Opportunity whenever sufficient evidence exists.

Example canonical identifier:

`opportunity_id = HRO-000184`

Source-system identifiers remain separate, including:

- `call_id`
- `form_submission_id`
- `crm_lead_id`
- `admission_id`
- `encounter_id`
- platform click identifiers

The Harbor Ridge opportunity ID is a canonical analytical identifier. It should not be assumed to originate in the telephony system, CRM, or EHR.

---

## Identity Resolution

Telephony systems recognize callers, phone numbers, browser sessions, and returning callers.

They do not inherently understand households, loved ones, or prospective-patient opportunities.

For example:

- Mother calls from one phone number.
- Father calls the next day from another number.
- Patient calls later from a third number.

The telephony system may initially see three unrelated callers even though all three interactions belong to one Patient Opportunity.

Potential contact roles include:

- Patient
- Loved One
- Professional Referral Source
- Other
- Unknown

Identity resolution must therefore occur downstream through CRM workflows, human reconciliation, stronger patient identifiers, or the canonical Harbor Ridge model.

---

## Duplicate Records

Duplicate leads should be treated as a structural characteristic of the behavioral-health acquisition environment rather than an exceptional error.

Duplicates may result from:

- separate calls from family members
- different phone numbers or email addresses
- directory leads followed by direct website submissions
- disconnected CRM and EHR systems
- shift changes
- manual entry errors
- weak CRM deduplication rules
- separate telephony and CRM records

Potential identity evidence includes:

### Strong Evidence

- Insurance Member ID
- Patient Date of Birth

### Moderate Evidence

- Patient Phone
- Patient Email

### Contextual Evidence

- Loved-One Phone
- Loved-One Email
- Patient Name
- Address
- Timing

Potential future match states may include:

- Confirmed
- Probable
- Possible
- Unmatched

These states are architectural concepts and are not yet finalized data-dictionary fields.

---

## Paid-Search Attribution

The trusted baseline paid-search chain is:

Google Ads  
→ Campaign  
→ Ad Group  
→ Keyword  
→ Landing Page  
→ Tracking Number / DNI  
→ Call

**Keyword and Search Term are not equivalent.**

Keyword represents the purchased/bidded targeting construct.

Search Term represents the user's actual query and may be incompletely observable because search-query visibility can be restricted.

Search Term should therefore remain outside the baseline trusted attribution chain and should carry its own availability and reliability considerations.

---

## Telephony Source-System Ownership

Telephony owns the call evidence.

A properly configured telephony/call-tracking platform may retain:

- `call_id`
- `caller_phone`
- `tracking_number`
- `tracking_source`
- `source`
- `medium`
- `campaign`
- `ad_group`
- `keyword`
- platform click identifier where available
- `landing_page`
- `referring_url`
- `call_timestamp`
- `call_duration`
- `answered_status`
- `agent_id`
- `returning_caller_flag`
- `previous_call_count`
- `recording_reference`

Not every call will contain every field.

The CRM may receive copies of some or all of this evidence through an integration. That does not make the CRM the authoritative origin of the data.

---

## Source-System Ownership Principle

A field should retain its authoritative source-system provenance.

Conceptually:

**Marketing Platform**
- Campaign
- Ad Group
- Keyword
- Spend
- Clicks
- Impressions

**Telephony**
- Call ID
- Tracking Number
- Caller
- Call Duration
- Answered / Missed Status
- Recording Reference
- Call-Level Attribution Evidence

**CRM / Admissions**
- Lead / Opportunity Workflow
- Status
- Disposition
- Admissions Notes
- VOB Progression
- Readiness / Admission Workflow

**EHR**
- Completed Admission
- Encounter
- Treatment Progression
- Discharge / Outcome Evidence

**Canonical Harbor Ridge Model**
- Cross-system Patient Opportunity
- Cross-system identifier resolution
- Analytical lineage

A downstream copy of an upstream field does not become its authoritative origin.

---

## Telephony-to-CRM Integration States

### State A — Strong Integration

Telephony evidence passes downstream through API, webhook, or native integration while preserving source provenance.

### State B — Partial / Fragmented Integration

Telephony, CRM, and EHR may each contain accurate information internally but fail to share enough identifiers to reconstruct the complete patient-acquisition journey.

This represents a data-lineage failure rather than necessarily a data-collection failure.

### State C — Manual Reconciliation

Organizations may reconcile completed admissions retrospectively through spreadsheets or exports.

A typical process may resemble:

EHR Admission Export  
→ Spreadsheet / CSV  
→ Marketing + IT Reconciliation  
→ CRM Match  
→ Telephony Lookup  
→ Retrospective Attribution

Marketing and IT commonly need to work together to produce the most accurate reconciliation.

---

## Attribution History

New attribution evidence should append to the patient journey rather than overwrite the original acquisition evidence.

The architecture should eventually support views such as:

- First-Touch Attribution
- Last-Touch Attribution
- Multi-Touch Journey
- Original Acquisition Source
- Most Recent Known Source

The architecture should preserve the evidence required to calculate these perspectives rather than prematurely declare one attribution model to be objective truth.

---

## Evidence Provenance

Data availability does not equal data reliability.

The system must distinguish among:

### System-Observed Evidence

Examples:

- Call Duration
- Timestamp
- Tracking Number
- Campaign
- Landing Page

### Human-Entered Evidence

Examples:

- Disposition
- "How did you hear about us?"
- Admissions Notes
- Loss Reason

### AI-Derived Evidence

Examples:

- Automated Call Summary
- Topic Detection
- Sentiment
- AI-Inferred Insurance Concern

These evidence types should not automatically receive equal analytical weight.

---

## Admissions Dispositions

Hard operational gates tend to produce more reliable structured dispositions, such as:

- No Accepted Insurance
- No OON Benefits
- Financially Infeasible
- Clinically Inappropriate
- Medical Clearance Required / Higher Level of Care

Behavioral or progression dispositions may be less reliable:

- Patient Unwilling
- Unable to Contact
- Went Elsewhere
- Loved-One Inquiry / Patient Not Engaged
- No-Show
- Changed Mind

Catch-all dispositions such as `Referred Out`, `Closed/Lost`, `Inquiry Nurturing`, or `Other` may obscure the actual reason contained in narrative notes.

The architecture should preserve both structured disposition data and free-text notes where available.

---

## Measurement Degradation Framework

Four distinct forms of measurement degradation have been identified.

### 1. Observability Loss

The evidence exists conceptually but cannot be fully observed.

Example:

Search Term is unavailable or suppressed.

### 2. Identity Loss

The organization cannot determine that multiple interactions belong to the same Patient Opportunity.

Example:

Mother, father, and patient appear as three unrelated leads.

### 3. Attribution Loss

Acquisition evidence exists upstream but does not survive a downstream system handoff.

Example:

CTM knows the Google Ads campaign and keyword, but the CRM only records `Google`.

### 4. Outcome-Linkage Loss

The organization cannot reliably connect the acquisition/admissions record to the final business outcome.

Example:

A CRM opportunity cannot be confidently connected to the completed EHR admission.

These four failure types should remain analytically distinct.

---

## Current Source-System Interview Status

Completed:

- [x] Admissions Funnel
- [x] CRM / Admissions Data
- [x] Telephony / Call Tracking

Remaining:

- [ ] Web / Digital Analytics + Web Forms
- [ ] Marketing Platforms
- [ ] SEO / Organic Search
- [ ] Professional Referral / Business Development
- [ ] EHR / Billing / Revenue Outcomes

---

## Next Interview Category

**Web / Digital Analytics + Web Forms**

The next interview begins with:

> When someone arrives on Harbor Ridge's website and submits a treatment inquiry form, what information do you believe a well-configured organization should capture about that visitor and submission, and what have you actually seen survive into the CRM in practice?

The same analytical discipline used for Telephony will be applied:

1. What exists?
2. What is reliable?
3. What survives the handoff?
4. What can an executive legitimately conclude from it?

---
---

## Source-System Interview Progress — August 21, 2026

### Web / Digital Analytics + Forms — COMPLETE

The Harbor Ridge V1 source-system interview established the web-form pathway as a distinct acquisition and inquiry mechanism rather than treating all digital conversions as equivalent.

Key architectural findings:

- Patient/referrer-facing web forms should remain intentionally minimal to reduce conversion friction.
- A representative behavioral-health inquiry form may contain:
  - First Name
  - Last Name
  - Email
  - Phone
  - How Can We Help?
- Marketing attribution should be captured passively where technically and legally appropriate rather than requiring the prospective patient or loved one to supply it manually.
- Web-form inquiries generally enter the CRM before clinical information is transferred to the EHR.
- Form routing may involve:
  - Admissions Director assignment
  - Direct assignment to an Admissions Representative
  - Round-robin distribution
  - Dedicated intake teams
- Website conversion events and CRM inquiries must remain separate business facts because analytics systems count actions while CRMs generally attempt to represent people/opportunities.
- Duplicate submissions, spam filtering, validation failures, privacy controls, script failures, and integration/API failures can create discrepancies between analytics conversions and CRM inquiries.
- First-touch and subsequent-touch evidence should be preserved rather than forcing the system to choose a single attribution narrative prematurely.
- High-intent landing-page behavior, form starts, form completions, geographic alignment, VOB progression, and speed-to-lead are substantially more useful operational signals than aggregate traffic alone.
- The web-form pathway should ultimately support reconciliation through:

  Web Visit → Form Interaction → Form Submission → CRM Inquiry → VOB → Admission

### Marketing Platforms — COMPLETE

The Harbor Ridge V1 interview established that advertising-platform data is valuable evidence but is not itself the source of truth for business outcomes.

Key architectural findings:

- Preserve the paid-search hierarchy:

  Platform → Account → Campaign → Ad Group → Keyword → Search Term

- Preserve the Meta hierarchy separately:

  Platform → Account → Campaign → Ad Set → Ad / Creative

- Platform metrics such as spend, impressions, clicks, CPC, CTR, impression share, frequency, CPM, campaign settings, match type, bidding strategy, geography, and creative context are valuable for reconstructing acquisition conditions.
- Platform-reported conversions must not automatically be treated as inquiries, VOBs, admissions, or revenue.
- Platform conversion counts and CRM inquiry counts should coexist so discrepancies can be diagnosed rather than silently reconciled away.
- Search-term evidence should remain distinct from purchased/bidded keyword evidence.
- Historical change data is critical for forensic reconstruction.
- Preserve material account changes including:
  - Bidding strategy changes
  - Network changes
  - Conversion-action changes
  - Keyword and match-type changes
  - Negative-keyword changes
  - Automated recommendation changes
  - Budget changes
  - Geographic targeting changes
  - Ad/creative changes
- Marketing effectiveness should ultimately be evaluated against downstream business outcomes rather than platform CPA alone.
- Clinical decision-making must remain operationally separate from marketing optimization.

### SEO / Organic Search — COMPLETE

The Harbor Ridge V1 interview established that aggregate organic traffic is insufficient for evaluating behavioral-health acquisition performance.

Key architectural findings:

- Organic traffic must be separated by intent and landing-page function.
- Commercial/high-intent organic traffic and informational organic traffic should remain analytically distinguishable.
- Preserve Google Search Console query-to-page evidence rather than relying exclusively on aggregated keyword-ranking reports.
- Preserve historical website architecture, redirects, page changes, and content publication history so organic failures can be reconstructed retrospectively.
- Content should be evaluated against downstream business contribution, including inquiry, VOB, and admission evidence where linkage is available.
- Local organic discovery should remain distinguishable from conventional website organic search.

Harbor Ridge should preserve at least three organic interaction pathways:

1. Google Business Profile / Maps
   → Dedicated static/source-specific tracking number
   → Call
   → Inquiry
   → VOB
   → Admission

2. Google Organic Search
   → Organic Landing Page
   → Website DNI
   → Call
   → Inquiry
   → VOB
   → Admission

3. Google Business Profile / Maps
   → UTM-tagged Website Link
   → Website
   → DNI or Form
   → Inquiry
   → VOB
   → Admission

Local/Maps attribution should therefore be modeled using separate concepts for:

- Acquisition Channel
- Acquisition Subchannel
- Source Platform
- Interaction Type
- Tracking Method

SEO failure analysis should compare:

- Commercial vs. informational traffic
- Query-to-page performance
- Historical rankings and impressions
- Website/page/redirect changes
- Local/Maps performance
- Analytics-to-CRM linkage
- VOB quality
- Admission outcomes

The architecture should identify evidence of contribution without automatically asserting causality.

### Current Source-System Interview Status

- Admissions Funnel — COMPLETE
- CRM / Admissions — COMPLETE
- Telephony / Call Tracking — COMPLETE
- Web / Digital Analytics + Forms — COMPLETE
- Marketing Platforms — COMPLETE
- SEO / Organic Search — COMPLETE
- Professional Referral / Business Development — REMAINING
- EHR / Billing / Outcomes — REMAINING

Six of the eight planned source-system interview categories are now complete.

### Architecture Principle Reinforced

Harbor Ridge V1 should not force disparate systems into one flattened attribution table.

The architecture should preserve:

1. Source-system evidence
2. Business facts
3. Identity-resolution evidence
4. Attribution evidence
5. Derived analytical conclusions

The system should preserve what each source actually knows, explicitly represent uncertainty and broken handoffs, and reconstruct the patient opportunity across systems without manufacturing precision that the underlying evidence cannot support.
## Development Rule

**Build deeply before expanding broadly.**

Harbor Ridge Behavioral Health Version 1 remains the sole development priority until the framework has been built, tested, documented, and validated.
---

## Professional Referral / Business Development

### Source-System Role

Professional Referral / Business Development represents a distinct acquisition pathway that cannot be treated as a simple marketing-source field.

Unlike digital acquisition, professional referral attribution depends heavily on human recognition, relationship management, intake documentation, and persistent linkage between the referring professional and the patient opportunity.

The canonical model should distinguish:

- Professional Account
- Outreach Representative / Account Owner
- Referral Event
- Patient Opportunity
- VOB Outcome
- Admission Outcome

A completed admission alone is not sufficient to evaluate professional referral performance.

### Professional Referral Intake

Ideally capture:

- Referring professional name
- Practice / organization
- Professional type / license
- Contact information
- NPI when applicable
- Patient identity and contact information
- Insurance / VOB information
- Referral context
- Clinical urgency
- Communication expectations
- Release-of-information status when relevant
- Primary Professional Account
- Assigned outreach representative / account owner

### Attribution Risk

Professional referral attribution is highly vulnerable to human-entry failure.

Common failure points include:

- Intake staff focusing on the patient crisis and failing to capture the referrer
- Referrer information being stored only in free-text notes
- Patients or family members failing to mention the referring professional
- Outreach representatives receiving no credit for relationships they developed
- Digital attribution claiming a lead that was actually initiated by a professional relationship
- Referral-source information disappearing during CRM-to-EHR handoff

Digital systems claim attribution automatically. Professional relationships often require explicit human recognition.

Therefore:

**Arrival channel and referral influence must be modeled separately.**

A patient may arrive through Google Organic, Paid Search, phone, or a web form while the true initiating influence was a professional referral.

### Professional Account Ownership

Professional relationships should be governed by explicit Rules of Engagement.

The system should distinguish:

- Primary Account Owner
- Assisting Representative
- Clinical / Executive Influence
- Verified Relationship Activity
- Referral Events
- Resulting Patient Opportunities

Account ownership should not be inferred solely from territory or the person who happened to receive the most recent call.

### Relationship Health

Professional-account performance should be evaluated through the full funnel:

Professional Account
→ Referral
→ Patient Opportunity
→ VOB
→ Admission

Referral representatives should not be evaluated solely on completed admissions because downstream outcomes may be affected by:

- Insurance incompatibility
- Patient choice
- Clinical appropriateness
- Admissions execution
- Payer restrictions

Relationship-decay detection should combine:

- Historical referral baseline
- Time since last referral
- Recent outreach activity
- Reciprocity of communication
- Prior-patient follow-up history

Silence alone is not proof of relationship decay.

### Executive BD Portfolio Signals

The proposed 15-minute Professional Referral / BD screen includes:

1. Portfolio Concentration Risk
2. Relationship Velocity
3. New Account Activation Yield
4. Account-Level Payer Viability
5. Rep Activity-to-Yield Efficiency
6. VOB-to-Admission Conversion
7. Unreciprocated Outreach / Relationship-Decay Flags

These metrics should distinguish between:

- Signals strong enough to support action
- Signals requiring additional investigation

---

## EHR / Billing / Revenue Outcomes

### Source-System Role

The EHR owns admission and treatment evidence.

Billing / RCM systems own claim, remittance, adjustment, and collection evidence.

The canonical Harbor Ridge layer must preserve these source boundaries rather than treating downstream clinical and financial information as a single dataset.

### Identity Architecture

A person, opportunity, episode of care, level-of-care segment, claim, and payment are separate entities.

The preferred deterministic identity chain is:

CRM Opportunity ID
→ EHR Episode / Patient ID
→ RCM Patient / Claim Identifier
→ Remittance / Payment Record

Deterministic identifiers should survive system boundaries wherever technically possible.

When deterministic linkage is unavailable, reconciliation may require:

Name + DOB + Date of Service + Payer

These matches should be treated as probabilistic and may require human review.

### Episode-of-Care Modeling

A behavioral-health treatment journey may appear as:

- One admission with Level-of-Care transfers

or

- Multiple discharge / readmission records across Detox and Residential

Therefore:

**PERSON ≠ OPPORTUNITY ≠ EPISODE ≠ LEVEL-OF-CARE SEGMENT**

Raw admission counts cannot automatically be interpreted as unique patients or unique acquisition events.

V1 downstream clinical scope remains limited to:

- Early AMA
- Detox completion
- Detox-to-Residential transition
- Residential completion
- Financial / reimbursement outcome

More expansive clinical, revenue-cycle, and longitudinal outcome measures remain outside the current V1 scope.

### Financial Architecture

Bed utilization does not equal realized financial value.

The financial progression is:

Billed Charges
→ Allowed Amount
→ Insurance / Patient Responsibility
→ Adjustments / Write-offs
→ Appeals
→ Actual Collections

These values must not be collapsed into a single `Revenue` field.

Financial information also matures over time.

The canonical layer should therefore preserve cohort maturity and distinguish between:

**Operational / Leading View**

Spend
→ Inquiry
→ VOB
→ Admission
→ LOC
→ LOS
→ Payer

and:

**Financial / Lagging View**

Spend
→ Mature Episode Cohort
→ Claims
→ Adjustments
→ Appeals
→ Actual Collections

Recent cohorts should not be compared directly with mature cohorts as though their financial data were equally complete.

### Last-Mile Financial Attribution

One treatment episode may generate:

- Multiple claims
- Multiple remittances
- Multiple insurance payments
- Patient-responsibility payments
- Adjustments
- Appeals
- Delayed recoveries

Therefore, a Claim ID cannot serve as the ultimate business key.

Preferred hierarchy:

Episode of Care
→ Claims
→ Remittances
→ Patient Payments
→ Adjustments / Appeals
→ Collected Cash

Readmissions must remain associated with the correct opportunity and episode so historical acquisition events do not incorrectly absorb later financial outcomes.

### Financial Attribution Evidence Standard

Before the system reports that collected revenue originated from a specific CRM opportunity or acquisition source, the preferred evidence includes:

1. CRM Opportunity ↔ EHR identity linkage
2. Episode / Date-of-Service ↔ RCM claim linkage
3. Remittance / payment evidence
4. Appeal / adjustment audit trail when applicable

When this deterministic evidence is incomplete, the system should expose the uncertainty rather than manufacture a definitive attribution.

### Executive Downstream Signals

The proposed 15-minute downstream executive screen includes:

1. Early AMA Velocity
2. Detox-to-Residential Step-Down Continuity
3. Days Sales Outstanding by Payer
4. Utilization Review Authorization Deficit
5. First-Pass Denial Rate
6. Cash Collected per Completed Admission for mature cohorts
7. CRM → EHR → RCM Identity Integrity Rate

Example thresholds discussed during discovery should be treated as configurable Harbor Ridge targets or historical baselines, not universal healthcare standards.

### Evidence State

Executive metrics should carry sufficient context to determine whether the number deserves action.

Where available, the canonical layer should preserve:

- Current Value
- Historical Baseline
- Configured Target / Threshold
- Source System
- Data Freshness
- Identity-Match Confidence
- Cohort Maturity
- Decision State

Decision states:

- `ACT`
- `INVESTIGATE`
- `INSUFFICIENT_EVIDENCE`

The system should be capable of saying that the evidence is insufficient rather than presenting false precision.

---

## Source-System Interview Status

| Source-System Category | Status |
|---|---|
| Web / Digital + Forms | COMPLETE |
| Marketing Platforms | COMPLETE |
| SEO / Organic | COMPLETE |
| Professional Referral / Business Development | COMPLETE |
| EHR / Billing / Revenue Outcomes | COMPLETE |

**SOURCE-SYSTEM INTERVIEW PHASE: COMPLETE**

### Architectural Findings to Carry Forward

The completed interviews establish the following principles for the Harbor Ridge canonical layer:

1. Preserve source-system ownership and provenance.
2. Separate people, opportunities, episodes, LOC segments, claims, and payments.
3. Prefer deterministic identifiers across system boundaries.
4. Assign confidence and human-review requirements to probabilistic matches.
5. Preserve referral influence separately from arrival channel.
6. Preserve financial cohort maturity.
7. Model revenue as financial events associated with episodes rather than one static field.
8. Reconcile marketing performance against CRM, VOB, admission, treatment, and realized financial outcomes.
9. Preserve metric provenance, freshness, identity confidence, and evidence state.
10. Expose uncertainty rather than manufacture certainty.

**Discovery milestone:** The planned source-system interview phase is complete.

**Next phase:** Source-System Map → Canonical Data Model → Measurement Specification → Harbor Ridge V1 build.
