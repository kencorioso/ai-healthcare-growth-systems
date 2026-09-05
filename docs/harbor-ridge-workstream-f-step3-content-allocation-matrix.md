# Harbor Ridge V1 — Workstream F, Step 3: Content Allocation Matrix

**Status:** APPROVED
**Governs:** Content allocation across the five-page hub-and-spoke architecture (Home, Evidence, Methodology & Evaluation, Portability & Lessons, About/Contact), per `docs/harbor-ridge-workstream-f-step2-information-architecture.md`.
**Source material:** Built directly from the live, frozen `docs/harbor-ridge-v1-site-copy.md` (Workstream A/D content) and `docs/harbor-ridge-workstream-f-step2-information-architecture.md` (Step 2 architecture), verified against GitHub at time of drafting, not reconstructed from memory.
**Purpose:** Establish, before any Home-page compression or Astro implementation began, exactly what happens to each frozen content unit — preserved, compressed, adapted, newly written, or linked deeper — so that compression could not quietly become deletion.

---

## Matrix

| # | Frozen Source Section | Destination Page | Treatment | Why This Treatment | Deeper Destination If Compressed | Claim-Risk / Persuasion Note |
|---|---|---|---|---|---|---|
| 1 | Executive Premise | Home | Preserve | Already written to function exactly as Home's opening; minimal compression needed. | — | The "It was not a Benchmark Result" disclaimer is already correctly inline — must not be trimmed for brevity. |
| 2 | Hiring-Manager Proof | Home | Preserve | Already Home-scoped. | — | MISS/MISS/CLEAN first stated here in full, alongside "that doesn't demonstrate reliability... it demonstrates how I respond" — the single most important guardrail sentence on the page. Cannot be softened or cut. |
| 3 | System | Home, compressed | Compress | Per the frozen mapping itself. Full schema/constraint-suite technical specificity doesn't belong on Home; the naming hierarchy and Golden Thread concept do. | Methodology & Evaluation | Low risk on schema detail (safe to cut heavily). The HEOS / Evidence Engine / Harbor Ridge naming distinction is NOT safe to compress away — collapsing it would reintroduce the exact conflation the naming resolution fixed earlier in this project. |
| 4 | Interactive Evidence | Evidence | Preserve + Link deeper (live embed is the deeper link) | 1:1 section-to-page mapping already. | — | Flagged duplication risk: frozen text states exact INN/OON numbers narratively; the live embedded page renders the same numbers again. Implementation should let narrative text stay qualitative, letting the embed carry the literal figures. |
| 5 | AI Reasoning | Methodology & Evaluation | Preserve | Appropriately scoped for this page's technical depth. | — | "Useful discovery and successful diagnosis are not the same claim" is a load-bearing taxonomy sentence — must survive intact. |
| 6 | Blind Evaluation | Methodology & Evaluation | Preserve | Same. | — | MISS/MISS/CLEAN's third appearance — legitimate repetition for orientation (different depth than Home's instance), not duplication. |
| 7 | Lessons & Limitations | Portability & Lessons | Preserve | Already exact-fit. | — | "I would not present V1 as production-validated, generally reliable" is the fifth guardrail from the Workstream D briefing — must survive verbatim or near-verbatim. Portability formula must stay process-scoped, never product-scoped. |
| 8 | Deeper Resources & Contact | About / Contact | Adapt | Frozen section is entirely a "go deeper" index (case study, methodology, GitHub, whitepaper); contains zero first-person biographical content. | — | Low claim-risk (an index, not an evidentiary claim) but a real content-completeness gap — see row 9. |
| 9 | *(no frozen source)* — concise professional bridge | About / Contact | **NEW COPY REQUIRED** — source only from verified career facts; draft during remaining-page population. | Step 2's spec explicitly requires "a concise account of Ken, why this project connects to his healthcare/growth/AI experience"; Workstream D never wrote it. | — | Bounded gap, does not create architectural uncertainty. Not required to resolve before Home proceeds. |
| 10 | *(no frozen source)* — contact form | About / Contact | New | Functional UI specified in Step 2 (Name/Email/Subject/Message, no phone, kcorioso@gmail.com) but not yet implemented. | — | None — settled and unambiguous, just not yet built. |

---

## Verification Against the Governing Mapping

The starting mapping (Executive Premise → Home; Hiring-Manager Proof → Home; System → Home, compressed; Interactive Evidence → Evidence; AI Reasoning → Methodology & Evaluation; Blind Evaluation → Methodology & Evaluation; Lessons & Limitations → Portability & Lessons; Deeper Resources & Contact → About/Contact) was checked directly against Section 5 of the live Step 2 document and matches exactly, word for word. No conflicts found between the frozen site copy and the frozen architecture.

## Repetition Analysis

- **Legitimate repetition for orientation:** MISS/MISS/CLEAN appearing on both Home (headline form) and Methodology & Evaluation (full technical form) — required by Workstream A's own rule that Home state the result completely on its own.
- **Compressed summary, correctly scoped:** the $251K figure appearing narratively on Home and numerically on Evidence — different depth, different job, not duplication.
- **Unnecessary duplication — identified and resolved during Home drafting:** the Golden Thread chain, originally at risk of being stated in full twice within Home itself (once in Executive Premise, once again in the compressed System block). Resolved: stated once, referenced by name thereafter.

## Confirmed Content Gap

About/Contact's "concise Ken" professional bridge does not exist anywhere in Workstream D. Recorded per Ken's decision as: **NEW COPY REQUIRED — source only from verified career facts; draft during remaining-page population.** This gap is bounded and does not block Home-page progression.

---

**End of Harbor Ridge V1 — Workstream F, Step 3: Content Allocation Matrix (APPROVED)**
