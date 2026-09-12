# Portability & Lessons — Implementation Brief (Final Revised)

**Status:** Final revision per Ken and ChatGPT's review. Ready for conversion into a Claude Code implementation prompt after final sign-off. Not yet authorized for implementation.

---

## 1. Page Purpose and the Cold Hiring-Manager Question

This page answers: **"What did Ken learn from the misses, and what part of this process can actually transfer beyond Harbor Ridge?"**

This page's job is interpretation and judgment, not re-presenting the benchmark result itself — that's already been given full visual weight on Home and Methodology & Evaluation.

## 2. Final Narrative Hierarchy / Section Sequence

1. **Hero / Intro**
2. **What Doesn't Transfer** (light)
3. **What Does Transfer + Video 3** (navy)
4. **The Analytical Limitations** (light)
5. **What I Learned** (navy)
6. **What This Adds Up To** (light)
7. **Go Deeper** (navy)

Seven sections, alternating cleanly, arrived at through content logic rather than forced counting — the V0.3 standalone section is removed per Decision 1, and its content folds into section 4.

## 3. Near-Final Public Copy

**Section: What Doesn't Transfer** *(revised per Decision 5 — checked against site copy §7, matches exactly with only the rhetorical sentence removed)*

> Harbor Ridge itself is not portable to another healthcare vertical. Its schema, synthetic facility, and benchmark results belong to this test environment.

**Section: What Does Transfer** *(unchanged from site copy §7, verbatim)*

> What is portable is the process I demonstrated by building it:
>
> **Source-system mapping → Data dictionary → Schema → Synthetic data → Scenario design → Frozen Ground Truth → Blind evaluation**
>
> For another organization, I would rebuild that process around its actual operating reality rather than transplant Harbor Ridge and pretend healthcare organizations are interchangeable.

**Section: The Analytical Limitations** *(revised per Decisions 1 and 4 — the benchmark-result restatement and the V0.3 point are both checked against the frozen record before inclusion)*

> The V0.2 blind evaluation missed both planted failures while the Healthy Baseline remained clean. That clean result is useful evidence about the control test — it does not establish general reliability.
>
> A later diagnostic suggested experimental signal-to-noise structure may have contributed, particularly because one affected cohort ultimately contained only roughly three to eight admissions per month. That explanation is directional, not proven.
>
> I deferred another evaluation iteration rather than repeatedly modify the experiment in pursuit of a passing result.
>
> So I would not present V1 as a production-validated, generally reliable autonomous diagnostic system.

*Verification note: every clause above traces directly to site copy §7 or the already-approved Methodology & Evaluation language (the "3–8 admissions per month" and "directional, not proven" phrasing is verbatim from the frozen record, not paraphrased). The new sentence — "I deferred another evaluation iteration rather than repeatedly modify the experiment in pursuit of a passing result" — is Ken's own supplied language, checked against the frozen record: it doesn't claim what a hypothetical V0.3 would have shown, doesn't frame deferral as incapability, and matches the existing "I have deferred V0.3 rather than use repeated experimentation to chase a passing result" sentence from site copy §7 closely enough that it can be read as a restatement, not a new claim.*

**Section: What I Learned** *(new section, per Decision 2 — each lesson checked individually against the frozen record before inclusion)*

> **Useful discovery and successful diagnosis are not the same claim.** The Evidence Engine surfaced a genuine OON collections-realization disparity. It did not reliably recover the planted root causes. I built the evaluation to keep those two facts separate rather than let one stand in for the other.
>
> **A clean control result is real evidence, but it isn't proof of reliability.** The Healthy Baseline stayed clean when nothing was wrong. That's useful — it means the system didn't invent a problem where none existed. It doesn't mean the system would stay right under different conditions.
>
> **When an evaluation produces a result I didn't want, the discipline is to preserve it before investigating why.** I froze Ground Truth and the evaluation protocol before running the blind sessions specifically so I couldn't redefine failure after seeing the outcome. When the misses came in, the diagnostic came after the freeze, not instead of it.
>
> **Portability comes from rebuilding around another organization's reality, not transplanting a testbed.** Harbor Ridge's schema and scenarios are specific to this synthetic environment. What transfers is the discipline of mapping a real organization's own systems before asking an AI to reason about them.

*Verification note: all four lessons trace directly to language already present in the frozen record (site copy §5's "useful discovery and successful diagnosis are not the same claim," §6's freeze-before-scoring discipline, §7's portability argument). A fifth candidate lesson — "investigation after a benchmark miss can generate useful hypotheses without retroactively changing the benchmark result" — is functionally covered by the third lesson above and by The Analytical Limitations section's own content; including it separately risked redundancy rather than adding new grounded content, so it's folded in rather than stated twice.*

**Section: What This Adds Up To** *(unchanged from site copy §7, verbatim)*

> What I can demonstrate is the complete build-and-evaluate process — including what I did when validation exposed defects, when AI surfaced something I hadn't planted, and when the final benchmark failed.

## 4. Allowed Claims and Required Qualifications

**Allowed:** stating plainly that Harbor Ridge itself doesn't transfer; describing the seven-step process as portable *with reconstruction*; the four "What I Learned" lessons as stated above.

**Required qualification, every time the diagnostic or Healthy Baseline is mentioned:** "does not establish general reliability" / "directional, not proven" must appear in the same unit as the claim, never standing alone.

**Forbidden:** recreating the large-scale MISS/MISS/CLEAN visual object; any V0.3 technical proposal or roadmap; any implication Harbor Ridge transplants without reconstruction; calling the misses partial successes.

## 5. Final Treatment of the Closing Diagnostic

Stated once, inside "The Analytical Limitations," in prose only — no dedicated visual object, no navy "reveal" treatment. The "3–8 admissions per month" detail is included as supporting context for *why* the diagnostic leans the way it does, immediately followed by "directional, not proven" in the same paragraph. This section remains the most visually restrained on the page.

## 6. Final Presentation of the Seven-Step Portable Process

The process-chain component already established and approved on Methodology & Evaluation (bounded container, connected rail, ordered nodes), reused without modification to the visual grammar. No result-tag styling on the final node — unlike Methodology & Evaluation's chain, this one doesn't end in a MISS/MISS/CLEAN-style outcome, so the "filled navy tag on the last node" treatment doesn't apply here and shouldn't be forced.

## 7. Visual Treatment Per Section

- **Hero/Intro:** light, standard Hero pattern (H1 + lead), no video here per Decision 3.
- **What Doesn't Transfer:** light, editorial, brief — a claim, not an object.
- **What Does Transfer + Video 3:** **navy**, the page's strongest visual section. The seven-step process chain and Video 3's placeholder are composed together as one intentional unit — process chain and video placeholder sitting adjacent within the same section, not the process chain alone followed by an isolated video block.
- **The Analytical Limitations:** light, quiet, restrained — no object treatment.
- **What I Learned:** navy, but explicitly *not* styled like a benchmark-result reckoning — four lessons presented with real typographic weight and hierarchy (this is a consequential section) but without the oversized MISS/MISS/CLEAN-style numerals; treating each lesson as its own labeled block within the section gives it structure without borrowing the reckoning component's specific visual signature.
- **What This Adds Up To:** light, calm, the page's human closing beat.
- **Go Deeper:** navy, indexed-list family — see Section 10 for exact destination status.

## 8. Final Video 3 Placement and Role

Video 3 ("Different Healthcare Vertical / Portability") sits adjacent to "What Does Transfer," composed as one section with the process chain — not in the Hero, not as an isolated standalone block. Placeholder treatment only; no playable controls, no implication finished media exists. Production remains deferred to Workstream G.

## 9. Content Deliberately Excluded From This Page

- The large-scale MISS/MISS/CLEAN visual object — referenced in prose only.
- Any standalone V0.3 section — folded into The Analytical Limitations as one sentence.
- The $251K arithmetic or any Evidence Trail material.
- Any V0.3 technical proposal, roadmap, or speculation about hypothetical results.
- The seed-search near-miss story (Home's specific beat).

## 10. Go Deeper Destinations — Current Publication/Link Status

Per the Content Allocation Matrix's frozen mapping, Case Study, Methodology, GitHub, and Whitepaper links were architecturally assigned to **About/Contact** (Section 8, "Deeper Resources & Contact") — not as standalone routes scattered across other pages. About/Contact has not been built yet this session. This means, as of this brief:

| Destination | Status | Link behavior for this page |
|---|---|---|
| **Full Methodology** | **Reserved destination** — route exists at `/full-methodology` (child of Methodology & Evaluation), content not yet published | Active link to `/full-methodology`, which itself honestly states it's not yet published (same pattern as Methodology & Evaluation's own Go Deeper entry) |
| **GitHub** | **Active destination** — a real, live, external URL right now (`github.com/kencorioso/ai-healthcare-growth-systems`) | Active external link, safe to include now |
| **Case Study** | **Future destination** — no route exists anywhere yet; belongs to About/Contact once built | Do not link; omit from this page's Go Deeper list entirely, or list as non-linked text explicitly marked "coming soon" |
| **Whitepaper** | **Future destination** — the asset itself doesn't exist yet (Workstream G scope) | Same treatment as Case Study — omit or non-linked placeholder text |

**Recommendation:** Go Deeper on this page lists exactly two items for now — **Full Methodology** (reserved, honestly labeled) and **GitHub** (active) — rather than including four items where two would be dead or placeholder text with no real destination at all.

## 11. Responsive Considerations

Standard: 375/768/958/1024/1440px. The seven-step process chain reuses Methodology & Evaluation's exact responsive fallback (vertical connected-rail list below 900px) — direct component reuse, not a new pattern.

## 12. Accessibility Considerations

Same established conventions: Electric-Blue-on-navy focus states on dark sections; Video 3's placeholder needs an honest `aria-label`; the process chain needs the same `role`/`aria-label` pattern already used on Methodology & Evaluation.

## 13. Claude Code Implementation Guardrails

Do not invent copy beyond what's specified here; do not create a standalone V0.3 section; do not recreate the large MISS/MISS/CLEAN visual object; do not link Case Study or Whitepaper to any URL — they have no real destination yet; every mention of the diagnostic or Healthy Baseline must include its qualifier in the same unit; do not produce or embed actual video; do not reopen Home, Evidence, Evidence Trail, or Methodology & Evaluation; reuse the existing process-chain component exactly rather than modifying its visual grammar.

## 14. Human Browser-Review Acceptance Criteria

"What Does Transfer + Video 3" reads as the page's visual centerpiece; "What I Learned" feels consequential without resembling a benchmark-result reckoning; "The Analytical Limitations" stays visually quiet; Go Deeper contains only real, honest destinations (no dead links); light/navy alternation holds; no horizontal overflow at any tested width including 958px.

## 15. Remaining Open Items

1. **"What I Learned"'s four lessons and the new V0.3 sentence are both new copy compositions** (grounded in frozen language but not direct verbatim lifts) — flagged for final sign-off, consistent with how Methodology & Evaluation's non-verbatim sections were handled.
2. **The Go Deeper two-item recommendation (Section 10) is a real scope decision**, not just an implementation detail — presenting a shorter Go Deeper list now rather than placeholder-labeling all four destinations the way Full Methodology was originally handled.

---

**End of Portability & Lessons Implementation Brief (Final Revised)**
