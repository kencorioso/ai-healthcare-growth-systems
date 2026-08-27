# Harbor Ridge V1 — Phase D V0.1 Blind-Test Evaluation Summary

**Version:** 1.0  
**Status:** Evaluation Record  
**Scope:** Phase D V0.1 blind analyses of Scenario 1 and Scenario 2  
**Purpose:** Record what occurred in the blind test and what was learned. This document does not define V0.2 changes or next-step decisions.

---

## 1. Overall Result

Reasoning discipline was strong in both independent blind runs, including quantification, uncertainty handling, fact-versus-hypothesis separation, and causal restraint. Primary hidden-failure detection was unsuccessful overall: Scenario 1 achieved a partial detection but missed the intended localization and full mechanism, while Scenario 2 clearly missed the intended failure and reached the opposite rep-level conclusion from the Ground Truth.

---

## 2. Phase D V0.1 Scorecard

| Dimension | Scenario 1 | Scenario 2 |
|---|---|---|
| Primary failure detection | **Partial** | **Miss** |
| Correct localization | **Miss** | **Miss** |
| Intended mechanism recovered | **Partial at best** | **Miss** |
| Comparison-group use | **Some, wrong granularity** | **Some, wrong granularity** |
| Quantification | **Strong** | **Strong** |
| Sample-size discipline | **Strong** | **Strong** |
| Fact vs. hypothesis discipline | **Strong** | **Strong** |
| Causal restraint | **Strong** | **Strong** |
| Executive prioritization vs. Ground Truth | **Miss** | **Miss** |

---

## 3. Scenario 1 — Paid-Search Inquiry-Quality Deterioration

### What the blind analysis correctly found

The analysis identified several valid patterns, including:

- lower aggregate Paid admission conversion than Organic acquisition;
- a specific paid-search campaign with zero admissions and low absolute spend;
- lower aggregate OON admission conversion than INN, while correctly treating that difference as statistically unestablished;
- strong relational linkage across inquiries, opportunities, episodes, and claims;
- no evidence that poor linkage or attribution quality explained the observed business patterns;
- no justified conclusion that Admissions competence was the primary problem.

The analysis also maintained appropriate caution around an incidental outreach-rep difference and did not convert it into a performance verdict.

### What the Ground Truth expected but the analysis missed

The intended failure was localized to three affected Google campaigns:

- `CMP-1002` — Behavioral Health - Non-Brand
- `CMP-1003` — Detox Near Me - Geo
- `CMP-1005` — Family Crisis - Non-Brand

The analysis did not reconstruct the required campaign-by-month evidence chain showing:

- affected-cohort Opportunity → Admission conversion deteriorating from **32.0% in May → 12.5% in June → 7.9% in July**;
- July OON concentration reaching **60.5%**;
- poor VOB outcomes progressing from **29.2% → 40.0% → 64.0%**;
- Not Financially Cleared progressing from **36.0% → 58.3% → 73.7%**;
- healthy internal Google comparison campaigns remaining comparatively stable;
- affected-campaign inquiry volume remaining present rather than collapsing.

The intended executive finding was therefore not recovered: paid-search activity remained present while the financial quality and downstream admission yield of a specific campaign cohort deteriorated.

### Evaluation

The blind analysis compared acquisition performance primarily at aggregate or individual-campaign levels rather than performing the required **campaign × month** decomposition across financial-quality and admission outcomes. The result was a partial detection of the relevant analytical territory without correct localization of the planted mechanism.

---

## 4. Scenario 2 — Professional-Outreach Quality Deterioration

### What the blind analysis correctly found

The analysis correctly observed that:

- facility-wide opportunity volume remained stable across May–July;
- blended admission conversion remained essentially flat;
- aggregate rep-level referral volume appeared fairly even;
- no facility-wide acquisition or admissions decline was established;
- several unrelated patterns in the database, including apparent residential census over-capacity and a paid-search campaign outlier, warranted examination but did not justify unsupported causal conclusions.

The finding that rep-level surface activity looked relatively healthy is itself consistent with part of the designed scenario: the hidden failure was intended to exist beneath superficially healthy activity.

### What the Ground Truth expected but the analysis missed

The intended affected cohort was **Alicia Ferreira's 14-account owned portfolio**, defined through professional-account ownership.

The analysis did not reconstruct the required rep-owned-portfolio-by-month evidence chain showing:

- outreach activities of **25 → 31 → 22**;
- referral events of **15 → 17 → 14**;
- referral linkage deteriorating from **100.0% → 76.5% → 78.6%**;
- OON + Private Pay economic compatibility deteriorating from **46.7% → 38.5% → 27.3%**;
- linked-opportunity admission conversion deteriorating from **26.67% → 15.38% → 9.09%**;
- referral-event admission yield deteriorating from **26.67% → 11.76% → 7.14%**;
- pooled three-month referral-event admission yield of **15.22%**;
- the healthy comparison behavior of Marcus Webb, Priya Anand, and Devon Castillo.

Instead, the blind analysis concluded that rep-level referral performance was fairly even and that no individual rep was established as underperforming.

### Evaluation

The blind analysis stopped at an aggregate rep comparison rather than performing the required **rep-owned portfolio × month** decomposition through referral linkage, economic compatibility, and downstream admission yield. This produced a clear miss and an opposite rep-level conclusion from the Ground Truth.

---

## 5. Shared OON Claims-Realization Finding

Both isolated blind sessions independently elevated a large OON claims-realization difference.

Scenario 1 observed approximately:

- INN allowed amount: **78.8% of billed**
- OON allowed amount: **50.6% of billed**

Scenario 2 independently observed approximately:

- INN allowed amount: **78.7% of billed**
- OON allowed amount: **51.0% of billed**

Review of the shared baseline-generation logic confirmed that this pattern is structurally generated. Allowed amounts are produced using different payer-relationship distributions:

```python
if payer_relationship == "INN":
    allowed_amount = billed_amount * uniform(0.72, 0.85)

elif payer_relationship == "OON":
    allowed_amount = billed_amount * uniform(0.40, 0.65)
```

The near-identical blind findings are therefore a **genuine shared-baseline artifact**, not a hallucination or random coincidence. Claude correctly discovered a real economic characteristic present in both databases.

Relative to the frozen Ground Truth, the error was not observing the OON difference. The error was **executive prioritization**: a large baseline characteristic was elevated above the smaller, scenario-specific planted deterioration signals.

---

## 6. Open Interpretation for V0.1

The blind-test result supports one clear observation: the operating instructions produced disciplined analysis once candidate findings were identified, but neither run successfully decomposed the data to the granularity required to recover its planted hidden failure.

One possible explanation is a **discovery-procedure gap**: HEOS V0.1 may not yet search the available dimensional space systematically enough before ranking candidate findings.

A companion hypothesis must remain open. The OON signal is structurally broad, high-N, and dollar-denominated across both scenario databases, while the planted failures occupy much smaller cohorts. Scenario 1's affected cohort is approximately **25–38 opportunities per month**, and Scenario 2's affected cohort is approximately **9–11 linked opportunities per month**. The experimental environment may therefore contain a genuinely lopsided signal-to-noise relationship in which a stable baseline economic characteristic naturally dominates smaller planted signals during exploratory analysis.

At the close of V0.1 evaluation, the evidence does not establish whether the misses are explained purely by discovery procedure, partly by experimental signal-to-noise structure, or by both.

Neither interpretation implies that the frozen Ground Truth should be revised.

---

## 7. Freeze-Rule Status

The **Harbor Ridge Ground-Truth Answer Key was not modified** in response to anything Claude found, failed to find, prioritized, or omitted during Phase D V0.1.

This preserves the Ground Truth's pre-analysis Freeze Rule and keeps the blind-test evaluation anchored to the benchmark defined before Claude's analyses were run.

Design of any **Phase D V0.2 discovery procedure** is a separate upcoming decision. It is intentionally outside the scope of this evaluation record.

**End of Harbor Ridge V1 — Phase D V0.1 Blind-Test Evaluation Summary**
