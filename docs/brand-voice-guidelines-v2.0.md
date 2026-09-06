# Brand & Voice Guidelines — v2.0

**Status:** v2.0 APPROVED — browser-dependent typography values remain PROVISIONAL PENDING BRAND PROOF SHEET VALIDATION. v2.0 supersedes v1.1 §1 (Color Palette) and §2 (Typography) in full and updates the referenced visual values in §3. All other v1.1 provisions remain inherited except where explicitly amended in this document.
**Scope:** Cross-project shared infrastructure — HEOS / Harbor Ridge, CompliantVoice, Ken Corioso personal portfolio.
**Phase:** Phase 1 (working reference document). No Phase 2 showcase/portfolio work is included here.
**Constraint carried forward:** No named trademarked commercial products, brands, or designers anywhere in this document. All style references are generic.

---

## 1. Color Palette — "Sovereign Intelligence" Foundation [v2.0]

| Token | Hex | Role |
|---|---|---|
| sovereign-navy | `#0B192C` | Primary dark surface; primary text on light surfaces |
| quantum-electric-blue | `#00D2FF` | Accent — constrained use, see below |
| steel-gray-canvas | `#F8FAFC` | Primary light canvas (page background) |
| steel-gray-surface | `#E2E8F0` | Secondary surface (card/panel background) |
| white | `#FFFFFF` | Text on dark navy surfaces |
| slate-text-secondary | `#475569` | Secondary/muted text on light surfaces |
| slate-border | `#64748B` | Dividers, borders, input outlines |
| navy-muted-on-dark | `#94A3B8` | Secondary text on the navy dark surface |
| navy-hover | `#1B324F` | Hover state for navy-fill primary CTAs |

Four tokens beyond the original palette proposal were identified and governed during review — slate-text-secondary, slate-border, navy-muted-on-dark, and navy-hover — each verified numerically below, not silently invented during implementation.

**Contrast, checked, not assumed:**

- sovereign-navy on steel-gray-canvas: 16.87:1 (exceeds AAA)
- sovereign-navy on steel-gray-surface: 14.32:1 (exceeds AAA)
- white on sovereign-navy: 17.65:1 (exceeds AAA)
- white on navy-hover: 13.00:1 (exceeds AAA — no accessibility regression on hover)
- quantum-electric-blue on sovereign-navy: 9.80:1 (exceeds AAA)
- slate-text-secondary on steel-gray-canvas: 7.24:1 (exceeds AAA)
- slate-text-secondary on steel-gray-surface: 6.15:1 (exceeds AAA)
- slate-border on steel-gray-canvas: 4.55:1 (clears the 3:1 UI-component minimum with real margin)
- navy-muted-on-dark on sovereign-navy: 6.88:1 (exceeds AAA)

**Critical constraint, verified numerically:** quantum-electric-blue **fails** as text on steel-gray-canvas (1.72:1) and **fails** as a fill with white text (1.80:1). It is reliable only (a) as an accent/text color against the sovereign-navy dark surface (9.80:1), or (b) as a fill with dark text — sovereign-navy (9.80:1) or black (11.66:1) — on top. It must never be used as text on the light canvas, and never as a fill with white text.

**Focus-state treatment:** 2px solid sovereign-navy outline on light surfaces (16.87:1 on canvas, 14.32:1 on surface — both vastly exceed the 3:1 non-text minimum); 2px solid quantum-electric-blue outline on dark navy surfaces (9.80:1). Single-ring in both cases — the margin above the 3:1 requirement is wide enough that a dual-ring treatment adds complexity without accessibility benefit.

**Primary CTA:** sovereign-navy fill, white text (17.65:1). **Hover: navy-hover fill (`#1B324F`), white text (13.00:1)** — a governed token, not an implementation-time choice.

**Explicit guardrail — no traffic-light semantics:** No color in this palette represents MISS or CLEAN as an evaluative outcome. All evaluation results render in identical, neutral styling (sovereign-navy text on steel-gray-surface, slate-border dividers) regardless of which result is stated. This preserves the discipline the evidence taxonomy depends on — a viewer must not be able to infer "good" or "bad" from color alone.

Any future palette addition must be checked against its actual adjacent surface and documented with its ratio before adoption — not added on visual instinct.

---

## 2. Typography [v2.0]

**Heading / display:** Jost, weight 600 (H1/H2), weight 500 (H3).
**Body / UI / data:** Inter, weight 400 (body), weight 600 (inline emphasis, buttons, evidence numbers — tabular figures enabled), weight 500 (navigation, metadata/eyebrows, uppercase, +0.05em letter-spacing).

**Licensing:** Both Jost and Inter are SIL Open Font License (OFL), freely available via Google Fonts, no restriction on self-hosting or redistribution in any of the three projects. Self-hosting as WOFF2 is an implementation step, not a licensing question.

**Fallback stacks:**
- Heading: `Jost, "Helvetica Neue", Arial, sans-serif`
- Body: `Inter, -apple-system, "Segoe UI", Roboto, sans-serif`

**Type scale (rem, 16px base):** 0.875 (small/meta) · 1 (body) · 1.25 (lead) · 1.5 (H3) · 2 (H2) — inherited from v1.1, provisional pending validation with Jost/Inter in the browser.

**H1 desktop size and line-height: PROVISIONAL PENDING BRAND PROOF SHEET VALIDATION.** Not fixed by this document. Must be determined by rendering the actual Home H1 text in Jost at the reference desktop width; final value is frozen only once confirmed to render in no more than three lines while retaining appropriate executive visual weight.

**H1 mobile step-down: PROVISIONAL PENDING BRAND PROOF SHEET VALIDATION.** Not assumed to inherit v1.1's breakpoint behavior; must be visually validated with the real headline text in Jost before being frozen.

**Line heights:** Body 1.5 (inherited from v1.1, provisional pending validation). Heading 1.15–1.2 (tightened from v1.1's 1.2–1.3 as a judgment call reflecting Jost's tighter geometric proportions — provisional pending Brand Proof Sheet confirmation, not a measured requirement).

**Section canvas vs. prose measure:** Sections may use a wide architectural canvas. Long-form prose maintains a controlled readable measure (60–80 characters) within that canvas, rather than forcing the entire section — including headings, CTAs, video placeholders, and evidence displays — into a narrow centered column sized for paragraph text.

**Responsive typography:** provisional pending Brand Proof Sheet validation for H1; body text otherwise inherits v1.1's fixed 1rem across breakpoints (no fluid/clamp scaling), provisional pending confirmation this still holds with Inter's metrics.

---

## 3. Wordmark Treatment [values updated, rules inherited from v1.1]

**"HEOS"** — Jost, weight 600, all caps, letter-spacing +0.06em to +0.08em. Color: sovereign-navy by default; quantum-electric-blue permitted only when HEOS appears as a standalone isolated mark against a dark navy surface (not against the light canvas, per §1's constraint) — never body-copy-adjacent. Never lowercase, never italicized, no drop shadow or 3D treatment.

**"HEOS Evidence Engine"** — "HEOS" per above; "Evidence Engine" in Jost weight 500, sentence case. Always sovereign-navy. Never quantum-electric-blue on this compound name.

**"Ken Corioso"** — Jost (byline/credential) or Inter (inline prose), mixed case, always sovereign-navy. No all-caps, no accent color, no tracking beyond the type scale.

**General rules (unchanged):** Never invert any of the three names to accent-on-dark or apply a fill behind the text as a logo substitute. Never combine more than one of the three names in a single tracked-caps treatment.

---

## 4. Spacing & Accessibility Principles [inherited with two v2.0 additions: corrected focus-state guidance and the section-canvas-vs-prose-measure principle. All pre-existing §4 provisions otherwise remain unchanged.]

Base unit: 8px. Scale: 4·8·16·24·32·48·64·96 (px). Body measure: 60–80 characters for long-form content, per the section-canvas-vs-prose-measure principle in §2 above.

**Accessibility (unchanged):** Minimum contrast 4.5:1 normal text, 3:1 large text/meaningful UI elements. Never use accent color alone to convey status — text label or icon required. Visible focus state required (border/outline, not color-only) — see §1 for the specific verified treatment. Minimum tap target 44×44px. Alt text on all meaningful images.

---

## 5. Voice Principles — Behavioral Rules [inherited from v1.1, unchanged]

These are not adjectives ("confident," "honest," "precise") — they're rules extracted directly from patterns already present and repeated across the four frozen HEOS Evidence Engine video scripts. Each rule cites the script(s) it was drawn from.

**Rule 1 — State the finding, then interpret it.** Never fuse the two into one editorialized sentence. Every script separates what happened from what it means into distinct, sequential sentences. (Video 1)

**Rule 2 — Name the evidence category before making the claim.** The scripts use explicit, consistent category labels (Observed Finding / Benchmark Result / Control Result) rather than letting a reader infer the weight of a claim from tone. (Video 1, Video 2)

**Rule 3 — State failure in short, plain, declarative sentences.** No hedging, no euphemism. Failure is never softened into passive or vague language. (Video 2, Video 4)

**Rule 4 — Follow an admitted failure with what was learned, not with justification.** The sentence immediately after a MISS pivots to new information, not defense. (Video 4)

**Rule 5 — Name the tempting shortcut and state directly that it was refused.** Rather than simply claiming rigor, the scripts narrate the specific moment a shortcut was available and rejected. (Video 1, Video 4)

**Rule 6 — Define technical terms in plain language in the same breath they're introduced,** not in a separate glossary beat. Jargon is never left to stand alone. (Video 1)

**Rule 7 — Put the scope limitation directly beside the impressive claim,** not in fine print after it. Strong claims are immediately bounded in the adjacent sentence. (Video 3)

**Rule 8 — Own outcomes in first person, active voice — including failures.** "I built," "I tested," "I caught," "I stopped the command" — the narrator is the actor in both successes and failures. (Video 1, Video 2, Video 3, Video 4)

**Rule 9 — End on the standing value proposition, not a retraction of the honesty already given.** Closing lines return to what the work is actually for, without walking back any admitted limitation. (Video 1, Video 4)

---

## 6. Cross-Project Modulation [inherited from v1.1, unchanged]

The palette, typography, wordmark rules, and all nine voice rules above are constant across all three projects. What flexes is narrative person and jargon density — not the underlying honesty/evidence discipline.

**Personal portfolio (Ken Corioso site):** Warmest register of the three. First person throughout. Voice Rules 5, 8, and 9 carry the most weight here.

**HEOS / Harbor Ridge (technical-demonstration tone):** Precise, evidence-category vocabulary is mandatory (Rule 2). System description may shift to third person while judgment/narrative beats stay first person — this mixed register is already present in the frozen scripts and should be preserved.

**CompliantVoice.com (SaaS tone):** The furthest shift: narrative-journey framing drops, first person may shift to product-voice or "we." What does not change: Rule 1, Rule 3, Rule 6, and Rule 7. Palette and typography are unchanged — CompliantVoice should read as the same identity system in a more commercial register, not a different brand.

---

## 7. Version & Provenance Governance

This document's canonical source lives in the dedicated, cross-project Brand & Voice Foundation Claude Project (outside any single project's repository). Harbor Ridge (and any other project) holds a governed reference copy, explicitly labeled as a reference copy, noting which version it is synced to. Any future change gets a new version number and a changelog entry recording date, what changed, why, and which projects are affected. No silent edits to a frozen version. A project adopting a new version updates its local reference copy deliberately, on its own schedule.

**Changelog:**

| Version | Date | Change | Affected Projects |
|---|---|---|---|
| v1.0 | 2026-08-30 | Initial draft: palette, typography, wordmark, spacing/accessibility, voice principles, cross-project modulation, governance, Definition of Done. FROZEN. | Harbor Ridge (gating), CompliantVoice, personal portfolio |
| v1.1 | 2026-09-04 | Amended §1 only: crimson-fill exception for small bounded interactive elements. FROZEN. | Harbor Ridge (originating), CompliantVoice, personal portfolio |
| v2.0 | 2026-09-05 | Superseded §1 (Color Palette) and §2 (Typography) in full: replaced cream/black/crimson with the Sovereign Intelligence foundation (sovereign-navy, quantum-electric-blue, steel-gray-canvas, steel-gray-surface) plus four newly identified and governed supporting tokens (slate-text-secondary, slate-border, navy-muted-on-dark, navy-hover); replaced Archivo/Source Serif 4 with Jost/Inter. Corrected an initial focus-state proposal that failed verification (quantum-electric-blue against light surfaces, 1.72:1) to a verified sovereign-navy/electric-blue split by surface. Added the section-canvas-vs-prose-measure principle to §4. H1 desktop/mobile sizing and line-height explicitly marked PROVISIONAL PENDING BRAND PROOF SHEET VALIDATION, not fixed by this revision. §3 wordmark values updated to v2.0 tokens; §3 rules, §4 pre-existing provisions, §5, §6 inherited unchanged. APPROVED. | Harbor Ridge (originating implementation), CompliantVoice, personal portfolio (any future visual work across all three) |

---

## 8. Definition of Done [re-verified against v2.0]

Unchanged criteria from v1.1, checked against this revision: every color has a documented hex and role including all four newly identified tokens ✓; contrast ratios stated and verified, including the one pairing that failed and was corrected ✓; both fonts named, freely licensed, weights specified ✓; wordmark treatments updated to v2.0 values ✓; base spacing unit and scale unchanged and valid ✓; accessibility minimums stated as concrete numbers ✓; voice rules untouched and still testable ✓; cross-project modulation untouched ✓; version/changelog clear ✓.

**One explicit exception to "done":** H1 sizing is knowingly and deliberately left open, marked PROVISIONAL, pending the Brand Proof Sheet. This document is not incomplete by oversight here — it is correctly incomplete by design until that specific browser validation occurs.

---

*No Phase 2 showcase/portfolio work is included. No named trademarked commercial products, brands, or designers appear anywhere above.*
