# HEOS Evidence Engine — Harbor Ridge V1

**Status: completed portfolio project (closed October 25, 2026).**
Public site: **[heosevidenceengine.com](https://heosevidenceengine.com)**

HEOS (the Evidence Engine) is an AI reasoning system for evidence-based executive performance analysis in healthcare. Harbor Ridge Behavioral Health is the fictional, fully synthetic organization I built to test it. This repository holds the data model, synthetic datasets, evaluation records and the source for the public site.

> **Synthetic data only.** No real patient, protected health information (PHI), or confidential employer/client data is used anywhere in this repository.

## The problem

Harbor Ridge's completed admissions and census were declining while marketing spend and inquiry volume rose. Marketing believed admissions was failing to convert demand. Admissions believed marketing was sending lower-quality inquiries. Neither side had evidence connecting the two departments. The project asks whether an AI system can reason across those silos, and, just as importantly, how to evaluate that claim honestly.

## What was built

- **A modeled organization.** A source-system map, a frozen data dictionary, and an 11-table relational schema (`schema.sql`) with a 22-test constraint suite (`test_constraints.py`).
- **Synthetic datasets.** A healthy baseline plus two scenarios with deliberately hidden deteriorations (paid-search inquiry quality and professional-outreach quality), generated deterministically from fixed seeds (`generate_synthetic_data.py`).
- **A frozen Ground Truth answer key**, written before any AI analysis (`docs/harbor-ridge-ground-truth-answer-key.md`).
- **A blind evaluation** (Phase D, V0.1 and V0.2): a generic discovery procedure designed without Harbor Ridge context, audited by two AI reviewers (one Claude, one ChatGPT), frozen, then run in three isolated sessions (Scenario 1, Scenario 2, healthy-baseline control) and scored against a pre-registered interpretation protocol.
- **A public portfolio site** (Astro, static), four videos, a 14-page whitepaper and a one-page AI Summary.

## What it found

| Result | Outcome |
|---|---|
| Scenario 1 (benchmark) | **MISS** |
| Scenario 2 (benchmark) | **MISS** |
| Healthy Baseline (negative control) | **CLEAN** |

The system did not recover either planted problem. It did independently surface a large gap between in-network (INN) and out-of-network (OON) claims realization that I had not planted. That is classified as an **Observed Finding**, not a Benchmark Result: INN claims collected 66.77% of billed charges versus 30.38% for OON claims. Applying the INN rate to OON billed claims gives an **estimated collections gap of about $251K** (reconstructed exactly as $250,397.60). This is an estimate under a stated counterfactual in synthetic data. It is not recovered, saved, generated or realized revenue.

## What this does not demonstrate

- Reliable discovery of hidden, localized problems (both planted problems were missed).
- Performance on real data or in a real organization.
- General reliability. One clean control result does not establish it.
- Production readiness. This is a portfolio project, not a deployed product.
- Third-party or human-expert validation. The two audits of the discovery procedure were AI-assisted.
- Portability of Harbor Ridge itself. The build-and-evaluate *process* is what transfers, by rebuilding it around another organization's real operating environment.

## Verify the $251K finding yourself

All Python scripts use only the standard library (tested with Python 3.13). From the repository root:

```bash
python generate_synthetic_data.py --mode scenario1    # regenerates harbor_ridge_scenario1.db and data/csv_export_scenario1/
python validate_scenario1.py                          # validation checks
python scripts/export_evidence_trail_251k.py          # regenerates src/data/evidence-trail-251k.json
git status                                            # the committed JSON should be unchanged
```

The baseline and Scenario 2 datasets regenerate the same way (`--mode baseline`, `--mode scenario2`; checks in `validate_baseline.py` and `validate_scenario2.py`, the latter including a large-sample mechanism check that takes a few minutes).

What to expect:

- The regenerated `evidence-trail-251k.json` is byte-identical to the committed one: 101 INN and 59 OON claims, estimated gap `250397.59793…`. The regenerated CSV exports match the committed ones apart from line endings.
- `validate_scenario1.py` reports two `[FAIL]` lines (OON share peaking at 60.5% against an approximate 60% ceiling, and June mean cost at -3.5% against an expected +5%). These match the committed `scenario1_validation_results.txt` and are recorded in the answer key.
- Databases regenerated from the fixed seeds were checked table by table (all 11 tables) against the original frozen Scenario 1 and Scenario 2 databases and were identical. `validate_baseline.py` and `validate_scenario2.py` report all checks passed on regenerated data.
- The `.db` files are gitignored; they are regenerated by the first command.

## Not included in this repository

- The original V0.1 raw output (`scenario1_claude_analysis_v0.1.md`), which produced the roughly $251,000 estimate. It is named in the evaluation summaries but was not committed and could not be located. The three V0.2 raw outputs and the Neutral Analyst Brief **are** published, unedited, in [`docs/blind-test-outputs/`](docs/blind-test-outputs/).
- Model and version identifiers for the blind sessions.
- A dashboard, an automated workflow or any n8n automation. These appeared in the original plan and were not built. The public site replaced the dashboard; n8n was removed from scope.

## Repository map

| Path | What it holds |
|---|---|
| `docs/harbor-ridge-business-scenario.md` | The organization, funnel and hidden failure scenarios |
| `docs/minimum-viable-data-dictionary.md`, `schema.sql` | The data dictionary and schema |
| `docs/source-system-map.md`, `docs/source-system-architecture-notes.md` | System architecture and identity chain |
| `docs/harbor-ridge-scenario-1-specification.md`, `...scenario-2-specification.md` | Scenario designs |
| `docs/harbor-ridge-ground-truth-answer-key.md` | Frozen Ground Truth (public by decision, post-evaluation) |
| `docs/phase-d-v0.2-discovery-procedure.md` | The frozen blind discovery procedure |
| `docs/phase-d-v0.2-evaluation-interpretation-protocol.md` | The pre-registered scoring protocol |
| `docs/phase-d-v0.2-run-manifest.md`, `...evaluation-summary.md`, `phase-d-closing-diagnostic.md` | What was run, how it was scored, and the diagnosis |
| `docs/harbor-ridge-v1-case-study.md`, `harbor-ridge-v1-methodology.md` | Narrative write-ups |
| `docs/harbor-ridge-v1-feature-freeze.md` | The frozen V1 scope |
| `generate_synthetic_data.py`, `validate_*.py`, `test_constraints.py` | Dataset generation and validation |
| `data/csv_export*/` | CSV exports of the baseline and both scenarios |
| `scripts/export_evidence_trail_251k.py` | Reproduces the $251K arithmetic |
| `src/`, `public/` | The Astro site source and downloads |
| `docs/videos/` | The four videos (Git LFS) |

## Site

An Astro 4 static site, deployed to Cloudflare Workers static assets from `main`. To build locally (Node required):

```bash
npm install
npm run build
```

## Project principles

1. **Synthetic data only.**
2. **AI supports judgment, not decisions.**
3. **Observations and hypotheses stay separate.**
4. **Attribution before optimization.**
5. **Build before polish.**

## Author

**Kenneth Corioso** — healthcare growth and operations professional focused on practical AI systems at the intersection of analytics, technology and executive decision-making. [LinkedIn](https://www.linkedin.com/in/kenneth-corioso/)
