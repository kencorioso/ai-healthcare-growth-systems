# Harbor Ridge V1 — Workstream F, Step 1: Design System Implementation Spec

**Status:** Revised draft (v2), corrections applied per independent review — ready for freeze and handoff to Claude Code
**Purpose:** Translate the frozen Brand & Voice Guidelines into the smallest stable token layer Astro needs — not a design system exercise, not more tokens than the guidelines actually specify.

---

## 1. Scope Discipline

This spec implements exactly what `brand-voice-guidelines-v1.0.md` defines: the color palette (§1), typography (§2), wordmark rules (§3), and spacing/accessibility principles (§4). It does not invent additional colors, additional type scales, additional spacing values, or component-level design decisions not present in the frozen source. Anything needed later that isn't here is a sign the guidelines need a versioned update (v1.1), not that this implementation should quietly extend past them.

---

## 2. Color Tokens

Implemented as CSS custom properties, exact hex values from §1, no interpretation:

```css
:root {
  /* Cream family */
  --color-cream-canvas: #F6F1E7;   /* primary page background */
  --color-cream-surface: #FCFAF5;  /* card/panel surface */
  --color-cream-muted: #EDE6D6;    /* subtle section backgrounds, table stripes */

  /* Ink family */
  --color-ink-primary: #171614;    /* primary text, structural elements, headings */
  --color-ink-secondary: #4A473F;  /* secondary text, captions, metadata */
  --color-ink-border: #D9D2C0;     /* dividers, borders, input outlines */

  /* Crimson family — single accent, used sparingly per §1's 60/30/10 ratio guidance */
  --color-crimson-accent: #A81C1C; /* CTAs, key numbers, highlighted data points */
  --color-crimson-deep: #7A1414;   /* hover/pressed states, small-size accent text */
  --color-crimson-tint: #F3DEDE;   /* light accent background, e.g. callout box */
}
```

**Implementation guardrail, not an enforced rule:** a CSS custom property declared in `:root` is always directly accessible — nothing at the CSS layer can technically prohibit `background: var(--color-crimson-accent)` from being written. What Step 1 actually provides is a guardrail that reduces accidental misuse: normal site components should consume crimson through the specific semantic treatments named in §5 below (a CTA treatment, a highlighted-statistic treatment), not through the raw token directly. This is a convention supported by structure, not a technical guarantee.

**Contrast values are already verified in the frozen source** (ink-primary/cream-canvas ≈16:1; crimson-accent/cream-canvas ≈6.5:1) — no re-verification needed here, just correct token usage.

---

## 3. Typography Tokens

```css
:root {
  --font-heading: 'Archivo', 'Helvetica Neue', Arial, sans-serif;
  --font-body: 'Source Serif 4', Georgia, 'Times New Roman', serif;

  /* Type scale, rem, 16px base — exact values from §2 */
  --text-small: 0.875rem;
  --text-body: 1rem;
  --text-lead: 1.25rem;
  --text-h3: 1.5rem;
  --text-h2: 2rem;
  --text-h1: 2.75rem;
  --text-hero: 3.5rem; /* use sparingly, per source */
}
```

Both fonts loaded via Google Fonts (free, open-license, per §2 — no licensing decision needed). Archivo weights 700/600 for headings/subheads; Source Serif 4 weights 400/600 for body/emphasis. Tabular figures enabled on Archivo wherever numbers appear in a table or the evidence-trail page (`font-variant-numeric: tabular-nums`), per §2's explicit instruction.

---

## 4. Wordmark Implementation

Two named treatments built as components at Step 1; the third implemented directly, not abstracted, per review:

- **`<Wordmark name="HEOS" />`** — Archivo 700, all-caps, letter-spacing 0.06–0.08em, `--color-ink-primary` by default. A separate `isolated` prop permits `--color-crimson-accent` only when used as a standalone corner mark — never inline with body copy. Built as a component now because its naming and styling guardrails have repeatedly mattered throughout this project.
- **`<Wordmark name="HEOS Evidence Engine" />`** — "HEOS" in the treatment above; "Evidence Engine" in Archivo 500–600, sentence case, same color. Always `--color-ink-primary` — crimson is explicitly prohibited on this compound name per §3. Same reasoning as above for building this as a component now.
- **Ken Corioso wordmark** — implemented directly (not as a polymorphic component) using whichever single typeface the Harbor Ridge site shell actually calls for. §3 authorizes either Archivo (byline/credential context) or Source Serif 4 (inline prose context) depending on where it appears, and that rule remains documented for future reference — but Step 1 does not build a `context`-prop abstraction to select between them until a second real usage on the site actually requires it. Always mixed case, `--color-ink-primary`, no crimson, no tracking beyond standard scale.

---

## 5. Spacing, Accessibility & Approved Semantic Treatments

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 32px;
  --space-6: 48px;
  --space-7: 64px;
  --space-8: 96px;

  --line-height-body: 1.5;
  --line-height-heading: 1.25; /* implementation choice: midpoint of frozen 1.2–1.3 range */
}
```

Body measure constrained to 60–80 characters per line via a `max-width` on long-form text containers (case study, methodology excerpts), not left to the browser default. Minimum tap target 44×44px enforced on all interactive elements. Every interactive element gets a visible, non-color-only focus state (a border/outline change, not just a color shift), per §4's explicit accessibility requirement. All meaningful images require alt text; decorative images get empty alt attributes.

**Approved semantic treatments for Step 1 — concrete, not a general utility-class system:** only these four are built now, each solving a specific need already present in the first implementation. Nothing broader (no `.bg-muted`, `.text-accent`, `.space-6` general-purpose utilities) is created unless Step 2 or Step 3 demonstrates an actual need. CSS variables themselves are sufficient reusable infrastructure beyond these four:

- CTA treatment (crimson-accent, per the guardrail in §2)
- Highlighted-statistic treatment (crimson-accent, per the guardrail in §2)
- Focus-state treatment (visible border/outline, non-color-only, per §4)
- Wordmark components (§4 above)

---

## 6. What This Step Does NOT Include

- Component-level layout decisions (that's Step 2, site information architecture)
- Page-specific content or copy placement (Step 3)
- Any color, font, or spacing value not present in the frozen guidelines
- A general-purpose utility-class or component library beyond the four semantic treatments and two wordmark components named above
- A polymorphic Ken Corioso wordmark component (deferred until a second real usage context exists)

---

## 7. Acceptance Check Before Step 1 Is Considered Complete

- [ ] Every token value matches the frozen source exactly — verified against the live `docs/brand-voice-guidelines-v1.0.md`, not memory or a prior summary.
- [ ] No additional colors, fonts, or spacing values introduced beyond what §1–§4 specify.
- [ ] No general-purpose utility classes exist beyond the four named semantic treatments in §5.
- [ ] Every implementation choice that resolves a range or ambiguity in the frozen guidelines is explicitly labeled as an implementation choice, not represented as a frozen source value (the heading line-height is the known example; if another ambiguity surfaces, label it the same way).
- [ ] A minimal Astro test page — a token proof sheet, not a designed page and not Step 2 — renders heading, body copy, CTA, highlighted statistic, wordmark, focus state, and long-form text measure correctly at desktop and mobile widths.

---

**End of Harbor Ridge V1 — Workstream F, Step 1: Design System Implementation Spec (v2, revised)**
