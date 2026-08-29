# Harbor Ridge V1 --- Phase D V0.2 Blind-Test Evaluation Summary

**Version:** 1.0\
**Status:** Evaluation Record\
**Scope:** Phase D V0.2 blind analyses of Scenario 1, Scenario 2, and
the healthy-baseline negative control\
**Purpose:** Record what occurred in the V0.2 blind test and what was
learned under the frozen Evaluation Interpretation Protocol. This
document does not define a V0.3 design or recommend a next step.

------------------------------------------------------------------------

## 1. Overall Result

Under the frozen Phase D V0.2 Evaluation Interpretation Protocol,
**Scenario 1 was classified Miss, Scenario 2 was classified Miss, and
the healthy baseline was classified Clean**.

This is a categorically different failure mode from V0.1. V0.1 was
principally a **non-detection / insufficient-decomposition failure**:
the analyses stopped at overly aggregated comparisons and did not
recover the required localized evidence chains. V0.2 was a
**mis-detection failure**: the more systematic discovery procedure found
real, localized, well-corroborated incidental findings, elevated them as
the material executive findings, and affirmatively characterized the
business domains containing the planted failures as normal or
non-problematic. Both known-scenario results are Misses under the frozen
V0.2 protocol, but the observed failure mode is not the same as V0.1 and
should not be summarized as "no improvement."

The healthy-baseline negative control behaved differently. It found
legitimate candidate signals but preserved uncertainty, discounted
unsupported escalation, and did not manufacture a material localized
problem.

------------------------------------------------------------------------

## 2. Phase D V0.2 Classification Scorecard

  Evaluation                                        Result
  ------------------------------------------------- -----------
  Scenario 1 --- known-scenario detection           **Miss**
  Scenario 2 --- known-scenario detection           **Miss**
  Healthy Baseline --- negative-control restraint   **Clean**

### Known-scenario Pass criteria

  -----------------------------------------------------------------------
  Section 2 Pass          Scenario 1              Scenario 2
  Criterion                                       
  ----------------------- ----------------------- -----------------------
  1\. Intended hidden     **Fail**                **Fail**
  failure identified as a                         
  material executive                              
  finding                                         

  2\. Correct             **Fail**                **Fail**
  localization to the                             
  actual affected                                 
  cohort/process                                  

  3\. Correct material    **Fail**                **Fail**
  direction of associated                         
  downstream                                      
  deterioration                                   

  4\. Correct affected    **Fail**                **Fail**
  cohort distinguished                            
  from appropriate                                
  internal comparisons                            

  5\. Exact Ground-Truth  **Evaluation tolerance  **Evaluation tolerance
  reconstruction not      satisfied;              satisfied;
  required                non-dispositive**       non-dispositive**

  Partial criteria        **No**                  **No**
  satisfied                                       

  Affirmative Miss        **Yes**                 **Yes**
  definition satisfied                            

  **Final                 **MISS**                **MISS**
  classification**                                
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Scenario 1 --- Paid-Search Inquiry-Quality Deterioration

### What V0.2 found

The V0.2 analysis identified **Marcus Webb** as an established
professional-outreach performance finding on two independent measures:

-   reciprocated-contact rate of **60.0% (45/75)** versus
    **73.8--76.7%** for the other reps;
-   referral-to-admission conversion of **12.0% (3/25 matched
    referrals)** versus **19.4--39.3%** for peers.

The analysis tested persistence across time and activity types and
examined portfolio mix, activity/referral volume, and data-quality mix
as possible confounds. It concluded:

> "Established finding: Marcus Webb (outreach rep) is underperforming on
> two independent measures"

and prioritized:

> "Marcus Webb's numbers --- this is the one lever with real, actionable
> signal."

It also identified two payer-level signals, Keystone Wellness Plan and
Redwood Mutual, but appropriately left them suggestive because of small
admitted-patient denominators.

These are data-supported incidental findings. Their validity does not
make them the planted Scenario 1 failure.

### What Ground Truth required

Scenario 1's intended failure was localized to three Google Ads
campaigns:

-   `CMP-1002` --- Behavioral Health - Non-Brand
-   `CMP-1003` --- Detox Near Me - Geo
-   `CMP-1005` --- Family Crisis - Non-Brand

The required evidence chain was:

``` text
Affected Google campaigns
→ worsening OON opportunity mix
→ worsening VOB / financial clearance
→ falling Opportunity → Admission conversion
→ fewer downstream episodes / claims
```

The frozen real-seed evidence included affected-cohort Opportunity →
Admission conversion of **32.0% → 12.5% → 7.9%**, Poor VOB outcomes of
**29.2% → 40.0% → 64.0%**, and Not Financially Cleared rates of **36.0%
→ 58.3% → 73.7%**.

V0.2 did not recover this as a material finding.

### Criterion-by-criterion evaluation

**Criterion 1 --- Material executive finding: Fail.** The intended
paid-search failure was not elevated. Marcus Webb was elevated instead.

**Criterion 2 --- Correct localization: Fail.** The established finding
was localized precisely, but to the wrong cohort.

**Criterion 3 --- Correct downstream direction: Fail.** The affected
paid-search cohort's worsening financial quality and admission
conversion were not identified.

**Criterion 4 --- Correct internal differentiation: Fail.**
Marcus-versus-peer comparisons were sophisticated but bracketed the
wrong cohort.

**Criterion 5 --- Exact reconstruction not required: Evaluation
tolerance satisfied; non-dispositive.** The failure was substantive
rather than a disagreement over exact identifiers, wording, or numeric
reconstruction.

### Partial test

**Partial was not satisfied.** The analysis examined payer mix,
financial clearance, admissions, lead source, and funnel conversion, but
did not recover a material component of the intended localized
paid-search mechanism.

### Affirmative Miss test

**Miss was affirmatively satisfied.** The output did not merely omit the
planted finding. It stated:

> "Aggregate admissions, payer mix, financial collections, and
> authorization management all look like normal operating variation."

It also described the financially-cleared-but-not-admitted conversion
pattern as:

> "essentially flat across month, payer type, and lead source --- it's a
> structural funnel rate, not a localized problem to fix."

Those conclusions substantially contradict the frozen Ground Truth
regarding deterioration in the intended affected cohort.

**Final classification: MISS.**

------------------------------------------------------------------------

## 4. Scenario 2 --- Professional-Outreach Quality Deterioration

### What V0.2 found

The V0.2 analysis identified **Behavioral Health - Non-Brand** as a
sustained paid-search conversion problem:

  Month     Touches   Conversions   Conversion Rate   Cost/Lead
  ------- --------- ------------- ----------------- -----------
  May            54            10             18.5%       \$155
  June           61             6              9.8%       \$302
  July           47             5             10.6%       \$295

It checked the pattern across ad groups and match types, verified that
platform conversions matched linked inquiries 1:1, ruled out a tracking
artifact, and noted stable spend while cost per lead approximately
doubled.

It described the finding as:

> "What stands out: one campaign has quietly broken"

and concluded:

> "that's the one lever I'd pull on this week."

This was a real, localized, internally compared finding in the Scenario
2 database. It was not the planted Scenario 2 failure.

### What Ground Truth required

Scenario 2's intended failure was centered on **Alicia Ferreira's owned
portfolio of 14 professional accounts**.

The required evidence chain was:

``` text
Alicia-owned professional portfolio
→ activity remains present
→ referral effectiveness weakens
→ economic compatibility deteriorates
→ referral-derived admission yield falls
```

The frozen evidence included activities **25 → 31 → 22**; referral
events **15 → 17 → 14**; referral linkage **100.0% → 76.5% → 78.6%**;
OON + Private Pay compatibility **46.7% → 38.5% → 27.3%**;
linked-opportunity admission conversion **26.67% → 15.38% → 9.09%**; and
referral-event admission yield **26.67% → 11.76% → 7.14%**.

V0.2 did not recover this as a material finding.

### Criterion-by-criterion evaluation

**Criterion 1 --- Material executive finding: Fail.** The intended
professional-outreach failure was not elevated.

**Criterion 2 --- Correct localization: Fail.** The campaign was
precisely localized, but it was not Alicia Ferreira's owned
professional-account portfolio.

**Criterion 3 --- Correct downstream direction: Fail.** The
deterioration in referral linkage, economic compatibility, and
referral-derived admission yield was not recovered.

**Criterion 4 --- Correct internal differentiation: Fail.** The
campaign-versus-paid-search-peer comparison was well constructed but
bracketed the wrong cohort.

**Criterion 5 --- Exact reconstruction not required: Evaluation
tolerance satisfied; non-dispositive.** The disagreement was substantive
rather than a failure to reproduce exact wording or numbers.

### Partial test

**Partial was not satisfied.** The analysis examined
professional-outreach data but did not recover Alicia's owned portfolio
or a material component of its downstream deterioration.

### Affirmative Miss test

**Miss was affirmatively satisfied.** The output stated:

> "Referral rep performance (4 reps) and reciprocation rates are all in
> a normal, tight band."

That conclusion substantially contradicts the frozen Ground Truth
regarding deterioration in the intended professional-outreach cohort.

**Final classification: MISS.**

------------------------------------------------------------------------

## 5. Crossed Localization

The two V0.2 known-scenario runs produced a notable crossed-domain
pattern:

-   **Scenario 1**, whose planted failure was in paid search, elevated
    **Marcus Webb / professional outreach**.
-   **Scenario 2**, whose planted failure was in professional outreach,
    elevated **Behavioral Health - Non-Brand / paid search**.

This is a **crossed localization of business domains**, not a
cross-discovery of the other scenario's planted answer.

Scenario 1 did not discover Scenario 2's Ground-Truth mechanism: Marcus
Webb is not Alicia Ferreira, and the identified pattern is not Alicia's
owned-portfolio deterioration chain.

Scenario 2 likewise did not discover Scenario 1's Ground-Truth
mechanism: Behavioral Health - Non-Brand alone is not the three-campaign
affected cohort, and its conversion/CPL pattern is not the planted
OON/VOB/financial-clearance/admission-conversion chain.

The factual observation is limited to this: **the business domain of
each elevated incidental finding crossed into the domain containing the
other scenario's planted failure.**

------------------------------------------------------------------------

## 6. Healthy Baseline --- Negative Control

The healthy-baseline analysis stated:

> "Bottom line: I didn't find a material localized problem."

It nevertheless performed systematic decomposition and surfaced
legitimate descriptive differences without converting them into
unsupported diagnoses.

### Section 4 Clean criteria

  -----------------------------------------------------------------------------
  Clean Criterion               Result                  Key Evidence
  ----------------------------- ----------------------- -----------------------
  1\. No unsupported localized  **Pass**                Explicitly found no
  deterioration asserted                                material localized
                                                        problem

  2\. No ordinary               **Pass**                INN/OON claims
  cross-sectional difference                            difference treated as
  converted into decline                                structural rather than
                                                        deterioration

  3\.                           **Pass**                Organic and Detox Geo
  Benchmark/context-dependent                           findings labeled
  findings appropriately                                soft/watch signals
  qualified                                             

  4\. Uncertainty preserved     **Pass**                Explicit
                                                        multiple-comparisons
                                                        reasoning; lack of
                                                        localization reduced
                                                        confidence

  5\. No primary executive      **Pass**                No unsupported
  problem manufactured                                  intervention target
                                                        elevated

  6\. Executive priority        **Pass**                "Watch" rather than
  proportionate to evidence                             "fix"; additional data
                                                        recommended

  **Final classification**      **CLEAN**               All six Clean criteria
                                                        satisfied
  -----------------------------------------------------------------------------

### OON handling relative to V0.1

The healthy-baseline run encountered the large structural INN/OON claims
pattern that had attracted executive priority in V0.1. In V0.2, the
analysis recognized that the allowed-amount split:

> "maps exactly onto in-network vs. out-of-network status"

and characterized it as:

> "the expected contractual structure ... not a payer performance
> issue."

This is a factual improvement in handling relative to V0.1: the large
OON baseline characteristic was identified without being promoted into a
primary operational diagnosis.

### Multiple-comparisons restraint

The organic-channel signal was explicitly discounted:

> "I ran \~15 comparisons in this pass, so a single one at this
> significance level is exactly what I'd expect to see from chance
> alone."

The Detox Near Me - Geo campaign was also left unestablished. Failure to
reveal a specific keyword, geography, or match-type driver was treated
as evidence for **less confidence**, not as a reason to continue slicing
until a diagnosis appeared.

**Borderline was not satisfied.** The soft findings were not paired with
disproportionate urgency or intervention.

**False Positive was not satisfied.** No non-embedded deterioration was
presented as a material primary diagnosis.

**Final classification: CLEAN.**

------------------------------------------------------------------------

## 7. Technical Intervention Record

One intervention occurred across the three V0.2 execution sessions.

-   **Scenario 1:** no intervention.
-   **Scenario 2:** the initial terminal display of the
    already-completed analysis rendered with corrupted/garbled
    formatting. Under the Run Manifest's technical-intervention rule,
    the same session was asked only to export its own already-completed
    response verbatim to a file. No analytical content was requested,
    changed, or added.
-   **Healthy Baseline:** no intervention.

This was a display/export correction rather than analytical coaching or
prompt refinement and remained within the technical-failure allowance
defined before execution.

------------------------------------------------------------------------

## 8. Frozen Section 5 Outcome

The individual classifications were fixed before combined
interpretation:

-   **Scenario 1: MISS**
-   **Scenario 2: MISS**
-   **Healthy Baseline: CLEAN**

Section 5.A applies because its trigger is **"Partial or Miss on either
known scenario."** Both known scenarios independently satisfy that
condition.

The mechanically permitted known-scenario conclusion is:

> **The specific V0.2 discovery procedure was insufficient to reliably
> recover the previously demonstrated localized failures under the
> existing Harbor Ridge experimental conditions.**

Under Section 5.A, this failure **increases the plausibility that
experimental signal-to-noise structure contributes to the difficulty,
but it does not establish that signal-to-noise is the primary cause.**
It also **does not eliminate the possibility that a different
general-purpose discovery procedure could succeed.**

The healthy-control result is reported alongside the known-scenario
result as **Clean**.

No stronger success, generalization, causal, or failure-mechanism
conclusion is authorized by the frozen protocol.

------------------------------------------------------------------------

## 9. Open Interpretation After V0.2

The three propositions carried into V0.2 remain the appropriate bounded
frame:

1.  **V0.1's epistemic discipline worked.** Quantification, sample-size
    caution, uncertainty handling, and causal restraint were
    consistently strong.
2.  **The known localized failures still were not reliably recovered.**
    V0.2's more systematic discovery procedure produced two affirmative
    Misses under the frozen protocol.
3.  **The explanation remains unresolved.** The evidence does not
    establish whether the misses are explained primarily by the
    discovery procedure, by the experimental signal-to-noise structure,
    or by some combination of both.

V0.2 adds one bounded fact: **a more systematic general-purpose
discovery procedure was not sufficient to recover either known planted
failure under the existing Harbor Ridge experimental conditions.** This
establishes that the attempted procedural fix did not fully solve the
benchmark problem.

It does **not**, by itself, determine which of the two original
hypotheses is correct. It does not establish that signal-to-noise is the
primary cause, and it does not establish that discovery procedure alone
explains the misses.

The healthy-baseline Clean result remains a separate observation:
increased systematic decomposition did not, in this negative control,
manufacture or over-prioritize a localized failure.

This evaluation summary makes **no recommendation for a V0.3 design or
any other next step**. That remains a separate, upcoming decision
outside the scope of this record.

------------------------------------------------------------------------

## 10. Freeze-Rule Status

The **Harbor Ridge Ground-Truth Answer Key was not modified** in
response to anything Claude found, failed to find, prioritized, or
rejected during Phase D V0.2.

This preserves the Ground Truth's pre-analysis Freeze Rule and keeps the
evaluation anchored to the benchmark defined before the V0.2 analyses
were run.

The V0.2 classifications and combined interpretation were applied under
the independently frozen **Phase D V0.2 Evaluation Interpretation
Protocol**. No Pass/Partial/Miss, Clean/Borderline/False Positive, or
Section 5 interpretation rule was revised after the outputs were seen.

Any decision concerning V0.3 or another next step is intentionally
outside this evaluation record.

**End of Harbor Ridge V1 --- Phase D V0.2 Blind-Test Evaluation
Summary**
