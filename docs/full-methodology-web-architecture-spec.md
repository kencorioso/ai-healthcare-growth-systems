# Full Methodology — Web Architecture & Implementation Specification

**Status:** Approved governing specification. Ready for Claude Code implementation. Not yet implemented.
**Governs:** The `/full-methodology` page only. Does not reopen Home, Evidence, Evidence Trail, Methodology & Evaluation, Portability & Lessons, About, or Contact.

---

## 1. Purpose and Governing Objective

**The methodology is already finished. The implementation task is to make it inspectable.**

`docs/harbor-ridge-v1-methodology.md` is a frozen, complete, authoritative 19-section technical account of how Harbor Ridge V1 was designed, built, validated, tested, and evaluated. This specification governs the *publication* of that already-finished document as a real web page — not its rewriting, reinterpretation, condensation, or improvement.

Methodology & Evaluation (the existing frozen page) already tells the executive-level story. Full Methodology has a different, deeper job: let a technically sophisticated reader — an analytics leader, an AI leader, a healthcare technology executive, or any reviewer evaluating whether Ken actually understands experimental design and AI evaluation — inspect the actual rigor behind the project, including the validation failures caught, the judgment calls made under real pressure, and the exact precommitment mechanics that make the governing MISS/MISS/CLEAN result real rather than asserted.

The page must demonstrate rigor through the work itself, not by repeatedly claiming the work is rigorous.

---

## 2. Sources of Truth

- **`docs/harbor-ridge-v1-methodology.md`** — the frozen, authoritative 19-section methodology. This is the sole content source for the page's substantive prose. Do not summarize, condense, reinterpret, or paraphrase its analytical claims — reproduce them faithfully, reorganized only at the presentation/navigation layer described below.
- **`src/pages/full-methodology.astro`** — the existing reserved placeholder route (committed, currently a minimal stub). This file is replaced by the real implementation.
- **`src/pages/methodology-evaluation.astro`** and **`src/pages/portability-lessons.astro`** — each contains a Go Deeper reference to Full Methodology that must be updated only after this page is built and verified (see Section 15).
- **`src/pages/evidence.astro`** — the source of the exact, already-live, already-corrected Result Taxonomy wording to be reused here for consistency (see Section 11).
- **`src/pages/evidence-trail.astro`** — the destination for the full forensic $251K arithmetic; this page must link to it, not duplicate its claim-level table.
- **Brand & Voice v2.0** and the existing site component patterns (process chain, `dl.reckoning`, editorial grid, index-list, chip/finding treatment) — the material and visual system this page must remain unmistakably part of.

---

## 3. Frozen Analytical/Content Constraints

The following governs every sentence on this page and may not be altered, softened, strengthened, or reinterpreted:

- Governing result: **Scenario 1: MISS. Scenario 2: MISS. Healthy Baseline: CLEAN.**
- The ~$251K result (exact figure: **$250,397.60**) is an **Observed Finding**, never a Benchmark Result.
- Healthy Baseline CLEAN is a **Control Result**; it does not establish general reliability.
- Benchmark misses do not erase the Observed Finding's usefulness.
- The two misses were **affirmative mis-detections** — the system found and prioritized other patterns, not simple non-detection. This is called **crossed localization** in the frozen text and must not be simplified into "the AI found nothing."
- The closing diagnostic (signal-to-noise structure, driven by the ~3–8 admissions/month figure) is explicitly **"directional... not decisive"** and must never be presented as a settled explanation.
- V0.3 is **deferred by priority**, never framed as incapability or abandonment.
- Harbor Ridge itself is **not portable**; the demonstrated build-and-evaluate *process* is what transfers, through reconstruction.
- Do not add V0.3, invent new methodology, change Ground Truth, introduce new experiments, or alter evaluation criteria.
- Do not remove limitations because they are inconvenient. Do not convert directional findings into proven explanations.

---

## 4. Final Page Architecture — Section/Source/Purpose/Background/Presentation Map

| Section | Source Material | Purpose | Background | Presentation Treatment |
|---|---|---|---|---|
| 1. Hero | New presentation copy (Section 6 below) | Frame the document; state synthetic-environment status plainly | LIGHT | Single-tone Sovereign Navy H1, standard Hero pattern, no video |
| 2. Table of Contents | New (navigational only) | Let a reader jump directly to a section | LIGHT | Compact anchor-link list, 7 items, non-sticky |
| 3. The Problem and the Architecture | §1–2, verbatim | Establish the executive problem and the organizational architecture built before any analysis | LIGHT | Prose + reuse of the existing process-chain component for the six-stage Golden Thread (acquisition → inquiry → financial qualification → admission → treatment → revenue) |
| 4. Building and Validating the Environment | §3–5, verbatim | Show the synthetic data build, the two caught real defects, and the seed-search near-miss | NAVY | Prose with two restrained callouts: (a) the two caught data/scenario defects, (b) the seed-search near-miss (see Section 12 guardrail) |
| 5. Freezing Ground Truth | §6, verbatim | State the precommitment boundary the evaluation's credibility rests on | LIGHT | Prose only; one small callout for the Freeze Rule sentence |
| 6. The First Blind Evaluation — V0.1 | §7–9, verbatim | Explain V0.1, its mixed results, and the emergence of the $251K Observed Finding | LIGHT, separated from Section 5 by a Steel Gray Surface divider/rule (see Section 7) | Prose + compact summary table (see Section 13) + Result Taxonomy restatement (see Section 11) + link to Evidence Trail |
| 7. The Governing Evaluation — V0.2 | §10–12, verbatim | Explain the redesigned, precommitted V0.2 evaluation and its governing result | NAVY | Prose + reuse of the exact `dl.reckoning` MISS/MISS/CLEAN component already live on Home and Methodology & Evaluation |
| 8. Investigating the Result | §13–14, verbatim | Explain the post-hoc diagnostic and the V0.3 deferral | LIGHT | Prose, with one restrained callout for the 25–38-opportunities-vs-3–8-admissions/month statistical point. No crossed-localization visualization in this pass (see Section 17). |
| 9. What This Demonstrates, and What Remains Open | §15–19, verbatim | Synthesize the evidence categories, state capability boundaries, portability, and the closing methodological principle | NAVY | Prose; §17's nine-item decision list as a simple styled list, not a process chain (these are a narrative recap, not sequential stages) |
| 10. Go Deeper / Back to Top | New | Contextual exit points; return-to-top affordance | LIGHT | Existing indexed Go Deeper list pattern + simple "Back to Top" link |

**On adjacent LIGHT sections (Sections 5 and 6 above):** this is intentional and approved. Do not insert an arbitrary NAVY section merely to maintain strict alternation. Instead, create clear editorial separation between them using: a visible section divider/rule, a Steel Gray Surface background band (not full Sovereign Navy) if a subtle tonal shift is desired, generous vertical spacing, and consistent heading hierarchy (each section gets its own numbered, anchored `<h2>`). The reader should never be in doubt about where one section ends and the next begins, even without a color change.

---

## 5. Table of Contents / Navigation Specification

Place a compact table of contents immediately after the Hero, before Section 3. It links to exactly these 7 items (matching the 7 content sections in Section 4, not all 19 original subsections):

1. The Problem and the Architecture
2. Building and Validating the Environment
3. Freezing Ground Truth
4. The First Blind Evaluation — V0.1
5. The Governing Evaluation — V0.2
6. Investigating the Result
7. What This Demonstrates, and What Remains Open

**Non-sticky.** Do not implement sticky or semi-sticky desktop navigation — this would introduce a UI pattern not used anywhere else on the site. A simple in-page anchor list is sufficient for a reader who wants to jump to a specific section; a reader reading sequentially simply scrolls past it.

Add a simple **"Back to Top"** link/affordance after the final content section (Section 10), before Go Deeper.

Each of the 7 section headings must carry a stable, unique `id` attribute matching its Table of Contents anchor, so the sections are directly linkable from outside the page (e.g., from Methodology & Evaluation's Go Deeper entry, if desired later).

---

## 6. Hero Specification

**Single-tone Sovereign Navy H1. No two-tone treatment.** The two-tone convention exists to dramatize a rhetorical turn; this is a factual document header with no turn to dramatize.

**Approved H1 (exact, new presentation copy):**

> How Harbor Ridge V1 Was Built, Tested, and Evaluated.

**Approved supporting copy (exact, new presentation copy):**

> The complete technical account behind Methodology & Evaluation — including validation failures, judgment calls, and the exact precommitment discipline that makes the governing result real. Harbor Ridge is a synthetic evaluation environment, not a real healthcare organization or production deployment.

No video in the Hero. No CTA cluster. Standard Hero layout pattern already established site-wide (eyebrow label, H1, lead paragraph).

---

## 7. Content-to-Presentation Mapping

**Reuse verbatim, no new component:**
- Golden Thread six-stage process chain (Section 3) — identical grammar to Home/Methodology & Evaluation/Portability & Lessons.
- `dl.reckoning` MISS/MISS/CLEAN component (Section 7) — identical grammar to Home and Methodology & Evaluation. Equal visual weight across all three results. No color-coding.
- Editorial label-rail-plus-body grid — used for every section's heading/body relationship, matching every other depth page.
- Indexed Go Deeper list pattern (Section 10).

**New, minimal components (see Section 9):**
- A compact anchor-linked Table of Contents block (Section 2).
- A restrained inline callout/pull-quote treatment, used sparingly at exactly four points: the two caught defects (Section 4), the seed-search near-miss (Section 4), the Freeze Rule sentence (Section 5), and the 25–38-vs-3–8 statistical point (Section 8).
- A compact summary table for the $251K arithmetic (Section 6) — see Section 13.

**Deliberately plain prose, no visualization:**
- Section 5 (Freezing Ground Truth) — conceptual, not structural; a forced graphic would add noise.
- Section 9 (synthesis/portability/closing) — reflective content; the existing prose already carries the argument clearly.
- The V0.2 procedure's step sequence within Section 7 — do not rebuild this as a second copy of Methodology & Evaluation's existing process chain for the same six steps. Reference it in prose and/or link back to Methodology & Evaluation's own rendering of it, to avoid two independently-maintained copies of the same visual fact silently drifting apart over time.

---

## 8. Existing Components/Patterns to Reuse

Process-chain component · `dl.reckoning` equal-weight result component · editorial label-rail-plus-body grid · indexed Go Deeper list pattern · the established "Observed Finding" chip/label treatment · existing focus-state and accessibility conventions (Electric-Blue-on-navy dark-surface focus, Sovereign-Navy-on-light-surface focus) · existing responsive breakpoint conventions.

---

## 9. Minimum New Patterns/Components Required

Exactly two:

1. **Table of Contents block** — a simple, non-sticky anchor-link list. New only because no prior page has been long enough to require one.
2. **Restrained inline callout treatment** — a lighter-weight visual cousin of the existing chip/finding treatment, used only at the four specific points named in Section 7. Should read as "notice this" without becoming a competing visual centerpiece — this page's actual centerpiece remains the MISS/MISS/CLEAN section.

Do not introduce any other new component. Do not introduce a new color, font, or spacing value beyond what Brand & Voice v2.0 already defines.

---

## 10. Result-Taxonomy Treatment

Restate the three categories briefly, using the exact wording already live and already corrected on the Evidence page, for full site-wide consistency — do not compose a third, differently-worded version of the same taxonomy:

> **Observed Finding** — A real pattern the analysis surfaced — not necessarily a planted failure.
>
> **Benchmark Result** — The formal outcome of testing whether a planted, hidden problem was recovered.
>
> **Control Result** — The formal outcome of the Healthy Baseline negative-control test — whether the system stayed quiet when no planted failure was present.

This restatement must appear within Section 6 (The First Blind Evaluation — V0.1), positioned before or alongside the $251K discussion, so a reader entering Full Methodology directly can correctly interpret every subsequent reference to these terms without needing to visit Evidence first. Evidence remains the deeper treatment and should still be linked from this page's Go Deeper section.

---

## 11. $251K Observed Finding Treatment

Keep this **compact and methodological** — this is not a re-creation of Evidence Trail. Show enough arithmetic to substantiate the finding and preserve its classification, then link out for the rest.

**Required, exact figures (frozen, verified):**

| | Billed | Collected | Realization Rate |
|---|---|---|---|
| INN claims | $1,216,954.73 | $812,530.95 | 66.77% |
| OON claims | $688,137.27 | $209,054.85 | 30.38% |

**Counterfactual:** Expected OON collections at the INN rate = **$459,452.45**. Actual OON collected = $209,054.85. **Estimated gap = $250,397.60** (the frozen "~$251,000" figure).

This should render as a compact summary table (not the full 160-row claim-level records) — reuse table styling consistent with the site's existing conventions, with the same bounded-scroll-container discipline used on Evidence Trail if the table risks overflow at narrow widths.

**Required link:** immediately following this compact table, link explicitly to **Evidence Trail** for "the complete forensic chain and underlying claim-level records" — do not duplicate that content here.

---

## 12. Seed-Search Historical Guardrail

**This is a hard factual constraint, not a stylistic preference.**

The frozen record states precisely: *"A command was prepared that would have searched across seeds for a different result. I stopped it before it ran... So the command was not executed. I went back and corrected the validation rule instead."*

**The implementation must never state or imply that seed-searching actually occurred.** Acceptable framing: a seed-search command was *prepared*, *queued*, or *contemplated*, and was *stopped before execution*. Unacceptable framing, under any phrasing: that seed-searching "was performed," "was done," "was used," or any construction implying the process actually ran. This applies to the callout in Section 4 specifically, and to any other place on the page that references this episode.

---

## 13. Analytical Claim Guardrails (Full List)

In addition to Sections 3 and 12 above, explicitly protect: the exact MISS/MISS/CLEAN wording and the "affirmative mis-detections... crossed localization" distinction (must not be simplified to "the AI found nothing"); the "directional... not decisive" qualifier on the closing diagnostic, which must appear every time that diagnostic is referenced; the V0.3 deferral framed as "a project-priority decision," never as incapability; the portability boundary stated plainly ("I would not claim that Harbor Ridge itself is portable... It isn't"); the distinction that the honest handling of V0.2 demonstrates the integrity of the *process*, not the reliability of the *system* (§12 of the frozen text makes this distinction explicitly — do not collapse it).

---

## 14. Responsive/Accessibility Requirements

Test at 375px, 768px, 958px, 1280px, 1440px, consistent with every other page's launch discipline. The $251K summary table is the highest overflow risk — apply the same bounded-scroll-container pattern already proven on Evidence Trail's claim table. The Table of Contents must remain a simple, usable stacked list at narrow widths — no complex collapsing behavior required. All anchor links must be keyboard-reachable with visible, non-color-only focus states, matching existing site conventions. Section headings must wrap naturally at all widths — no forced single-line treatment. Maintain WCAG-compliant contrast throughout, consistent with existing Brand & Voice v2.0 token usage.

---

## 15. Publication-State Dependency Sequence

**Do not act on this section until Full Methodology is fully implemented, built successfully, and browser-verified.**

Once verified, update exactly these two locations:

- `src/pages/methodology-evaluation.astro`, Go Deeper section: change *"the complete technical account — reserved, not yet published"* to *"the complete technical account."*
- `src/pages/portability-lessons.astro`, Go Deeper section: identical change.

No other file references this publication-state language. Do not make this change as part of the same commit that implements the page — verify first, then apply this as a small, separate, mechanical follow-up change.

---

## 16. Required Implementation Scope

- All 10 sections specified in Section 4, in the specified order, with the specified backgrounds.
- The Table of Contents and Back to Top affordance (Section 5).
- The exact Hero copy (Section 6).
- The Result Taxonomy restatement (Section 10), using the exact wording specified.
- The compact $251K summary table plus link to Evidence Trail (Section 11).
- The seed-search guardrail correctly applied (Section 12).
- All analytical guardrails preserved (Sections 3, 13).
- Responsive/accessibility requirements met (Section 14).

## 17. Explicit Non-Scope

Do not: rewrite, condense, reinterpret, or paraphrase any analytical claim in the frozen methodology; add V0.3 content of any kind; build the crossed-localization visualization (deferred — prose is sufficient unless later browser inspection reveals a genuine comprehension problem); duplicate Evidence Trail's full claim-level table; rebuild Methodology & Evaluation's V0.2 process-chain as a second, separately-maintained copy; introduce sticky navigation; introduce any new color, font, or spacing token; modify Home, Evidence, Evidence Trail, Methodology & Evaluation, Portability & Lessons, About, Contact, or global navigation/footer; update the two publication-state references before this page is verified; commit or push without explicit authorization.

---

## 18. Browser Verification / Acceptance Criteria

Production build succeeds. All 10 sections render in the specified order with the specified backgrounds. Table of Contents anchors correctly scroll to each of the 7 sections. Back to Top works. The Result Taxonomy definitions match Evidence's wording exactly. The $251K table shows the exact frozen figures with no calculation drift, and links correctly to Evidence Trail. The seed-search callout uses only "prepared/queued and stopped before execution" framing — never implies it occurred. MISS/MISS/CLEAN renders via the reused `dl.reckoning` component with equal visual weight, no color-coding. No horizontal overflow at 375/768/958/1280/1440px. All anchor links and interactive elements are keyboard-reachable with visible focus states. If browser automation is unavailable in the implementing session, this must be stated plainly and structural verification substituted — do not claim visual confirmation that wasn't performed.

## 19. Optional Polish That Must Not Block Workstream F

The crossed-localization two-column comparison (Section 17) — explicitly deferred, not required. Any further visual refinement beyond what is specified above should not delay treating this page as complete for Workstream F purposes once the required scope (Section 16) is met and verified.

---

**End of Full Methodology Web Architecture & Implementation Specification.**
