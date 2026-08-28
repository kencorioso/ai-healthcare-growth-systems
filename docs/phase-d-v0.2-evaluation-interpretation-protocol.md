# Harbor Ridge V1 — Phase D V0.2 Evaluation Interpretation Protocol

**Version:** 0.2
**Status:** FROZEN
**Purpose:** Define, before any V0.2 discovery procedure is designed or analysis is run, how results from Scenario 1, Scenario 2, and the healthy baseline will be classified and interpreted. These rules are intended to prevent post-result reinterpretation, threshold shifting, or retroactive redefinition of success.

---

## 1. Scope

Phase D V0.2 Tier 1 will be evaluated against three datasets:

* Scenario 1
* Scenario 2
* Healthy baseline

Scenario 1 and Scenario 2 will be evaluated against the already-frozen Harbor Ridge Ground-Truth Answer Key.

The healthy baseline will serve as a negative control. Its purpose is to test whether the V0.2 discovery procedure manufactures or overstates a localized failure when no scenario-specific failure was deliberately embedded.

The Ground-Truth Answer Key remains frozen and will not be changed as a result of V0.2 findings.

---

## 2. Scenario-Detection Criteria

Each known scenario will receive one of three detection ratings: **Pass, Partial, or Miss**.

### Pass

A scenario receives **Pass** only if the analysis:

1. identifies the intended hidden failure as a **material executive finding**;
2. localizes it sufficiently to the correct affected business cohort, process, or organizational segment to direct investigation toward the right area;
3. identifies the material direction of the associated downstream deterioration or performance change;
4. distinguishes the affected cohort from appropriate internal comparisons or from the broader organization sufficiently to show that the finding is localized rather than merely aggregate;
5. does not require the Ground Truth's exact wording, exact numeric values, exact identifier list, or exact causal language to qualify.

Exact reconstruction of every Ground-Truth metric is **not required**.

A correct finding appearing only in exploratory commentary, a minor aside, or Findings Not Established does not qualify as a Pass if the analysis does not recognize it as materially important.

### Partial

A scenario receives **Partial** if the analysis enters the correct analytical territory but fails one or more essential elements required for Pass.

Examples include:

* identifying the correct broad function but not the affected cohort;
* identifying one component of the deterioration but not the material mechanism;
* locating an affected subgroup but failing to recognize the temporal or downstream pattern;
* observing relevant evidence but explicitly treating the intended failure as non-material or unestablished.

A Partial result is informative but **does not count as success** for the Tier 1 known-scenario benchmark.

### Miss

A scenario receives **Miss** if the analysis:

* does not materially identify the intended hidden failure;
* concentrates on unrelated findings while failing to recover the intended failure;
* materially localizes the problem to the wrong business area;
* or reaches a conclusion that substantially contradicts the Ground Truth regarding whether the intended affected cohort or process is deteriorating.

---

## 3. Incidental and Competing Findings

The presence of additional valid findings does not by itself reduce a scenario's rating.

An analysis may identify real baseline characteristics, operational anomalies, or secondary findings not included in the designed scenario.

Such findings are acceptable if they are:

* supported by the data;
* appropriately qualified;
* and not elevated in a way that prevents recognition of the planted primary failure.

A real incidental finding is therefore not automatically a false positive.

The evaluation concerns whether the analysis correctly distinguishes **real but secondary observations** from the **primary scenario-specific deterioration** embedded in the dataset.

---

## 4. Healthy-Control Criteria

The healthy baseline is **not** expected to produce a finding of "nothing whatsoever."

The analysis may identify legitimate descriptive differences, stable baseline economic characteristics, unusual records, data-quality questions, or operational observations. The negative-control test concerns whether those observations are represented with a degree of concern, certainty, or executive priority proportionate to what the healthy data actually support.

The healthy-control analysis will receive one of three ratings: **Clean, Borderline, or False Positive**.

### Clean

The healthy control receives **Clean** if the analysis:

1. does not assert a localized deterioration, failure, or worsening process that was not deliberately embedded;
2. does not convert ordinary cross-sectional differences into evidence of decline without appropriate temporal or comparative support;
3. appropriately qualifies findings that require external benchmarks or additional operational context;
4. preserves uncertainty when the data support observation but not diagnosis;
5. does not manufacture a primary executive problem merely because the discovery procedure is searching systematically;
6. presents any legitimate baseline characteristics or incidental anomalies with executive priority proportionate to the evidence.

A Clean result does **not** require the analysis to declare the organization healthy, nor does it require the absence of findings.

### Borderline

The healthy control receives **Borderline** when the analysis stops short of a confident unsupported diagnosis but nevertheless gives one or more non-embedded findings **disproportionate executive weight relative to the evidence**.

Indicators of a Borderline result include:

* technically hedged language paired with prominent placement or urgency that would reasonably steer an executive toward unwarranted concern;
* recommending material investigation or intervention around a pattern that lacks adequate temporal, comparative, or benchmark support;
* repeatedly emphasizing an incidental difference in a manner that functionally elevates it toward a primary problem despite verbal caveats;
* using cautious wording while the overall structure, prioritization, or recommended action communicates substantially greater confidence than the evidence supports.

Classification will therefore consider **the analysis as a whole**, including wording, prominence, prioritization, and recommended action. Hedging language alone does not automatically make a finding appropriately restrained.

A Borderline result is **not classified as a Healthy-Control False Positive**, because the analysis has not crossed the threshold into a materially unsupported primary diagnosis.

However, Borderline also does **not qualify as healthy-control restraint for the strongest Tier 1 outcome**. It represents an intermediate result indicating that increased discovery sensitivity may be creating some executive over-prioritization even though a full false positive was avoided.

### False Positive

The healthy control receives **False Positive** if the analysis presents a non-embedded deterioration or failure as a material primary diagnosis with a level of confidence, specificity, or recommended action not supported by the healthy baseline.

This includes cases in which the analysis materially directs executive attention or intervention toward a supposed localized failure that the evidence does not support, even if minor caveats appear elsewhere in the response.

A legitimate baseline characteristic, correctly identified and appropriately qualified and prioritized, does **not** count as a False Positive.

---

## 5. Tier 1 Outcome-Interpretation Rules

These interpretations are frozen before V0.2 is designed or run.

### A. Known-Scenario Failure

If V0.2 receives **Partial or Miss on either known scenario**, that result will be treated as evidence that the specific V0.2 discovery procedure is **insufficient to reliably recover the previously demonstrated localized failures under the existing Harbor Ridge experimental conditions**.

Such a failure increases the plausibility that experimental signal-to-noise structure contributes to the difficulty, but it does **not** establish that signal-to-noise is the primary cause.

Failure also does not eliminate the possibility that a different general-purpose discovery procedure could succeed.

### B. Known-Scenario Success

If V0.2 receives **Pass on both Scenario 1 and Scenario 2**, the result will be interpreted only as:

> **V0.2 cleared the minimum known-scenario benchmark.**

It will not be interpreted as proof that:

* the discovery procedure generalizes;
* the procedure has been "fixed";
* the improvement would transfer to unseen healthcare datasets;
* or the procedure was free from subtle adaptation to the known evaluation environment.

Generalization remains unproven because the same two scenarios contributed evidence that motivated the redesign.

### C. Healthy-Control False Positive

If the healthy baseline receives **False Positive**, the result will be interpreted as evidence that the V0.2 discovery procedure's increased sensitivity may have come at the expense of analytical specificity or restraint.

A Healthy-Control False Positive means V0.2 **does not qualify as successful Tier 1 validation**, regardless of its Scenario 1 and Scenario 2 ratings.

Known-scenario detection and healthy-control specificity must therefore be evaluated jointly.

### D. Healthy-Control Borderline

If the healthy baseline receives **Borderline**, the result will be treated as an intermediate specificity concern.

Borderline does not erase or downgrade a Pass earned independently on either known scenario, and it will not be relabeled as a False Positive. However, it prevents the combined V0.2 result from qualifying for the strongest Tier 1 interpretation defined in Section 5.E.

If Scenario 1 and Scenario 2 both receive Pass while the healthy control receives Borderline, the permitted conclusion will be:

> **V0.2 cleared the known-scenario benchmark but showed a borderline specificity concern on the healthy control.**

This result demonstrates improved performance on the known scenarios while leaving unresolved whether the procedure achieves an acceptable balance between discovery sensitivity and executive restraint.

It will not be described as successful Tier 1 validation or as evidence of generalization.

### E. Known-Scenario Success Plus Healthy-Control Restraint

If V0.2:

* receives **Pass** on Scenario 1;
* receives **Pass** on Scenario 2;
* and receives **Clean** on the healthy baseline;

the result will be interpreted as the **strongest result available from Tier 1**.

The permitted conclusion will be:

> **V0.2 recovered both known localized failures while preserving appropriate restraint on the healthy control.**

This result still will **not** establish out-of-sample generalization.

Any claim of generalizable diagnostic improvement would require evidence from a genuinely unseen evaluation case or equivalent out-of-sample test.

### F. Mixed Known-Scenario Results

If one known scenario receives Pass and the other receives Partial or Miss, the overall known-scenario benchmark is **not cleared**, regardless of the healthy-control rating.

The individual Pass remains valid evidence that V0.2 recovered that scenario. It will not be discarded or downgraded because the other scenario failed.

The overall interpretation will nevertheless remain governed by Section 5.A:

> **The specific V0.2 discovery procedure was insufficient to reliably recover both previously demonstrated localized failures under the existing Harbor Ridge experimental conditions.**

The healthy-control rating will still be reported independently as Clean, Borderline, or False Positive.

---

## 6. Prohibited Post-Result Reinterpretation

After the three V0.2 outputs are frozen:

* Pass/Partial/Miss definitions will not be changed.
* Clean/Borderline/False Positive definitions will not be changed.
* A Partial result will not be promoted to Pass because the analysis was "close."
* A Borderline healthy-control result will not be promoted to Clean because the analysis used technically cautious wording.
* A Borderline result will not be demoted to False Positive merely because the known-scenario results were strong.
* A real incidental finding will not be retroactively added to Ground Truth.
* A healthy-control anomaly will not be reclassified as an embedded failure.
* Exact numeric agreement will not be newly required if it was not required before the run.
* Exact numeric disagreement will not be ignored if it changes the substantive diagnosis.
* The evaluation standard will not be tightened after an unexpectedly strong result or relaxed after an unexpectedly weak one.
* The combined interpretation will follow the rules frozen in Section 5 rather than a narrative constructed after seeing all three results.

---

## 7. Freeze Statement

This protocol was reviewed and frozen **before the V0.2 discovery procedure was designed and before any V0.2 analysis session was launched**.

Once frozen, it governs classification and interpretation of all three Phase D V0.2 Tier 1 outputs.

The Harbor Ridge Ground-Truth Answer Key remains independently frozen under its existing Freeze Rule.

**End of Harbor Ridge V1 — Phase D V0.2 Evaluation Interpretation Protocol**
