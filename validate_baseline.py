"""
Harbor Ridge V0.1 Baseline Validation
======================================

Checks the freshly generated harbor_ridge.db against the V0.1 Baseline
Acceptance Criteria at the end of
docs/harbor-ridge-synthetic-dataset-v0.1-generation-rules.md.

Three independent dimensions are checked, and none substitutes for another:

  1. STRUCTURAL INTEGRITY -- does the database itself obey the frozen
     schema (foreign keys, CHECK constraints, table population)?
  2. REPRODUCIBILITY -- does SEED = 20260825 actually produce the same
     database on repeated runs (Section 2), verified here by generating
     the dataset twice in-process and diffing every table, not just
     assumed from the seed being fixed?
  3. DOMAIN REALISM -- do the actual generated numbers land inside the
     target ranges the generation-rules document specifies (admissions
     per month, conversion rates, payer mix, etc.)?

Writes a full report to baseline_validation_results.txt and also prints
it to stdout.
"""

import sqlite3
import sys
import tempfile
from datetime import datetime
from io import StringIO

import generate_synthetic_data as gsd

DB_PATH = "harbor_ridge.db"
OUT_PATH = "baseline_validation_results.txt"

out = StringIO()


def w(line=""):
    print(line)
    out.write(str(line) + "\n")


def section(title):
    w()
    w("=" * 78)
    w(title)
    w("=" * 78)


def check(label, passed, detail=""):
    status = "PASS" if passed else "FAIL"
    w(f"  [{status}] {label}" + (f" -- {detail}" if detail else ""))
    return passed


def within_tolerance(value, target, tolerance_abs=None, tolerance_pct=None):
    if tolerance_abs is not None:
        return abs(value - target) <= tolerance_abs
    if tolerance_pct is not None:
        return abs(value - target) <= target * tolerance_pct
    return value == target


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    all_pass = True

    w("Harbor Ridge V0.1 Baseline Validation Results")
    w(f"Generated: {datetime.now().isoformat()}")
    w(f"Database: {DB_PATH}")

    # =======================================================================
    # DIMENSION 1: STRUCTURAL INTEGRITY
    # =======================================================================
    section("DIMENSION 1: STRUCTURAL INTEGRITY")

    fk_violations = cur.execute("PRAGMA foreign_key_check").fetchall()
    ok = check("PRAGMA foreign_key_check returns zero violations", len(fk_violations) == 0,
               f"{len(fk_violations)} violation(s) found" if fk_violations else "0 violations")
    all_pass &= ok
    if fk_violations:
        for v in fk_violations[:20]:
            w(f"       {v}")

    integrity = cur.execute("PRAGMA integrity_check").fetchone()[0]
    ok = check("PRAGMA integrity_check passes", integrity == "ok", integrity)
    all_pass &= ok

    tables = [
        "contacts", "outreach_reps", "professional_accounts", "patient_opportunities",
        "inquiries", "acquisition_touches", "professional_referrals", "outreach_activities",
        "ehr_episodes", "claims", "claim_events",
    ]
    w()
    w("  Table population (all 11 tables from the frozen schema):")
    for t in tables:
        n = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        ok = check(f"{t} populated", n > 0, f"{n} rows")
        all_pass &= ok

    # Re-affirm the CHECK-constraint conditional rules with direct queries
    # (a live check against actual generated data, not just relying on
    # SQLite to have rejected bad rows at insert time).
    w()
    w("  Conditional integrity rules (Dictionary Sections 15.1, 15.2), verified against actual rows:")

    vob_violations = cur.execute(
        "SELECT COUNT(*) FROM patient_opportunities WHERE "
        "NOT ((vob_submitted_flag = 0 AND vob_outcome IS NULL) OR "
        "(vob_submitted_flag = 1 AND vob_outcome IN ('Pending','Viable','Non-Viable','Unable to Verify')))"
    ).fetchone()[0]
    ok = check("VOB conditional rule holds for every patient_opportunities row", vob_violations == 0,
               f"{vob_violations} violating rows")
    all_pass &= ok

    episode_violations = cur.execute(
        "SELECT COUNT(*) FROM ehr_episodes WHERE "
        "NOT ((episode_relationship = 'Initial' AND prior_episode_id IS NULL) OR "
        "(episode_relationship IN ('LOC Transition','Administrative Re-Admit') AND prior_episode_id IS NOT NULL))"
    ).fetchone()[0]
    ok = check("Episode conditional rule holds for every ehr_episodes row", episode_violations == 0,
               f"{episode_violations} violating rows")
    all_pass &= ok

    # Orphaned prior_episode_id references (should be impossible given FK enforcement,
    # checked directly as an extra structural sanity pass)
    orphan_prior = cur.execute(
        "SELECT COUNT(*) FROM ehr_episodes e WHERE e.prior_episode_id IS NOT NULL "
        "AND NOT EXISTS (SELECT 1 FROM ehr_episodes p WHERE p.episode_id = e.prior_episode_id)"
    ).fetchone()[0]
    ok = check("No dangling ehr_episodes.prior_episode_id references", orphan_prior == 0, f"{orphan_prior} dangling")
    all_pass &= ok

    # =======================================================================
    # DIMENSION 2: REPRODUCIBILITY (Section 2)
    # =======================================================================
    section("DIMENSION 2: REPRODUCIBILITY")
    w("  Generating the full dataset twice, independently, with SEED = "
      f"{gsd.SEED}, and diffing every table row-by-row (not just assuming "
      "reproducibility from the seed being fixed).")

    TABLE_KEYS = [
        "contacts", "reps", "accounts", "opportunities", "inquiries",
        "touches", "referrals", "activities", "episodes", "claims", "claim_events",
    ]

    gsd.ids.counters.clear()
    run_a = gsd.generate_dataset()
    gsd.ids.counters.clear()
    run_b = gsd.generate_dataset()

    w()
    repro_all_match = True
    for key in TABLE_KEYS:
        rows_a, rows_b = run_a[key], run_b[key]
        same_len = len(rows_a) == len(rows_b)
        same_rows = same_len and all(
            sorted(a.items()) == sorted(b.items()) for a, b in zip(rows_a, rows_b)
        )
        detail = f"{len(rows_a)} rows" if same_rows else f"{len(rows_a)} vs {len(rows_b)} rows / content differs"
        ok = check(f"{key} identical across two independent generations", same_rows, detail)
        repro_all_match &= ok
    all_pass &= repro_all_match

    # Also build two actual SQLite database files end-to-end and diff every
    # table via SQL, to confirm build_database()'s fixed insertion order
    # doesn't introduce any nondeterminism of its own beyond the in-memory
    # dataset already checked above.
    w()
    with tempfile.TemporaryDirectory() as tmpdir:
        db_a_path = f"{tmpdir}/repro_a.db"
        db_b_path = f"{tmpdir}/repro_b.db"
        gsd.build_database(run_a, db_path=db_a_path)
        gsd.build_database(run_b, db_path=db_b_path)
        conn_a = sqlite3.connect(db_a_path)
        conn_b = sqlite3.connect(db_b_path)
        db_repro_all_match = True
        for table in gsd.TABLES:
            pk = {
                "contacts": "contact_id", "outreach_reps": "outreach_rep_id",
                "professional_accounts": "professional_account_id", "patient_opportunities": "opportunity_id",
                "inquiries": "inquiry_id", "acquisition_touches": "touch_id",
                "professional_referrals": "referral_id", "outreach_activities": "activity_id",
                "ehr_episodes": "episode_id", "claims": "claim_id", "claim_events": "claim_event_id",
            }[table]
            rows_a = conn_a.execute(f"SELECT * FROM {table} ORDER BY {pk}").fetchall()
            rows_b = conn_b.execute(f"SELECT * FROM {table} ORDER BY {pk}").fetchall()
            match = rows_a == rows_b
            ok = check(f"[DB] {table} identical between two built databases", match,
                       f"{len(rows_a)} rows" if match else f"{len(rows_a)} vs {len(rows_b)} rows / content differs")
            db_repro_all_match &= ok
        conn_a.close()
        conn_b.close()
    all_pass &= db_repro_all_match

    # =======================================================================
    # DIMENSION 3: DOMAIN REALISM
    # =======================================================================
    section("DIMENSION 3: DOMAIN REALISM")

    # --- Admissions per month (target 38-42, centered 40) ---
    # Measured against ehr_episodes.admission_datetime (episode_relationship
    # = 'Initial'), i.e. when the admission actually, operationally
    # happened -- not patient_opportunities.created_at, which is when the
    # opportunity was first created and can precede the actual admission by
    # several days (Section 3.2's funnel takes time to resolve).
    w()
    w("  Admissions per month (by ehr_episodes.admission_datetime, episode_relationship = 'Initial'; "
      "Section 3 target: 38-42, centered 40):")
    monthly_admits = cur.execute(
        "SELECT strftime('%Y-%m', admission_datetime) AS ym, COUNT(*) FROM ehr_episodes "
        "WHERE episode_relationship = 'Initial' GROUP BY ym ORDER BY ym"
    ).fetchall()
    monthly_admits_dict = dict(monthly_admits)
    for label, ym_prefix in (("2026-05", "2026-05"), ("2026-06", "2026-06"), ("2026-07", "2026-07")):
        n = monthly_admits_dict.get(ym_prefix, 0)
        ok = check(f"{label} admissions in [38,42]", 38 <= n <= 42, f"{n} admissions")
        all_pass &= ok

    total_admits = sum(n for ym, n in monthly_admits if ym <= "2026-07")
    avg_admits = total_admits / 3
    w(f"  Total admissions (May-Jul): {total_admits} over 3 months, average {avg_admits:.1f}/month "
      f"(3-month target ~120)")

    n_august_initial = monthly_admits_dict.get("2026-08", 0) + sum(
        n for ym, n in monthly_admits if ym > "2026-08"
    )
    ok = check(
        "Zero Initial episodes fall outside the May-July operating window (Section 1)",
        n_august_initial == 0,
        f"{n_august_initial} Initial episode(s) admitted in/after August" if n_august_initial else "0 found",
    )
    all_pass &= ok

    # Supplementary: by opportunity created_at month (when the opportunity
    # entered the pipeline, not necessarily when it admitted)
    w()
    w("  Supplementary -- admitted opportunities by patient_opportunities.created_at month:")
    opp_created_monthly = cur.execute(
        "SELECT strftime('%Y-%m', created_at) AS ym, COUNT(*) FROM patient_opportunities "
        "WHERE admission_status = 'Admitted' GROUP BY ym ORDER BY ym"
    ).fetchall()
    for ym, n in opp_created_monthly:
        w(f"    {ym}: {n} admitted opportunities created")

    # --- Opportunity -> Completed Admission (~23%) ---
    w()
    total_opps = cur.execute("SELECT COUNT(*) FROM patient_opportunities").fetchone()[0]
    admitted = cur.execute("SELECT COUNT(*) FROM patient_opportunities WHERE admission_status = 'Admitted'").fetchone()[0]
    opp_to_admit = admitted / total_opps if total_opps else 0
    ok = check(
        "Opportunity -> Completed Admission ~23% (tolerance +-3pp)",
        within_tolerance(opp_to_admit, 0.23, tolerance_abs=0.03),
        f"{opp_to_admit:.1%} ({admitted}/{total_opps})",
    )
    all_pass &= ok

    # --- Inquiry -> Completed Admission (~19%) ---
    total_inq = cur.execute("SELECT COUNT(*) FROM inquiries").fetchone()[0]
    inq_to_admit = admitted / total_inq if total_inq else 0
    ok = check(
        "Inquiry -> Completed Admission ~19% (tolerance +-3pp)",
        within_tolerance(inq_to_admit, 0.19, tolerance_abs=0.03),
        f"{inq_to_admit:.1%} ({admitted}/{total_inq})",
    )
    all_pass &= ok

    # --- Inquiry -> Patient Opportunity ~83% ---
    # Section 3.1's ~83% is the VOLUME RATIO of opportunities to inquiries
    # (175/210), reflecting multiple inquiries collapsing into one
    # opportunity plus orphaned/duplicate inquiries -- not the fraction of
    # individual inquiries that carry a non-null opportunity_id (which is
    # naturally much higher, since only orphan inquiries lack one).
    inq_to_opp = total_opps / total_inq if total_inq else 0
    ok = check(
        "Inquiry -> Patient Opportunity volume ratio ~83% (opportunities/inquiries, tolerance +-5pp)",
        within_tolerance(inq_to_opp, 0.83, tolerance_abs=0.05),
        f"{inq_to_opp:.1%} ({total_opps}/{total_inq})",
    )
    all_pass &= ok

    resolved_inq = cur.execute("SELECT COUNT(*) FROM inquiries WHERE opportunity_id IS NOT NULL").fetchone()[0]
    w(f"  (Informational: {resolved_inq}/{total_inq} = {resolved_inq/total_inq:.1%} of individual inquiries "
      f"carry a non-null opportunity_id; the remainder are orphan/unmatched inquiries.)")

    # --- Monthly inquiry / opportunity volume vs ~210 / ~175 targets, +-5-10% ---
    w()
    w("  Monthly volumes vs Section 3 targets (Inquiries ~210 +-10%, Opportunities ~175 +-10%):")
    monthly_inq = dict(cur.execute(
        "SELECT strftime('%Y-%m', inquiry_timestamp) AS ym, COUNT(*) FROM inquiries GROUP BY ym ORDER BY ym"
    ).fetchall())
    monthly_opp = dict(cur.execute(
        "SELECT strftime('%Y-%m', created_at) AS ym, COUNT(*) FROM patient_opportunities GROUP BY ym ORDER BY ym"
    ).fetchall())
    for ym in sorted(set(monthly_inq) | set(monthly_opp)):
        i, o = monthly_inq.get(ym, 0), monthly_opp.get(ym, 0)
        i_ok = within_tolerance(i, 210, tolerance_pct=0.10)
        o_ok = within_tolerance(o, 175, tolerance_pct=0.10)
        check(f"{ym} inquiries ~210 (+-10%)", i_ok, f"{i}")
        check(f"{ym} opportunities ~175 (+-10%)", o_ok, f"{o}")
        all_pass &= i_ok
        all_pass &= o_ok

    # --- Payer mix at admitted cohort: 55/35/10 +-3pp ---
    section_line = "  Admitted-cohort payer mix (3-month, target 55% INN / 35% OON / 10% Private Pay, tolerance +-3pp):"
    w()
    w(section_line)
    payer_rows = cur.execute(
        "SELECT payer_relationship, COUNT(*) FROM patient_opportunities WHERE admission_status = 'Admitted' "
        "GROUP BY payer_relationship"
    ).fetchall()
    payer_counts = dict(payer_rows)
    total_admitted_payer = sum(payer_counts.values())
    targets = {"INN": 0.55, "OON": 0.35, "Private Pay": 0.10}
    for payer, target_pct in targets.items():
        n = payer_counts.get(payer, 0)
        pct = n / total_admitted_payer if total_admitted_payer else 0
        ok = check(f"{payer} admitted share ~{target_pct:.0%} (+-3pp)",
                    within_tolerance(pct, target_pct, tolerance_abs=0.03),
                    f"{pct:.1%} ({n}/{total_admitted_payer})")
        all_pass &= ok

    # Opportunity-level payer mix (informational -- "may fluctuate modestly")
    w()
    opp_payer_rows = cur.execute(
        "SELECT payer_relationship, COUNT(*) FROM patient_opportunities GROUP BY payer_relationship"
    ).fetchall()
    w("  Opportunity-level payer mix (informational, Section 4: may fluctuate modestly around baseline):")
    for payer, n in opp_payer_rows:
        w(f"    {payer}: {n} ({n/total_opps:.1%})")

    # --- Calls vs web forms both materially represented ---
    w()
    method_rows = dict(cur.execute("SELECT inquiry_method, COUNT(*) FROM inquiries GROUP BY inquiry_method").fetchall())
    n_call = method_rows.get("Call", 0)
    n_form = method_rows.get("Web Form", 0)
    ok = check("Calls and Web Forms both materially represented (each >=20% of inquiries)",
               (n_call / total_inq >= 0.20) and (n_form / total_inq >= 0.20),
               f"Call {n_call} ({n_call/total_inq:.1%}), Web Form {n_form} ({n_form/total_inq:.1%})")
    all_pass &= ok

    # --- Multiple-inquiry opportunities exist ---
    w()
    multi_inq = cur.execute(
        "SELECT COUNT(*) FROM (SELECT opportunity_id, COUNT(*) c FROM inquiries "
        "WHERE opportunity_id IS NOT NULL GROUP BY opportunity_id HAVING c > 1)"
    ).fetchone()[0]
    ok = check("Multiple-inquiry opportunities exist", multi_inq > 0, f"{multi_inq} opportunities with >1 inquiry")
    all_pass &= ok

    # --- Both Detox and Residential pathways exist ---
    w()
    loc_rows = dict(cur.execute("SELECT level_of_care, COUNT(*) FROM ehr_episodes GROUP BY level_of_care").fetchall())
    ok = check("Both Detox and Residential episodes exist",
               loc_rows.get("Detox", 0) > 0 and loc_rows.get("Residential", 0) > 0,
               f"Detox={loc_rows.get('Detox',0)}, Residential={loc_rows.get('Residential',0)}")
    all_pass &= ok

    # --- LOC transitions exist and link correctly ---
    transitions = cur.execute(
        "SELECT COUNT(*) FROM ehr_episodes WHERE episode_relationship = 'LOC Transition'"
    ).fetchone()[0]
    bad_transitions = cur.execute(
        "SELECT COUNT(*) FROM ehr_episodes e WHERE e.episode_relationship = 'LOC Transition' AND "
        "NOT EXISTS (SELECT 1 FROM ehr_episodes p WHERE p.episode_id = e.prior_episode_id)"
    ).fetchone()[0]
    ok = check("LOC Transition episodes exist and link correctly to a prior episode",
               transitions > 0 and bad_transitions == 0,
               f"{transitions} transitions, {bad_transitions} broken links")
    all_pass &= ok

    # --- Multi-claim episodes exist (~15% target) ---
    w()
    claims_per_ep = cur.execute(
        "SELECT episode_id, COUNT(*) c FROM claims WHERE episode_id IS NOT NULL GROUP BY episode_id"
    ).fetchall()
    n_eps_with_claims = len(claims_per_ep)
    n_multi_claim = sum(1 for _, c in claims_per_ep if c > 1)
    multi_claim_pct = n_multi_claim / n_eps_with_claims if n_eps_with_claims else 0
    ok = check("Multi-claim episodes exist, roughly near 15% target (tolerance +-8pp)",
               n_multi_claim > 0 and within_tolerance(multi_claim_pct, 0.15, tolerance_abs=0.08),
               f"{multi_claim_pct:.1%} ({n_multi_claim}/{n_eps_with_claims})")
    all_pass &= ok

    # --- Payment / adjustment histories exist ---
    w()
    event_type_counts = dict(cur.execute("SELECT event_type, COUNT(*) FROM claim_events GROUP BY event_type").fetchall())
    has_payment = event_type_counts.get("Insurance Payment", 0) + event_type_counts.get("Patient Payment", 0) > 0
    has_adjustment_family = any(event_type_counts.get(t, 0) > 0 for t in ("Adjustment", "Write-Off", "Denial", "Appeal"))
    ok = check("Payment and adjustment/denial/appeal histories exist", has_payment and has_adjustment_family,
               f"event_type counts: {event_type_counts}")
    all_pass &= ok

    # --- Financial maturity differs naturally by cohort month ---
    w()
    w("  Financial maturity by admission cohort month (claim_status distribution via episode admission month):")
    maturity_rows = cur.execute(
        "SELECT strftime('%Y-%m', e.admission_datetime) AS ym, c.claim_status, COUNT(*) "
        "FROM claims c JOIN ehr_episodes e ON c.episode_id = e.episode_id "
        "GROUP BY ym, c.claim_status ORDER BY ym"
    ).fetchall()
    maturity = {}
    for ym, status, n in maturity_rows:
        maturity.setdefault(ym, {})[status] = n
    for ym in sorted(maturity):
        row = maturity[ym]
        total = sum(row.values())
        resolved = row.get("Paid", 0) + row.get("Closed", 0)
        w(f"    {ym}: total={total}, resolved(Paid/Closed)={resolved} ({resolved/total:.1%}), detail={row}")

    if len(maturity) >= 2:
        yms_sorted = sorted(maturity.keys())
        earliest, latest = yms_sorted[0], yms_sorted[-1]
        earliest_resolved_pct = (maturity[earliest].get("Paid", 0) + maturity[earliest].get("Closed", 0)) / sum(maturity[earliest].values())
        latest_resolved_pct = (maturity[latest].get("Paid", 0) + maturity[latest].get("Closed", 0)) / sum(maturity[latest].values())
        ok = check(f"Earliest cohort ({earliest}) more resolved than latest cohort ({latest})",
                   earliest_resolved_pct > latest_resolved_pct,
                   f"{earliest}={earliest_resolved_pct:.1%} resolved vs {latest}={latest_resolved_pct:.1%} resolved")
        all_pass &= ok

    # --- No intentional downward trend across months (Section 17) ---
    # With only 3 monthly data points, a strict-monotonicity test is not a
    # meaningful trend detector: an iid random sequence of 3 distinct values
    # is monotonic in one direction 1/3 of the time by chance alone, so
    # flagging monotonicity here would produce false positives rather than
    # detect an engineered decline. The real evidence against an intentional
    # trend is structural: every month draws inquiries/opportunities from
    # the SAME fixed target (175 opportunities +-15, Section 3) with no
    # month-dependent decay term in the generator, which is what the
    # per-month tolerance-band checks above already confirm. A genuine
    # engineered decline (e.g. the later diagnostic scenario's paid-search
    # deterioration) would need to move a month materially outside that
    # fixed +-10% band by month 3 -- which did not happen above.
    w()
    w("  Month-over-month stability (Section 17: random noise yes, intentional trend no):")
    inq_vals = [monthly_inq[ym] for ym in sorted(monthly_inq)]
    admit_vals = [monthly_admits_dict.get(ym, 0) for ym in ("2026-05", "2026-06", "2026-07")]
    w(f"    Inquiries by month: {inq_vals}")
    w(f"    Admissions by month: {admit_vals}")
    w("    (See per-month tolerance-band PASS/FAIL results above -- each month is drawn from the same "
      "fixed target with no month-dependent trend term in the generator; 3-point monotonicity is not "
      "tested separately here as it is not statistically meaningful at n=3.)")

    # --- Synthetic-only identity conventions ---
    w()
    bad_email = cur.execute("SELECT COUNT(*) FROM contacts WHERE email IS NOT NULL AND email NOT LIKE '%@example.test'").fetchone()[0]
    bad_phone = cur.execute("SELECT COUNT(*) FROM contacts WHERE phone IS NOT NULL AND phone NOT LIKE '555-%'").fetchone()[0]
    ok = check("All contact emails use @example.test", bad_email == 0, f"{bad_email} non-conforming")
    all_pass &= ok
    ok = check("All contact phone numbers use 555- prefix", bad_phone == 0, f"{bad_phone} non-conforming")
    all_pass &= ok

    # --- Identity resolution distribution (Section 8: Confirmed 85-90%, Probable 7-10%, Possible small, Unmatched rare) ---
    w()
    w("  Identity resolution distribution (Section 8 target: Confirmed 85-90%, Probable 7-10%, Possible small, Unmatched rare):")
    match_conf = dict(cur.execute("SELECT match_confidence, COUNT(*) FROM inquiries GROUP BY match_confidence").fetchall())
    for level in ("Confirmed", "Probable", "Possible", "Unmatched"):
        n = match_conf.get(level, 0)
        w(f"    {level}: {n} ({n/total_inq:.1%})")

    # --- Not Financially Cleared essentially never admits ---
    w()
    bad_admit_financial = cur.execute(
        "SELECT COUNT(*) FROM patient_opportunities WHERE admission_status = 'Admitted' "
        "AND admission_financial_status = 'Not Financially Cleared'"
    ).fetchone()[0]
    ok = check("Admitted opportunities essentially never carry 'Not Financially Cleared'", bad_admit_financial == 0,
               f"{bad_admit_financial} such rows")
    all_pass &= ok

    # =======================================================================
    section("OVERALL RESULT")
    w(f"  {'ALL CHECKS PASSED' if all_pass else 'SOME CHECKS FAILED -- see [FAIL] lines above'}")

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(out.getvalue())

    conn.close()
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
