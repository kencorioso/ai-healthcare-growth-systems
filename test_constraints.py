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

# ===========================================================================
# Batch 2: broader schema integrity (foreign keys, enums, booleans, golden thread)
# ===========================================================================

# ---------------------------------------------------------------------------
# 2.1 Foreign-key rejection
# ---------------------------------------------------------------------------
run(
    'FK REJECT: inquiries.contact_id references nonexistent contact',
    "INSERT INTO inquiries (inquiry_id, opportunity_id, contact_id, inquiry_timestamp, contact_role, "
    "inquiry_method, arrival_channel, source_platform, tracking_number, call_duration_seconds, landing_page, "
    "match_confidence, source_system, evidence_class) VALUES "
    "('INQ-000901', NULL, 'CNT-999999', '2026-06-10T09:00:00', 'Patient', 'Call', 'Organic', NULL, NULL, NULL, "
    "NULL, 'Confirmed', 'CRM', 'System-Observed')",
    (), 'reject',
)

run(
    'FK REJECT: claims.episode_id (non-null) references nonexistent episode',
    "INSERT INTO claims (claim_id, episode_id, service_start_date, service_end_date, payer, billed_amount, "
    "allowed_amount, patient_responsibility, claim_status, source_system, evidence_class) VALUES "
    "('CLM-000901', 'KIPU-999999', '2026-06-10', '2026-06-15', 'Acme Health Plan', 12000.00, NULL, NULL, "
    "'Submitted', 'RCM', 'System-Observed')",
    (), 'reject',
)

run(
    'FK REJECT: professional_referrals.professional_account_id references nonexistent account',
    "INSERT INTO professional_referrals (referral_id, professional_account_id, opportunity_id, "
    "referral_timestamp, referral_channel, source_system, evidence_class, attribution_confidence) VALUES "
    "('REF-000901', 'PRO-999999', NULL, '2026-06-10T09:00:00', 'Call', 'CRM', 'Human-Entered', 'Possible')",
    (), 'reject',
)

# ---------------------------------------------------------------------------
# 2.2 Enum rejection
# ---------------------------------------------------------------------------
run(
    'ENUM REJECT: patient_opportunities.payer_relationship invalid value',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000901', 'CNT-000241', '2026-06-10T09:00:00', 0, NULL, NULL, 'Medicare Advantage', "
    "'Not Financially Cleared', 'Open', 'Organic', NULL, NULL, 'Possible')",
    (), 'reject',
)

run(
    'ENUM REJECT: patient_opportunities.admission_financial_status invalid value',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000902', 'CNT-000241', '2026-06-10T09:05:00', 0, NULL, NULL, 'Private Pay', "
    "'Pending Review', 'Open', 'Organic', NULL, NULL, 'Possible')",
    (), 'reject',
)

run(
    'ENUM REJECT: inquiries.match_confidence invalid value',
    "INSERT INTO inquiries (inquiry_id, opportunity_id, contact_id, inquiry_timestamp, contact_role, "
    "inquiry_method, arrival_channel, source_platform, tracking_number, call_duration_seconds, landing_page, "
    "match_confidence, source_system, evidence_class) VALUES "
    "('INQ-000902', NULL, 'CNT-000241', '2026-06-10T09:10:00', 'Patient', 'Call', 'Organic', NULL, NULL, NULL, "
    "NULL, 'Certain', 'CRM', 'System-Observed')",
    (), 'reject',
)

run(
    'ENUM REJECT: ehr_episodes.episode_relationship invalid value',
    "INSERT INTO ehr_episodes (episode_id, opportunity_id, prior_episode_id, episode_relationship, "
    "admission_datetime, discharge_datetime, level_of_care, payer, authorization_start, authorization_end, "
    "discharge_disposition, source_system, evidence_class) VALUES "
    "('KIPU-000901', NULL, NULL, 'Readmission', '2026-06-10T09:00:00', NULL, 'Residential', NULL, NULL, NULL, "
    "NULL, 'EHR', 'System-Observed')",
    (), 'reject',
)

run(
    'ENUM REJECT: claims.claim_status invalid value',
    "INSERT INTO claims (claim_id, episode_id, service_start_date, service_end_date, payer, billed_amount, "
    "allowed_amount, patient_responsibility, claim_status, source_system, evidence_class) VALUES "
    "('CLM-000902', NULL, '2026-06-10', '2026-06-15', 'Acme Health Plan', 12000.00, NULL, NULL, "
    "'In Review', 'RCM', 'System-Observed')",
    (), 'reject',
)

# ---------------------------------------------------------------------------
# 2.3 Boolean rejection
# ---------------------------------------------------------------------------
run(
    'BOOL REJECT: patient_opportunities.vob_submitted_flag = 2',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000903', 'CNT-000241', '2026-06-10T09:15:00', 2, NULL, NULL, 'Private Pay', "
    "'Not Financially Cleared', 'Open', 'Organic', NULL, NULL, 'Possible')",
    (), 'reject',
)

run(
    'BOOL REJECT: acquisition_touches.platform_conversion = 2',
    "INSERT INTO acquisition_touches (touch_id, inquiry_id, touch_timestamp, channel, platform, campaign_id, "
    "campaign_name, ad_group, keyword, search_term, match_type, landing_page, geography, cost, "
    "platform_conversion, source_system, evidence_class) VALUES "
    "('TOUCH-000901', NULL, '2026-06-10T09:00:00', 'Organic', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, "
    "NULL, NULL, 2, 'Google Analytics', 'System-Observed')",
    (), 'reject',
)

run(
    'BOOL REJECT: outreach_reps.active_flag = -1',
    "INSERT INTO outreach_reps (outreach_rep_id, rep_name, active_flag) VALUES "
    "('REP-000901', 'Test Rep', -1)",
    (), 'reject',
)

# ---------------------------------------------------------------------------
# 2.4 Golden Thread valid insert (Contact -> Patient Opportunity -> Inquiry ->
#     EHR Episode -> Claim -> Claim Event), respecting the circular-reference
#     insertion order: opportunity is created with its originating IDs NULL,
#     the inquiry and touch are created against that opportunity, and only
#     then is the opportunity updated to point at its originating touch.
# ---------------------------------------------------------------------------
run(
    'GOLDEN THREAD 1/8: insert contact',
    "INSERT INTO contacts (contact_id, first_name, last_name, phone, email, date_of_birth, created_at) VALUES "
    "('CNT-000501', 'David', 'Nguyen', '555-020-4471', 'david.nguyen@example.test', NULL, '2026-06-12T08:00:00')",
    (), 'accept',
)

run(
    'GOLDEN THREAD 2/8: insert patient_opportunity (originating IDs NULL)',
    "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
    "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
    "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) VALUES "
    "('HRO-000501', 'CNT-000501', '2026-06-12T08:05:00', 1, 'Viable', 'Acme Health Plan', 'INN', "
    "'Financially Cleared', 'Admitted', 'Paid', NULL, NULL, 'Confirmed')",
    (), 'accept',
)

run(
    'GOLDEN THREAD 3/8: insert inquiry linked to opportunity and contact',
    "INSERT INTO inquiries (inquiry_id, opportunity_id, contact_id, inquiry_timestamp, contact_role, "
    "inquiry_method, arrival_channel, source_platform, tracking_number, call_duration_seconds, landing_page, "
    "match_confidence, source_system, evidence_class) VALUES "
    "('INQ-000501', 'HRO-000501', 'CNT-000501', '2026-06-12T08:02:00', 'Patient', 'Call', 'Paid Search', "
    "'Google Ads', '555-030-1188', 245, NULL, 'Confirmed', 'Call Tracking', 'System-Observed')",
    (), 'accept',
)

run(
    'GOLDEN THREAD 4/8: insert acquisition_touch linked to inquiry',
    "INSERT INTO acquisition_touches (touch_id, inquiry_id, touch_timestamp, channel, platform, campaign_id, "
    "campaign_name, ad_group, keyword, search_term, match_type, landing_page, geography, cost, "
    "platform_conversion, source_system, evidence_class) VALUES "
    "('TOUCH-000501', 'INQ-000501', '2026-06-12T08:01:30', 'Paid Search', 'Google Ads', 'CMP-4471', "
    "'Behavioral Health - Brand', 'Admissions', 'harbor ridge behavioral health', 'harbor ridge behavioral health', "
    "'Exact', 'https://harborridge.example.test/admissions', 'CA', 18.50, 1, 'Google Ads', 'System-Observed')",
    (), 'accept',
)

run(
    'GOLDEN THREAD 5/8: update opportunity.originating_touch_id to close the loop',
    "UPDATE patient_opportunities SET originating_touch_id = 'TOUCH-000501' WHERE opportunity_id = 'HRO-000501'",
    (), 'accept',
)

run(
    'GOLDEN THREAD 6/8: insert ehr_episode linked to opportunity',
    "INSERT INTO ehr_episodes (episode_id, opportunity_id, prior_episode_id, episode_relationship, "
    "admission_datetime, discharge_datetime, level_of_care, payer, authorization_start, authorization_end, "
    "discharge_disposition, source_system, evidence_class) VALUES "
    "('KIPU-000501', 'HRO-000501', NULL, 'Initial', '2026-06-13T14:00:00', NULL, 'Residential', "
    "'Acme Health Plan', '2026-06-13', '2026-06-27', NULL, 'EHR', 'System-Observed')",
    (), 'accept',
)

run(
    'GOLDEN THREAD 7/8: insert claim linked to episode',
    "INSERT INTO claims (claim_id, episode_id, service_start_date, service_end_date, payer, billed_amount, "
    "allowed_amount, patient_responsibility, claim_status, source_system, evidence_class) VALUES "
    "('CLM-000501', 'KIPU-000501', '2026-06-13', '2026-06-27', 'Acme Health Plan', 24500.00, 19600.00, 1200.00, "
    "'Paid', 'RCM', 'System-Observed')",
    (), 'accept',
)

run(
    'GOLDEN THREAD 8/8: insert claim_event linked to claim',
    "INSERT INTO claim_events (claim_event_id, claim_id, event_date, event_type, amount, source_system, "
    "evidence_class) VALUES "
    "('CEV-000501', 'CLM-000501', '2026-07-05', 'Insurance Payment', 19600.00, 'RCM / Financial Ledger', "
    "'System-Observed')",
    (), 'accept',
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
