# Harbor Ridge V1 --- Site Copy Architecture

**Status:** Final\
**Workstream:** D --- Content Architecture & Core Writing\
**Intended repository path:** `docs/harbor-ridge-v1-site-copy.md`

## Scope

This document defines **section-level content only** for the Harbor
Ridge V1 site. It does not define navigation structure or visual design.
Those remain **Workstream F decisions**.

## Open Note for Workstream F

**Section 4 publishing dependency:** The "inspect it yourself" language
in Interactive Evidence should be reviewed when Workstream B's live
evidence-trail page is actually linked into the site. This is a
publishing-order dependency, not a content revision. The approved
Section 4 copy remains unchanged here.

------------------------------------------------------------------------

## 1. Executive Premise

### When the numbers look healthy, but the business isn't

I built the HEOS Evidence Engine around a deceptively simple executive
problem:

**Why are completed admissions and census declining despite increasing
marketing spend and inquiry volume, and where should leadership
investigate first?**

In Harbor Ridge, marketing believed admissions was failing to convert
demand. Admissions believed marketing was delivering lower-quality
inquiries. Neither side had enough evidence to resolve the disagreement.

I wanted to investigate the entire chain instead of optimizing one
department's version of the story.

So I built a synthetic 32-bed behavioral health facility and connected
the journey from **acquisition → inquiry → financial qualification →
admission → treatment → revenue.** Then I used AI to reason across that
evidence.

One result immediately mattered: an **Observed Finding** estimated
approximately **\$251,000 in additional collections if out-of-network
claims had realized at the in-network rate.**

That finding was real within the synthetic data. **It was not a
Benchmark Result, and it was not one of the hidden problems I had built
the system to find.**

When I later blind-tested the Evidence Engine against those deliberately
hidden problems, it missed both.

I kept both results.

Because the point of this project wasn't to manufacture an AI success
story. It was to build a system whose conclusions could be inspected,
tested, and challenged.

**Video:** Video 1, CEO / Executive Premise

*Claim trace: `docs/harbor-ridge-v1-methodology.md`;
`docs/harbor-ridge-v1-case-study.md`; Workstream A Content/Evidence
Map.*

------------------------------------------------------------------------

## 2. Hiring-Manager Proof

### What I did when the evidence stopped cooperating

A convincing AI demonstration is easy to manufacture when the builder
already knows the answer.

I encountered that problem before the blind evaluation even began.

While constructing Scenario 2, a legitimate validation failure appeared.
I had a command prepared that would search across random seeds for a
different result.

**I stopped the command before it ran.**

Searching until I found a friendlier dataset could have preserved the
appearance of success while weakening the experiment. I went back and
corrected the validation rule instead.

Later, the final blind evaluation gave me another decision to make:

**Scenario 1: MISS. Scenario 2: MISS. Healthy Baseline: CLEAN.**

The Evidence Engine did not recover either deliberately hidden
deterioration.

I could have continued engineering V0.3, V0.4 and beyond until the
benchmark turned green. Instead, I froze the V1 analytical core with the
misses intact and documented what the evidence actually supported.

That doesn't demonstrate that the Evidence Engine is reliable.

**It demonstrates how I respond when the system I built produces
evidence I would rather not receive.**

**Video:** Video 4, Hiring Manager / Judgment Under Failure

*Claim trace: `docs/harbor-ridge-v1-methodology.md`;
`docs/harbor-ridge-v1-case-study.md`; Scenario 2 specification/validator
provenance identified in the Workstream A Content/Evidence Map.*

------------------------------------------------------------------------

## 3. System

### From executive question to evidence

I started by modeling the organization, not prompting the AI.

**HEOS** is my broader vision for an AI-enabled executive intelligence
layer for healthcare organizations.

The **HEOS Evidence Engine** is the V1 capability I built toward that
vision: an AI reasoning system for evidence-based executive performance
analysis.

**Harbor Ridge Behavioral Health** is the synthetic evaluation testbed I
built to test and characterize that capability. It is not the product.

I mapped Harbor Ridge across a Golden Thread:

**Acquisition → Inquiry → Financial Qualification → Admission →
Treatment → Revenue**

I translated that operating model into a frozen data dictionary and an
**11-table relational schema**, validated through a **22-test constraint
suite**.

From there, I generated a synthetic baseline and two deliberately hidden
deteriorations: one involving paid-search inquiry quality and another
involving professional-outreach quality.

Then I froze the answers before asking the AI the questions.

That order matters. **The organizational model came first. The evidence
came next. The AI came after both.**

*Claim trace: `docs/harbor-ridge-v1-methodology.md`; Workstream A
Content/Evidence Map.*

------------------------------------------------------------------------

## 4. Interactive Evidence

### Inspect the \$251K finding yourself

I don't want the most persuasive number in this project to depend on
taking my word for it.

The Evidence Engine surfaced an **Observed Finding**: an estimated
**\$251,000 additional collections opportunity if out-of-network claims
had realized at the in-network rate.**

I later reconstructed that finding directly from the Scenario 1
database:

**INN**\
\$1,216,954.73 billed → \$812,530.95 collected → **66.77% realization**

**OON**\
\$688,137.27 billed → \$209,054.85 collected → **30.38% realization**

Applying the INN realization rate to OON billed claims produces expected
OON collections of **\$459,452.45**.

The calculated difference is **\$250,397.60**.

The interactive evidence trail exposes that transformation from **billed
→ collected → realization rate → counterfactual → estimated gap**,
followed by the underlying claim-level records.

The exporter is deterministic. Repeated runs produced byte-identical
JSON with matching SHA-256 hashes.

**The goal isn't to make the \$251K number impressive. It's to make it
inspectable.**

**Functional UI:** `Explore the Evidence Trail`

*Claim trace: `docs/harbor-ridge-v1-methodology.md`; Workstream B
evidence-trail implementation as mapped by the frozen source record.*

------------------------------------------------------------------------

## 5. AI Reasoning

### I wanted reasoning across the whole chain

The executive problem wasn't confined to marketing, admissions, finance,
or operations.

So I designed the analytical environment around the relationships
between them.

The Evidence Engine had access to a relational representation of Harbor
Ridge spanning acquisition, inquiry, financial qualification, admission,
treatment and revenue. I wanted the analysis to distinguish different
kinds of performance problems rather than assume that declining
admissions automatically meant an admissions problem.

For the blind evaluation, I went further.

I froze Ground Truth before AI analysis began. The answer key was based
on the actual generated scenarios, and the rule was explicit: **what
counted as the correct answer could not change based on what the AI
later found or missed.**

That created a clean separation between two questions:

**Did the analysis surface something useful?**

and

**Did it recover the deliberately hidden problem it was being tested to
find?**

Those questions eventually produced different answers.

The Evidence Engine surfaced a genuine OON collections-realization
disparity.

It did not reliably recover the planted root causes.

**Useful discovery and successful diagnosis are not the same claim.**

*Claim trace: `docs/harbor-ridge-v1-methodology.md`; Workstream A
Content/Evidence Map.*

------------------------------------------------------------------------

## 6. Blind Evaluation

### I froze the rules before I saw the answers

After the first blind-analysis attempt produced mixed results, I
redesigned the evaluation.

For V0.2, I froze an Evaluation Interpretation Protocol defining **Pass
/ Partial / Miss** for known scenarios and **Clean / Borderline / False
Positive** for a Healthy Baseline negative control.

The discovery procedure was designed without Harbor Ridge context. I
subjected it to two independent genericity audits. **Both returned 10/10
PASS.**

Only then did I freeze the procedure and run three fresh, isolated blind
sessions: Scenario 1, Scenario 2 and the Healthy Baseline.

The outputs were frozen before scoring.

The result was:

**Scenario 1: MISS**\
**Scenario 2: MISS**\
**Healthy Baseline: CLEAN**

The misses were not cases where the system simply found nothing. In both
scenarios, it found and prioritized other patterns that substantially
contradicted the frozen Ground Truth.

The Healthy Baseline remained clean, which is useful evidence about that
control test. **It does not prove general reliability.**

I designed the evaluation so the Evidence Engine could fail without
letting me redefine failure afterward.

Then it did.

**Video:** Video 2, Technical Practitioner / Evidence of Rigor

*Claim trace: `docs/harbor-ridge-v1-methodology.md`;
`docs/phase-d-v0.2-evaluation-summary.md` and related evaluation
artifacts identified in Workstream A's Content/Evidence Map.*

------------------------------------------------------------------------

## 7. Lessons & Limitations

### What transfers, and what doesn't

**Harbor Ridge itself is not portable to another healthcare vertical. It
isn't.**

Its schema, synthetic facility and benchmark results belong to this test
environment.

What **is** portable is the process I demonstrated by building it:

**source-system mapping → data dictionary → schema → synthetic data →
scenario design → frozen Ground Truth → blind evaluation**

For another organization, I would rebuild that process around its actual
operating reality rather than transplant Harbor Ridge and pretend
healthcare organizations are interchangeable.

There are analytical limitations too.

The V0.2 evaluation did not demonstrate reliable recovery of the hidden
failures. A later diagnostic suggested experimental signal-to-noise
structure may have contributed, particularly because one affected cohort
ultimately contained only roughly **three to eight admissions per
month**. That explanation is directional, not proven.

I have deferred V0.3 rather than use repeated experimentation to chase a
passing result.

So I would not present V1 as a production-validated, generally reliable
autonomous diagnostic system.

**What I can demonstrate is the complete build-and-evaluate process,
including what I did when validation exposed defects, when AI surfaced
something I hadn't planted, and when the final benchmark failed.**

**Video:** Video 3, Different Healthcare Vertical / Portability

*Claim trace: `docs/harbor-ridge-v1-methodology.md`;
`docs/harbor-ridge-v1-case-study.md`; Feature Freeze and Closing
Diagnostic as identified in Workstream A's Content/Evidence Map.*

------------------------------------------------------------------------

## 8. Deeper Resources & Contact

### Inspect the work behind the conclusions

I've deliberately kept the deeper project record available because the
strongest claims on this site should survive scrutiny beyond the page
that presents them.

The **case study** is the concise employer-facing account of what I
built, what happened, what the Evidence Engine found, what it missed,
and how I responded.

The **methodology** provides the higher-resolution technical account:
architecture, synthetic-data construction, Ground Truth, blind
evaluation, results, closing diagnostic and unresolved questions.

The **GitHub repository** provides the underlying project record and
implementation history.

And the **whitepaper** provides a direct path into the deeper project
material.

If you're evaluating how I think about healthcare growth, AI, data, and
executive decision-making, those materials let you go as deep as you
want.

**I built Harbor Ridge to make the reasoning inspectable. The same
principle applies to evaluating the person who built it.**

**Functional UI:** `Read the Case Study` · `Read the Methodology` ·
`Download the Whitepaper` · `View GitHub` · `Contact Ken`

*Claim trace: Workstream A Experience Architecture and its three-tier
understanding test; `docs/harbor-ridge-v1-methodology.md`;
`docs/harbor-ridge-v1-case-study.md`.*
