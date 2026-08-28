# Harbor Ridge V1 — Phase D V0.2 Discovery Procedure

**Version:** 0.2  
**Status:** FROZEN  
**Provenance:** Produced by a blind procedure-designer session (Incognito chat, zero Harbor Ridge context) using the frozen designer prompt. Frozen without modification following the independent genericity audits recorded in `docs/phase-d-v0.2-genericity-audit-record.md`.

---

# Relational Database Analytical Discovery Procedure

## Purpose and Scope

This procedure guides systematic investigation of a relational business database to identify meaningful performance patterns, with particular attention to localized effects that aggregate analysis conceals. It applies regardless of industry, schema design, or business model. Follow the phases in order. Do not skip to decomposition before completing structural and aggregate groundwork — premature slicing produces spurious findings, while skipping decomposition entirely produces false negatives. Both failure modes are addressed below.

---

## Phase 1: Structural Understanding

Before computing anything, build a map of the database:

1. **Identify entity tables and fact/event tables.** Distinguish tables that describe *who/what* (entities: customers, products, locations, employees, accounts) from tables that record *what happened* (events: transactions, tickets, shipments, claims, sessions).

2. **Identify grain.** For each fact table, determine the unit of one row (one transaction line, one daily snapshot, one interaction). Misreading grain is the single most common source of downstream analytical error — verify it by checking whether a natural key is actually unique per row.

3. **Map relationships and cardinality.** Trace foreign keys between entities and facts, and between fact tables themselves (e.g., an order table linked to a fulfillment table linked to a returns table). Note which relationships are 1:1, 1:many, or many:many, since this determines whether joins will duplicate or drop rows.

4. **Inventory dimensional attributes.** For each entity table, list attributes that could serve as a grouping dimension: categorical fields (type, tier, region, channel, segment), hierarchical fields (category > subcategory, region > territory > site), and any fields with a natural time component (created date, effective date, status-change date).

5. **Inventory measures.** For each fact table, list the quantitative fields that represent outcomes or performance (amounts, durations, counts, rates, flags indicating success/failure/error/delay). Distinguish *volume* measures (counts, totals) from *rate/quality* measures (ratios, averages, percentages, error rates) — they behave differently under aggregation and require different handling.

6. **Note data quality boundaries.** Identify date ranges, known gaps, nullability patterns, and any fields with suspiciously uniform or default values. Do not attempt to fix these; just record them as constraints on later interpretation.

This phase produces a working schema map and measure inventory. Do not proceed until you can state, for at least the primary fact table(s), the grain, the available dimensions, and the available measures.

---

## Phase 2: Aggregate Baseline

1. **Establish top-line metrics.** For each primary measure, compute the overall value across the full available time range: totals, rates, central tendency, and spread (mean and median together — divergence between them signals skew worth noting).

2. **Establish the overall time trend.** Plot or tabulate each primary measure at a coarse time resolution (e.g., monthly) across the full history. This is the baseline against which all later localized findings will be compared. Note the direction, stability, and any visible inflection points, but do not interpret inflection points yet — record them as candidates for Phase 3 temporal decomposition.

3. **Record aggregate sample sizes.** Note total row counts, total entity counts, and counts per coarse time bucket. These numbers will be the denominators for later significance judgments.

4. **State the aggregate finding explicitly**, including its limitations: an aggregate result describes the average behavior of a mixture of subpopulations and processes. It should be reported as a starting hypothesis space, not a conclusion. Explicitly note: "This aggregate could conceal offsetting or concentrated sub-patterns; Phase 3 determines whether decomposition is warranted."

Do not stop here. An aggregate that looks stable, unremarkable, or "fine" is not evidence of uniformity — it is only evidence about the mixture. This is the specific gap this procedure exists to close.

---

## Phase 3: Principled Dimensional Decomposition

This is the core of the procedure. The goal is to decompose aggregates along dimensions that are *analytically plausible*, not to slice every combination of every field.

### 3.1 Selecting which dimensions merit decomposition

A dimension merits examination if at least one of the following holds:

- **Structural plausibility**: the dimension corresponds to a distinct operational unit, process path, or population with its own resourcing, policy, or handling logic (e.g., location, channel, product line, vendor, employee, plan type, cohort of origin). Dimensions that plausibly reflect *different underlying processes* are higher priority than dimensions that are purely descriptive labels with no operational consequence.
- **Adequate support**: the dimension has enough distinct categories with enough volume per category to support comparison (see 3.4 on sample size). A dimension with 40 categories averaging 3 records each is not usable at that granularity; consider whether a coarser grouping (e.g., a hierarchy parent) is.
- **Prior signal**: something in Phase 2 (an inflection point, an unexplained spread between mean and median, a known data-quality boundary) points toward a specific dimension as a plausible driver.
- **Domain-standard segmentation**: the dimension is one that the business itself would ordinarily use to manage or report performance (this can be inferred from schema design — e.g., if a field is indexed, has a reference/lookup table of its own, or appears repeatedly across fact tables, it is likely operationally meaningful).

A dimension does **not** merit examination merely because it exists and is easy to group by. Reject dimensions that are effectively identifiers (near-unique per row), pure metadata with no operational link to the measure (e.g., a free-text field), or redundant with a dimension already examined (e.g., zip code when region has already been checked and zip code doesn't refine it further).

Build a short, explicit list of dimensions to examine before running any comparisons, with one line of justification each referencing the criteria above. This list is the decomposition plan. Treat it as revisable — if Phase 3 results surface a new plausible dimension, add it and justify it the same way — but do not let the plan grow through unstructured trial and error.

### 3.2 Decomposition procedure

For each dimension on the plan:

1. Compute the primary measure(s) by category within that dimension.
2. Compute the volume (row/entity count) per category alongside the measure — a rate computed on a tiny category is not comparable in confidence to one computed on a large category.
3. Compare each category against two reference points: (a) the overall aggregate from Phase 2, and (b) the other categories within the same dimension.
4. Flag a category as a **candidate localized pattern** if it deviates from the aggregate or from peer categories by a margin that is both practically meaningful (large enough to matter to the business, not merely nonzero) and not plausibly explained by sample size alone (see 3.4).
5. Do not stop at one level. If a flagged category is itself heterogeneous (e.g., "Region X" underperforms, and Region X contains multiple sites), decompose one level further within that category before concluding the pattern is real at that grain. Localization should be pursued to the finest grain that still has adequate support, not left at the first level that showed a difference.
6. Conversely, if no dimension on the plan shows a flagged category, do not manufacture one by re-cutting the same data more finely without a structural justification from 3.1.

### 3.3 When temporal decomposition is appropriate

Temporal decomposition is a special case of dimensional decomposition, warranted when:

- Phase 2's coarse trend showed instability, inflection, or a level shift.
- A dimension flagged in 3.2 might be time-bound rather than persistent (e.g., a category's underperformance might be a recent-only phenomenon or a one-time event, not a standing condition).
- The business process has known temporal structure (onboarding cohorts, seasonal cycles, product launches, policy changes) that could plausibly interact with the measure.

When warranted, decompose time at a resolution finer than Phase 2's baseline (e.g., weekly instead of monthly), but not finer than what still yields adequate per-bucket sample size. Look specifically for: step changes (a persistent shift starting at a point in time), transient spikes (a temporary deviation that resolves), and divergence that only appears when combined with a dimension from 3.2 (a category that was fine historically but has recently deteriorated, or vice versa — this interaction is often exactly what aggregate-only or dimension-only analysis conceals).

Do not decompose time purely exploratory across every possible granularity; anchor the choice of resolution to a reason (cohort length, known cycle, or a signal from Phase 2).

### 3.4 Subgroup and cohort comparisons

Subgroup or cohort comparison (as opposed to simple categorical decomposition) is appropriate when the population is plausibly non-homogeneous in ways that a single dimension doesn't capture — for example, comparing entities by tenure, by origination cohort, by size tier, or by a derived behavioral grouping. Use this when:

- A candidate pattern from 3.2 might be confounded by composition (e.g., a category looks worse only because it disproportionately contains newer or smaller entities, and age/size independently affects the measure).
- The measure is known or suspected to have a lifecycle shape (e.g., degrades or improves with entity age/tenure), making raw cross-sectional comparison misleading without cohort alignment.

When comparing cohorts, align them on the relevant time axis (e.g., "months since origination" rather than calendar month) so that cohorts are compared at equivalent lifecycle points, not equivalent calendar points.

### 3.5 Sample size and uncertainty

Apply this consistently across all decomposition:

- Report the count underlying every category-level statistic alongside the statistic itself. Never present a rate or average without its denominator.
- For rate/proportion measures, use an uncertainty measure appropriate to count data (e.g., a confidence interval or standard error that accounts for the category's volume) rather than treating small-sample rates as directly comparable to large-sample rates.
- Treat categories below a reasonable minimum volume threshold (context-dependent, but as a general floor, treat anything under approximately 30 observations as too sparse for a standalone conclusion) as **directionally suggestive at most** — worth noting, not worth elevating, unless corroborated by Phase 4 tracing through independent related data.
- When comparing many categories within a dimension, account for the fact that examining many categories increases the chance of an extreme-looking one appearing by chance. A single flagged category out of 4-5 examined is more credible on its face than the most extreme of 40 examined. Prefer patterns that are large in magnitude, consistent across adjacent time windows or related sub-categories, and directionally coherent with a plausible mechanism, over the single most extreme point estimate in a large set of categories.

---

## Phase 4: Tracing Candidate Findings Through Related Data

A candidate localized pattern identified in Phase 3 should not be reported on the strength of one measure in one table alone. Before elevating it:

1. **Identify upstream and downstream tables** connected to the fact table where the pattern was found, via the relationship map from Phase 1. Upstream tables often hold explanatory context (what inputs, configurations, or handling produced this population); downstream tables often hold consequences (what happened as a result — retention, cost, escalation, recurrence, satisfaction).

2. **Check whether the pattern is corroborated by an independent measure.** If a category shows a poor value on measure A, check whether related measures B and C (ideally from different tables, not just different columns of the same fact table) move in a consistent direction. Independent corroboration across tables substantially strengthens a candidate finding; its absence should reduce confidence, though absence of a related field is not itself disconfirming if no such field exists.

3. **Check whether the pattern traces to a specific mechanism in the relational structure**, such as a specific upstream source, a specific handling path, a specific vendor/partner/owner, or a specific configuration value that is disproportionately present in the flagged category. Finding such a link does not prove causation, but it converts a floating statistical observation into a structurally grounded one, which is a meaningfully stronger form of evidence.

4. **Check for confounds using related tables**, not just within-dimension controls. If the flagged category also differs systematically from the rest of the population on some other attribute available in a related table (size, complexity, price point, risk profile), note this explicitly as a competing explanation, and if feasible, compare within strata that hold the confound roughly constant.

5. **Do not overreach in tracing.** Follow relationships that are plausibly connected to the measure in question; do not chase every reachable table. If tracing through two or three logically connected tables neither corroborates nor undermines the pattern, say so plainly rather than continuing to search for confirmation.

---

## Phase 5: Evidentiary Threshold for Elevation

Before ranking any finding as important, classify it using the following tiers. State the tier explicitly for every candidate finding carried forward.

**Established / high-confidence** — elevate to a primary finding when:
- The deviation is practically meaningful in magnitude, not just statistically distinguishable from zero.
- It rests on adequate sample size (per 3.5), or, if individual strata are small, the pattern is consistent across multiple adjacent strata or time windows.
- It survives the decomposition-to-finer-grain check in 3.2 (localizes to a specific, describable sub-population rather than dissolving into noise when examined more closely).
- It is corroborated by at least one independent measure or structural mechanism from Phase 4, or, absent that, it is large enough and consistent enough across time/cohort that chance is an implausible sole explanation.

**Suggestive / qualified** — report as noteworthy but not elevated when:
- The magnitude or direction is consistent with a real effect, but sample size is marginal, corroboration is unavailable rather than absent-and-checked, or the pattern did not survive finer-grain decomposition cleanly.
- State explicitly what additional data or volume would be needed to resolve it.

**Unestablished / not supported** — explicitly state that no material localized pattern was found when:
- Decomposition across the justified dimension list did not surface deviations exceeding what sample-size-adjusted variation would plausibly produce.
- Apparent deviations dissolved under finer-grained decomposition, cohort alignment, or confound-stratification.
- This is a legitimate and expected outcome of the procedure, not a failure of it. Do not manufacture a finding to avoid a null result, and do not soften a genuine null result into false ambiguity. State it plainly: "No localized deterioration meeting the evidentiary threshold was identified in the dimensions examined; aggregate patterns are unremarkable and available decompositions are consistent with normal variation."

---

## Phase 6: Ranking

Only findings that reached at least the "suggestive" tier are candidates for ranking; do not rank noise.

Rank findings by a composite of:

1. **Magnitude of practical impact** — the size of the effect scaled by the volume it affects (a large deviation in a small population may matter less in absolute terms than a moderate deviation in a large one, and vice versa; report both the rate-level deviation and its estimated aggregate impact).
2. **Confidence tier** (established outranks suggestive at equal magnitude).
3. **Actionability/specificity** — a finding localized to a specific, well-defined sub-population or mechanism (Phase 4 tracing) is more useful than a diffuse one, even at similar statistical strength, because it points toward a concrete next step.
4. **Persistence** — a finding consistent across multiple time windows or corroborating measures outranks a single-window or single-measure finding of similar magnitude.

Present ranked findings with their tier, supporting sample sizes, and — for anything below "established" — an explicit statement of what would raise its confidence. Do not present a ranked list without also stating, for each entry, why it is not higher-ranked (insufficient volume, single-measure support, unresolved confound, etc.). This keeps the ranking auditable rather than a black-box ordering.

---

## Cross-Cutting Discipline

- At every phase, prefer *fewer, better-justified* comparisons over exhaustive combinatorial slicing. The decomposition plan (3.1) is a commitment device against ad hoc data dredging; deviations from it should be justified in the same terms as the original plan.
- Every quantitative claim about a subgroup must travel with its sample size.
- A pattern is not a finding until it has been checked at a finer grain (3.2), checked for confounds (3.4/4.4), and, where possible, corroborated through a related table (4.2–4.3).
- The absence of a localized problem is a valid, useful, and often correct output of this procedure. Report it with the same rigor as a positive finding.
