# Harbor Ridge V1 --- Phase D Closing Diagnostic

**Status:** Post-Hoc Decision Memo\
**Scope:** Closing analytical note for Phase D as currently scoped\
**Purpose:** Evaluate whether the unresolved Phase D discovery problem
is more consistent with a fixable discovery-procedure gap or with
asymmetry in the experimental signal structure, without initiating
another build-and-test cycle.

> **Methodological status:** This document is not a pre-registered
> protocol, frozen evaluation rule, or additional scoring instrument. It
> is a post-hoc analytical judgment made after the V0.2 results were
> known. It sits alongside the frozen Ground Truth and the V0.1/V0.2
> evaluation records and does not revise or reinterpret them.

------------------------------------------------------------------------

## 1. Question

Section 9 of `docs/phase-d-v0.2-evaluation-summary.md` closed V0.2 with
the central causal question still unresolved:

1.  Did the known-scenario misses primarily reflect a remaining
    **discovery-procedure gap**?
2.  Did they primarily reflect the **experimental signal-to-noise
    structure**?
3.  Or did both contribute?

V0.2 established that a more systematic general-purpose discovery
procedure was insufficient to recover either planted failure. It did not
establish why.

Before closing Phase D, one inexpensive diagnostic was therefore
performed to inform the project-level decision about whether a V0.3
procedure iteration represented a reasonable near-term bet.

The diagnostic was deliberately limited to analysis on paper. No
database, generator, scenario specification, Ground Truth, frozen
evaluation protocol, or Claude output was changed.

------------------------------------------------------------------------

## 2. Diagnostic Method: Consult, Don't Build

The diagnostic compared two statistical objects from Scenario 1:

### A. Planted Scenario 1 evidence chain

The affected three-campaign cohort contained approximately **25--38
Patient Opportunities per month** and exhibited the following realized
deterioration:

  Metric                            May        June        July
  ------------------------- ----------- ----------- -----------
  Opportunity → Admission     **32.0%**   **12.5%**    **7.9%**
  Poor VOB Outcome            **29.2%**   **40.0%**   **64.0%**
  Not Financially Cleared     **36.0%**   **58.3%**   **73.7%**

The pattern is large and coherent once the correct cohort is already
known. Correct diagnosis, however, requires discovery of the
three-campaign grouping, temporal decomposition, and downstream tracing
through payer mix, VOB, financial clearance, and admission outcome.

### B. Shared OON financial signal

Phase D V0.1 independently surfaced an approximately **78% INN versus
51% OON allowed-amount relationship** in both known-scenario databases.
Review of the shared baseline generator confirmed that this was a real
structural feature of the synthetic data rather than hallucination or
coincidence.

The OON relationship is:

-   dataset-wide rather than confined to a small hidden cohort;
-   directly exposed by a first-order `payer_relationship`
    decomposition;
-   supported across the claims population;
-   expressed in financially material, six-figure-dollar terms when
    aggregated;
-   structurally generated throughout the applicable claims records.

The comparison therefore asked a narrow question:

> As raw statistical objects available to a blind general-purpose
> analyst, are the planted Scenario 1 deterioration and the structural
> OON financial difference comparably findable, or does the experimental
> design give the OON signal a substantial discovery advantage?

### Clarification regarding V0.2

The OON signal should not be described as the finding that **both V0.1
and V0.2 Scenario 1 runs elevated instead of the planted failure**. That
would overstate the record. V0.1 prominently elevated the OON financial
characteristic; V0.2 Scenario 1 instead elevated the Marcus Webb
professional-outreach finding. V0.2's healthy-control run also
demonstrated improved handling of the structural OON difference by
correctly treating it as expected INN/OON structure rather than a
primary deterioration.

The OON signal remains useful for this diagnostic because it is the
clearest known example of a large, structurally generated baseline
signal competing in the same analytical environment. This memo preserves
that distinction rather than rewriting the V0.2 result.

------------------------------------------------------------------------

## 3. Key Reasoning: Effect Size Is Not the Same as Blind Findability

The Scenario 1 planted effects are not small once the affected cohort
has been identified.

From May to July:

-   Opportunity → Admission falls from **32.0% to 7.9%**, a **24.1
    percentage-point decline**;
-   Poor VOB rises from **29.2% to 64.0%**, a **34.8-point increase**;
-   Not Financially Cleared rises from **36.0% to 73.7%**, a
    **37.7-point increase**.

Those are operationally meaningful movements.

The discovery problem is that the raw cohort size overstates the
effective evidentiary weight of the most downstream outcome.

### 3.1 Effective sample size at the admission endpoint

The affected cohort contains roughly **25--38 opportunities per month**,
but Opportunity → Admission is a binary downstream outcome. At the
observed rates, the monthly number of admissions contributing to that
rate is only approximately:

-   May: roughly **8 admissions** at a 32.0% conversion rate;
-   June: roughly **3 admissions** at a 12.5% conversion rate;
-   July: roughly **3 admissions** at a 7.9% conversion rate.

The exact monthly opportunity denominators determine the exact counts,
but the analytical point is unchanged: the admission-rate deterioration
is ultimately expressed through **single-digit monthly admission
counts** inside a subgroup that the analyst must first discover.

That makes the downstream rate substantially more vulnerable to ordinary
binomial variation than the raw 25--38 opportunity denominator might
initially suggest. It also makes small additional subdivisions of the
affected cohort increasingly noisy.

The VOB and financial-clearance measures provide corroboration, which
strengthens the planted chain after localization. But a blind procedure
must first discover that the three campaigns belong together and then
trace the same cohort across those downstream measures before the
corroborating structure becomes apparent.

### 3.2 Discovery complexity

The planted Scenario 1 signal is therefore strong **conditional on
correct localization**, but it is not a first-order aggregate feature.

A general-purpose analyst must, without knowing the answer:

1.  decompose paid acquisition beyond aggregate channel performance;
2.  identify the relevant campaign-level behavior;
3.  recognize that three campaigns form a meaningful affected cohort;
4.  compare that cohort across time;
5.  distinguish it from healthy Google/internal comparison campaigns;
6.  trace the cohort into payer relationship and VOB;
7.  trace it further into financial clearance and admission outcome;
8.  decide that the coherent downstream deterioration is more
    diagnostically important than other real findings in the database.

Each step is reasonable. The sequence as a whole creates a materially
larger search space than a single first-order partition.

### 3.3 OON signal as a competing statistical object

The structural OON signal has very different geometry.

The approximately **78% versus 51% allowed-amount relationship** is a
roughly **27-percentage-point cross-sectional separation** that appears
directly when claims are grouped by payer relationship. It does not
require discovery of a special entity combination or temporal cohort
before becoming visible.

It also carries several properties that naturally increase executive
salience:

-   substantially larger effective sample support;
-   persistence across the dataset rather than one localized monthly
    cohort;
-   direct dollar denomination;
-   large aggregate financial materiality;
-   simple relational interpretation;
-   reproducibility across independently generated scenario databases
    because the relationship is embedded in shared baseline logic.

The planted signal and the OON signal are therefore not comparably easy
to discover even though both have large percentage-point differences.

The planted failure is **high-effect but localization-dependent**.

The OON signal is **high-effect, high-support, low-search-complexity,
and financially salient**.

------------------------------------------------------------------------

## 4. Diagnostic Conclusion

**The closing diagnostic leans structural.**

The evidence is more consistent with the view that the existing Harbor
Ridge experimental environment created **materially asymmetric signal
competition** than with the view that the remaining Scenario 1 miss is
primarily a simple search-order or procedural defect.

This is not decisive proof.

The diagnostic is a post-hoc paper comparison, not a new blind run, and
it does not experimentally separate discovery procedure from
signal-to-noise structure. The frozen V0.2 evaluation conclusion
therefore remains unchanged: discovery procedure, signal-to-noise
structure, or both remain formally possible explanations for the misses.

The directional judgment is nevertheless clear enough to inform project
disposition.

Scenario 1's planted deterioration is substantial after localization,
but its most downstream evidence is carried by only roughly **3--8
admissions per month** within a hidden three-campaign cohort. Recovering
the complete mechanism requires multi-stage relational and temporal
decomposition. By comparison, the OON financial relationship is a
dataset-wide, high-support, financially material first-order feature.

Accordingly, a procedure-only V0.3 would be a **lower-confidence bet
than the raw planted percentage changes alone suggest**. A more
exhaustive procedure could increase sensitivity, but doing so would also
increase the number of subgroup/time/outcome comparisons, the
opportunity for incidental findings to compete for priority, and the
risk of tuning the procedure toward a benchmark whose answers are
already known.

The conclusion of this memo is therefore:

> **The remaining Phase D discovery problem leans more toward structural
> signal asymmetry than toward a straightforward procedural/search-order
> defect. This is a directional post-hoc judgment, not a causal proof
> and not a revision of the frozen V0.2 interpretation.**

------------------------------------------------------------------------

## 5. Disposition

No V0.3 build cycle will be pursued within the current pre-launch V1
scope.

Procedural refinement remains a **deferred, documented opportunity for
consideration after launch / Phase F**. This is an explicit deferral,
not an abandonment of the question.

The reason is project prioritization rather than a claim that further
experimentation could not succeed. The next planned work converts the
validated Harbor Ridge system into its automation, dashboard,
executive-output, case-study, and employer-facing portfolio form. Given
the job-search timeline, the expected value of completing those
deliverables is higher than initiating an open-ended
procedure-versus-experimental-design investigation before launch.

If Phase D discovery research is reopened later, it should begin as a
separately scoped research decision rather than as an assumed
continuation required to make V1 acceptable.

------------------------------------------------------------------------

## 6. Forward-Looking Experimental-Design Lesson

The Phase D experience identifies one design-control lesson for future
scenario work, including the deferred multiple-selectable-demo-datasets
feature:

> **Before calibrating a planted scenario, future baseline datasets
> should be screened for large incidental signals that could compete
> with the planted scenario's blind detectability.**

This check should occur **before** the scenario is calibrated and before
its final detectability thresholds are frozen.

The purpose would not be to remove every realistic baseline difference
or make the planted answer artificially dominant. Real healthcare
operating data should contain legitimate competing signals. The purpose
would be to characterize the baseline signal environment prospectively
so that scenario difficulty is calibrated relative to the strongest
incidental patterns already present.

A future scenario-design process should therefore distinguish at least:

-   magnitude of the planted effect after localization;
-   effective sample size at the downstream endpoint;
-   number of relational/decomposition steps required to expose it;
-   strength and simplicity of large baseline competitors;
-   financial or operational salience of those competitors;
-   whether the planted signal remains detectable without requiring
    answer-aware search instructions.

This would convert a lesson discovered retrospectively in Phase D into a
prospective experimental-design control for future scenario
construction.

------------------------------------------------------------------------

## 7. Phase D Closure and Record Integrity

This memo closes **Phase D as currently scoped**.

It does not modify, supersede, or retroactively reinterpret:

-   the frozen Harbor Ridge Ground-Truth Answer Key;
-   `docs/phase-d-v0.1-evaluation-summary.md`;
-   `docs/phase-d-v0.2-evaluation-summary.md`;
-   the frozen V0.2 Evaluation Interpretation Protocol;
-   the frozen V0.2 discovery procedure;
-   the individual V0.1 or V0.2 Claude outputs.

The Ground Truth remains unchanged.

The V0.1 evaluation remains the contemporaneous record of the V0.1
experiment.

The V0.2 evaluation remains the authoritative criterion-by-criterion
scoring record and the source of the mechanically applied Section 5
interpretation. Its conclusion that discovery procedure versus
signal-to-noise causation remains formally unresolved is not altered by
this memo.

This document sits **alongside** those artifacts as a closing analytical
decision note. Its role is narrower: to record the post-hoc paper
diagnostic used to decide whether another pre-launch Phase D build cycle
was warranted.

The resulting project decision is:

> **Phase D closes at V0.2. The unresolved discovery question is
> documented, the closing diagnostic leans toward structural signal
> asymmetry, procedural refinement is explicitly deferred for possible
> post-launch consideration, and the project advances without
> retroactively changing its Ground Truth or evaluation records.**

**End of Harbor Ridge V1 --- Phase D Closing Diagnostic**
