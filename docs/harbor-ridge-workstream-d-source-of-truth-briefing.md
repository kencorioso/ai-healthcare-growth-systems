# Harbor Ridge V1 — Workstream D Source-of-Truth Briefing

**Purpose:** This is the factual skeleton for Workstream D's writing (methodology expansion, case study, site copy). Every claim below is sourced to a specific frozen artifact. Write FROM this document — do not reconstruct facts from general memory of the project, and do not introduce a claim that isn't traceable to a row below.

**Hard constraint, carried from the Feature Freeze and the Result-Category Vocabulary:** MISS/MISS/CLEAN must never be converted into a claim that the AI recovered the planted root causes. The $251K figure is an Observed Finding, not a Benchmark Result. Portability (Video 3's territory) is scoped to method, never to the Harbor Ridge product itself. Naming is HEOS (vision) → HEOS Evidence Engine (built) → Harbor Ridge Behavioral Health (testbed), and Harbor Ridge "tested and characterized" the engine — it never "proved" it works.

---

## 0. The Original Executive Problem

Verbatim, from the project's frozen canonical business scenario: **"Why are Harbor Ridge's completed admissions and census declining despite increasing marketing spend and inquiry volume, and where should leadership investigate first?"**

Context: marketing investment and inquiry volume were both increasing, yet completed admissions and census were falling and cost per completed admission was rising. Marketing pointed to admissions as the problem; admissions leadership argued inquiry quality had deteriorated. Neither side had the evidence to resolve the disagreement. This is the executive tension the entire project exists to investigate — introduce it before any schema, dataset, or evaluation detail.

Source: docs/harbor-ridge-business-scenario.md, "Version 1 Executive Business Problem."

## 1. Project Architecture

- **Golden Thread:** acquisition → inquiry → financial qualification → admission → treatment → revenue. Source: `docs/harbor-ridge-source-system-map.md`.
- **Four degradation types** framework (Observability, Identity, Attribution, Outcome-Linkage Loss) — the analytical lens the Source-System Map is built around.
- **Schema:** 11 relational tables, built from a frozen Minimum Viable Data Dictionary, validated with a 22-test constraint suite (structural integrity, conditional rules, foreign keys, enums, booleans, and a full 8-step Golden Thread insert). Source: `schema.sql`, `test_constraints.py`, commit `3442bbb`.

## 2. Synthetic Dataset

- **Harbor Ridge Behavioral Health:** fictional 32-bed dual-diagnosis facility (8 detox / 24 residential), synthetic data only, no PHI.
- **Baseline dataset (V0.1):** generated, validated three independent ways (structural integrity, dual reproducibility, domain realism), then manually CSV-inspected — two real defects found and fixed (LOC transition timing variance, At-Risk Admission rebalancing bias). Committed and pushed, verified live on GitHub.
- **Scenario 1 (paid-search inquiry-quality deterioration):** specified, math-verified (funnel dilution proven by hand before code was written), built as scenario-aware generation (not post-hoc mutation), corrected twice during review (a demotion-logic leak; a May-anchoring distortion where a noisy control month inflated every downstream measurement). Committed `4b6439f`, `6473464`.
- **Scenario 2 (professional-outreach quality deterioration):** same rigor, plus a mandatory large-N mechanism-verification gate (500,000 draws/month, required to converge within ±0.25pp of theoretical targets before any real seed was run) and a caught-and-corrected seed-search near-miss (a queued command to seed-search around a real validation failure was stopped before running). Committed `4efedd2`, `ecd8824`.
- **Ground-Truth Answer Key:** written and frozen before any AI analysis, sourced from the two frozen specifications and each scenario's actual real-seed validation results (not theoretical figures). Includes an explicit Freeze Rule: never revised based on what later analysis finds or misses.

## 3. Phase D V0.1 (Blind Analysis — First Attempt)

- Two isolated blind-test environments built (separate folders outside the Git repo), each containing only the scenario database, a Neutral Analyst Brief (field glossary, no analytical guidance), and frozen Operating Instructions.
- **Result:** Scenario 1 — partial detection, without correct campaign-level localization. Scenario 2 — a clear miss, reaching the opposite rep-level conclusion from Ground Truth.
- A notable secondary finding both sessions converged on independently: an OON-vs-INN claims-realization gap, later traced to the shared baseline-generator code and confirmed as a genuine, unplanted artifact.
- Source: `docs/phase-d-v0.1-evaluation-summary.md`.

## 4. Phase D V0.2 (Blind Analysis — Redesigned, More Rigorous Attempt)

- **Pre-test design:** a frozen Evaluation Interpretation Protocol (Pass/Partial/Miss for known scenarios, Clean/Borderline/False Positive for a Healthy Baseline negative control, a full pre-registered outcome matrix). A blind procedure-designer session (Incognito chat, zero Harbor Ridge context) produced one complete discovery procedure. Two fully independent genericity audits (Claude and ChatGPT, neither seeing the other's conclusions first) both returned 10/10 PASS. Procedure frozen exactly as generated. Committed `511e873`, `b8d809e`.
- **Execution:** three fresh, isolated blind sessions (Scenario 1, Scenario 2, Healthy Baseline), zero coaching, one cleanly-logged technical intervention (a display/export fix, no analytical content touched). All three outputs frozen before any scoring began.
- **Result: Scenario 1 MISS. Scenario 2 MISS. Healthy Baseline CLEAN.** Scored criterion-by-criterion against the frozen Interpretation Protocol.
- **Crossed-localization finding:** each known scenario's elevated incidental finding landed in the *other* scenario's actual business domain — Scenario 1's session elevated a professional-outreach finding (Scenario 2's actual domain); Scenario 2's session elevated a paid-search finding (Scenario 1's actual domain). This was **not** either session discovering the other's specific planted mechanism — the entities and details don't match — only a crossed business domain in each incidental finding.
- This is a categorically different failure mode from V0.1: **mis-detection, not non-detection.** Both misses were affirmative — each session's output stated a conclusion substantially contradicting Ground Truth's actual deterioration, not merely an absence of the right answer.
- Source: `docs/phase-d-v0.2-evaluation-summary.md`.

## 5. Closing Diagnostic

- A post-hoc, non-decisive paper analysis comparing Scenario 1's planted evidence chain against the shared OON structural signal both V0.1 and V0.2 elevated instead.
- **Key reasoning:** the affected cohort's raw size (25–38 opportunities/month) is not the statistically relevant quantity — the actual *admission count* within that cohort (roughly 3–8/month) is, and that is a genuinely harder quantity for any systematic procedure to distinguish from noise than the raw cohort size suggests.
- **Conclusion: leans structural, not decisive proof** — the misses more plausibly reflect experimental signal-to-noise structure than a simple procedural gap, but this is a directional judgment, not a proven finding.
- **V0.3 is explicitly deferred to after launch, not abandoned** — a project-priority decision made given the active job-search timeline, not a capability judgment about whether the underlying approach could eventually work.
- Source: `docs/phase-d-closing-diagnostic.md`.

## 6. Feature Freeze

- The analytical core (source-system architecture, Data Dictionary, schema, generator, all three databases, Ground Truth, Neutral Analyst Brief, V0.2 discovery procedure, all Phase D evaluation artifacts) is formally locked.
- Governing principle: new views of existing data are permitted; new analytical reality is not.
- Source: `docs/harbor-ridge-v1-feature-freeze.md`.

## 7. Workstream A — Experience Architecture

- Eight-section narrative spine: Executive Premise → Hiring-Manager Proof → System → Interactive Evidence → AI Reasoning → Blind Evaluation → Lessons & Limitations → Deeper Resources & Contact.
- Hiring-Manager Proof placed second, deliberately — the strongest evidence shouldn't require the most persistent visitor to reach it.
- A verified Content/Evidence Map ties every public claim to a specific frozen source (used throughout this briefing).
- Source: `docs/harbor-ridge-workstream-a-experience-architecture.md`.

## 8. Workstream B — The $251K Evidence Trail (Real, Verified Numbers)

- **The claim, verbatim:** "an estimated $251,000 additional collections opportunity if out-of-network claims had realized at the in-network rate." This is a collections-realization claim, sourced to Scenario 1's V0.1 blind analysis. It is an **Observed Finding**, not a Benchmark Result — it was not one of the two deliberately hidden problems the engine was tested against.
- **Verified against the real database:** INN billed $1,216,954.73 → collected $812,530.95 (66.77% realization). OON billed $688,137.27 → collected $209,054.85 (30.38% realization). Expected OON collections at the INN rate: $459,452.45. **Computed gap: $250,397.60**, against the frozen "roughly $251,000" — confirmed within rounding.
- The exporter (`scripts/export_evidence_trail_251k.py`) produces byte-identical output across repeated runs (matching SHA-256 hashes), reading only from `harbor_ridge_scenario1.db`.
- The Astro page (`src/pages/index.astro`) shows the full transformation chain (billed → collected → rate → counterfactual → gap) before exposing the underlying claim-level records.
- Source: `docs/harbor-ridge-workstream-b-implementation-spec.md`, commits `925919c`, `a5cf235`.

## 9. Naming and Voice

- **HEOS** — the long-term vision (an AI-enabled executive intelligence layer for healthcare organizations).
- **HEOS Evidence Engine** — the demonstrated V1 capability. An AI reasoning system for evidence-based executive performance analysis.
- **Harbor Ridge Behavioral Health** — the synthetic evaluation testbed. Never the product.
- Harbor Ridge **tested and characterized** the Evidence Engine's capabilities and limitations under controlled blind conditions. It never "proved" the engine works.
- **Result-Category Vocabulary:** Observed Finding (a real pattern the analysis surfaced, not necessarily a planted failure) / Benchmark Result (the formal outcome of testing whether a planted failure was recovered) / Control Result (the formal outcome of the Healthy Baseline negative-control test). Observed finding does not equal benchmark success. Benchmark miss does not mean no useful findings. Healthy-control success does not prove general reliability.
- Voice principles (nine, each cited to a specific script) and the full palette/typography system are frozen in `docs/brand-voice-guidelines-v1.0.md` — this is the canonical source for tone, and Workstream D's prose should be checked against its nine behavioral voice rules before being treated as final.

## 10. What Must NOT Be Claimed, Stated Plainly

- The AI did not "solve" or "find" either of the two planted Harbor Ridge scenario failures. It Missed both, under the final, governing V0.2 evaluation.
- The $251K finding is not evidence the AI passed its benchmark test — it is a separate, legitimate discovery made in the course of testing, explicitly not one of the hidden problems.
- Harbor Ridge itself is not portable to another healthcare vertical. The demonstrated *build process* (source-system mapping → data dictionary → schema → synthetic data → scenario design → frozen Ground Truth → blind evaluation) is what would be rebuilt for a different organization — a claim about the builder's process, not the product's current reach.
- V0.3 is deferred, not because the approach was proven unworkable, but as a documented project-priority decision.
- Do not present the HEOS Evidence Engine V1 as a production-validated, generally reliable, autonomous diagnostic system. Harbor Ridge demonstrated specific analytical capabilities and characterized specific limitations under controlled synthetic conditions. Claims about what the engine can do must remain bounded by what the frozen Harbor Ridge record actually demonstrated.

## 11. How to Tell This Story (Persuasion Guidance, Not New Facts)

Section 10 defines what may be claimed. This section is about how persuasively it may be said — the two are separate questions, and this document should not be read as favoring caution in tone just because it favors caution in fact. Below are reusable rhetorical patterns already proven in this project's own frozen material — not new liberties, applications of moves that already worked.

**Pattern 1 — Scope precisely, then claim confidently within it (the Video 3 move).**
Never soften a limitation into vagueness. State it plainly, then pivot immediately to what's actually true and provable: *"I would not claim [X] is portable. It isn't. What IS portable is my proven process for building an [X]-like system for a genuinely new organization — and I've already executed that process once, completely, from source-system mapping through blind evaluation."* This reads as more confident than an unqualified claim would, because a technically literate reader trusts precise scope over a sweeping one. Use this exact shape anywhere Workstream D discusses what this project does or doesn't prove about future engagements.

**Pattern 2 — Reframe rigorous honesty as the stronger credential, not a caveat (the V0.2 evaluation move).**
A system that only ever reports clean wins is either undertested or hiding its failures. A system that found something real (the $251K Observed Finding) *and* was rigorously, honestly tested against known hard cases — reporting MISS where the evidence supports MISS — is a more complete and more trustworthy picture than either half alone. Don't apologize for the V0.2 result or bury it in a subordinate clause. State it as evidence of process integrity, the same way the evaluation summary and Video 4 already do.

**Pattern 3 — Narrate the moment of near-failure, not just the principle (the Video 4 move).**
"I value honesty" is a claim. "I had a command ready to search for a different result, and I caught myself before running it" is a demonstration. Wherever Workstream D discusses judgment or integrity, prefer the specific, real, in-the-moment version of the story over the abstract statement of the value — the seed-search near-miss, the May-anchoring correction, the metric-conflation catch in Workstream B's own spec review are all real, usable instances of this.

**Pattern 4 — Let a real number carry the persuasive weight (the Video 1 move).**
"$251,000" persuades in a way "a meaningful pattern in the data" does not. Wherever a verified figure exists in this briefing (Section 8's exact numbers, the 22-test constraint suite, the 500,000-draw mechanism-verification gate), use it directly rather than paraphrasing it into something vaguer. Precision is itself a persuasive device here, not just a factual obligation.

**Pattern 5 — State the category before the claim, and treat that precision as confidence, not hedging (the Result-Category Vocabulary move).**
"Here's an Observed Finding" read aloud sounds more credible to a technical audience than an unqualified assertion would, precisely because it signals the speaker knows the difference between categories of evidence and isn't blurring them for effect. Don't relegate the Observed Finding / Benchmark Result distinction to a footnote — state it as part of the claim's opening, the way Video 1 does, so precision itself becomes part of the pitch.

**The governing rule across all five patterns:** every persuasive move above works by being *more specific*, never by being *more sweeping*. If a sentence in Workstream D's output could be made more persuasive by making it vaguer or more general, that's the wrong direction — the same discipline that's held throughout this project applies here too: when a result feels like it needs softening to sound better, the actual fix is more precision, not less honesty.

**Persuasion check:** a rhetorical pattern may change emphasis, sequencing, contrast, framing, or narrative tension. It may not change the factual scope, evidentiary category, certainty level, causal status, or demonstrated generalizability of the underlying claim. If removing the rhetorical framing leaves a stronger factual claim than the source artifact supports, the sentence fails review.

One specific application of this test, worth stating explicitly given Pattern 2 above: honest failure-handling demonstrates the integrity of the development and evaluation process, and Ken's judgment as the builder — it does not demonstrate the reliability of the analytical engine itself. Do not let Pattern 2 slide from "the process was honest" into "therefore the system can be trusted." Those are different claims, and Workstream D is ultimately selling Ken as the builder, using the Evidence Engine as supporting evidence — not selling the Evidence Engine's reliability directly.

---

**End of Workstream D Source-of-Truth Briefing.**

