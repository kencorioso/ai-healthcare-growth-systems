# Methodology & Evaluation — Implementation Brief (Final Revised)

**Status:** Approved architecture, revised per Ken and ChatGPT's review. Ready for conversion into a Claude Code implementation prompt after final sign-off. Not yet authorized for implementation.

---

## 1. Page Purpose and the Cold Hiring-Manager Question

This page answers: **"How did Ken test whether this AI system's reasoning could actually find problems whose answers were already known?"**

Where Evidence explained the *taxonomy* (what kind of result the $251K finding is), this page explains the *method* — how the blind-test architecture was built to prevent Ken from quietly steering the AI toward the right answer, and what happened when that architecture was put to the test. The rigor is demonstrated through the actual process, not asserted through the page describing itself as rigorous.

## 2. Approved Narrative/Section Sequence

1. **Intro** — reasoning-across-silos premise
2. **Freezing the Rules** — Ground Truth frozen before analysis
3. **Designing V0.2** — Evaluation Interpretation Protocol, blind procedure design, dual genericity audits
4. **Video 2** — Technical Practitioner placement (placeholder only)
5. **The Result** — MISS/MISS/CLEAN, restated in full, Sovereign Navy, equal visual weight
6. **What It Means, and What It Doesn't** — revised per Decision 3 below
7. **Go Deeper** — link to the full methodology document; Portability & Lessons for the closing diagnostic's full reasoning

## 3. Near-Final Public Copy

**Section: Intro** *(unchanged, site copy §5)*

> The executive problem wasn't confined to marketing, admissions, finance, or operations. So I designed the analytical environment around the relationships between them. The Evidence Engine had access to a relational representation of Harbor Ridge spanning acquisition, inquiry, financial qualification, admission, treatment and revenue. I wanted the analysis to distinguish different kinds of performance problems rather than assume that declining admissions automatically meant an admissions problem.

**Section: Freezing the Rules** *(unchanged, site copy §5)*

> For the blind evaluation, I went further. I froze Ground Truth before AI analysis began. The answer key was based on the actual generated scenarios, and the rule was explicit: what counted as the correct answer could not change based on what the AI later found or missed.
>
> That created a clean separation between two questions: **did the analysis surface something useful?** and **did it recover the deliberately hidden problem it was being tested to find?** Those questions eventually produced different answers.

**Section: Designing V0.2** *(unchanged copy; per Decision 2, no schema/constraint-suite technical detail added — the sequence stays at the level a cold hiring-manager audience can follow)*

> After the first blind-analysis attempt produced mixed results, I redesigned the evaluation. For V0.2, I froze an Evaluation Interpretation Protocol defining Pass/Partial/Miss for known scenarios and Clean/Borderline/False Positive for a Healthy Baseline negative control.
>
> The discovery procedure was designed without Harbor Ridge context. I subjected it to two independent genericity audits. Both returned 10/10 PASS. Only then did I freeze the procedure and run three fresh, isolated blind sessions: Scenario 1, Scenario 2, and the Healthy Baseline. The outputs were frozen before scoring.

**Governing sequence for this section, stated plainly for both copy and visual pacing:** Ground Truth frozen → evaluation criteria frozen → blind procedure designed/audited → fresh isolated sessions → outputs frozen → scoring → MISS/MISS/CLEAN.

**Section: The Result** *(unchanged, verbatim — restated in full per Decision 1, not summarized or cross-referenced to Home)*

> **Scenario 1: MISS. Scenario 2: MISS. Healthy Baseline: CLEAN.**
>
> The misses were not cases where the system simply found nothing. In both scenarios, it found and prioritized other patterns that substantially contradicted the frozen Ground Truth. The Healthy Baseline remained clean, which is useful evidence about that control test. **It does not prove general reliability.**
>
> I designed the evaluation so the Evidence Engine could fail without letting me redefine failure afterward. Then it did.

**Section: What It Means, and What It Doesn't** *(revised per Decision 3, fidelity-checked against the frozen closing diagnostic)*

> The specific V0.2 discovery procedure was insufficient to reliably recover the previously demonstrated localized failures under the existing Harbor Ridge experimental conditions.
>
> That conclusion is intentionally narrow. The evaluation showed that this procedure did not reliably recover the planted failures under these conditions. It did not erase the useful findings the analysis surfaced elsewhere, and the Healthy Baseline's CLEAN result did not establish general reliability.
>
> A subsequent diagnostic examined why the misses may have occurred and found evidence consistent with signal-to-noise structure in the experimental environment. That analysis was informative, but not decisive. I therefore preserved the benchmark result rather than changing the evaluation after seeing it.

## 4. Allowed Claims and Required Qualifications

**Allowed:** MISS/MISS/CLEAN stated plainly; the freeze-before-analysis architecture described as a genuine methodological safeguard; the misses described as affirmative (found *something*, just not the right thing), not empty.

**Required qualification, every time reliability is discussed:** Healthy Baseline CLEAN must never appear without "does not prove general reliability" in the same breath or visual unit.

**Forbidden:** "built to fail honestly" in that specific phrasing, anywhere on this page. Any language that reads as defending or excusing the AI's performance in the sentence(s) immediately following the MISS/MISS/CLEAN statement — the closing-diagnostic discussion must read as investigation, not defense, which the revised Decision 3 wording is specifically built to achieve ("informative, but not decisive... I therefore preserved the benchmark result" — a statement about Ken's judgment, not the system's excuse).

## 5. Visual Treatment Per Section

- **Intro:** light Steel Gray Canvas, editorial label-rail + body grid — matching Evidence's established pattern, no new device.
- **Freezing the Rules:** light, editorial — a conceptual beat, not an evidence object.
- **Designing V0.2:** light, editorial; a simple sequence treatment (matching the six-step chain stated in Section 3 above) is appropriate if it reads better than prose — implementation judgment call within existing patterns, not a new visual language.
- **Video 2:** placeholder treatment matching Home's established video-object pattern — reserved space, honest placeholder styling, not the Hero's two-zone composition.
- **The Result:** **Sovereign Navy**, MISS/MISS/CLEAN rendered with genuinely equal visual weight, no color-coding — same component pattern already proven on Home, not reinvented here.
- **What It Means, and What It Doesn't:** light, quiet, editorial — the calm-after-the-dark-section beat, same emotional logic as Home's "What This Demonstrates."
- **Go Deeper:** same indexed-list family as Home's and Evidence's deeper-resource links.

## 6. Video 2 Placement and Role

Per frozen Workstream A architecture, Video 2 belongs adjacent to "Designing V0.2" and "The Result" — its actual content (methodological rigor, frozen rules, preserving unfavorable results) directly supports the surrounding copy. **Production remains fully deferred to Workstream G.** Placeholder/reserved-space treatment only this pass.

## 7. Contextual Links / Deeper Resources

- Full methodology document, for the complete technical account (including the schema/constraint-suite detail deliberately excluded from this page's main narrative per Decision 2).
- Portability & Lessons, for the closing diagnostic's full reasoning — this page states the narrow conclusion and the existence of that diagnostic; it does not reproduce the diagnostic's full argument.

## 8. Content That Should NOT Appear Here

- **The $251K arithmetic chain or any Evidence Trail material** — explicitly excluded per this revision's direction.
- **The closing diagnostic's full reasoning** (the 3-8 admissions/month statistical point, the full signal-to-noise argument) — only the restrained summary in Section 3 belongs here; the full argument stays on Portability & Lessons.
- **Any V0.3 discussion** — explicitly excluded per this revision's direction.
- Any claim about HEOS's general capability or production readiness.
- The seed-search near-miss story (Home's Real Test section's specific beat — redundant here, not reinforcing).

## 9. Responsive and Accessibility Considerations

Test at 375/768/958/1024/1440px, per the 958px lesson from Home. MISS/MISS/CLEAN's equal-weight treatment must survive mobile stacking exactly as rigorously as it did on Home. Video placeholder needs a real accessible label even while empty. Focus states on the dark section use the established Electric-Blue-on-navy convention.

## 10. Implementation Guardrails for Claude Code

Do not invent copy beyond what's specified here; do not add the schema/constraint-suite technical detail to the main narrative (Decision 2); do not reproduce the closing diagnostic's full reasoning beyond the Section 3 summary (Decision 3); do not add $251K/Evidence Trail material; do not add V0.3 discussion; do not use "built to fail honestly" in that phrasing; do not reopen Home, Evidence, or Evidence Trail; do not produce or embed actual video; MISS/MISS/CLEAN must use the exact same neutral, equal-weight component pattern already proven on Home.

## 11. Human Browser-Review Acceptance Criteria

MISS/MISS/CLEAN reads with genuinely equal visual weight and is fully restated (not summarized or merely cross-referenced to Home); the Healthy-Baseline qualification is visually inseparable from the CLEAN result; the revised closing-diagnostic paragraph reads as investigation, not defense, and does not follow immediately after MISS/MISS/CLEAN in a way that feels like an excuse; the governing conclusion sentence appears exactly as specified; Video 2's placeholder is honestly a placeholder; no horizontal overflow at any tested width including 958px.

## 12. Remaining Open Items

None outstanding from this revision — all three decisions from Ken and ChatGPT's review are incorporated, and the one wording adjustment (exact frozen term "signal-to-noise structure") is a fidelity correction, not a new open question. This brief is ready for conversion into a Claude Code implementation prompt once Ken and ChatGPT give final sign-off on this revised version.

---

**End of Methodology & Evaluation Implementation Brief (Final Revised)**
