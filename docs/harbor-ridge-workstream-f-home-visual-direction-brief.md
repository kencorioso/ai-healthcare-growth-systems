# Harbor Ridge / HEOS Evidence Engine — Home Visual Direction Brief

**Status: APPROVED AND FROZEN FOR HOME IMPLEMENTATION**
**Governs Home only.** Does not reopen Brand & Voice v2.0, Workstream A's frozen narrative architecture, approved Home copy, or frozen analytical claims.

---

## 1. Dark/Light Entry Strategy

Evidentiary Entry, decided. Steel Gray Canvas hero. Sovereign Navy is reserved exclusively for the What Happened section — the page's one deliberate dark moment, motivated by that being the narrative's real point of reckoning. No other section uses Sovereign Navy as its primary surface.

---

## 2. Hero / Video 1 Composition — Decided

Integrated two-zone composition. Not overlapping.

**Desktop:** One composed unit, two zones, side by side. Zone one (positioning copy — headline, subhead) and Zone two (Video 1) sit adjacent within the same architectural canvas (§3), functioning visually as a single opening statement rather than two sequential sections. Neither zone overlaps or sits behind the other.

**Narrower/mobile:** Stacked, narrative first, Video 1 second. This is a direct order — text zone renders first in document order and visually first on mobile, video zone follows immediately after with no intervening section.

This is a fixed decision, not a range of options — Claude Code implements this specific two-zone, non-overlapping structure.

---

## 3. Architectural Canvas — Decided

One consistent wide outer canvas, shared across Hero, both videos, the Golden Thread object, the evidence objects, and Go Deeper. All of these align to the same common outer boundary — they are visually one architectural system, not independently-sized sections.

Prose nests inside this canvas at a controlled readable measure; prose width never defines section width. This applies to Problem, the narrative portions of the Real Test, and What This Demonstrates — each renders its paragraph text at the narrower measure while the section itself still occupies the full shared canvas width.

Exact max-width value is browser-refined during implementation — this brief fixes the alignment *system* (one shared boundary, prose nested inside it) as non-negotiable; the specific pixel/rem value is legitimate implementation mechanics, not a creative decision, and is left open deliberately.

---

## 4. What I Built — Decided

Central visual idea: a Golden Thread operating-chain object.

Six sequential stages, rendered as a connected chain, not a paragraph and not a complex systems diagram:

**Acquisition → Inquiry → Financial Qualification → Admission → Treatment → Revenue**

Purpose: communicate cross-silo visibility and the Evidence Engine's reasoning scope at a glance. This is a chain object — six labeled stages connected by a consistent visual connector (arrow or equivalent) — not a flowchart with branches, not an architecture diagram with boxes-and-lines for the schema, not an illustration.

The HEOS / HEOS Evidence Engine / Harbor Ridge naming hierarchy is integrated only where it clarifies the relationship between the vision, the engine, and the testbed — it does not need its own separate diagram or object; a brief editorial sentence adjacent to the chain object, establishing which layer built and tested the chain, is sufficient. Do not build a second object for the naming hierarchy.

---

## 5. What Happened — Decided

A complete reckoning composition on the Sovereign Navy surface, not three cards dropped onto a dark background. Required components, in this order:

1. A concise setup — one to two sentences establishing that this is the actual governing evaluation result (already-approved copy exists for this; this brief governs composition, not new text).
2. The three equal-weight MISS/MISS/CLEAN evaluation objects, positioned side by side on desktop (§6), each carrying identical visual weight — no object is larger, brighter, or more prominent than the others.
3. A brief interpretation, immediately following the three objects, that preserves the already-approved meaning of the Healthy Baseline (useful restraint demonstrated, not general reliability established) and the already-approved meaning of the two misses (real analytical discovery elsewhere, no reliable Ground-Truth recovery here).

This is one continuous compositional sequence — setup, then evidence, then interpretation — not three independent elements that happen to share a background color.

---

## 6. Responsive Transformation — Decided Per Composition

| Composition | Desktop | Mobile / Narrow |
|---|---|---|
| Hero / Video 1 | Two zones, side by side | Stack: narrative first, Video 1 second |
| Golden Thread object | Six-stage horizontal chain | Preserve sequential reading order (stacks vertically or wraps, but the six stages remain in their fixed Acquisition→Revenue sequence — never reordered, never split into an unrelated grouping) |
| MISS/MISS/CLEAN | 3-up, side by side | Stacked, equal weight preserved (no object becomes visually larger or more prominent when stacked) |
| Real Test + Video 4 | Composed narrative-plus-media unit, following the same non-overlapping adjacency principle as §2 | Stack — video and its narrative context stay adjacent to each other; Video 4 must never be separated from the paragraph(s) that introduce or follow it by an unrelated section |
| Go Deeper | All four destinations visible simultaneously | All four destinations remain visible; no hidden/tabbed mobile interaction under any circumstance |

Exact pixel breakpoints are browser-refined implementation mechanics. The transformation behavior specified in this table is fixed and not open to reinterpretation.

---

## 7. Typography Hierarchy

Two-tone headline treatment (bold lead phrase, lighter continuation) remains an available technique, applied only where a headline genuinely contains two distinct ideas worth visually separating. The Hero headline is the one pre-identified strong candidate for this treatment; any other application during implementation must be justified by the specific sentence's structure, not applied by default.

---

## 8. Claims vs. Evidence — Governing Content Principle

Claims remain editorial. Evidence becomes object-like. Editorial/prose treatment: Problem, the narrative portions of the Real Test, What This Demonstrates. Object treatment: the Golden Thread (§4), the $251K finding (§9), MISS/MISS/CLEAN (§5), and Go Deeper (§10). This is a content-type test applied per-block, not a universal container rule.

---

## 9. Evidence Presentation — The $251K Finding

A bounded object, using a chip-style "Observed Finding" label (§11). The figure itself remains in Sovereign Navy per the already-approved `.stat-highlight` treatment — unchanged in color and category claim; only the surrounding container and label styling are addressed by this brief.

---

## 10. Go Deeper — Decided

Always-visible archival index. No tabs, no hidden interaction, on any viewport size. Four entries, each with a title and a one-line description, presented as a coherent indexed list within the shared architectural canvas (§3) — not four disconnected buttons, not a tabbed reveal.

---

## 11. Metadata and Eyebrow Treatment — Decided, Scoped Narrowly

Pill/chip treatment is reserved exclusively for genuine categorical labels — the confirmed example is "OBSERVED FINDING." Standard section eyebrows and general metadata remain simple Inter typography, consistent with Brand & Voice v2.0's existing metadata specification — no pill treatment applied by default across the page. If another genuine categorical label emerges during implementation (a label that names *what kind of thing* a reader is looking at, the same way "Observed Finding" does), it may also use the chip treatment; a label that is merely a section title or heading does not qualify.

---

## 12. Dividers, Borders, Surfaces

Thin, low-weight borders with generous internal padding define object boundaries only (Golden Thread, the $251K object, MISS/MISS/CLEAN objects, Go Deeper's index). Editorial section-to-section transitions rely on spacing and the shape-change already established per block (§8), not a visible divider line.

---

## 13. Interaction and Motion Philosophy

Restrained and functional. No decorative animation or motion system is introduced. Interaction is limited to functional behaviors already required by the experience, including navigation, video controls, links, hover/focus states, and resource-index destinations. Do not introduce scroll effects, parallax, decorative reveals, animated counters, or motion whose primary purpose is visual spectacle.

---

## 14. What Remains Genuinely Open to Implementation Mechanics

Exact pixel/rem values for the shared canvas max-width, exact breakpoint values, exact spacing-scale token selections within the already-approved v2.0 spacing system, and exact connector styling for the Golden Thread chain (arrow glyph vs. line vs. another consistent marker) are the only things this brief leaves to Claude Code — all are implementation mechanics, not composition, hierarchy, content form, or interaction decisions.

---

**End of Harbor Ridge V1 — Home Visual Direction Brief (Approved and Frozen)**
