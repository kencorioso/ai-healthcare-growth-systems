# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

This repository is currently in the **planning/architecture phase**, not the build phase. Every subdirectory (`analysis/`, `dashboard/`, `data/`, `docs/`, `prompts/`, `screenshots/`, `workflow/`) presently contains only a `README.md` describing what will eventually go there — there is no application code, no dependency manifest (no `requirements.txt`/`pyproject.toml`/`package.json`), and no test suite yet. `harbor-ridge-test.ipynb` is the only executable artifact, a scratch notebook exercising the Anthropic Python SDK (`anthropic.Anthropic()` + `dotenv`).

Before assuming a build/lint/test command exists, check whether it has actually been added — the "Planned Tools" sections in each README describe intent, not current state.

## What This Project Is

An AI-powered system for healthcare marketing analytics: ingest channel-level marketing performance data, compute core metrics (spend, leads, conversions/admissions, CPL, CPA, conversion rate), detect anomalies, and use an LLM to produce an executive summary that explicitly separates **observed facts** from **hypotheses**, flags **recommended investigations**, and calls out **findings not established** by the data. The system supports executive judgment; it does not replace it.

Full narrative context lives in `README.md` — read it before making architectural decisions, since it defines the validation roadmap and non-negotiable project principles (synthetic data only, no PHI, attribution before optimization).

### Validation roadmap

The project is deliberately built through one domain at a time, in this order, and later versions are not started until the current one is validated:

1. **V1 — Harbor Ridge Behavioral Health** (current, sole focus): establishes the core patient-acquisition model, analytical architecture, and reasoning approach.
2. **V2 — Orthopedics**: tests generalization to a different specialty/constraint.
3. **V3 — Women's Health**: stress-tests multiple simultaneous constraints.

**Development rule: build deeply before expanding broadly.** Do not scaffold V2/V3 concepts while V1 is incomplete — this is a stated project principle, not just sequencing.

## The Harbor Ridge V1 Scenario (essential context)

Harbor Ridge Behavioral Health is the synthetic organization used to build/validate V1. The detailed scenario, funnel, and architecture are documented across three files that any analysis, dataset, or prompt work must stay consistent with:

- `docs/harbor-ridge-business-scenario.md` — organization profile, payer mix, acquisition channels, the patient-acquisition funnel (Inquiry → Admissions Contact → Clinical/Safety Assessment → Financial Verification → Readiness Assessment → Admission Decision → Scheduling → Logistics → Arrival → Paperwork → **Completed Admission**), the strict admission definition, and the **hidden failure scenario** the synthetic dataset must encode (paid-search inquiry-quality deterioration + professional-outreach quality deterioration, both masked by healthy-looking top-line activity metrics).
- `docs/source-system-architecture-notes.md` — how acquisition/telephony/CRM/EHR source systems relate, identity resolution, duplicate handling, attribution history, and the "Measurement Degradation Framework" (Observability Loss, Identity Loss, Attribution Loss, Outcome-Linkage Loss).
- `docs/source-system-map.md` — the approved (v1.0) canonical architecture: six operational layers (Acquisition → Inquiry Capture → Opportunity/Qualification → Clinical Episode → Revenue Cycle → Executive Intelligence), the canonical `Patient Opportunity` entity (`HRO-######`) and identity chain (CRM Opportunity → EHR Episode `KIPU-####` → RCM Claim `CL-#####` → Payment/Adjustment), and system-of-record ownership rules.

Key modeling rules that recur throughout these docs and must not be violated when writing analysis, prompts, or a data model:

- **Inquiry ≠ Patient Opportunity.** Multiple contacts (mother, father, patient) can collapse into one opportunity; identity match confidence is one of `Confirmed / Probable / Possible / Unmatched`, never silently upgraded to certain.
- **Referral influence ≠ arrival channel.** A patient can arrive via "Google Organic" while the true originating influence is a professional referral — preserve both, don't let one overwrite the other.
- **Platform conversions ≠ CRM inquiries ≠ admissions ≠ revenue.** Never collapse these into a single number; discrepancies between them are diagnostic signal, not noise to reconcile away.
- **Activity metrics ≠ outcome metrics** (e.g., outreach "meetings/contacts" can look healthy while referral quality/admissions decline — this is one of the two hidden failures the synthetic dataset is designed to test detection of).
- **VOB viability ≠ admission decision.** "At-Risk Admissions" (clinically appropriate, financially unresolved) are a deliberate, named operating state, not an error case.
- **Revenue is not one field.** Track the progression Billed Charges → Allowed Amount → Insurance/Patient Responsibility → Adjustments → Appeals → Actual Collections, and respect **cohort maturity** (don't compare a 20-day-old cohort's financials to a 200-day-old cohort's as if equally mature).
- Every derived/executive metric should be able to carry a decision state of `ACT`, `INVESTIGATE`, or `INSUFFICIENT_EVIDENCE` — the system must be able to say evidence is insufficient rather than manufacture false precision.

## Project Principles (apply to all work in this repo)

1. **Synthetic data only** — no real PHI, patient-level data, or confidential employer/client data, ever.
2. **AI supports judgment, not decisions** — AI output is decision support.
3. **Observations and hypotheses stay separate** — any analysis or prompt output should be structured to distinguish what the data shows from what the AI infers.
4. **Attribution before optimization.**
5. **Build before polish** — iterate, document progress via commits.

## Secrets

`.env` holds `ANTHROPIC_API_KEY` and is gitignored — keep it that way. Never print, log, or commit its contents; the notebook loads it via `python-dotenv`.
