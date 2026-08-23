import sqlite3

conn = sqlite3.connect('harbor_ridge.db')
conn.execute('PRAGMA foreign_keys = ON')

results = []


def run(label, sql, params, expect):
    """expect: 'accept' or 'reject'"""
    try:
        conn.execute(sql, params)
        conn.commit()
        outcome = 'ACCEPTED'
    except sqlite3.IntegrityError as e:
        conn.rollback()
        outcome = f'REJECTED ({e})'
    passed = (outcome == 'ACCEPTED') if expect == 'accept' else outcome.startswith('REJECTED')
    results.append((label, expect.upper(), outcome, 'PASS' if passed else 'FAIL'))


# --- Baseline reference data needed for FK-satisfying test rows ---
conn.execute(
    "INSERT INTO contacts (contact_id, first_name, last_name, phone, email, date_of_birth, created_at) "
    "VALUES ('CNT-000241', 'Susan', 'Miller', '555-010-8821', 'susan.miller@example.test', NULL, '2026-06-03T14:22:00')"
)
conn.commit()

# ===========================================================================
# Section 11.2 example 1 (VALID): episode_relationship = Initial, prior_episode_id = NULL
# ===========================================================================
run(
    'ehr_episodes VALID #1 (Initial / prior_episode_id=NULL)',
    "INSERT INTO ehr_episodes (episode_id, opportunity_id, prior_episode_id, episode_relationship, "
    "admission_datetime, discharge_datetime, level_of_care, payer, authorization_start, authorization_end, "
    "discharge_disposition, source_system, evidence_class) VALUES "
    "('KIPU-000101', NULL, NULL, 'Initial', '2026-06-01T09:00:00', NULL, 'Residential', NULL, NULL, NULL, NULL, 'EHR', 'System-Observed')",
    (), 'accept',
)

# ===========================================================================
# Section 11.2 example 2 (VALID): episode_relationship = LOC Transition, prior_episode_id = KIPU-000101
# ===========================================================================
run(
    'ehr_episodes VALID #2 (LOC Transition / prior_episode_id=KIPU-000101)',
    "INSERT INTO ehr_episodes (episode_id, opportunity_id, prior_episode_id, episode_relationship, "
    "admission_datetime, discharge_datetime, level_of_care, payer, authorization_start, authorization_end, "
    "discharge_disposition, source_system, evidence_class) VALUES "
    "('KIPU-000102', NULL, 'KIPU-000101', 'LOC Transition', '2026-06-05T09:00:00', NULL, 'Detox', NULL, NULL, NULL, NULL, 'EHR', 'System-Observed')",
    (), 'accept',
)

# ===========================================================================
# Section 11.2 example 3 (INVALID): episode_relationship = LOC Transition, prior_episode_id = NULL
# ===========================================================================
run(
    'ehr_episodes INVALID #1 (LOC Transition / prior_episode_id=NULL)',
    "INSERT INTO ehr_episodes (episode_id, opportunity_id, prior_episode_id, episode_relationship, "
    "admission_datetime, discharge_datetime, level_of_care, payer, authorization_start, authorization_end, "
    "discharge_disposition, source_system, evidence_class) VALUES "
    "('KIPU-000103', NULL, NULL, 'LOC Transition', '2026-06-06T09:00:00', NULL, 'Residential', NULL, NULL, NULL, NULL, 'EHR', 'System-Observed')",
    (), 'reject',
)

# ===========================================================================
# Section 11.2 example 4 (INVALID): episode_relationship = Initial, prior_episode_id = KIPU-000099
# ===========================================================================
run(
    'ehr_episodes INVALID #2 (Initial / prior_episode_id=KIPU-000099)',
    "INSERT INTO ehr_episodes (episode_id, opportunity_id, prior_episode_id, episode_relationship, "
    "admission_datetime, discharge_datetime, level_of_care, payer, authorization_start, authorization_end, "
    "discharge_disposition, source_system, evidence_class) VALUES "
    "('KIPU-000104', NULL, 'KIPU-000099', 'Initial', '2026-06-07T09:00:00', NULL, 'Residential', NULL, NULL, NULL, NULL, 'EHR', 'System-Observed')",
    (), 'reject',
)

# ===========================================================================
# Section 15.1 VOB rule — additional coverage beyond the 11.2 set
# ===========================================================================
# VALID: vob_submitted_flag = 0, vob_outcome = NULL
run(
    'patient_opportunities VALID (vob_submitted_flag=0, vob_outcome=NULL)',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000184', 'CNT-000241', '2026-06-03T14:25:00', 0, NULL, NULL, 'Private Pay', 'Not Financially Cleared', "
    "'Open', 'Organic', NULL, NULL, 'Probable')",
    (), 'accept',
)

# VALID: vob_submitted_flag = 1, vob_outcome = 'Viable'
run(
    'patient_opportunities VALID (vob_submitted_flag=1, vob_outcome=Viable)',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000185', 'CNT-000241', '2026-06-03T15:00:00', 1, 'Viable', 'Acme Health Plan', 'INN', "
    "'Financially Cleared', 'Admitted', 'Paid', NULL, NULL, 'Confirmed')",
    (), 'accept',
)

# INVALID: vob_submitted_flag = 0 but vob_outcome is NOT NULL
run(
    'patient_opportunities INVALID (vob_submitted_flag=0, vob_outcome=Pending)',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000186', 'CNT-000241', '2026-06-03T15:10:00', 0, 'Pending', NULL, 'Private Pay', "
    "'Not Financially Cleared', 'Open', 'Organic', NULL, NULL, 'Possible')",
    (), 'reject',
)

# INVALID: vob_submitted_flag = 1 but vob_outcome is NULL
run(
    'patient_opportunities INVALID (vob_submitted_flag=1, vob_outcome=NULL)',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000187', 'CNT-000241', '2026-06-03T15:20:00', 1, NULL, 'Acme Health Plan', 'INN', "
    "'At-Risk Admission', 'Open', 'Paid', NULL, NULL, 'Confirmed')",
    (), 'reject',
)

# INVALID: vob_submitted_flag = 1 but vob_outcome not in allowed set
run(
    'patient_opportunities INVALID (vob_submitted_flag=1, vob_outcome=Approved [not allowed])',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000188', 'CNT-000241', '2026-06-03T15:30:00', 1, 'Approved', 'Acme Health Plan', 'INN', "
    "'Financially Cleared', 'Admitted', 'Paid', NULL, NULL, 'Confirmed')",
    (), 'reject',
)

conn.close()

print(f"{'TEST':70} {'EXPECTED':10} {'OUTCOME':45} {'RESULT'}")
print('-' * 145)
all_pass = True
for label, expect, outcome, result in results:
    print(f"{label:70} {expect:10} {outcome:45} {result}")
    if result == 'FAIL':
        all_pass = False

print()
print('ALL TESTS PASSED' if all_pass else 'SOME TESTS FAILED')
