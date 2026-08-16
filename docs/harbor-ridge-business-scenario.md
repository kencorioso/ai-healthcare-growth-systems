# Harbor Ridge Behavioral Health
## Version 1 — Domain Validation Business Scenario

## Purpose

Harbor Ridge Behavioral Health is the synthetic healthcare organization used to build and validate Version 1 of the Patient Acquisition & Executive Insight Engine.

Version 1 is intentionally grounded in behavioral healthcare because the project owner has direct operating, marketing, admissions, attribution, and executive experience within this environment.

The objective is not to build a behavioral-health-specific analytics tool.

The objective is to use deep domain knowledge to build and validate an analytical framework capable of identifying patient-acquisition constraints, separating evidence from hypotheses, and supporting executive decision-making.

After Version 1 is completed and validated, the framework will later be tested in other healthcare specialties to determine whether it generalizes beyond the domain in which it was developed.

---

## Organization Profile

**Organization:** Harbor Ridge Behavioral Health

**Organization Type:** Independent behavioral healthcare provider

**Operating Model:** Single-campus organization

**Population:** Adults

**Total Capacity:** 32 beds

### Levels of Care

Harbor Ridge operates two levels of care:

- 8 detoxification beds
- 24 residential treatment beds

The 1:3 detox-to-residential capacity ratio allows Harbor Ridge to stabilize patients requiring detoxification while maintaining a larger residential treatment population.

Patients may enter Harbor Ridge through different treatment pathways depending on clinical need.

Typical pathways include:

- Detox → Residential → Discharge
- Detox → External Step-Down / Discharge
- Residential → Discharge

Not every residential patient requires detoxification before entering treatment.

---

## Clinical Positioning

Harbor Ridge operates as a dual-diagnosis behavioral healthcare organization.

The organization treats adults whose primary needs may involve:

- Substance use disorders
- Mental health conditions
- Co-occurring substance use and mental health disorders

Clinical appropriateness is determined during the admissions assessment.

Patients whose medical, psychiatric, or safety needs exceed Harbor Ridge's capabilities are referred to a more appropriate level of care.

The organization is not intended to function as an acute locked psychiatric hospital or emergency medical facility.

---

## Payer Strategy

Harbor Ridge represents an established behavioral healthcare organization that has progressed beyond an exclusively out-of-network reimbursement model.

Version 1 assumes Harbor Ridge accepts:

- Commercial in-network insurance
- Commercial out-of-network insurance
- Private pay

Harbor Ridge does not participate in state Medicaid programs within the Version 1 scenario.

### Target Payer Mix

The synthetic target payer mix is:

- 55% In-Network Commercial
- 35% Out-of-Network Commercial
- 10% Private Pay

These percentages are design assumptions for the synthetic organization and should not be interpreted as universal behavioral-health industry benchmarks.

The payer mix creates an important executive tension between:

- predictable volume,
- reimbursement potential,
- financial risk,
- patient responsibility,
- and census stability.

---

## Patient Acquisition Environment

Harbor Ridge competes for clinically appropriate prospective patients whose financial circumstances and payer benefits are compatible with the organization's treatment and reimbursement model.

Generating inquiry volume alone is therefore not sufficient.

A successful acquisition system must generate prospective patients who are:

1. Clinically appropriate
2. Financially viable or represent acceptable reimbursement risk
3. Ready and willing to enter treatment
4. Able to complete the logistical process required to arrive at the facility

This distinction between inquiry volume and viable patient demand is central to the Version 1 analytical problem.

---

## Acquisition Channels

Harbor Ridge uses a diversified patient-acquisition strategy.

### Major Sources

- Google Ads / Paid Search
- Organic Search / SEO
- Professional and Clinical Referrals

### Moderate Sources

- Hospital / Emergency Department / Crisis Referrals
- Alumni and Patient Referrals
- Independent Interventionists

### Minor Sources

- Microsoft Ads
- Direct / Brand Traffic
- Meta / Social Media

These classifications describe Harbor Ridge's synthetic acquisition architecture and are not intended to establish universal industry performance benchmarks.

---

## Baseline Controllable Marketing Allocation

During the healthy baseline period, Harbor Ridge allocates its controllable marketing investment approximately as follows:

- 45% Google Ads
- 20% Professional Outreach / Business Development
- 15% SEO / Organic Content Development
- 10% Events / Community / Referral Development
- 5% Microsoft Ads
- 5% Meta

This allocation provides a synthetic baseline from which later changes in marketing performance can be evaluated.

Actual dollar amounts will be finalized during development of the measurement model and synthetic dataset.

---

## Patient Acquisition Funnel

The Harbor Ridge patient-acquisition process begins when a prospective patient, loved one, or professional referral source contacts the organization.

### Core Funnel

Inquiry

→ Admissions Contact

→ Clinical / Safety Assessment

→ Financial Verification & Coverage Assessment

→ Patient Readiness Assessment

→ Admission Decision

→ Admission Scheduled

→ Bed / Medical / Travel Coordination

→ Patient Arrival

→ Admission Paperwork Completed

→ Completed Admission

---

## Inquiry Initiators

An inquiry may originate from:

- The prospective patient
- A loved one
- A professional or healthcare referral source

A loved-one inquiry is not equivalent to patient readiness.

When a loved one initiates contact, admissions must ultimately establish direct communication with the prospective patient and determine whether the patient is willing to participate in voluntary treatment.

---

## Clinical and Safety Assessment

Admissions determines whether the prospective patient appears appropriate for Harbor Ridge's available levels of care.

Assessment considerations may include:

- Primary presenting condition
- Substance use history
- Mental health history
- Previous treatment
- Withdrawal risk
- Medical stability
- Immediate safety concerns
- Appropriate level of care

Prospective patients requiring a higher level of medical or psychiatric intervention are referred to an appropriate provider.

---

## Financial Verification and Coverage Assessment

Admissions collects the patient's insurance and financial information.

Verification may be performed through:

- An internal billing or insurance-verification team
- A third-party verification service
- A third-party web portal
- Direct payer contact
- Other facility-specific verification workflows

Verification results are documented in systems accessible to admissions and billing personnel.

Typical financial outcomes include:

- Cleared to admit with no immediate patient responsibility
- Cleared to admit with a deductible or other defined patient responsibility
- Coverage or reimbursement is uncertain
- Insurance will not cover the proposed treatment

Financial verification informs the admission decision but does not always function as an absolute gate.

---

## At-Risk Admissions

Behavioral healthcare organizations sometimes admit clinically appropriate patients despite unresolved reimbursement uncertainty.

Within Harbor Ridge, this is classified as an:

**At-Risk Admission**

An at-risk admission may occur when Harbor Ridge believes there is a reasonable probability of eventual reimbursement despite unresolved coverage or authorization questions.

The decision may incorporate:

- Known payer behavior
- Historical reimbursement experience
- Available benefit information
- Estimated financial exposure
- Patient circumstances
- Clinical urgency
- Organizational risk tolerance

Routine admissions may proceed under predefined criteria.

Questionable cases are generally escalated to the Admissions Director or another authorized decision-maker.

This creates an operating model combining:

**Rules-based admissions with judgment-based exceptions.**

---

## Patient Readiness

Readiness is treated as a distinct stage of the acquisition process.

Potential readiness classifications include:

- Ready / Immediate
- Ambivalent
- Deferred
- Refusing

Patient-initiated inquiries and loved-one-initiated inquiries may have substantially different readiness dynamics.

Admissions must distinguish between the motivation of the inquiry initiator and the willingness of the prospective patient.

This distinction is important because a highly motivated loved one does not necessarily represent a patient who is ready to enter treatment.

---

## Admission Definition

For Version 1, Harbor Ridge uses a strict conversion definition.

A patient is considered a:

**Completed Admission**

only when the patient:

1. Physically arrives at Harbor Ridge, and
2. Completes the required admission paperwork.

The following events do not independently count as completed admissions:

- Verbal commitment
- Financial clearance
- Admission approval
- Reserved bed
- Scheduled arrival
- Booked transportation
- Airport pickup arrangement

This definition establishes the primary patient-acquisition outcome used by the analytical system.

---

## Pre-Admission Logistics

After approval and scheduling, Harbor Ridge coordinates the operational requirements necessary to complete the admission.

These may include:

- Bed availability
- Medical clearance when required
- Medication and packing instructions
- Transportation
- Flight coordination
- Facility pickup
- Arrival timing
- Continued patient and loved-one communication

Potential pre-admission failure outcomes include:

- Patient changes mind
- No-show
- Transportation or travel failure
- Medical clearance issue
- Bed availability issue
- Unable to re-establish contact
- Referral to another level of care
- Other or unknown reason

These outcomes allow the analytical system to distinguish an acquisition or admissions problem from a logistical conversion problem.

---

## Downstream Quality Signals

Version 1 remains primarily a patient-acquisition analytics system.

However, a limited set of downstream outcomes will be retained to determine whether completed admissions represent appropriate and economically meaningful patient acquisition.

Potential downstream signals include:

- Early Against Medical Advice (AMA) discharge
- Detox completion
- Detox-to-residential transition
- Residential program completion
- Financial / reimbursement outcome

Additional clinical, revenue-cycle, and longitudinal outcome measures may be explored in later versions.

The system must not assume that an acquisition channel caused a downstream clinical outcome merely because an association exists.

---

# Version 1 Executive Business Problem

Harbor Ridge historically maintained a healthy census and functioning patient-acquisition system.

Over several months, leadership observes a troubling pattern:

- Marketing investment increases
- Total inquiry volume increases
- Overall inquiry-to-admission conversion declines
- Cost per completed admission increases
- Completed admissions decline
- Census begins to fall

Marketing reports strong inquiry volume.

Leadership begins questioning whether the admissions team is failing to convert prospective patients.

Admissions leadership argues that the quality of incoming inquiries has deteriorated.

Executive leadership needs to determine where the actual constraint exists.

## Primary Executive Question

**Why are Harbor Ridge's completed admissions and census declining despite increasing marketing spend and inquiry volume, and where should leadership investigate first?**

---

# Hidden Failure Scenario

The synthetic dataset will contain two major underlying performance failures.

These failures represent the ground truth used to evaluate whether the Patient Acquisition & Executive Insight Engine can correctly diagnose the available evidence.

## Primary Failure — Paid Search Inquiry Quality Deterioration

Harbor Ridge's Google Ads program gradually shifts toward optimizing for greater inquiry volume.

Campaign-management and targeting changes increase the number of lower-cost inquiries while reducing the proportion of inquiries compatible with Harbor Ridge's payer and patient-acquisition requirements.

Surface-level marketing reports initially appear positive:

- Click volume increases
- Inquiry volume increases
- Cost per inquiry may improve

However, deeper funnel performance deteriorates:

- Payer eligibility declines
- Financial viability declines
- Completed admissions from paid search decline
- Cost per completed admission increases

The analytical system should identify the deterioration without assuming that any individual Google Ads feature or match type is inherently responsible.

---

## Secondary Failure — Professional Outreach Quality Deterioration

During the same general period, Harbor Ridge loses experienced professional-outreach personnel with established referral relationships.

Replacement outreach activity remains superficially healthy.

Measures such as:

- Meetings
- Contacts
- Visits
- Outreach activity

may remain stable or increase.

However, the quality and economic compatibility of resulting referrals deteriorate.

The professional-referral pipeline produces fewer financially viable OON and private-pay opportunities and fewer completed admissions.

This creates a second executive lesson:

**Activity metrics are not necessarily outcome metrics.**

---

## Admissions Performance

The synthetic scenario is intentionally designed so that the admissions department remains reasonably effective when provided with prospective patients who are:

- Clinically appropriate
- Financially viable or approved as acceptable risk
- Ready to enter treatment

This allows the analytical system to test whether leadership's initial assumption about poor admissions performance is supported by evidence.

---

# Analytical Reasoning Requirements

The Patient Acquisition & Executive Insight Engine must distinguish among four categories of output.

## 1. Observed Facts

Statements directly supported by the available data.

## 2. Hypotheses

Possible explanations consistent with the evidence but not proven by the available data.

## 3. Recommended Investigations

Specific analyses, comparisons, or operational questions leadership should pursue next.

## 4. Findings Not Established

Claims that cannot responsibly be made from the available evidence.

The system must not convert correlation into causation or manufacture explanations that are not supported by the data.

---

# Version 1 Success Standard

Version 1 will be considered successful if the system can:

- Detect that rising inquiry volume is masking deteriorating acquisition quality
- Identify where in the patient-acquisition funnel performance is changing
- Compare performance across acquisition channels
- Detect changes in payer and financial viability
- Distinguish marketing-quality deterioration from admissions-conversion performance
- Identify professional-outreach deterioration despite healthy activity metrics
- Recognize logistical or capacity constraints when present
- Separate observed facts from hypotheses
- Recommend specific human investigations
- Avoid unsupported causal conclusions
- Communicate findings in language useful to healthcare executives

The purpose of Version 1 is not to automate executive judgment.

The purpose is to build a system that helps executives identify constraints faster, challenge incorrect assumptions, and ask better questions.

---

## Development Status

The Harbor Ridge business scenario is now defined.

Completed:

- Organization profile
- Levels of care
- Capacity model
- Clinical positioning
- Payer strategy
- Acquisition-channel architecture
- Patient-acquisition funnel
- Financial-verification model
- Patient-readiness model
- Admission definition
- Pre-admission logistics
- Downstream quality signals
- Executive business problem
- Hidden failure scenario
- Analytical reasoning requirements

Next:

**Develop the Version 1 data dictionary and measurement specification.**
