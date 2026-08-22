# Harbor Ridge V1 Source-System Map

**Version:** 1.0  
**Status:** Final / Approved  
**Approved:** August 21, 2026  
**Project:** Healthcare Executive Operating System (HEOS)  
**Use Case:** Harbor Ridge Behavioral Health V1

---

## 1. Purpose

The Harbor Ridge V1 Source-System Map defines how patient-acquisition, referral, clinical, billing, and financial data move through the Harbor Ridge operating environment.

Its purpose is to establish the minimum architecture required to reconstruct the patient journey from first observable acquisition activity through actual collected revenue while preserving uncertainty, attribution boundaries, identity relationships, and known data-quality limitations.

The map is intentionally limited to the Harbor Ridge V1 portfolio project.

It is not a production healthcare data architecture, EHR implementation specification, billing platform design, or enterprise data warehouse blueprint.

---

## 2. Executive Architecture

Harbor Ridge V1 is organized into six operational layers:

| Layer | Business Question | Primary Systems |
|---|---|---|
| 1. Acquisition | What created awareness, intent, or referral activity? | Google Ads, Microsoft Ads, Meta, Google Search Console, Google Business Profile, professional outreach |
| 2. Inquiry Capture | How did the person actually contact Harbor Ridge? | Web forms, call tracking, phone system, CRM |
| 3. Opportunity / Qualification | Did the inquiry become a legitimate patient opportunity? | CRM, VOB workflow, admissions |
| 4. Clinical Episode | Did the patient admit, and what happened during treatment? | EHR |
| 5. Revenue Cycle | What was billed, allowed, denied, appealed, and paid? | EHR billing interfaces, RCM / clearinghouse |
| 6. Executive Intelligence | What caused the observed business outcome? | Relational analytical layer / HEOS AI reasoning |

The architecture follows the operating funnel:

```text
Acquisition
    ↓
Inquiry Capture
    ↓
Patient Opportunity
    ↓
VOB / Qualification
    ↓
Admission
    ↓
EHR Episode(s)
    ↓
Claim(s)
    ↓
Payment(s) / Adjustment(s)
    ↓
Collected Revenue
    ↓
Executive Analysis
```

---

## 3. Layer 1 — Acquisition Systems

The acquisition layer describes how Harbor Ridge creates or receives demand.

### Paid Media

Primary sources:

- Google Ads
- Microsoft Ads
- Meta Ads

Relevant entities include:

- Platform
- Account
- Campaign
- Ad Group / Ad Set
- Keyword
- Search Term
- Match Type
- Creative / Ad
- Geographic targeting
- Device
- Spend
- Impressions
- Clicks
- Platform conversions
- Bidding strategy
- Campaign type
- Change history

Platform conversions are not treated as equivalent to CRM inquiries, VOBs, admissions, or revenue.

They represent platform-observed events and must be reconciled against downstream operational systems.

### Organic Search

Primary sources:

- Google Search Console
- GA4
- Google Business Profile
- Website / CMS

Relevant entities include:

- Search query
- Landing page
- Organic sessions
- Geographic location
- Search impressions
- Search clicks
- Average search position
- Commercial vs. informational page classification
- Local / Maps interaction
- Website structural changes
- Redirect history

Total organic traffic alone is not considered evidence of acquisition health.

Commercial intent, geography, inquiry generation, VOB viability, and downstream admissions must be evaluated separately.

### Professional Referral / Business Development

Primary sources:

- CRM professional accounts
- Outreach activity records
- Call tracking
- Intake attribution
- Professional referral records

Professional referral attribution is modeled separately from the mechanism through which the patient ultimately arrives.

For example:

```text
Psychiatrist referral
        ↓
Patient later searches Harbor Ridge
        ↓
Patient submits website form
```

The arrival mechanism is **Organic / Web Form**.

The originating professional influence remains **Professional Referral** if supported by sufficient evidence.

This distinction prevents digital systems from automatically absorbing credit for referral relationships.

---

## 4. Layer 2 — Inquiry Capture

Inquiry Capture records the actual inbound interaction with Harbor Ridge.

Primary systems:

- Web forms
- Call tracking
- Phone system
- CRM

Calls and forms remain separate source events because their collection mechanisms, attribution reliability, and failure modes differ.

### Web Form Inquiry

Potential fields include:

- Inquiry ID
- Timestamp
- Form ID
- Landing page
- Acquisition source
- Campaign ID
- Session / tracking identifiers
- Contact information
- CRM creation status

### Phone Inquiry

Potential fields include:

- Inquiry ID
- Timestamp
- Tracking number
- Caller number
- Call duration
- Call disposition
- Acquisition source
- Professional referral indicator
- CRM creation status

The CRM inquiry represents a human or human-associated inbound interaction.

It is not assumed that:

```text
1 platform conversion = 1 inquiry
```

or that:

```text
1 inquiry = 1 patient opportunity
```

---

## 5. Layer 3 — Patient Opportunity

The **Patient Opportunity** is the central commercial entity in Harbor Ridge V1.

A Patient Opportunity represents a potential episode of care being evaluated for Harbor Ridge.

Canonical identifier format:

```text
HRO-######
```

Example:

```text
HRO-000184
```

The Patient Opportunity becomes the primary parent identifier connecting acquisition, inquiry, qualification, admission, clinical episode, and financial outcomes.

### 5.1 Why Inquiry and Opportunity Are Separate

Multiple inquiries may represent one Patient Opportunity.

Example:

```text
Monday:
Mother calls Harbor Ridge.

Tuesday:
Father submits website form.

Wednesday:
Patient calls admissions.

Result:
3 inquiries
1 Patient Opportunity
```

Without identity resolution, Harbor Ridge could incorrectly report three independent leads.

### 5.2 Contact Roles

Contacts associated with an opportunity may have different roles:

- Patient
- Loved One / Family Member
- Professional Referral Source

Contact identity must therefore remain separate from Patient Opportunity identity.

### 5.3 Opportunity Relationships

Conceptually:

```text
PATIENT OPPORTUNITY
        │
        ├── Inquiry 1 — Mother
        ├── Inquiry 2 — Father
        ├── Inquiry 3 — Patient
        └── Professional Referral — Psychiatrist
```

This allows the model to preserve multiple acquisition and communication events without inflating the number of genuine patient opportunities.

### 5.4 Attribution

The Patient Opportunity should preserve both:

- **Arrival mechanism**
- **Originating influence**

when supported by evidence.

Example:

```text
Originating Influence:
Dr. Jane Smith / Professional Referral

Arrival Mechanism:
Google Organic → Website Form
```

These should not automatically overwrite one another.

### 5.5 Identity Resolution

Identity resolution determines whether separate contacts and inquiries represent the same Patient Opportunity.

Harbor Ridge V1 uses four match-confidence states:

| Match State | Meaning |
|---|---|
| Confirmed | Evidence establishes that the records represent the same Patient Opportunity |
| Probable | Strong evidence suggests a match, but deterministic proof is unavailable |
| Possible | Some evidence suggests a relationship, but uncertainty remains significant |
| Unmatched | No defensible relationship has been established |

Identity uncertainty must be preserved rather than silently converted into certainty.

A probabilistic match should never be represented as a deterministic match merely to improve reporting completeness.

---

## 6. VOB and Admission Financial Status

Verification of Benefits is a major operational gate between inquiry and admission.

### VOB Outcome

Harbor Ridge V1 distinguishes among:

- Submitted
- Pending
- Viable
- Non-Viable
- Unable to Verify

VOB viability represents the organization's current understanding of reimbursement feasibility.

It does not independently determine whether a patient will or should be admitted.

### Admission Financial Status

Admission financial status is modeled separately from VOB outcome.

Relevant states include:

- Financially Cleared
- At-Risk Admission
- Financially Declined / Not Cleared
- Pending Financial Resolution

An **At-Risk Admission** represents a clinically appropriate admission that Harbor Ridge elects to accept despite unresolved or uncertain reimbursement.

This distinction preserves a core operating reality:

```text
Clinical appropriateness
        ≠
Guaranteed reimbursement
```

The data model must not imply that VOB viability mechanically controls clinical admission decisions.

---

## 7. Professional Referral Attribution

Professional referral relationships require a distinct attribution model.

A professional account may generate:

```text
Professional Account
        ↓
Referral Opportunity
        ↓
VOB
        ↓
Admission
```

But the patient may arrive through:

- Direct professional call
- Patient phone call
- Family phone call
- Email or text coordination
- Website form
- Organic search
- Paid search

Therefore:

```text
Referral Source
        ≠
Arrival Channel
```

Harbor Ridge V1 preserves both whenever evidence exists.

### Representative Professional Entities

Relevant entities include:

- Professional Account
- Outreach Representative
- Account Owner
- Referral Event
- Patient Opportunity
- Outreach Activity
- Referral Outcome

Professional attribution must not depend solely on completed admissions.

A legitimate professional relationship can generate valid opportunities that fail downstream because of:

- payer incompatibility,
- clinical mismatch,
- patient choice,
- admission capacity,
- or other operational factors.

---

## 8. Layer 4 — Clinical Episode / EHR

Once the patient admits, the EHR becomes the primary clinical system of record.

Example EHR episode identifier:

```text
KIPU-9921
```

The EHR may contain:

- Admission date/time
- Program
- Level of Care
- Bed assignment
- Payer information
- Authorization windows
- Diagnoses
- Assigned clinicians
- Level-of-care transfers
- Discharge date
- Discharge disposition

### Episode Fragmentation

One Patient Opportunity may generate more than one EHR episode.

Example:

```text
HRO-000184
     │
     ├── KIPU-9921 — Detox
     │
     └── KIPU-10002 — Residential
```

This may occur when operational or billing configuration requires discharge and readmission between levels of care.

Therefore:

```text
1 Patient Opportunity
        ≠
necessarily 1 EHR Episode
```

Harbor Ridge must avoid counting administrative episode fragmentation as multiple independently acquired patients.

---

## 9. The Golden Thread

The central identity chain is:

```text
PATIENT OPPORTUNITY ID
        ↓
HRO-000184
        ↓
EHR EPISODE ID(S)
        ↓
KIPU-9921
        ↓
RCM CLAIM ID(S)
        ↓
CL-88127
        ↓
PAYMENT / ADJUSTMENT RECORD(S)
```

The Patient Opportunity ID is the preferred parent identifier for acquisition attribution.

Where possible, deterministic identifiers should bridge systems.

The preferred relationship is:

```text
CRM Opportunity ID
        ↓
EHR Episode ID
        ↓
RCM Claim ID
        ↓
Payment / Adjustment
```

If deterministic identifiers are unavailable, matching may require:

```text
Name
+
Date of Birth
+
Date of Service
+
Payer
```

Such matches must retain their confidence level and should not be silently treated as deterministic.

---

## 10. Layer 5 — Claims, Billing, and Collections

The RCM / billing environment becomes the financial system of record after services are delivered.

Relevant entities include:

- Claim ID
- EHR Episode ID
- Dates of Service
- Payer
- Billed Charges
- Allowed Amount
- Insurance Payment
- Patient Responsibility
- Adjustment
- Write-Off
- Denial
- Appeal
- Payment Date
- Actual Cash Collected

One EHR Episode may generate multiple claims.

One Claim may generate multiple:

- payments,
- adjustments,
- denials,
- appeals,
- or remittance events.

Therefore:

```text
Patient Opportunity
        1
        │
        ├── many Inquiries
        │
        └── many EHR Episodes
                 │
                 └── many Claims
                          │
                          └── many Payments / Adjustments
```

### Financial Truth

Harbor Ridge distinguishes among:

```text
Billed Charges
        ↓
Allowed Amount
        ↓
Expected Revenue
        ↓
Actual Collections
```

Actual collected cash is the strongest retrospective financial outcome for evaluating mature acquisition cohorts.

Recent cohorts must not be judged as though their revenue cycle were complete.

---

## 11. Cohort Maturity

Revenue outcomes mature over time.

Harbor Ridge V1 therefore distinguishes between immediate operational outcomes and mature financial outcomes.

Representative timeline:

| Cohort Age | Interpretation |
|---|---|
| 0–30 days | Operational / early billing data |
| 31–60 days | Initial payment visibility |
| 61–90 days | Emerging financial trajectory |
| 90–180 days | Increasingly mature collections |
| 180+ days | Appropriate for retrospective financial evaluation |

This prevents recent cohorts from appearing artificially unprofitable merely because claims remain unresolved.

---

## 12. Canonical Data Degradation Framework

Harbor Ridge V1 recognizes four analytically distinct forms of data degradation.

### 12.1 Observability Loss

The event occurred, but the system failed to observe it.

Example:

```text
Patient submits form
        ↓
CRM receives inquiry
        ↓
Browser blocks advertising conversion tag
```

The business event exists, but the marketing platform cannot see it.

### 12.2 Identity Loss

Multiple records represent the same underlying Patient Opportunity, but the relationship cannot be established reliably.

Example:

```text
Mother calls Monday
Father submits form Tuesday
Patient calls Wednesday
        ↓
3 inquiry records
        ↓
Identity resolution fails
        ↓
3 apparent leads instead of 1 opportunity
```

### 12.3 Attribution Loss

The inquiry is known, but its true originating influence is lost.

Example:

```text
Psychiatrist recommends Harbor Ridge
        ↓
Patient later searches Google
        ↓
Website form records Organic Search
        ↓
Professional referral influence disappears
```

### 12.4 Outcome-Linkage Loss

The acquisition event is known and the clinical or financial outcome exists, but the systems cannot connect them.

Example:

```text
HRO-000184
        ↓
Patient admits
        ↓
RCM collects $29,000
        ↓
CRM/EHR/RCM identifiers fail to connect
        ↓
Revenue becomes unattributed
```

These degradation types should remain analytically separate.

Fixing attribution does not necessarily fix identity.

Fixing identity does not necessarily fix observability.

Fixing observability does not necessarily restore financial outcome linkage.

---

## 13. Evidence Provenance and Trust

System-of-record designation answers:

> Which system should answer this question?

Evidence provenance answers a different question:

> How much confidence should Harbor Ridge place in this specific field or observation?

Harbor Ridge V1 therefore distinguishes among:

### System-Observed Evidence

Examples:

- Timestamped form submission
- Call-tracking event
- Advertising spend
- EHR admission timestamp
- Claim payment
- Bank-cleared collection event

Generally the strongest evidence when the instrumentation itself is functioning correctly.

### Human-Entered Evidence

Examples:

- Referral source selected by intake
- Outreach activity note
- Discharge disposition
- Free-text clinical note
- Relationship status

These fields may contain important operational truth but are more vulnerable to:

- incomplete entry,
- inconsistent interpretation,
- workflow pressure,
- retrospective editing,
- or incentive distortion.

### Derived / Analytical Evidence

Examples:

- Identity match confidence
- Attribution assignment
- Relationship-decay flag
- Cohort maturity classification
- AI-generated diagnostic conclusion

Derived evidence must remain traceable to the underlying source evidence used to create it.

### Hard-Gate vs. Soft Behavioral Fields

Structured operational fields tied directly to financial, compliance, or system workflow gates generally receive greater initial trust than subjective behavioral classifications.

However, system structure does not guarantee semantic truth.

For example:

```text
Structured Discharge Disposition:
AMA

Clinical Narrative:
Insurance authorization ended and family could not self-pay
```

The structured field is technically valid but may not accurately explain the underlying operational cause.

This is an evidence-reliability concern, not a break in the identity/attribution/outcome-linkage chain, and should be evaluated using this trust framework rather than the four degradation classes above.

The detailed evidence-provenance and trust-tier framework remains documented in:

```text
docs/source-system-architecture-notes.md
```

---

## 14. System-of-Record Hierarchy

Harbor Ridge should not ask every system to answer every question.

| Question | Preferred System of Record |
|---|---|
| What did the advertising platform deliver? | Advertising Platform |
| What did the user search organically? | Google Search Console |
| What page/session did the user experience? | GA4 / Website Analytics |
| Did a web form submit? | Form / CRM |
| Did a phone interaction occur? | Call Tracking / Phone System |
| Did a real inquiry exist? | CRM |
| Did multiple inquiries represent one opportunity? | Patient Opportunity / Identity Resolution Layer |
| Who referred the opportunity? | CRM Professional Referral Record |
| Was insurance viable? | VOB / Admissions Workflow |
| Did the patient admit? | EHR |
| What clinical episode occurred? | EHR |
| What was billed or denied? | RCM / Billing System |
| What was actually collected? | RCM + Financial Ledger |
| What caused the business outcome? | Cross-system analytical layer |

No single source system contains the complete truth.

---

## 15. Representative Cross-System Failure Points

| Failure Point | Example | Degradation Type |
|---|---|---|
| Platform → Inquiry | Google records conversion but no legitimate CRM inquiry exists | Observability / Measurement Error |
| Inquiry → Opportunity | Family members create multiple records for one patient | Identity Loss |
| Referral → Arrival | Professional referral becomes credited to Organic Search | Attribution Loss |
| Opportunity → EHR | CRM Opportunity ID is not carried into the EHR | Outcome-Linkage Loss |
| EHR → Claim | Episode identifiers are stripped or transformed by billing vendor | Outcome-Linkage Loss |
| Claim → Payment | Payment cannot be tied to correct DOS episode | Outcome-Linkage Loss |
| Admission → Attribution | Patient returns months later and prior marketing touch receives incorrect credit | Attribution Loss |

These are not merely technical defects.

They can directly alter executive conclusions about:

- marketing effectiveness,
- outreach performance,
- admissions operations,
- clinical quality,
- payer strategy,
- and financial return.

---

## 16. Harbor Ridge V1 Success Criteria

Harbor Ridge V1 does not need to eliminate every real-world healthcare data problem.

It must demonstrate that the architecture can:

1. Represent acquisition activity from paid, organic, and professional referral sources.
2. Preserve calls and forms as distinct inquiry mechanisms.
3. Connect multiple inquiries to a single Patient Opportunity.
4. Preserve contact roles and identity-match confidence.
5. Distinguish referral influence from arrival mechanism.
6. Represent VOB outcome separately from admission financial status.
7. Preserve clinically appropriate at-risk admissions without forcing a simplistic financial gate.
8. Connect a Patient Opportunity to one or more EHR episodes.
9. Connect EHR episodes to one or more claims.
10. Connect claims to payments and adjustments.
11. Distinguish operational outcomes from mature financial outcomes.
12. Preserve evidence provenance and uncertainty.
13. Identify Observability, Identity, Attribution, and Outcome-Linkage degradation separately.
14. Allow an analytical or AI layer to trace an executive conclusion back to underlying evidence.

If Harbor Ridge V1 can demonstrate these capabilities using synthetic data, the Source-System Map has accomplished its purpose.

---

## 17. V1 Scope Boundary

This document intentionally stops at the conceptual and analytical architecture required for Harbor Ridge V1.

The following are outside the scope of the Source-System Map:

- Production EHR integration
- Production CRM integration
- Production RCM integration
- Enterprise identity-resolution infrastructure
- Real patient data
- Real PHI
- Production HIPAA architecture
- Enterprise Master Patient Index implementation
- Production API orchestration
- Full FHIR implementation
- Enterprise data warehouse design
- Production cloud infrastructure
- Real-time event streaming
- Production attribution engine
- Production machine-learning identity matching

Identity resolution in Harbor Ridge V1 exists only to demonstrate that the analytical model can represent:

- multiple contacts,
- multiple inquiries,
- one underlying Patient Opportunity,
- and explicit uncertainty.

The project should not expand into production-grade identity infrastructure.

Likewise, evidence provenance exists to prevent the AI or executive layer from presenting uncertain or human-entered evidence as unquestionable system truth.

---

## 18. Canonical V1 Architecture

The final Harbor Ridge V1 source-system architecture is:

```text
                         ACQUISITION
                              │
        ┌─────────────────────┼──────────────────────┐
        │                     │                      │
   Paid Media             Organic / Local      Professional Referral
        │                     │                      │
        └─────────────────────┼──────────────────────┘
                              ↓
                       INQUIRY CAPTURE
                              │
                    ┌─────────┴─────────┐
                    │                   │
                  Calls               Forms
                    │                   │
                    └─────────┬─────────┘
                              ↓
                     IDENTITY RESOLUTION
                              │
                  Confirmed / Probable /
                  Possible / Unmatched
                              │
                              ↓
                     PATIENT OPPORTUNITY
                         HRO-######
                              │
                 ┌────────────┴────────────┐
                 │                         │
          Originating Influence      Arrival Mechanism
                 │                         │
                 └────────────┬────────────┘
                              ↓
                        VOB / QUALIFICATION
                              │
                              ↓
                 ADMISSION FINANCIAL STATUS
                              │
                  ┌───────────┼───────────┐
                  │           │           │
              Cleared      At-Risk     Pending /
                                      Not Cleared
                              │
                              ↓
                         EHR EPISODE(S)
                              │
                              ↓
                            CLAIM(S)
                              │
                              ↓
                    PAYMENT(S) / ADJUSTMENT(S)
                              │
                              ↓
                       CASH COLLECTIONS
                              │
                              ↓
                   EXECUTIVE / AI ANALYSIS
                              │
                              ↓
                 Evidence-Backed Diagnosis
```

---

## 19. Governing Principle

Harbor Ridge V1 is designed around one central principle:

> **The objective is not to create perfectly clean healthcare data. The objective is to preserve enough identity, provenance, uncertainty, and relational integrity that an executive or AI system can distinguish what is known, what is inferred, where the data degraded, and what evidence supports a business conclusion.**

The Source-System Map defines the boundaries of that system.

Further architecture should be added only when implementation demonstrates that a missing element prevents Harbor Ridge V1 from answering one of its defined executive diagnostic questions.

---

**End of Harbor Ridge V1 Source-System Map — Version 1.0**

Fix: reclassify failure-table rows to match four-class degradation framework
