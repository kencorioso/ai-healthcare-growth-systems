# Harbor Ridge V1 — Workstream A: Experience Architecture & Scope

**Status:** Revised draft, reconciliation fixes applied (v2) — ready for final gate check before freeze
**Purpose:** Formally record the employer-facing visitor journey, video placement, and content/evidence map that Workstreams B and F will build against.
**Gate (per roadmap):** Must answer what a hiring manager understands after 90 seconds, 5 minutes, and 20 minutes on the site; every public-facing claim must have an identified source in the frozen project record.

---

## 1. The Frozen Narrative Spine

The site is one continuous, unified narrative — not a scattered grid of assets — structured as eight sequential sections.

**Governing rule:** A visitor can stop at any point and already have received a complete, honest impression; nothing downstream is required to make an upstream section true. The site may reward deeper exploration, but it must never require deeper exploration to correct an impression created earlier. (Example: the $251K Observed Finding must never be presented in Section 1 in a way that reads as benchmark success, requiring Section 6 to correct that impression 15 minutes later. The opening has to be true on its own.)

| # | Section | Core Question It Answers |
|---|---|---|
| 1 | Executive Premise | What executive problem is this designed to address, and why does it matter? |
| 2 | Hiring-Manager Proof | Does this person show real judgment when things don't go as planned? |
| 3 | System | What is HEOS, what is the Evidence Engine, and how do they relate to Harbor Ridge? |
| 4 | Interactive Evidence | Can I see this actually work, not just read about it? |
| 5 | AI Reasoning | How does the Evidence Engine actually investigate a database? |
| 6 | Blind Evaluation | How was this tested, and how do I know the test wasn't rigged? |
| 7 | Lessons & Limitations | What doesn't this do yet, and what would it take to build it for a different organization? |
| 8 | Deeper Resources & Contact | Where do I go to verify this myself, or reach the builder? |

Hiring-Manager Proof is deliberately placed second, not last — the strongest, most differentiating evidence should not be something only the most persistent visitor reaches.

---

## 2. Video Placement Map

| Video | Persona / Hook | Section |
|---|---|---|
| Video 1 | CEO — risk/money (the $251K Observed Finding) | Executive Premise |
| Video 4 | Hiring Manager — judgment under failure (the seed-search near-miss, MISS/MISS/CLEAN) | Hiring-Manager Proof |
| Video 2 | Technical practitioner — rigor/craft (the blind-evaluation design itself) | Blind Evaluation |
| Video 3 | Different-vertical decision-maker — feasibility for them specifically | Lessons & Limitations |

Sections 3, 4, and 5 (System, Interactive Evidence, AI Reasoning) carry no video, by design — this keeps the site from becoming a video gallery wearing a website costume.

---

## 3. Content / Evidence Map

Every public claim traces to a source, ranked by authority: **frozen analytical artifact > frozen roadmap/project decision > public-facing asset.** A public-facing script or page is a *consumer* of this map, never a source for its own claims.

| Public Claim | Frozen Source |
|---|---|
| Three-layer naming (HEOS / HEOS Evidence Engine / Harbor Ridge) and "tested and characterized," never "proved" | Roadmap Revision 11 |
| The $251,000 Observed Finding | `scenario1_claude_analysis_v0.1.md` (frozen blind-test output) |
| Observed Finding / Benchmark Result / Control Result definitions | Roadmap Revision 10.3, "Result-Category Vocabulary for Public Presentation" |
| Golden Thread (acquisition -> inquiry -> financial qualification -> admission -> treatment -> revenue) | `docs/harbor-ridge-source-system-map.md` |
| Scenario 1 MISS, Scenario 2 MISS, Healthy Baseline CLEAN | `docs/phase-d-v0.2-evaluation-summary.md` |
| Crossed-localization finding | `docs/phase-d-v0.2-evaluation-summary.md`, Section 5 |
| Blind-test isolation design (frozen database, isolated folder, no cross-exposure) | `docs/phase-d-v0.2-run-manifest.md` |
| Healthy Baseline as negative control | `docs/phase-d-v0.2-evaluation-interpretation-protocol.md`, Section 4 |
| Scenario 2 generation-time seed-search near-miss, caught before execution | `docs/harbor-ridge-scenario-2-specification.md`, Section 17.K.6, and `validate_scenario2.py` (commit `ecd8824`) -- verified directly against the committed file, confirming `SCENARIO_2_SEED` was never searched over |
| Scenario 2 garbled-terminal-output technical intervention during V0.2 execution | `docs/phase-d-v0.2-run-manifest.md`, Intervention Log |
| Decision to defer V0.3 rather than iterate to a passing result | `docs/phase-d-closing-diagnostic.md` |
| Effective-sample-size reasoning (3-8 admissions/month vs. 25-38 cohort size) | `docs/phase-d-closing-diagnostic.md` |
| Genericity audits (dual independent review, 10/10 PASS) | `docs/phase-d-v0.2-genericity-audit-record.md` |
| Feature Freeze scope boundary | `docs/harbor-ridge-v1-feature-freeze.md` |
| Portability scope (method transfers, Harbor Ridge schema does not) | `docs/harbor-ridge-v1-feature-freeze.md`, Section 6.2 |
| "I've already executed this build process once, completely" (Video 3) | Full commit history, Phase A-D |

Any future public claim not traceable to a row in this table should not go live without first being added here, with its source verified, not assumed.

---

## 4. The Three-Tier Understanding Test

Rewritten around realistic scanning behavior, not sequential video-watching.

**After 90 seconds:** A visitor who scans the opening experience should understand what Ken built, why he built it, what executive problem it addresses, that Harbor Ridge is a synthetic testbed, and that the evaluation produced both useful findings and documented failures rather than a manufactured success story.

**After 5 minutes:** A visitor who explores the opening sections should understand the HEOS / Evidence Engine / Harbor Ridge relationship, see the $251K Observed Finding and its evidence trail, understand that the system failed to recover the two deliberately hidden problems in its final evaluation, and understand why that result was preserved rather than optimized away.

**After 20 minutes:** A visitor should understand the full blind-evaluation methodology, the honest MISS/MISS/CLEAN result and why it's presented as evidence of rigor rather than hidden, the specific and honest scope of what would transfer to their own organization, and have a clear path to the whitepaper, GitHub repo, or direct contact.

---

## 5. Explicitly Out of Scope for Workstream A

- Visual design, layout, and styling (Workstream F)
- The dashboard's actual implementation and the evidence-trail feature's technical build (Workstream B)
- Full site copy and case-study prose (Workstream D)
- Video production/recording (Workstream G)
- Any new analytical claim, dataset, or scenario -- prohibited outright by the Feature Freeze, not merely deferred

---

**End of Harbor Ridge V1 -- Workstream A: Experience Architecture & Scope (v2, revised)**
