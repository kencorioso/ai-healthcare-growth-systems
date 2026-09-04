# Harbor Ridge V1 — Workstream F, Step 2: Site Information Architecture Decision Spec

**Status:** Final — adopted in full following independent third-party review (ChatGPT), supersedes the earlier single-page-scroll draft
**Purpose:** Decide the actual technical shape the eight frozen Workstream A sections take as a real, multi-page website — a hub-and-spoke model, not a single continuous scroll and not a traditional five-page site with the story split into equal-weight silos.

---

## 1. The Constraint This Decision Must Satisfy

Workstream A's own governing rule, verbatim: *"A visitor can stop at any point and already have received a complete, honest impression; nothing downstream is required to make an upstream section true. The site may reward deeper exploration, but it must never require deeper exploration to correct an impression created earlier."*

This rule is why a traditional five-page site (story evenly split across pages, visitor must click in the right order to get the full picture) was rejected. If the MISS/MISS/CLEAN result only lived on a separate Methodology page, a visitor who reads Home and stops would walk away with a more persuasive but less accurate impression than the frozen record supports — precisely the failure mode this rule exists to prevent.

---

## 2. The Adopted Model: Hub-and-Spoke, Not Equal-Weight Pages

**Home is not a landing page pointing to five equal destinations. Home is the complete, compressed hiring case on its own.** Every other page is a deliberate depth path for a visitor who wants more — not a required stop to understand the basic, honest picture.

This resolves the actual tension between two legitimate goals: a genuinely multi-page site (real design craft, real pacing control, distinct entry points for different visitor priorities) without ever letting Workstream A's honesty guarantee depend on a visitor clicking further than Home.

**Relationship to Roadmap Revision 13 and Workstream A, stated explicitly:** Revision 13 described Harbor Ridge as a frozen eight-section integrated narrative experience. This decision does not reopen or contradict that. Workstream A's narrative architecture — the eight sections, their sequence, their content — remains exactly as frozen. Step 2 determines only how that already-frozen narrative is technically presented: as a five-page hub-and-spoke website rather than a single continuous-scroll page. Section 5 below maps every one of the eight frozen sections to its destination without renumbering, resequencing, or reinterpreting any of them. This is an implementation refinement of Workstream A, not a reopening of it.

---

## 3. Page Structure

### Home
**Includes:** Executive Premise, Hiring-Manager Proof, a compressed System overview, the $251K Observed Finding (with its Observed Finding / Benchmark Result distinction preserved), the MISS/MISS/CLEAN result stated plainly, and clear routes into every other page and destination (Evidence, Methodology & Evaluation, Portability & Lessons, About/Contact, Case Study, Whitepaper, GitHub).
**Videos:** Video 1 (CEO) near Executive Premise; Video 4 (Hiring Manager) near Hiring-Manager Proof. Presented with unequal visual weight — one video primary, the other integrated further down the page — not as two identical stacked blocks.
**This is the one page that must work completely if a visitor never clicks anything else.**

### Evidence
**Includes:** Workstream B's live, already-built $251K interactive evidence trail — the full transformation chain (billed → collected → realization rate → counterfactual → estimated gap) and the underlying claim-level drilldown — plus a concise restatement of what the evidence does and does not prove.
**Video:** None. This page is deliberately quiet; the interaction itself is the point.
**This resolves the previously-flagged Workstream D Section 4 dependency** — "inspect it yourself" becomes literally true once this page exists as a first-class route, not a buried link.

### Methodology & Evaluation
**Includes:** Golden Thread, the 11-table schema, synthetic-data design, scenario design, the frozen Ground Truth, the blind-test architecture, the V0.1/V0.2 story, MISS/MISS/CLEAN in full technical detail, the closing diagnostic, and a link to the complete 533-line methodology document.
**Video:** Video 2 (Technical Practitioner).

### Portability & Lessons
**Includes:** What transfers and what doesn't, the repeatable build process, analytical limitations, why V0.3 was deferred, and how the method would be rebuilt around a different organization rather than transplanted wholesale.
**Video:** Video 3 (Different Vertical).

### About / Contact
**Includes:** A concise account of Ken, why this project connects to his healthcare/growth/AI experience, links to resume, LinkedIn, GitHub, case study, whitepaper, and methodology.
**Video:** None.
**Contact form fields:** Name, Email, Subject, Message. No phone field — deliberately excluded per Ken's decision, to avoid unnecessary friction and a lead-form feel on a hiring-focused site.
**Receiving address:** kcorioso@gmail.com.

---

## 4. Destinations That Are Not Their Own Page

- **Case Study:** its own dedicated route, reachable from Home (and referenced elsewhere as appropriate) — a complete, standalone document per its own frozen structure, not folded into any of the five pages above.
- **Whitepaper:** a direct file download, no interstitial page, no lead-capture step, per the already-frozen Portfolio Delivery policy (Roadmap Revision 12). Surfaced from Home, Methodology & Evaluation, and About/Contact — not confined to one location.
- **GitHub repository:** an external link, opens in a new tab. Never replaces the current tab a visitor is reading in.

**"How It Works" as a page name is dropped entirely** — it was ambiguous about what it actually contained. "Evidence" and "Methodology & Evaluation" each tell a visitor exactly what's there before they click.

---

## 5. Mapping Back to Workstream A's Frozen Eight Sections

This model translates the frozen narrative spine into a multi-page architecture; it does not renumber, resequence, or reinterpret it:

| Workstream A Section | Lives On |
|---|---|
| 1. Executive Premise | Home |
| 2. Hiring-Manager Proof | Home |
| 3. System (compressed) | Home |
| 4. Interactive Evidence | Evidence |
| 5. AI Reasoning | Methodology & Evaluation |
| 6. Blind Evaluation | Methodology & Evaluation |
| 7. Lessons & Limitations | Portability & Lessons |
| 8. Deeper Resources & Contact | About / Contact |

---

## 6. How a Visitor Returns Without Getting Lost

- Standard persistent top navigation across all five pages (Home · Evidence · Methodology & Evaluation · Portability & Lessons · About/Contact) — a real, conventional multi-page nav, not anchor links within one document.
- Every page can be reached directly from any other page via that same navigation; no page is a dead end requiring a "back" link to escape.
- GitHub is the only destination that leaves the site (new tab); the whitepaper is a download, not a navigation state.

---

## 7. What This Step Does NOT Include

- Visual design of the navigation itself (Step 1's tokens apply during implementation, not a new decision here)
- Section-by-section copy placement within each page (Step 3)
- The technical embedding of Workstream B's evidence-trail page into the Evidence page (implementation detail, not an architecture decision)
- Any new analytical content, narrative section, or destination beyond what is already supported by frozen Workstreams A, B, and D or by the approved Phase E/F roadmap

---

## 8. Acceptance Check Before Step 2 Is Considered Complete

- [ ] Home alone contains the complete, honest hiring case — the $251K finding with its category distinction intact, and the MISS/MISS/CLEAN result stated plainly — verified by checking that a visitor who never clicks past Home still receives an accurate impression, per Workstream A's governing rule.
- [ ] Videos 1 and 4 both appear on Home, with genuinely unequal visual weight — not two identical stacked blocks.
- [ ] Evidence, Methodology & Evaluation, Portability & Lessons, and About/Contact each exist as their own page, correctly containing the Workstream A sections mapped to them in Section 5 above.
- [ ] The contact form contains exactly Name, Email, Subject, Message — no phone field — and submits to kcorioso@gmail.com.
- [ ] The whitepaper is a direct download with no interstitial page; GitHub opens in a new tab; Case Study has its own dedicated route.
- [ ] No page name is ambiguous about its contents before a visitor clicks it.

---

**End of Harbor Ridge V1 — Workstream F, Step 2: Site Information Architecture Decision Spec (Final, adopted in full)**
