# Brand & Voice Guidelines — v1.0

**Status:** FROZEN — v1.0
**Scope:** Cross-project shared infrastructure — HEOS / Harbor Ridge, CompliantVoice, Ken Corioso personal portfolio
**Phase:** Phase 1 (working reference document). No Phase 2 showcase/portfolio work is included here.
**Constraint carried forward:** No named trademarked commercial products, brands, or designers anywhere in this document. All style references are generic (e.g. "instrument-face clarity," "geometric sans") and are not tied to any specific named product, brand, or designer.

---

## 1. Color Palette

Base direction: cream / black / crimson, inspired generically by high-contrast, high-legibility instrument-face design — not any specific named product or manufacturer. Expanded here into a usable working palette with the variants a real interface needs.

| Token | Hex | Role |
|---|---|---|
| `cream-canvas` | `#F6F1E7` | Primary page background |
| `cream-surface` | `#FCFAF5` | Card / panel surface, sits "above" the canvas |
| `cream-muted` | `#EDE6D6` | Subtle section backgrounds, table stripes |
| `ink-primary` | `#171614` | Primary text, structural elements, primary headings |
| `ink-secondary` | `#4A473F` | Secondary text, captions, metadata |
| `ink-border` | `#D9D2C0` | Dividers, borders, input outlines |
| `crimson-accent` | `#A81C1C` | The single accent — CTAs, key numbers, highlighted data points |
| `crimson-deep` | `#7A1414` | Hover/pressed states, accent text at small sizes |
| `crimson-tint` | `#F3DEDE` | Light accent background (e.g. a highlighted callout box) |

**Ratio guidance (unchanged from creative-inputs direction):** roughly 60% cream/neutral, 30% ink/structural, 10% crimson. Crimson stays reserved for the single most important thing on a page — a CTA, a headline figure, a status flag. It should never become a background color or a decorative fill.

**Contrast, checked, not assumed** (consistent with the "Empirical Architect" disposition — a claim about legibility should be verified, not asserted):

- `ink-primary` (#171614) on `cream-canvas` (#F6F1E7): **≈16:1** — far exceeds AAA (7:1) for any text size.
- `crimson-accent` (#A81C1C) on `cream-canvas` (#F6F1E7): **≈6.5:1** — passes AA (4.5:1) for normal text and is close to AAA. Safe to use for accent-colored body-sized text, not just large text/icons.
- `crimson-deep` (#7A1414) on `cream-canvas`: darker than `crimson-accent`, so its contrast ratio is higher still — use it where an accent element sits at small sizes or needs extra margin above the AA floor (e.g. small links, hover-state text).
- `ink-secondary` (#4A473F) on `cream-canvas`: comfortably passes AA for normal text; use for secondary text, not for anything that must pass AAA.

Any future palette addition (a success/warning/info color, for example) should be checked against `cream-canvas` and documented with its ratio the same way, before it's adopted — not added on visual instinct alone.

---

## 2. Typography

Direction: a geometric sans for numbers/headings (precise, instrument-like), paired with a warmer serif or humanist sans for body text (so long-form reading doesn't feel cold). Both fonts below are free, open-license (SIL Open Font License) Google Fonts — no paid licensing required in any of the three projects.

**Heading / display / numerals: Archivo**
- A geometric grotesque sans with a clean, instrument-face character. Use weights 700 (headings) and 600 (subheads, labels, UI chrome).
- Enable tabular figures where the layout supports it (e.g. the dashboard, any evidence tables) — numbers should line up like instrument readouts, not shift width as digits change.
- Use for: page titles, section headings, callout numbers, nav labels, buttons.

**Body / long-form: Source Serif 4**
- A warmer, humanist serif that keeps long-form reading (case study prose, whitepaper, script transcripts) from feeling mechanical. Use weight 400 for body copy, 600 for inline emphasis (avoid italics as the primary emphasis mechanism — bold reads more reliably across screen sizes).
- Use for: paragraph text, captions, long-form article/whitepaper content.

**Fallback stack (if either font fails to load):**
- Heading: `Archivo, "Helvetica Neue", Arial, sans-serif`
- Body: `"Source Serif 4", Georgia, "Times New Roman", serif`

**Type scale (rem, 16px base):** 0.875 (small/meta) · 1 (body) · 1.25 (lead paragraph) · 1.5 (H3) · 2 (H2) · 2.75 (H1) · 3.5 (hero/display, use sparingly).

---

## 3. Wordmark Treatment

No illustrated logo or icon mark exists at v1.0 — all three names below are typographic only.

**"HEOS"**
- Set in Archivo, weight 700, all caps, letter-spacing +0.06em to +0.08em (tracked out, instrument-plate feel).
- Color: `ink-primary` by default. `crimson-accent` is permitted only when HEOS appears as a standalone, isolated mark (e.g. a small corner wordmark) — never as body-copy-adjacent text.
- Never set in lowercase, never italicized, never given a drop shadow or 3D treatment.

**"HEOS Evidence Engine"**
- "HEOS" keeps the treatment above (Archivo 700, tracked caps). "Evidence Engine" follows in the same typeface at weight 500–600, sentence case (not all caps) — this visually marks Evidence Engine as the specific demonstrated product, distinct from HEOS the broader vision, without needing a separate color or size jump.
- Always `ink-primary`. Do not apply `crimson-accent` to this compound name — crimson is reserved for data/emphasis, not for product naming.

**"Ken Corioso"**
- Set in either typeface depending on context (Archivo for a byline/credential line, Source Serif 4 if it appears inline in prose), always mixed case, always `ink-primary`.
- No all-caps, no crimson, no tracking beyond the normal type scale. The name is not an accent-worthy element — it should read as understated and credible, not promotional.

**General wordmark rules:**
- Never invert any of the three names to crimson-on-black or apply a background fill behind the text as a substitute for a logo.
- Never combine more than one of the three names in a single tracked-caps treatment (e.g. don't set "KEN CORIOSO — HEOS EVIDENCE ENGINE" as one tracked unit).

---

## 4. Spacing & Accessibility Principles

Deliberately short — this is a working baseline, not a full design system.

**Spacing**
- Base unit: **8px**. Use a 4px half-step only for tight contexts (icon padding, inline badges).
- Scale: 4 · 8 · 16 · 24 · 32 · 48 · 64 · 96 (px). Pick from this scale rather than arbitrary values.
- Body line-height: 1.5. Heading line-height: 1.2–1.3.
- Body measure (line length): target 60–80 characters per line for long-form content.

**Accessibility**
- Minimum contrast: 4.5:1 for normal text, 3:1 for large text (≥24px or ≥19px bold) and for meaningful non-text UI elements (icons, input borders). See §1 for the palette's checked ratios.
- Never use `crimson-accent` alone to convey status (e.g. "red = error") without a text label or icon — color is not the only signal.
- All interactive elements need a visible focus state (a border or outline, not just a color shift, since color-only focus indicators fail for low-vision and colorblind users).
- Minimum tap/click target: 44×44px for interactive elements on touch surfaces.
- Alt text required on all meaningful images; decorative images marked as such (empty alt).

---

## 5. Voice Principles — Behavioral Rules

These are not adjectives ("confident," "honest," "precise") — they're rules extracted directly from patterns already present and repeated across the four frozen HEOS Evidence Engine video scripts. Each rule cites the script(s) it was drawn from.

**Rule 1 — State the finding, then interpret it. Never fuse the two into one editorialized sentence.**
Every script separates *what happened* from *what it means* into distinct, sequential sentences. Video 1: "Here's one Observed Finding it surfaced: an estimated $251,000 additional collections opportunity if out-of-network claims had realized at the in-network rate." is immediately followed by a separate interpretive sentence: "That was a genuine pattern in the data. But it was not a Benchmark Result..." *(Video 1)*

**Rule 2 — Name the evidence category before making the claim.**
The scripts use explicit, consistent category labels (Observed Finding / Benchmark Result / Control Result) rather than letting a reader infer the weight of a claim from tone. Video 1 explicitly flags the $251K as "not a Benchmark Result." Video 2 states the formal result directly: "Under the final V0.2 evaluation, it did not recover either deliberately hidden failure." *(Video 1, Video 2)*

**Rule 3 — State failure in short, plain, declarative sentences. No hedging, no euphemism.**
Failure is never softened into passive or vague language. Video 2: "And the Evidence Engine failed the benchmark." Video 4: "The first version didn't find them." / "The second version still didn't find the two hidden problems." These are one-line, subject-verb-object statements — no "there were some challenges" phrasing. *(Video 2, Video 4)*

**Rule 4 — Follow an admitted failure with what was learned, not with justification.**
The sentence immediately after a MISS pivots to new information, not defense. Video 4, right after stating both scenarios missed: "But something interesting had happened." — then explains the crossed-localization pattern the failure revealed. *(Video 4)*

**Rule 5 — Name the tempting shortcut and state directly that it was refused.**
Rather than simply claiming rigor, the scripts narrate the specific moment a shortcut was available and rejected. Video 1: "It would have been easy to keep adjusting the test until I got the result I wanted. I didn't." Video 4: "I had a command ready to start searching for a different version of the data that would give me the result I wanted. And then I caught what I was doing." *(Video 1, Video 4)*

**Rule 6 — Define technical terms in plain language in the same breath they're introduced, not in a separate glossary beat.**
Jargon is never left to stand alone. Video 1 introduces "the Golden Thread" and defines it in the same sentence: "traceability from acquisition to inquiry, financial qualification, admission, treatment, and ultimately revenue." *(Video 1)*

**Rule 7 — Put the scope limitation directly beside the impressive claim, not in fine print after it.**
Strong claims are immediately bounded in the adjacent sentence. Video 3 opens with the limitation before anything else: "I would not take the HEOS Evidence Engine built for Harbor Ridge, point it at your organization's data, and tell you it's portable. It isn't." Video 3 later, on the logistics example: "That's an analogy, not a claim that Harbor Ridge has been validated in logistics." *(Video 3)*

**Rule 8 — Own outcomes in first person, active voice — including failures.**
"I built," "I tested," "I caught," "I stopped the command" — the narrator is the actor in both successes and failures, never a passive construction that distances the speaker from a miss. Video 4, describing the moment of catching and correcting his own mistake: "So I stopped the command before it ran, went back, and fixed the validation rule that was actually wrong." — active, first person, and naming the fix as his own action rather than something that "got corrected." Present throughout all four scripts, most concentrated in Video 4. *(Video 1, Video 2, Video 3, Video 4)*

**Rule 9 — End on the standing value proposition, not a retraction of the honesty already given.**
Closing lines return to what the work is actually for, without walking back any admitted limitation. Video 1 closes on: "The goal is to help executives see across organizational silos, identify where performance is actually breaking down, and inspect the evidence before trusting the conclusion." Video 4 closes on: "That's the judgment I would bring to your organization." Neither closing line softens or apologizes for the MISS/MISS record stated earlier in the same script. *(Video 1, Video 4)*

---

## 6. Cross-Project Modulation

The palette, typography, wordmark rules, and all nine voice rules above are **constant** across all three projects. What flexes is narrative person and jargon density — not the underlying honesty/evidence discipline.

**Personal portfolio (Ken Corioso site)**
- Warmest register of the three. First person throughout ("I built," "I tested"). Most narrative density — process and judgment are the point, not just outcomes.
- Voice Rules 5, 8, and 9 carry the most weight here (the personal-judgment story is the portfolio's core content).

**HEOS / Harbor Ridge (technical-demonstration tone)**
- Precise, evidence-category vocabulary is mandatory here (Rule 2) — every public claim must be tagged Observed Finding / Benchmark Result / Control Result.
- System description may shift to third person ("the Evidence Engine surfaced...") while judgment/narrative beats stay first person ("I stopped the command before it ran"). This mixed register is already present in the frozen scripts and should be preserved, not smoothed into one or the other.

**CompliantVoice.com (SaaS tone)**
- The furthest shift: narrative-journey framing drops, and first person may shift to product-voice or "we" for feature/benefit statements. This is the one place first person is not mandatory.
- What does **not** change: Rule 1 (state, then interpret), Rule 3 (plain declarative language for any acknowledged limitation), Rule 6 (define jargon in plain language inline), and Rule 7 (scope limitation beside the claim). A SaaS product page can say "we" instead of "I," but it still states a capability, then its actual boundary, in adjacent sentences rather than only the capability.
- Palette and typography are unchanged — CompliantVoice should read as recognizably the same identity system in a slightly more commercial register, not a different brand.

---

## 7. Version & Provenance Governance

- This document becomes **v1.0** once frozen. The canonical source lives in the dedicated, cross-project Brand & Voice Foundation Claude Project (outside any single project's repository).
- Harbor Ridge (and any other project) holds a **governed reference copy**, explicitly labeled as a reference copy, not the canonical source — noting which version it is synced to (e.g. "Synced to Brand & Voice Guidelines v1.0").
- Any future change — however small — gets a new version number (v1.1, v1.2, ...) and a changelog entry recording: date, what changed, why, and which project(s) are affected. No silent edits to a frozen version.
- A project adopting a new version updates its local reference copy deliberately, on its own schedule — a version bump in the canonical Project does not silently propagate.

**Changelog**

| Version | Date | Change | Affected projects |
|---|---|---|---|
| v1.0 | 2026-08-30 | Initial draft: palette, typography, wordmark, spacing/accessibility, voice principles, cross-project modulation, governance, Definition of Done | Harbor Ridge (gating), CompliantVoice, personal portfolio |

---

## 8. Definition of Done

This document is done, at v1.0, when a developer working in any of the three projects (Harbor Ridge, CompliantVoice, personal portfolio) can build a page **without asking a clarifying question**, specifically because all of the following are true:

- [ ] Every color used has a documented hex value and a stated role (§1) — no "pick something cream-ish" ambiguity.
- [ ] Contrast ratios for text-on-background combinations are stated, not assumed (§1).
- [ ] Both fonts are named, freely available, with weights specified per use case (§2).
- [ ] All three names (HEOS / HEOS Evidence Engine / Ken Corioso) have an unambiguous typographic treatment, including what NOT to do (§3).
- [ ] A base spacing unit and scale exist, so spacing decisions aren't ad hoc (§4).
- [ ] Minimum contrast and interaction-target rules are stated as concrete numbers, not general principles (§4).
- [ ] Voice rules are phrased as testable behaviors ("state the finding, then interpret it") rather than adjectives a writer would have to personally interpret (§5).
- [ ] It's clear which parts of the voice are constant vs. which are allowed to flex per project, and how (§6).
- [ ] It's clear this is v1.0, where the canonical copy lives, and what happens when something needs to change (§7).

If any of the above is missing or ambiguous, this document is not yet done — flag it before freezing, not after.

---

*End of first draft. No Phase 2 showcase/portfolio work is included. No named trademarked commercial products, brands, or designers appear anywhere above — all style references are generic.*
