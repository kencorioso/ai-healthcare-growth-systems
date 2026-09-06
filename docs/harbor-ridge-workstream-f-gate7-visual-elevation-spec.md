# Gate 7 — Visual Elevation Specification

**Status: APPROVED AND FROZEN FOR VISUAL ELEVATION IMPLEMENTATION**

**Scope:** Exactly three compositions — Hero + Video 1, What I Built / Golden Thread, What It Found / $251K. Everything from The Real Test through Go Deeper is frozen as-is for this pass. No copy changes. No new analytical facts. One decided composition per section — no alternatives presented.

---

## 1. Hero + Video 1

**Diagnosis:** The 4-line H1 and the "arranged in columns" feeling share one root cause — the two zones are sized and aligned as mirrored twins (same height, vertically centered against each other), which is exactly what makes a composition read as two independent panels rather than one art-directed scene. Stripe's actual hero achieves intentionality by never treating its second visual element as an equal-footing rectangle competing with the type; it commits to a decisive asymmetry with one specific alignment point tying the two together.

**Composition, decided:**

- **Asymmetric split, more decisive than the prior 58/42:** text zone occupies approximately **68% of the shared architectural canvas** at the inspected full-width desktop viewport; video zone occupies the remaining **~32%**.
- **Video media aspect ratio:** Desktop Video 1 should use a narrower, taller presentation than a standard 16:9 block if the final video asset supports that treatment without cropping important content or introducing awkward letterboxing. The 68/32 text-dominant relationship and the ≤3-line H1 requirement are non-negotiable; the exact media aspect ratio is browser- and asset-refined. Keep mobile at full-width 16:9 unless the final asset itself requires otherwise.
- **Two-tone headline treatment, applied and decided:** "Healthcare Growth Problems Rarely Live in One Department." renders in full-weight Sovereign Navy; "I Built an AI System to See Across Them." renders in Slate Text Secondary. This is not decorative — the clause break changes where the line-wrap naturally falls, directly assisting the 3-line requirement.
- **One connective device, decided (not optional):** a single thin horizontal rule spans the full shared canvas width, positioned at the register line where the subhead paragraph begins, passing behind the text zone and terminating at the video panel's top edge. This is the one alignment point that fuses the two zones into a single stage-set rather than two blocks with whitespace between them.
- **Asymmetric vertical anchoring:** the video panel's bottom edge aligns with the bottom edge of the subhead paragraph — not centered against the full text block. This asymmetry is the direct, decided translation of "not simply arranged in columns."

**Desktop behavior:** As specified above. Claude Code must verify via real measurement (not assumption) that the H1 resolves to 2 or 3 lines — never 4 — at the actual inspected viewport width, using the widened text-zone proportion and two-tone treatment together.

**Mobile transformation:** Stack, text first, video second (unchanged, frozen requirement). Video reverts to full-width 16:9 on mobile unless the final asset itself requires otherwise — the narrow portrait proportion exists specifically to solve desktop space competition, which doesn't exist once stacked. The connective horizontal rule does not need to persist on mobile; it is a desktop-composition device only.

**Remove:** The current equal-height, vertically-centered two-column treatment; the fixed 16:9 video frame at desktop width; single-tone headline rendering.

**Build:** The 68/32 asymmetric split; the video panel bottom-anchored to the subhead at a browser- and asset-refined aspect ratio; the single full-width connective rule at the subhead register line; two-tone H1; verified 2–3 line result at real content width.

---

## 2. What I Built / Golden Thread

**Diagnosis:** A single straight line with domain labels floating above naturally-uneven-width groupings (2 stages, 2 stages, 1 stage, 1 stage) cannot look balanced — the imbalance is structural, not a tuning problem. Linear's actual lesson isn't "everything must be equal width," it's that panels of different sizes read as intentional when they sit inside a disciplined outer grid with consistent borders and alignment. The uneven grouping needs a grid to sit inside, not a single line to hang from.

**Composition, decided:**

- **Four equal-width vertical panels**, one per domain — Marketing, Admissions, Clinical, Revenue Cycle — each the same width regardless of how many stages it contains. This is the direct fix for the irregular-width problem: the outer structure is equalized; the content inside each panel is not forced to be equal.
- Each panel: a thin top border (Slate Border), a domain label in Inter metadata treatment (uppercase, small, per Brand & Voice v2.0's existing metadata specification — not a chip), and beneath it, the panel's stage name(s) set at genuine Jost sub-heading scale, not small floating node labels.
- **One continuous connecting thread**, rendered as a thin horizontal rule running along the bottom edge of all four panels, unifying them left to right. Small tick marks on this thread mark each individual stage's position, preserving the traceable Acquisition→Revenue sequence even though the visible domain groupings are uneven in stage count.
- This is explicitly a **grid with a connecting rule**, not four bordered cards — the borders are structural dividers between equal-width architectural panels (Linear's device), not individual card boundaries around each domain.
- **Anti-card guardrail, explicit:** Domain boundaries are created by grid alignment and shared structural rules, not four enclosed rectangles. Do not turn the four domains into cards.

**Desktop behavior:** Four equal-width columns in a single row, thread running beneath, strict left-to-right sequence.

**Mobile transformation:** The four domain panels stack vertically in order (Marketing, Admissions, Clinical, Revenue Cycle), each showing its own stage(s). The connecting thread reorients to run vertically through the stacked panels rather than horizontally, preserving the same sequential relationship in a vertical reading order — per the frozen requirement that Acquisition→Revenue order is never broken.

**Remove:** The current single straight horizontal line, the irregular-width label groupings, the small floating dot nodes.

**Build:** The four-equal-width-panel grid; consistent thin border/rule treatment across all four (structural dividers, not enclosing card boundaries); stage names at real Jost sub-heading scale within each panel; one continuous connecting thread with tick marks traversing all four panels in sequence.

---

## 3. What It Found / $251K

**Diagnosis:** The left side (chip, numeral, explanation, two subordinate rate lines) is correctly hierarchized and should not be touched. The right side is empty because the realization-rate evidence is currently stacked *beneath* the explanation as text, rather than built as its own visual object that can occupy the counterweight position.

**Composition, decided:**

- **Two-column composition on desktop.** Left column: unchanged — OBSERVED FINDING chip, $251,000 numeral, supporting explanation sentence, all preserved exactly as currently succeeding.
- **Right column: a two-bar realization-rate comparison visualization**, built from the two already-frozen values. INN Realization (66.77%) renders as a horizontal bar at proportional length; OON Realization (30.38%) renders as a shorter horizontal bar directly beneath it, at proportionally correct length relative to the first.
- **Single-color treatment, decided deliberately:** both bars render in the same Sovereign Navy fill on a Steel Gray Surface track — differentiated only by length, never by color. This is a magnitude comparison, not an evaluative judgment like MISS/CLEAN, but using one consistent color at two different lengths keeps the treatment unambiguously free of any success/failure implication, consistent with the project's broader color discipline.
- Each bar is labeled plainly (e.g., "INN REALIZATION" / "OON REALIZATION" in Inter metadata treatment) with its exact percentage set in Jost at the bar's terminus.
- This visualization is the direct visual answer to "why $251K": the visible gap between the two bar lengths *is* the counterweight to the numeral on the left, without implying any causal analysis beyond what the two frozen percentages themselves state.

**Desktop behavior:** Left column (numeral block) and right column (bar comparison) sit side by side as two visual halves of equal presence — the numeral remains the dominant single object, the bar comparison is the evidentiary counterweight, not a competing headline.

**Mobile transformation:** Stack — the $251,000 block first (unchanged priority, per the already-frozen hierarchy), the bar comparison visualization second, both at full container width.

**Remove:** The current stacked, subordinate-text treatment of the two realization rates beneath the explanation sentence; the empty right-side void.

**Build:** The two-bar Sovereign-Navy-only proportional comparison visualization, built from the exact frozen 66.77%/30.38% values, positioned as the right-column counterweight to the $251,000 numeral.

---

**End of Gate 7 — Visual Elevation Specification (Approved and Frozen)**
