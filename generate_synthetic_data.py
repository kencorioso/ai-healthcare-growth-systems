"""
Harbor Ridge V0.1 Synthetic Baseline Generator
================================================

Implements docs/harbor-ridge-synthetic-dataset-v0.1-generation-rules.md
against the frozen schema in schema.sql / docs/minimum-viable-data-dictionary.md.

This is the HEALTHY BASELINE generator only. No diagnostic scenario
(paid-search inquiry-quality deterioration, professional-outreach
deterioration, etc.) is embedded here. That is a later step.

Run:
    python generate_synthetic_data.py

Produces a clean harbor_ridge.db (existing file is removed first),
prints a generation summary/manifest to stdout (including the
45/20/15/10/5/5 marketing-budget benchmark comparison described in
Section 6 of the generation rules -- that allocation is a generator
validation benchmark, NOT a stored schema field), and exports every
table to CSV under data/csv_export/.

Every field generated below traces to a column that already exists in
schema.sql. No table, column, or value outside that frozen schema is
introduced. Where the generation rules leave an implementation detail
unspecified (e.g. exact dollar amounts, name pools, per-diem rates),
the choice is a generator assumption, not an industry benchmark or a
canonical Harbor Ridge fact, consistent with the design principle
stated at the top of the generation-rules document.
"""

import argparse
import calendar
import csv
import os
import random
import sqlite3
from datetime import date, datetime, timedelta

# ===========================================================================
# Configuration (Sections 1-2 of the generation rules)
# ===========================================================================

SEED = 20260825

# Scenario 1 (docs/harbor-ridge-scenario-1-specification.md) uses a
# separate, fixed seed. SCENARIO_1_SEED must never be used to generate or
# alter harbor_ridge.db -- that file, SEED, and generate_dataset() /
# build_database() called with the default db_path are the frozen
# baseline generation path and stay completely untouched by Scenario 1.
SCENARIO_1_SEED = 20260826

DB_PATH = "harbor_ridge.db"
SCHEMA_PATH = "schema.sql"
CSV_EXPORT_DIR = os.path.join("data", "csv_export")

SCENARIO1_DB_PATH = "harbor_ridge_scenario1.db"
SCENARIO1_CSV_EXPORT_DIR = os.path.join("data", "csv_export_scenario1")

OBSERVATION_DATE = date(2026, 8, 31)

# (year, month, label) -- the three operating months, Section 1
MONTHS = [
    (2026, 5, "May"),
    (2026, 6, "June"),
    (2026, 7, "July"),
]

# ===========================================================================
# Reference data pools (Section 18: everything must be fictional)
# ===========================================================================

FIRST_NAMES = [
    "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda",
    "David", "Barbara", "William", "Elizabeth", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Andrew", "Emily", "Paul", "Donna", "Joshua", "Michelle",
    "Kenneth", "Dorothy", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
    "Edward", "Deborah", "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Laura",
    "Jeffrey", "Sharon", "Ryan", "Cynthia",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
]

INN_PAYERS = [
    "Meridian Health Partners", "BlueHarbor Insurance", "Continental Care Alliance",
    "Summit Behavioral Network", "Pinecrest Health Plan", "Cornerstone Assurance",
]

OON_PAYERS = [
    "Vantage Point Insurance", "Liberty Crest Health", "Redwood Mutual",
    "National Trust Health Plan", "Harborline Assurance", "Keystone Wellness Plan",
]

PRACTICE_PREFIXES = [
    "Cedar Grove", "Lakeside", "Riverside Regional", "New Horizons", "Willow Creek",
    "Bright Path", "Northgate", "Evergreen", "Sunrise Valley", "Fair Meadow",
    "Silver Birch", "Harborview", "Crestline", "Golden Oak", "Blue Ridge",
]

PRACTICE_SUFFIXES = [
    "Psychiatry", "Family Therapy", "Behavioral Health Group", "Medical Center",
    "Wellness Clinic", "Counseling Associates", "Recovery Partners", "Health System",
    "Interventions", "Primary Care",
]

PROFESSIONAL_TYPES = [
    "Therapist", "Psychiatrist", "Hospital", "Interventionist",
    "Primary Care Physician", "Psychologist", "Social Worker",
]

REP_NAMES = ["Alicia Ferreira", "Marcus Webb", "Priya Anand", "Devon Castillo"]

STATES = ["CA", "TX", "FL", "NY", "AZ", "WA", "CO", "OR", "NV", "UT"]

GOOGLE_CAMPAIGNS = [
    ("CMP-1001", "Behavioral Health - Brand"),
    ("CMP-1002", "Behavioral Health - Non-Brand"),
    ("CMP-1003", "Detox Near Me - Geo"),
    ("CMP-1004", "Residential Treatment - Geo"),
    ("CMP-1005", "Family Crisis - Non-Brand"),
]
MSFT_CAMPAIGNS = [
    ("CMP-2001", "Behavioral Health - Brand (Bing)"),
    ("CMP-2002", "Residential Treatment - Geo (Bing)"),
]
META_CAMPAIGNS = [
    ("CMP-3001", "Family Support Awareness"),
    ("CMP-3002", "Recovery Journey - Lookalike"),
    ("CMP-3003", "Local Community Awareness"),
]
AD_GROUPS = ["Admissions", "Detox Programs", "Residential Programs", "Family Support"]
KEYWORDS = [
    "behavioral health treatment near me", "residential treatment center",
    "detox center near me", "family intervention help",
    "substance abuse treatment options", "inpatient mental health treatment",
]

DISCHARGE_DISPOSITIONS = [
    "Successful Completion - Stepped Down to Outpatient",
    "Completed Treatment - Discharged Home",
    "Left Against Medical Advice",
    "Administrative Discharge",
    "Completed Detox - Declined Residential",
]

# ===========================================================================
# ID generation (Section 19: deterministic sequential IDs)
# ===========================================================================


class IdGen:
    def __init__(self):
        self.counters = {}

    def next(self, prefix):
        n = self.counters.get(prefix, 0) + 1
        self.counters[prefix] = n
        return f"{prefix}-{n:06d}"


ids = IdGen()


def wchoice(rng, options, weights):
    return rng.choices(options, weights=weights, k=1)[0]


def iso_ts(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def iso_date(d):
    return d.strftime("%Y-%m-%d")


def random_datetime_in_month(rng, year, month, day_low=1, day_high=None):
    days_in_month = calendar.monthrange(year, month)[1]
    if day_high is None:
        day_high = days_in_month
    day = rng.randint(day_low, min(day_high, days_in_month))
    hour = rng.randint(7, 20)
    minute = rng.randint(0, 59)
    second = rng.randint(0, 59)
    return datetime(year, month, day, hour, minute, second)


def fake_contact(rng, role, created_at, is_patient_of_record=False):
    first = rng.choice(FIRST_NAMES)
    last = rng.choice(LAST_NAMES)
    contact_id = ids.next("CNT")
    phone = f"555-{rng.randint(0,999):03d}-{rng.randint(0,9999):04d}"
    email = f"{first.lower()}.{last.lower()}.{contact_id[-4:]}@example.test"
    dob = None
    if role == "Patient" or is_patient_of_record:
        # plausible adult age 18-65 as of created_at
        years_old = rng.randint(18, 65)
        dob_year = created_at.year - years_old
        dob = date(dob_year, rng.randint(1, 12), rng.randint(1, 28))
    return {
        "contact_id": contact_id,
        "first_name": first,
        "last_name": last,
        "phone": phone,
        "email": email,
        "date_of_birth": iso_date(dob) if dob else None,
        "created_at": iso_ts(created_at),
    }


# ===========================================================================
# Section 16: Professional referral baseline (reps + accounts)
# ===========================================================================


def gen_outreach_reps():
    rows = []
    for name in REP_NAMES:
        rows.append({
            "outreach_rep_id": ids.next("REP"),
            "rep_name": name,
            "active_flag": 1,
        })
    return rows


def gen_professional_accounts(rng, reps, n_accounts=40):
    rows = []
    weights = {}
    for i in range(n_accounts):
        prefix = rng.choice(PRACTICE_PREFIXES)
        suffix = rng.choice(PRACTICE_SUFFIXES)
        org_name = f"{prefix} {suffix}"
        prof_first = rng.choice(FIRST_NAMES)
        prof_last = rng.choice(LAST_NAMES)
        prof_type = rng.choice(PROFESSIONAL_TYPES)
        owner_rep = rng.choice(reps)
        # created before the operating period (Jan-Apr 2026)
        created = datetime(2026, rng.randint(1, 4), rng.randint(1, 28),
                            rng.randint(8, 17), rng.randint(0, 59), 0)
        acct_id = ids.next("PRO")
        rows.append({
            "professional_account_id": acct_id,
            "professional_name": f"{prof_first} {prof_last}",
            "organization_name": org_name,
            "professional_type": prof_type,
            "owner_rep_id": owner_rep["outreach_rep_id"],
            "created_at": iso_ts(created),
        })
        # referral-volume concentration weight: skewed but not excessive
        weights[acct_id] = rng.uniform(0.4, 3.0)
    return rows, weights


# ===========================================================================
# Sections 3, 4, 9, 10: funnel simulation and financial-field derivation
# ===========================================================================

FUNNEL_STAGES = [
    ("clinical_safety", 0.88),
    ("financial_verification", None),  # payer-dependent, see below
    ("readiness", 0.78),
    ("admission_decision", 0.90),
    ("scheduling_contact", 0.88),
    ("logistics", 0.88),
    ("arrival", 0.74),
    ("paperwork", 0.95),
]

# Section 4.1: similar conversion rates across payer types (narrow range),
# but not identical -- a generator assumption implementing "economically
# visible but not operationally pathological" payer differentiation.
FINANCIAL_VERIFICATION_PASS_RATE = {
    "INN": 0.70,
    "OON": 0.64,
    "Private Pay": 0.68,
}

AT_RISK_PROBABILITY = {
    "INN": 0.05,
    "OON": 0.18,
    "Private Pay": 0.0,
}

# Section 4: target admitted payer mix (55% INN / 35% OON / 10% Private Pay),
# enforced tightly at the completed-admission cohort via post-hoc rebalancing.
PAYER_TARGET_SHARE = {
    "INN": 0.55,
    "OON": 0.35,
    "Private Pay": 0.10,
}


def simulate_funnel(rng, payer_relationship, financial_verification_rates=None):
    """Sequential attrition per Section 3.2. Returns (stage_failed, admitted).

    financial_verification_rates optionally overrides the healthy-baseline
    FINANCIAL_VERIFICATION_PASS_RATE dict for the financial_verification
    stage only -- every other stage's pass rate is untouched. Used by
    Scenario 1 (docs/harbor-ridge-scenario-1-specification.md Section 6)
    to substitute the month's scenario-specific rates for affected
    attributable opportunities. Baseline call sites never pass this
    argument, so baseline behavior is byte-for-byte unchanged.
    """
    rates = financial_verification_rates if financial_verification_rates is not None else FINANCIAL_VERIFICATION_PASS_RATE
    for stage_name, base_rate in FUNNEL_STAGES:
        rate = base_rate if base_rate is not None else rates[payer_relationship]
        if rng.random() > rate:
            return stage_name, False
    return None, True


def derive_financial_fields(rng, payer_relationship, stage_failed, admitted):
    """
    Encode the funnel outcome into the observable fields the frozen schema
    actually has (Section 10): vob_submitted_flag, vob_outcome,
    admission_financial_status, admission_status.
    """
    reached_financial_stage = stage_failed != "clinical_safety"
    passed_financial_stage = admitted or stage_failed not in ("clinical_safety", "financial_verification")

    if not reached_financial_stage:
        # Never got clinically past the first gate -- no VOB was ever submitted.
        return {
            "vob_submitted_flag": 0,
            "vob_outcome": None,
            "admission_financial_status": "Not Financially Cleared",
            "admission_status": "Not Admitted",
            "stage_failed": stage_failed,
        }

    if not passed_financial_stage:
        # Reached financial verification but failed it.
        if payer_relationship == "Private Pay":
            vob_submitted_flag, vob_outcome = 0, None
        else:
            # Section 9: some opportunities terminate before VOB even though
            # they reached this stage.
            if rng.random() < 0.15:
                vob_submitted_flag, vob_outcome = 0, None
            else:
                vob_submitted_flag = 1
                if payer_relationship == "OON":
                    vob_outcome = wchoice(rng, ["Non-Viable", "Unable to Verify", "Pending"], [0.55, 0.30, 0.15])
                else:
                    vob_outcome = wchoice(rng, ["Non-Viable", "Unable to Verify", "Pending"], [0.65, 0.20, 0.15])
        return {
            "vob_submitted_flag": vob_submitted_flag,
            "vob_outcome": vob_outcome,
            "admission_financial_status": "Not Financially Cleared",
            "admission_status": "Not Admitted",
            "stage_failed": stage_failed,
        }

    # Passed financial verification (readiness stage or later, or admitted).
    if payer_relationship == "Private Pay":
        vob_submitted_flag, vob_outcome = 0, None
    else:
        vob_submitted_flag = 1
        vob_outcome = wchoice(rng, ["Viable", "Pending"], [0.90, 0.10])

    if admitted:
        admission_status = "Admitted"
        at_risk = payer_relationship != "Private Pay" and rng.random() < AT_RISK_PROBABILITY[payer_relationship]
        if at_risk:
            admission_financial_status = "At-Risk Admission"
            if vob_outcome == "Viable":
                vob_outcome = rng.choice(["Pending", "Unable to Verify"])
        else:
            admission_financial_status = "Financially Cleared"
    else:
        # Cleared financially, but lost at readiness/decision/scheduling/
        # logistics/arrival/paperwork -- Section 10: admissions competence
        # is about clinically-appropriate, financially-viable, ready
        # patients; downstream loss for other reasons is expected.
        admission_status = "Not Admitted"
        admission_financial_status = "Financially Cleared"

    return {
        "vob_submitted_flag": vob_submitted_flag,
        "vob_outcome": vob_outcome,
        "admission_financial_status": admission_financial_status,
        "admission_status": admission_status,
        "stage_failed": stage_failed,
    }


# ===========================================================================
# Sections 5, 7, 8: acquisition channel / method / initiator mix
# ===========================================================================

ARRIVAL_CHANNELS = ["Paid Search", "Organic", "Professional Referral", "Local", "Direct", "Other"]
ARRIVAL_CHANNEL_WEIGHTS = [0.35, 0.20, 0.20, 0.10, 0.10, 0.05]

CHANNEL_TO_INFLUENCE = {
    "Paid Search": "Paid",
    "Other": "Paid",          # Meta / paid social -- schema has no separate arrival_channel value
    "Organic": "Organic",
    "Local": "Organic",
    "Direct": "Direct",
    "Professional Referral": "Professional Referral",
}

# Per-channel call-vs-form skew, tuned so the overall mix lands near 60/40 (Section 7)
CHANNEL_CALL_PROB = {
    "Paid Search": 0.55,
    "Organic": 0.55,
    "Professional Referral": 0.90,
    "Local": 0.75,
    "Direct": 0.55,
    "Other": 0.55,
}

CONTACT_ROLES = ["Patient", "Loved One", "Professional Referral Source"]
CONTACT_ROLE_WEIGHTS = [0.55, 0.40, 0.05]

N_INQUIRIES_PER_OPP = [1, 2, 3]
N_INQUIRIES_WEIGHTS = [0.81, 0.15, 0.04]


def pick_source_platform(rng, channel):
    if channel == "Paid Search":
        return wchoice(rng, ["Google Ads", "Microsoft Ads"], [0.90, 0.10])
    if channel == "Organic":
        return "Google Organic"
    if channel == "Local":
        return "GBP"
    if channel == "Other":
        return "Meta"
    return None  # Direct, Professional Referral


def make_touch_for_first_inquiry(rng, channel, platform, inquiry_id, touch_dt, forced_campaign=None):
    """One acquisition_touch tied to an opportunity's first (originating) inquiry.

    forced_campaign optionally supplies a pre-chosen (campaign_id, campaign_name)
    tuple instead of letting this function pick one at random -- used by
    Scenario 1's build_opportunity_scenario1(), which must know the campaign
    BEFORE the funnel decision (Section 14 of the Scenario 1 spec), so the
    campaign used here must match the one eligibility was already checked
    against, not be re-rolled. Baseline call sites never pass this
    argument, so baseline behavior (including its rng.choice() call and
    consumption) is unchanged.
    """
    if channel not in ("Paid Search", "Organic", "Local", "Direct", "Other"):
        return None

    touch_channel = "Paid Social" if channel == "Other" else channel
    row = {
        "touch_id": ids.next("TOUCH"),
        "inquiry_id": inquiry_id,
        "touch_timestamp": iso_ts(touch_dt - timedelta(minutes=rng.randint(2, 90))),
        "channel": touch_channel,
        "platform": platform,
        "campaign_id": None,
        "campaign_name": None,
        "ad_group": None,
        "keyword": None,
        "search_term": None,
        "match_type": None,
        "landing_page": None,
        "geography": rng.choice(STATES),
        "cost": None,
        "platform_conversion": 1,
        "source_system": platform if platform else "Google Analytics",
        "evidence_class": "System-Observed",
    }

    if platform == "Google Ads":
        cmp_id, cmp_name = forced_campaign if forced_campaign is not None else rng.choice(GOOGLE_CAMPAIGNS)
        kw = rng.choice(KEYWORDS)
        row.update({
            "campaign_id": cmp_id, "campaign_name": cmp_name,
            "ad_group": rng.choice(AD_GROUPS), "keyword": kw, "search_term": kw,
            "match_type": rng.choice(["Exact", "Phrase", "Broad"]),
            "landing_page": "https://harborridge.example.test/admissions",
            "cost": round(rng.uniform(14, 45), 2),
            "source_system": "Google Ads",
        })
    elif platform == "Microsoft Ads":
        cmp_id, cmp_name = forced_campaign if forced_campaign is not None else rng.choice(MSFT_CAMPAIGNS)
        kw = rng.choice(KEYWORDS)
        row.update({
            "campaign_id": cmp_id, "campaign_name": cmp_name,
            "ad_group": rng.choice(AD_GROUPS), "keyword": kw, "search_term": kw,
            "match_type": rng.choice(["Exact", "Phrase", "Broad"]),
            "landing_page": "https://harborridge.example.test/admissions",
            "cost": round(rng.uniform(8, 32), 2),
            "source_system": "Microsoft Ads",
        })
    elif platform == "Meta":
        cmp_id, cmp_name = forced_campaign if forced_campaign is not None else rng.choice(META_CAMPAIGNS)
        row.update({
            "campaign_id": cmp_id, "campaign_name": cmp_name,
            "ad_group": rng.choice(["Family Support", "Community Awareness"]),
            "landing_page": "https://harborridge.example.test/family-support",
            "cost": round(rng.uniform(3, 15), 2),
            "source_system": "Meta",
        })
    elif channel == "Organic":
        row["landing_page"] = "https://harborridge.example.test/treatment-programs"
    elif channel == "Local":
        row["landing_page"] = "https://harborridge.example.test/contact"
        row["source_system"] = "GBP"
    else:  # Direct
        row["landing_page"] = "https://harborridge.example.test/"
        row["source_system"] = "Direct / Analytics"

    return row


NON_CONVERTING_MULTIPLIER = {
    "Google Ads": 4,
    "Microsoft Ads": 3,
    "Meta": 5,
    "Organic": 2,
}


def make_non_converting_touches(rng, year, month, platform_key, count):
    """Extra impression/click-only touches (Section 6 spend benchmark realism)."""
    rows = []
    for _ in range(count):
        touch_dt = random_datetime_in_month(rng, year, month)
        if platform_key == "Google Ads":
            cmp_id, cmp_name = rng.choice(GOOGLE_CAMPAIGNS)
            kw = rng.choice(KEYWORDS)
            rows.append({
                "touch_id": ids.next("TOUCH"), "inquiry_id": None,
                "touch_timestamp": iso_ts(touch_dt), "channel": "Paid Search", "platform": "Google Ads",
                "campaign_id": cmp_id, "campaign_name": cmp_name, "ad_group": rng.choice(AD_GROUPS),
                "keyword": kw, "search_term": kw, "match_type": rng.choice(["Exact", "Phrase", "Broad"]),
                "landing_page": "https://harborridge.example.test/admissions", "geography": rng.choice(STATES),
                "cost": round(rng.uniform(14, 45), 2), "platform_conversion": 0,
                "source_system": "Google Ads", "evidence_class": "System-Observed",
            })
        elif platform_key == "Microsoft Ads":
            cmp_id, cmp_name = rng.choice(MSFT_CAMPAIGNS)
            kw = rng.choice(KEYWORDS)
            rows.append({
                "touch_id": ids.next("TOUCH"), "inquiry_id": None,
                "touch_timestamp": iso_ts(touch_dt), "channel": "Paid Search", "platform": "Microsoft Ads",
                "campaign_id": cmp_id, "campaign_name": cmp_name, "ad_group": rng.choice(AD_GROUPS),
                "keyword": kw, "search_term": kw, "match_type": rng.choice(["Exact", "Phrase", "Broad"]),
                "landing_page": "https://harborridge.example.test/admissions", "geography": rng.choice(STATES),
                "cost": round(rng.uniform(8, 32), 2), "platform_conversion": 0,
                "source_system": "Microsoft Ads", "evidence_class": "System-Observed",
            })
        elif platform_key == "Meta":
            cmp_id, cmp_name = rng.choice(META_CAMPAIGNS)
            rows.append({
                "touch_id": ids.next("TOUCH"), "inquiry_id": None,
                "touch_timestamp": iso_ts(touch_dt), "channel": "Paid Social", "platform": "Meta",
                "campaign_id": cmp_id, "campaign_name": cmp_name,
                "ad_group": rng.choice(["Family Support", "Community Awareness"]),
                "keyword": None, "search_term": None, "match_type": None,
                "landing_page": "https://harborridge.example.test/family-support",
                "geography": rng.choice(STATES), "cost": round(rng.uniform(3, 15), 2),
                "platform_conversion": 0, "source_system": "Meta", "evidence_class": "System-Observed",
            })
        else:  # Organic
            rows.append({
                "touch_id": ids.next("TOUCH"), "inquiry_id": None,
                "touch_timestamp": iso_ts(touch_dt), "channel": "Organic", "platform": "Google Organic",
                "campaign_id": None, "campaign_name": None, "ad_group": None, "keyword": None,
                "search_term": None, "match_type": None,
                "landing_page": "https://harborridge.example.test/treatment-programs",
                "geography": rng.choice(STATES), "cost": None, "platform_conversion": 0,
                "source_system": "Google Analytics", "evidence_class": "System-Observed",
            })
    return rows


# ===========================================================================
# Opportunity + inquiry + touch/referral assembly (one opportunity at a time)
# ===========================================================================


def build_opportunity(rng, year, month, professional_accounts_by_id, account_weights):
    payer_relationship = wchoice(rng, ["INN", "OON", "Private Pay"], [0.55, 0.35, 0.10])
    payer = None
    if payer_relationship == "INN":
        payer = rng.choice(INN_PAYERS)
    elif payer_relationship == "OON":
        payer = rng.choice(OON_PAYERS)

    stage_failed, admitted = simulate_funnel(rng, payer_relationship)
    fin_fields = derive_financial_fields(rng, payer_relationship, stage_failed, admitted)

    channel = wchoice(rng, ARRIVAL_CHANNELS, ARRIVAL_CHANNEL_WEIGHTS)
    platform = pick_source_platform(rng, channel)
    n_inquiries = wchoice(rng, N_INQUIRIES_PER_OPP, N_INQUIRIES_WEIGHTS)

    opp_id = ids.next("HRO")

    contacts = []
    inquiries = []
    first_inquiry_dt = None
    patient_contact_id = None

    # Leave headroom so a second/third inquiry (up to +3 days later) never
    # spills into the following month. Opportunities the funnel has already
    # determined will admit get a tighter buffer still: gen_episodes_for_
    # admitted_opportunity() below adds up to a 15-day admission delay on
    # top of created_at, and Section 1's operating window closes July 31 --
    # so an admitted opportunity's creation day must leave room for that
    # full delay, not just the 3-day multi-inquiry offset.
    days_in_month = calendar.monthrange(year, month)[1]
    if admitted:
        day_high = max(days_in_month - 15, 1)
    else:
        day_high = days_in_month - 3
    base_dt = random_datetime_in_month(rng, year, month, day_high=day_high)

    for i in range(n_inquiries):
        role = wchoice(rng, CONTACT_ROLES, CONTACT_ROLE_WEIGHTS)
        if i == 0:
            inq_dt = base_dt
        else:
            inq_dt = base_dt + timedelta(days=rng.randint(0, 3), hours=rng.randint(0, 6))
        contact = fake_contact(rng, role, inq_dt, is_patient_of_record=(role == "Patient"))
        contacts.append(contact)

        if role == "Patient" and patient_contact_id is None:
            patient_contact_id = contact["contact_id"]

        is_call = rng.random() < CHANNEL_CALL_PROB[channel]
        inquiry_method = "Call" if is_call else "Web Form"

        match_confidence = wchoice(rng, ["Confirmed", "Probable", "Possible"], [0.90, 0.07, 0.03])

        if channel == "Professional Referral":
            source_system = "CRM"
            evidence_class = "Human-Entered"
        elif is_call:
            source_system = "Call Tracking"
            evidence_class = "System-Observed"
        else:
            source_system = "Web Form"
            evidence_class = "System-Observed"

        inquiry_id = ids.next("INQ")
        inquiries.append({
            "inquiry_id": inquiry_id,
            "opportunity_id": opp_id,
            "contact_id": contact["contact_id"],
            "inquiry_timestamp": iso_ts(inq_dt),
            "contact_role": role,
            "inquiry_method": inquiry_method,
            "arrival_channel": channel,
            "source_platform": platform if channel != "Professional Referral" else None,
            "tracking_number": (f"555-{rng.randint(0,999):03d}-{rng.randint(0,9999):04d}" if is_call else None),
            "call_duration_seconds": (rng.randint(90, 900) if is_call else None),
            "landing_page": (None if is_call else "https://harborridge.example.test/contact"),
            "match_confidence": match_confidence,
            "source_system": source_system,
            "evidence_class": evidence_class,
        })
        if i == 0:
            first_inquiry_dt = inq_dt
            first_inquiry_id = inquiry_id
            first_match_confidence = match_confidence

    if patient_contact_id is None:
        # No inquiry in this opportunity was made by the patient themselves
        # (e.g. Mom -> Dad only). patient_contact_id must still represent
        # "the contact believed to be the prospective patient" (Dictionary
        # Section 4) -- it must never point at a Loved One or Professional
        # Referral Source contact. Create a separate synthetic Patient
        # contact who did not personally place an inquiry.
        patient_contact = fake_contact(rng, "Patient", first_inquiry_dt, is_patient_of_record=True)
        contacts.append(patient_contact)
        patient_contact_id = patient_contact["contact_id"]

    touch = None
    referral = None
    originating_touch_id = None
    originating_referral_id = None
    attribution_confidence = first_match_confidence

    if channel == "Professional Referral":
        account_id = wchoice(rng, list(professional_accounts_by_id.keys()),
                              [account_weights[a] for a in professional_accounts_by_id.keys()])
        ref_confidence = wchoice(rng, ["Confirmed", "Probable", "Possible"], [0.75, 0.20, 0.05])
        referral = {
            "referral_id": ids.next("REF"),
            "professional_account_id": account_id,
            "opportunity_id": opp_id,
            "referral_timestamp": iso_ts(first_inquiry_dt - timedelta(hours=rng.randint(1, 48))),
            "referral_channel": rng.choice(["Call", "Email/Text Coordination", "Patient Told to Call", "Other"]),
            "source_system": "CRM",
            "evidence_class": wchoice(rng, ["System-Observed", "Human-Entered"], [0.3, 0.7]),
            "attribution_confidence": ref_confidence,
        }
        originating_referral_id = referral["referral_id"]
        attribution_confidence = ref_confidence
    else:
        touch = make_touch_for_first_inquiry(rng, channel, platform, first_inquiry_id, first_inquiry_dt)
        if touch is not None:
            originating_touch_id = touch["touch_id"]

    opportunity = {
        "opportunity_id": opp_id,
        "patient_contact_id": patient_contact_id,
        "created_at": iso_ts(first_inquiry_dt),
        "vob_submitted_flag": fin_fields["vob_submitted_flag"],
        "vob_outcome": fin_fields["vob_outcome"],
        "payer": payer,
        "payer_relationship": payer_relationship,
        "admission_financial_status": fin_fields["admission_financial_status"],
        "admission_status": fin_fields["admission_status"],
        "originating_influence_type": CHANNEL_TO_INFLUENCE[channel],
        "originating_touch_id": originating_touch_id,      # applied via UPDATE, not INSERT
        "originating_referral_id": originating_referral_id,  # applied via UPDATE, not INSERT
        "attribution_confidence": attribution_confidence,
        # internal bookkeeping, not schema columns:
        "_admitted": admitted,
        "_created_dt": first_inquiry_dt,
        "_month": (year, month),
    }
    return opportunity, contacts, inquiries, touch, referral


def maybe_reopen_late_july(rng, opportunity):
    """A late-created opportunity that lost may genuinely still be 'Open' at
    the observation date rather than firmly 'Not Admitted'. Small, realistic
    minority; does not touch admitted opportunities."""
    year, month = opportunity["_month"]
    if (year, month) != (2026, 7):
        return
    created = opportunity["_created_dt"]
    days_in_month = calendar.monthrange(year, month)[1]
    if created.day < days_in_month - 6:
        return
    if opportunity["admission_status"] == "Not Admitted" and rng.random() < 0.35:
        opportunity["admission_status"] = "Open"
        if opportunity["vob_submitted_flag"] == 1 and opportunity["vob_outcome"] not in (None, "Pending"):
            opportunity["vob_outcome"] = "Pending"


# ===========================================================================
# Scenario 1: Paid-Search Inquiry-Quality Deterioration
# docs/harbor-ridge-scenario-1-specification.md
#
# Everything in this section is additive: build_opportunity() above and
# generate_dataset()/build_database() called with their default arguments
# are never called by Scenario 1 code, and are not modified by it.
# ===========================================================================

# Section 2/3: the three Google Ads campaigns Scenario 1 degrades.
# CMP-1001 (Brand) and CMP-1004 (Residential Geo) are the unaffected
# internal comparison campaigns and must keep using healthy-baseline rates.
SCENARIO1_AFFECTED_CAMPAIGNS = {"CMP-1002", "CMP-1003", "CMP-1005"}

# Section 5: revised payer-mix parameters, for affected attributable
# opportunities only (Section 3's exact definition). Keyed by calendar
# month number to match the (year, month, label) tuples in MONTHS.
SCENARIO1_PAYER_MIX = {
    5: {"INN": 0.55, "OON": 0.35, "Private Pay": 0.10},   # May -- healthy control
    6: {"INN": 0.47, "OON": 0.43, "Private Pay": 0.10},   # June -- emerging deterioration
    7: {"INN": 0.35, "OON": 0.55, "Private Pay": 0.10},   # July -- established deterioration
}

# Section 6: revised financial-verification pass rates, for affected
# attributable opportunities only. Every other funnel stage (Section 7)
# keeps its healthy-baseline pass rate untouched.
SCENARIO1_FINANCIAL_VERIFICATION = {
    5: {"INN": 0.70, "OON": 0.64, "Private Pay": 0.68},
    6: {"INN": 0.60, "OON": 0.48, "Private Pay": 0.62},
    7: {"INN": 0.45, "OON": 0.22, "Private Pay": 0.50},
}

# Section 10: modest cost inflation applied to affected-campaign
# acquisition_touches.cost only.
SCENARIO1_COST_MULTIPLIER = {5: 1.00, 6: 1.05, 7: 1.10}

# Section 13: opportunities that are NOT Scenario-1-affected must keep
# using healthy-baseline rates exactly. This is the same {INN: 0.55,
# OON: 0.35, Private Pay: 0.10} weighting already inline as a literal in
# build_opportunity() above -- named here only so
# build_opportunity_scenario1() can choose between two tables; the
# original build_opportunity() literal is untouched.
SCENARIO1_BASELINE_PAYER_MIX = {"INN": 0.55, "OON": 0.35, "Private Pay": 0.10}


def build_opportunity_scenario1(rng, year, month, accounts_by_id, account_weights):
    """
    Scenario-1-aware opportunity construction. Mirrors build_opportunity()
    but reorders its steps per Section 14 of the Scenario 1 spec:

        Channel -> Platform -> Campaign -> Month -> Scenario eligibility
        -> Scenario-specific payer mix -> Scenario-specific financial-
        verification pass rate -> Funnel decision -> Admission status

    Scenario eligibility (Section 3's exact definition: originating touch
    platform = 'Google Ads' AND campaign_id in the Scenario 1 affected set)
    is therefore known BEFORE payer_relationship and the funnel outcome are
    decided, so no opportunity is ever admitted and then "un-admitted" --
    the funnel decision made here is final.

    Every other mechanic -- the other seven funnel stages, AT_RISK_
    PROBABILITY, VOB-outcome flavor, contact/inquiry generation, identity-
    resolution weights, call-vs-form mix -- reuses the exact same shared
    functions and constants the healthy baseline uses, unchanged.
    """
    # Channel -> Platform -> Campaign
    channel = wchoice(rng, ARRIVAL_CHANNELS, ARRIVAL_CHANNEL_WEIGHTS)
    platform = pick_source_platform(rng, channel)
    campaign = None
    if platform == "Google Ads":
        campaign = rng.choice(GOOGLE_CAMPAIGNS)
    elif platform == "Microsoft Ads":
        campaign = rng.choice(MSFT_CAMPAIGNS)
    elif platform == "Meta":
        campaign = rng.choice(META_CAMPAIGNS)

    # Month is the `month` parameter already. Scenario eligibility:
    is_affected = platform == "Google Ads" and campaign is not None and campaign[0] in SCENARIO1_AFFECTED_CAMPAIGNS

    # Scenario-specific (or healthy-baseline) payer mix and financial-
    # verification pass rate.
    if is_affected:
        payer_mix = SCENARIO1_PAYER_MIX[month]
        fin_verification_rates = SCENARIO1_FINANCIAL_VERIFICATION[month]
    else:
        payer_mix = SCENARIO1_BASELINE_PAYER_MIX
        fin_verification_rates = FINANCIAL_VERIFICATION_PASS_RATE

    payer_relationship = wchoice(rng, list(payer_mix.keys()), list(payer_mix.values()))
    payer = None
    if payer_relationship == "INN":
        payer = rng.choice(INN_PAYERS)
    elif payer_relationship == "OON":
        payer = rng.choice(OON_PAYERS)

    # Funnel decision -> admission status. simulate_funnel()/derive_
    # financial_fields() are the exact same functions the healthy baseline
    # calls; only the financial-verification rate table differs here.
    stage_failed, admitted = simulate_funnel(rng, payer_relationship, financial_verification_rates=fin_verification_rates)
    fin_fields = derive_financial_fields(rng, payer_relationship, stage_failed, admitted)

    n_inquiries = wchoice(rng, N_INQUIRIES_PER_OPP, N_INQUIRIES_WEIGHTS)
    opp_id = ids.next("HRO")

    contacts = []
    inquiries = []
    first_inquiry_dt = None
    patient_contact_id = None

    days_in_month = calendar.monthrange(year, month)[1]
    if admitted:
        day_high = max(days_in_month - 15, 1)
    else:
        day_high = days_in_month - 3
    base_dt = random_datetime_in_month(rng, year, month, day_high=day_high)

    for i in range(n_inquiries):
        role = wchoice(rng, CONTACT_ROLES, CONTACT_ROLE_WEIGHTS)
        if i == 0:
            inq_dt = base_dt
        else:
            inq_dt = base_dt + timedelta(days=rng.randint(0, 3), hours=rng.randint(0, 6))
        contact = fake_contact(rng, role, inq_dt, is_patient_of_record=(role == "Patient"))
        contacts.append(contact)

        if role == "Patient" and patient_contact_id is None:
            patient_contact_id = contact["contact_id"]

        is_call = rng.random() < CHANNEL_CALL_PROB[channel]
        inquiry_method = "Call" if is_call else "Web Form"

        match_confidence = wchoice(rng, ["Confirmed", "Probable", "Possible"], [0.90, 0.07, 0.03])

        if channel == "Professional Referral":
            source_system = "CRM"
            evidence_class = "Human-Entered"
        elif is_call:
            source_system = "Call Tracking"
            evidence_class = "System-Observed"
        else:
            source_system = "Web Form"
            evidence_class = "System-Observed"

        inquiry_id = ids.next("INQ")
        inquiries.append({
            "inquiry_id": inquiry_id,
            "opportunity_id": opp_id,
            "contact_id": contact["contact_id"],
            "inquiry_timestamp": iso_ts(inq_dt),
            "contact_role": role,
            "inquiry_method": inquiry_method,
            "arrival_channel": channel,
            "source_platform": platform if channel != "Professional Referral" else None,
            "tracking_number": (f"555-{rng.randint(0,999):03d}-{rng.randint(0,9999):04d}" if is_call else None),
            "call_duration_seconds": (rng.randint(90, 900) if is_call else None),
            "landing_page": (None if is_call else "https://harborridge.example.test/contact"),
            "match_confidence": match_confidence,
            "source_system": source_system,
            "evidence_class": evidence_class,
        })
        if i == 0:
            first_inquiry_dt = inq_dt
            first_inquiry_id = inquiry_id
            first_match_confidence = match_confidence

    if patient_contact_id is None:
        patient_contact = fake_contact(rng, "Patient", first_inquiry_dt, is_patient_of_record=True)
        contacts.append(patient_contact)
        patient_contact_id = patient_contact["contact_id"]

    touch = None
    referral = None
    originating_touch_id = None
    originating_referral_id = None
    attribution_confidence = first_match_confidence

    if channel == "Professional Referral":
        account_id = wchoice(rng, list(accounts_by_id.keys()),
                              [account_weights[a] for a in accounts_by_id.keys()])
        ref_confidence = wchoice(rng, ["Confirmed", "Probable", "Possible"], [0.75, 0.20, 0.05])
        referral = {
            "referral_id": ids.next("REF"),
            "professional_account_id": account_id,
            "opportunity_id": opp_id,
            "referral_timestamp": iso_ts(first_inquiry_dt - timedelta(hours=rng.randint(1, 48))),
            "referral_channel": rng.choice(["Call", "Email/Text Coordination", "Patient Told to Call", "Other"]),
            "source_system": "CRM",
            "evidence_class": wchoice(rng, ["System-Observed", "Human-Entered"], [0.3, 0.7]),
            "attribution_confidence": ref_confidence,
        }
        originating_referral_id = referral["referral_id"]
        attribution_confidence = ref_confidence
    else:
        touch = make_touch_for_first_inquiry(rng, channel, platform, first_inquiry_id, first_inquiry_dt,
                                              forced_campaign=campaign)
        if touch is not None:
            originating_touch_id = touch["touch_id"]
            # Section 10: cost multiplier on affected-campaign touch cost.
            if is_affected and touch["cost"] is not None:
                touch["cost"] = round(touch["cost"] * SCENARIO1_COST_MULTIPLIER[month], 2)

    opportunity = {
        "opportunity_id": opp_id,
        "patient_contact_id": patient_contact_id,
        "created_at": iso_ts(first_inquiry_dt),
        "vob_submitted_flag": fin_fields["vob_submitted_flag"],
        "vob_outcome": fin_fields["vob_outcome"],
        "payer": payer,
        "payer_relationship": payer_relationship,
        "admission_financial_status": fin_fields["admission_financial_status"],
        "admission_status": fin_fields["admission_status"],
        "originating_influence_type": CHANNEL_TO_INFLUENCE[channel],
        "originating_touch_id": originating_touch_id,      # applied via UPDATE, not INSERT
        "originating_referral_id": originating_referral_id,  # applied via UPDATE, not INSERT
        "attribution_confidence": attribution_confidence,
        # internal bookkeeping, not schema columns:
        "_admitted": admitted,
        "_created_dt": first_inquiry_dt,
        "_month": (year, month),
        "_scenario1_affected": is_affected,
    }
    return opportunity, contacts, inquiries, touch, referral


# ===========================================================================
# Section 16: outreach activities + unlinked referrals
# ===========================================================================


def gen_outreach_activities(rng, professional_accounts, reps):
    rows = []
    rep_ids = [r["outreach_rep_id"] for r in reps]
    for acct in professional_accounts:
        n_activities = rng.randint(3, 10)
        for _ in range(n_activities):
            year, month, _ = rng.choice(MONTHS)
            act_dt = random_datetime_in_month(rng, year, month)
            activity_type = rng.choice(["Call", "Email", "Meeting", "Lunch", "Presentation", "Tour"])
            direction = wchoice(rng, ["Outbound", "Inbound"], [0.70, 0.30])
            reciprocated = 1 if rng.random() < 0.70 else 0
            evidence_class = "System-Observed" if activity_type == "Email" else "Human-Entered"
            rows.append({
                "activity_id": ids.next("ACT"),
                "professional_account_id": acct["professional_account_id"],
                "outreach_rep_id": acct["owner_rep_id"] if rng.random() < 0.8 else rng.choice(rep_ids),
                "activity_timestamp": iso_ts(act_dt),
                "activity_type": activity_type,
                "direction": direction,
                "reciprocated_flag": reciprocated,
                "evidence_class": evidence_class,
            })
    return rows


def gen_unlinked_referrals(rng, professional_accounts_by_id, account_weights, n_linked_referrals):
    """A modest share of referral events that never resolve to a captured
    Patient Opportunity (Section 9 dictionary note: opportunity_id is
    nullable to represent this without an invalid FK)."""
    n_unlinked = round(0.12 * n_linked_referrals)
    rows = []
    for _ in range(n_unlinked):
        year, month, _ = rng.choice(MONTHS)
        ref_dt = random_datetime_in_month(rng, year, month)
        account_id = wchoice(rng, list(professional_accounts_by_id.keys()),
                              [account_weights[a] for a in professional_accounts_by_id.keys()])
        rows.append({
            "referral_id": ids.next("REF"),
            "professional_account_id": account_id,
            "opportunity_id": None,
            "referral_timestamp": iso_ts(ref_dt),
            "referral_channel": rng.choice(["Call", "Email/Text Coordination", "Patient Told to Call", "Other"]),
            "source_system": "CRM",
            "evidence_class": wchoice(rng, ["System-Observed", "Human-Entered"], [0.3, 0.7]),
            "attribution_confidence": wchoice(rng, ["Possible", "Unmatched", "Probable"], [0.55, 0.30, 0.15]),
        })
    return rows


# ===========================================================================
# Sections 11-15: EHR episodes, claims, claim events
# ===========================================================================

DETOX_PER_DIEM_RANGE = (1200, 1600)
RESIDENTIAL_PER_DIEM_RANGE = (650, 950)


def sample_transition_gap(rng):
    """Natural bed-transfer timing variation for a Detox -> Residential LOC
    Transition (Sections 11-12): most transfers happen same-day, a few
    hours after Detox discharge; some occur later the same day or into the
    next morning; a small share wait overnight or, occasionally, a couple
    of days for a Residential bed to open up. Never zero -- an LOC
    Transition's admission_datetime should never be identical to the prior
    episode's discharge_datetime by default."""
    bucket = wchoice(
        rng,
        ["same_day_soon", "same_day_later", "overnight", "bed_wait"],
        [0.55, 0.25, 0.13, 0.07],
    )
    if bucket == "same_day_soon":
        return timedelta(hours=rng.uniform(0.5, 6))
    if bucket == "same_day_later":
        return timedelta(hours=rng.uniform(6, 14))
    if bucket == "overnight":
        return timedelta(hours=rng.uniform(14, 30))
    return timedelta(hours=rng.uniform(30, 96))  # occasional multi-day bed wait


def gen_episodes_for_admitted_opportunity(rng, opportunity):
    episodes = []
    admission_dt = opportunity["_created_dt"] + timedelta(days=rng.randint(3, 15), hours=rng.randint(0, 10))
    # Safety net: build_opportunity() already bounds created_at for
    # opportunities the funnel simulation originally determines will admit,
    # so this delay stays within the opportunity's own creation month for
    # the large majority of cases. This clamp only catches the rarer case
    # where an opportunity was promoted to Admitted post-hoc (the monthly
    # admit-count / payer-mix rebalancing in generate_dataset()) after
    # having been built with the wider, non-admitted date buffer.
    #
    # Clamping to the END OF THE OPPORTUNITY'S OWN CREATION MONTH (not a
    # fixed July 31 constant) does double duty: it guarantees every Initial
    # episode still admits within the May-July operating window (Section
    # 1), AND it keeps each admitted opportunity's admission_datetime in
    # the same calendar month it was created in -- which the monthly
    # admit-count / payer-mix rebalancing above assumes when it targets
    # 38-42 admits per created_at-month cohort (Section 3). Without this,
    # a promoted opportunity created near month-end could admit into the
    # following month, silently pulling ehr_episodes.admission_datetime
    # counts out of the band the rebalancing thinks it already hit.
    year, month = opportunity["_month"]
    days_in_month = calendar.monthrange(year, month)[1]
    month_close = datetime(year, month, days_in_month, 23, 59, 59)
    if admission_dt > month_close:
        admission_dt = month_close
    payer_text = opportunity["payer"] if opportunity["payer"] else "Private Pay"

    starts_detox = rng.random() < 0.50

    def close_episode(admission_dt, los_days):
        planned_discharge = admission_dt + timedelta(days=los_days)
        if planned_discharge.date() <= OBSERVATION_DATE:
            return planned_discharge
        return None

    if starts_detox:
        los = rng.randint(3, 7)
        discharge_dt = close_episode(admission_dt, los)
        ep1_id = ids.next("KIPU")
        auth_start = admission_dt.date()
        auth_end = (discharge_dt or (admission_dt + timedelta(days=los))).date()
        episodes.append({
            "episode_id": ep1_id, "opportunity_id": opportunity["opportunity_id"], "prior_episode_id": None,
            "episode_relationship": "Initial", "admission_datetime": iso_ts(admission_dt),
            "discharge_datetime": iso_ts(discharge_dt) if discharge_dt else None,
            "level_of_care": "Detox", "payer": payer_text,
            "authorization_start": iso_date(auth_start) if rng.random() < 0.9 else None,
            "authorization_end": iso_date(auth_end) if rng.random() < 0.9 else None,
            "discharge_disposition": (rng.choice(DISCHARGE_DISPOSITIONS) if discharge_dt else None),
            "source_system": "EHR", "evidence_class": "System-Observed",
            "_planned_end": admission_dt + timedelta(days=los),
        })
        transitions = rng.random() < 0.60
        if transitions:
            ep1_end = discharge_dt if discharge_dt else (admission_dt + timedelta(days=los))
            ep2_admission = ep1_end + sample_transition_gap(rng)
            los2 = rng.randint(14, 30)
            discharge_dt2 = close_episode(ep2_admission, los2)
            ep2_id = ids.next("KIPU")
            auth_start2 = ep2_admission.date()
            auth_end2 = (discharge_dt2 or (ep2_admission + timedelta(days=los2))).date()
            episodes.append({
                "episode_id": ep2_id, "opportunity_id": opportunity["opportunity_id"], "prior_episode_id": ep1_id,
                "episode_relationship": "LOC Transition", "admission_datetime": iso_ts(ep2_admission),
                "discharge_datetime": iso_ts(discharge_dt2) if discharge_dt2 else None,
                "level_of_care": "Residential", "payer": payer_text,
                "authorization_start": iso_date(auth_start2) if rng.random() < 0.9 else None,
                "authorization_end": iso_date(auth_end2) if rng.random() < 0.9 else None,
                "discharge_disposition": (rng.choice(DISCHARGE_DISPOSITIONS) if discharge_dt2 else None),
                "source_system": "EHR", "evidence_class": "System-Observed",
                "_planned_end": ep2_admission + timedelta(days=los2),
            })
        else:
            episodes[0]["discharge_disposition"] = episodes[0]["discharge_disposition"] or "External Discharge / Transfer"
    else:
        los = rng.randint(14, 30)
        discharge_dt = close_episode(admission_dt, los)
        ep_id = ids.next("KIPU")
        auth_start = admission_dt.date()
        auth_end = (discharge_dt or (admission_dt + timedelta(days=los))).date()
        episodes.append({
            "episode_id": ep_id, "opportunity_id": opportunity["opportunity_id"], "prior_episode_id": None,
            "episode_relationship": "Initial", "admission_datetime": iso_ts(admission_dt),
            "discharge_datetime": iso_ts(discharge_dt) if discharge_dt else None,
            "level_of_care": "Residential", "payer": payer_text,
            "authorization_start": iso_date(auth_start) if rng.random() < 0.9 else None,
            "authorization_end": iso_date(auth_end) if rng.random() < 0.9 else None,
            "discharge_disposition": (rng.choice(DISCHARGE_DISPOSITIONS) if discharge_dt else None),
            "source_system": "EHR", "evidence_class": "System-Observed",
            "_planned_end": admission_dt + timedelta(days=los),
        })
    return episodes


def simulate_claim_lifecycle(rng, payer_relationship, billed_amount, service_end_date):
    """Returns (allowed_amount, patient_responsibility, claim_status, events)
    where events is a list of (event_type, event_date, amount)."""
    events = []

    if payer_relationship == "INN":
        allowed_amount = round(billed_amount * rng.uniform(0.72, 0.85), 2)
        patient_responsibility = round(allowed_amount * rng.uniform(0.03, 0.12), 2)
    elif payer_relationship == "OON":
        allowed_amount = round(billed_amount * rng.uniform(0.40, 0.65), 2)
        patient_responsibility = round(allowed_amount * rng.uniform(0.15, 0.35), 2)
    else:
        allowed_amount = None
        patient_responsibility = round(billed_amount * rng.uniform(0.85, 0.97), 2)

    if payer_relationship in ("INN", "OON"):
        submission_delay = rng.randint(2, 7)
        processing_delay = rng.randint(10, 25) if payer_relationship == "INN" else rng.randint(20, 45)
        decision_date = service_end_date + timedelta(days=submission_delay + processing_delay)
        denial_prob = 0.10 if payer_relationship == "INN" else 0.25

        if rng.random() < denial_prob:
            if decision_date <= OBSERVATION_DATE:
                events.append(("Denial", decision_date, None))
                appeal_date = decision_date + timedelta(days=rng.randint(10, 30))
                if appeal_date <= OBSERVATION_DATE:
                    events.append(("Appeal", appeal_date, None))
                    if rng.random() < 0.65:
                        payment_date = appeal_date + timedelta(days=rng.randint(10, 25))
                        if payment_date <= OBSERVATION_DATE:
                            events.append(("Insurance Payment", payment_date, round(allowed_amount * rng.uniform(0.9, 1.0), 2)))
                    else:
                        writeoff_date = appeal_date + timedelta(days=rng.randint(10, 20))
                        if writeoff_date <= OBSERVATION_DATE and rng.random() < 0.5:
                            events.append(("Write-Off", writeoff_date, round(allowed_amount * rng.uniform(0.5, 1.0), 2)))
        else:
            if decision_date <= OBSERVATION_DATE:
                pay_amount = round(allowed_amount * rng.uniform(0.92, 1.0), 2)
                events.append(("Insurance Payment", decision_date, pay_amount))
                if patient_responsibility and rng.random() < 0.70:
                    pp_date = decision_date + timedelta(days=rng.randint(5, 30))
                    if pp_date <= OBSERVATION_DATE:
                        events.append(("Patient Payment", pp_date, round(patient_responsibility * rng.uniform(0.6, 1.0), 2)))
                if rng.random() < 0.15:
                    adj_date = decision_date + timedelta(days=rng.randint(3, 10))
                    if adj_date <= OBSERVATION_DATE:
                        events.append(("Adjustment", adj_date, round(billed_amount * rng.uniform(0.01, 0.05), 2)))
    else:  # Private Pay -- shorter collection timing, no insurance events
        pay_date = service_end_date + timedelta(days=rng.randint(5, 20))
        if pay_date <= OBSERVATION_DATE:
            if rng.random() < 0.70:
                events.append(("Patient Payment", pay_date, patient_responsibility))
            else:
                part1 = round(patient_responsibility * rng.uniform(0.4, 0.6), 2)
                events.append(("Patient Payment", pay_date, part1))
                pay_date2 = pay_date + timedelta(days=rng.randint(10, 30))
                if pay_date2 <= OBSERVATION_DATE:
                    events.append(("Patient Payment", pay_date2, round(patient_responsibility - part1, 2)))
            if rng.random() < 0.08:
                wo_date = pay_date + timedelta(days=rng.randint(20, 35))
                if wo_date <= OBSERVATION_DATE:
                    events.append(("Write-Off", wo_date, round(patient_responsibility * rng.uniform(0.05, 0.15), 2)))

    # Derive claim_status from the resulting event set.
    event_types = [e[0] for e in events]
    if "Denial" in event_types and "Appeal" not in event_types:
        claim_status = "Denied"
    elif "Appeal" in event_types and "Insurance Payment" not in event_types:
        claim_status = "Appealed"
    elif "Insurance Payment" in event_types or (payer_relationship == "Private Pay" and "Patient Payment" in event_types):
        if "Patient Payment" in event_types or payer_relationship == "Private Pay" or "Write-Off" in event_types:
            claim_status = "Closed" if (payer_relationship == "Private Pay" or "Patient Payment" in event_types) else "Paid"
        else:
            claim_status = "Paid"
    else:
        days_since = (OBSERVATION_DATE - service_end_date).days
        claim_status = "Submitted" if days_since < 10 else "Pending"

    return allowed_amount, patient_responsibility, claim_status, events


def gen_claims_and_events_for_episode(rng, episode):
    admission_dt = datetime.fromisoformat(episode["admission_datetime"])
    if episode["discharge_datetime"]:
        discharge_dt = datetime.fromisoformat(episode["discharge_datetime"])
    else:
        planned_end = episode["_planned_end"]
        discharge_dt = min(planned_end, datetime.combine(OBSERVATION_DATE, admission_dt.time()))
        if discharge_dt < admission_dt:
            discharge_dt = admission_dt

    los_days = max((discharge_dt - admission_dt).days, 1)
    per_diem_range = DETOX_PER_DIEM_RANGE if episode["level_of_care"] == "Detox" else RESIDENTIAL_PER_DIEM_RANGE
    per_diem = rng.uniform(*per_diem_range)

    payer_relationship = "Private Pay" if episode["payer"] == "Private Pay" else (
        "OON" if episode["payer"] in OON_PAYERS else "INN"
    )

    claims = []
    claim_events = []

    two_claims = rng.random() < 0.15 and los_days >= 4
    if two_claims:
        split = max(los_days // 2, 1)
        periods = [(0, split), (split, los_days)]
    else:
        periods = [(0, los_days)]

    for period_start_day, period_end_day in periods:
        period_days = max(period_end_day - period_start_day, 1)
        service_start = (admission_dt + timedelta(days=period_start_day)).date()
        service_end = (admission_dt + timedelta(days=period_end_day)).date()
        billed_amount = round(per_diem * period_days * rng.uniform(0.92, 1.08), 2)

        allowed_amount, patient_responsibility, claim_status, events = simulate_claim_lifecycle(
            rng, payer_relationship, billed_amount, service_end
        )

        claim_id = ids.next("CLM")
        claims.append({
            "claim_id": claim_id, "episode_id": episode["episode_id"],
            "service_start_date": iso_date(service_start), "service_end_date": iso_date(service_end),
            "payer": episode["payer"], "billed_amount": billed_amount,
            "allowed_amount": allowed_amount, "patient_responsibility": patient_responsibility,
            "claim_status": claim_status, "source_system": "RCM", "evidence_class": "System-Observed",
        })
        for event_type, event_date, amount in events:
            claim_events.append({
                "claim_event_id": ids.next("CEV"), "claim_id": claim_id,
                "event_date": iso_date(event_date), "event_type": event_type, "amount": amount,
                "source_system": "RCM / Financial Ledger", "evidence_class": "System-Observed",
            })

    return claims, claim_events


# ===========================================================================
# Orchestration
# ===========================================================================


def select_demotion_candidates(rng, pool, k):
    """Pick k opportunities to demote from Admitted back to Not Admitted,
    preferring non-At-Risk ones first.

    Promotion (the mirror operation elsewhere in this rebalancing) can
    never create a new At-Risk Admission -- its candidate pool is always
    "Financially Cleared, Not Admitted" opportunities, since At-Risk only
    ever arises inside derive_financial_fields() for opportunities the
    funnel simulation itself admitted. That makes demotion a one-way
    valve on the At-Risk population: every demotion that happens to pick
    an At-Risk opportunity permanently drains it (converting it to
    Financially Cleared), with no corresponding mechanism to replenish it.
    Demoting non-At-Risk opportunities first whenever there are enough of
    them keeps the At-Risk share from being systematically thinned out by
    rebalancing churn beyond what AT_RISK_PROBABILITY itself produced.
    """
    non_at_risk = [o for o in pool if o["admission_financial_status"] != "At-Risk Admission"]
    at_risk = [o for o in pool if o["admission_financial_status"] == "At-Risk Admission"]
    if len(non_at_risk) >= k:
        return rng.sample(non_at_risk, k)
    return non_at_risk + rng.sample(at_risk, k - len(non_at_risk))


def generate_dataset():
    # ids is module-level global state (shared by every ID-emitting helper
    # via `ids.next(prefix)`). Reset it here so generate_dataset() is safely
    # re-callable within a single Python process -- e.g. back-to-back in a
    # reproducibility test -- and not just safely re-runnable as a fresh
    # `python generate_synthetic_data.py` subprocess. Without this reset, a
    # second in-process call would resume ID numbering where the first call
    # left off instead of restarting at 1, producing a different (though
    # equally valid) dataset from the same seed.
    ids.counters.clear()
    rng = random.Random(SEED)

    reps = gen_outreach_reps()
    accounts, account_weights = gen_professional_accounts(rng, reps)
    accounts_by_id = {a["professional_account_id"]: a for a in accounts}

    all_contacts, all_opportunities, all_inquiries = [], [], []
    all_touches, all_referrals = [], []

    monthly_opp_counts = {}

    for year, month, label in MONTHS:
        n_opportunities = 175 + rng.randint(-15, 15)  # Section 3: approx +-5-10%
        monthly_opp_counts[label] = n_opportunities
        linked_referrals_this_month = 0

        month_opportunities = []
        for _ in range(n_opportunities):
            opp, contacts, inquiries, touch, referral = build_opportunity(
                rng, year, month, accounts_by_id, account_weights
            )
            maybe_reopen_late_july(rng, opp)
            month_opportunities.append(opp)
            all_contacts.extend(contacts)
            all_inquiries.extend(inquiries)
            if touch is not None:
                all_touches.append(touch)
            if referral is not None:
                all_referrals.append(referral)
                linked_referrals_this_month += 1

        # Section 3: "Completed admissions should remain tighter: 38-42 per
        # month, centered on 40." The independent per-opportunity funnel
        # draws above have realistic binomial variance around ~23%, which is
        # wider than that band on its own. Reconcile the two by nudging the
        # month's admit count to a randomly chosen target within [38, 42]:
        # opportunities are promoted/demoted between "Admitted" and
        # "Financially Cleared, Not Admitted" (a state the funnel already
        # produces naturally for late-stage losses), so every adjustment
        # lands on an outcome the funnel logic already considers valid.
        target_admits = rng.randint(38, 42)
        currently_admitted = [o for o in month_opportunities if o["admission_status"] == "Admitted"]
        current_count = len(currently_admitted)
        if current_count > target_admits:
            to_demote = select_demotion_candidates(rng, currently_admitted, current_count - target_admits)
            for o in to_demote:
                o["admission_status"] = "Not Admitted"
                o["_admitted"] = False
                if o["admission_financial_status"] == "At-Risk Admission":
                    o["admission_financial_status"] = "Financially Cleared"
        elif current_count < target_admits:
            candidates = [
                o for o in month_opportunities
                if o["admission_status"] == "Not Admitted"
                and o["admission_financial_status"] in ("Financially Cleared", "At-Risk Admission")
            ]
            n_needed = min(target_admits - current_count, len(candidates))
            for o in rng.sample(candidates, n_needed):
                o["admission_status"] = "Admitted"
                o["_admitted"] = True

        # Section 4: enforce the 55/35/10 payer mix "most tightly at the
        # completed-admission cohort" (tolerance +-3pp over the full
        # 3-month cohort). Rebalance which opportunities occupy this
        # month's (now-fixed) admit count across payer_relationship,
        # again only moving opportunities between "Admitted" and
        # "Financially Cleared, Not Admitted" -- states the funnel
        # simulation already produces -- so total admits this month is
        # unchanged and no financial-status value is invented.
        admitted_now = [o for o in month_opportunities if o["admission_status"] == "Admitted"]
        total_admit_this_month = len(admitted_now)
        raw_targets = {p: PAYER_TARGET_SHARE[p] * total_admit_this_month for p in PAYER_TARGET_SHARE}
        desired = {p: int(raw_targets[p]) for p in PAYER_TARGET_SHARE}
        remainder = total_admit_this_month - sum(desired.values())
        for p, _ in sorted(raw_targets.items(), key=lambda kv: kv[1] - int(kv[1]), reverse=True)[:remainder]:
            desired[p] += 1

        current_by_payer = {p: [o for o in admitted_now if o["payer_relationship"] == p] for p in PAYER_TARGET_SHARE}
        for p in PAYER_TARGET_SHARE:
            cur_n = len(current_by_payer[p])
            want_n = desired[p]
            if cur_n > want_n:
                for o in select_demotion_candidates(rng, current_by_payer[p], cur_n - want_n):
                    o["admission_status"] = "Not Admitted"
                    o["_admitted"] = False
                    if o["admission_financial_status"] == "At-Risk Admission":
                        o["admission_financial_status"] = "Financially Cleared"
            elif cur_n < want_n:
                candidates = [
                    o for o in month_opportunities
                    if o["payer_relationship"] == p and o["admission_status"] == "Not Admitted"
                    and o["admission_financial_status"] in ("Financially Cleared", "At-Risk Admission")
                ]
                n_needed = min(want_n - cur_n, len(candidates))
                for o in rng.sample(candidates, n_needed):
                    o["admission_status"] = "Admitted"
                    o["_admitted"] = True

        all_opportunities.extend(month_opportunities)

        # Non-patient / duplicate contacts that never resolve to a legitimate
        # Patient Opportunity (Section 3.1, 5.1 of the data dictionary).
        n_orphans = max(round(n_opportunities * 0.03), 2)
        for _ in range(n_orphans):
            orphan_dt = random_datetime_in_month(rng, year, month)
            role = wchoice(rng, CONTACT_ROLES, CONTACT_ROLE_WEIGHTS)
            contact = fake_contact(rng, role, orphan_dt)
            all_contacts.append(contact)
            channel = wchoice(rng, ARRIVAL_CHANNELS, ARRIVAL_CHANNEL_WEIGHTS)
            platform = pick_source_platform(rng, channel)
            is_call = rng.random() < CHANNEL_CALL_PROB[channel]
            all_inquiries.append({
                "inquiry_id": ids.next("INQ"), "opportunity_id": None, "contact_id": contact["contact_id"],
                "inquiry_timestamp": iso_ts(orphan_dt), "contact_role": role,
                "inquiry_method": "Call" if is_call else "Web Form", "arrival_channel": channel,
                "source_platform": platform if channel != "Professional Referral" else None,
                "tracking_number": (f"555-{rng.randint(0,999):03d}-{rng.randint(0,9999):04d}" if is_call else None),
                "call_duration_seconds": (rng.randint(30, 300) if is_call else None),
                "landing_page": (None if is_call else "https://harborridge.example.test/contact"),
                "match_confidence": "Unmatched",
                "source_system": "Call Tracking" if is_call else "Web Form",
                "evidence_class": "System-Observed",
            })

        # Non-converting digital touches, for spend-benchmark realism (Section 6).
        n_google_conv = sum(1 for t in all_touches if t["platform"] == "Google Ads"
                             and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        n_msft_conv = sum(1 for t in all_touches if t["platform"] == "Microsoft Ads"
                           and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        n_meta_conv = sum(1 for t in all_touches if t["platform"] == "Meta"
                           and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        n_organic_conv = sum(1 for t in all_touches if t["platform"] == "Google Organic"
                              and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        all_touches.extend(make_non_converting_touches(rng, year, month, "Google Ads", n_google_conv * NON_CONVERTING_MULTIPLIER["Google Ads"]))
        all_touches.extend(make_non_converting_touches(rng, year, month, "Microsoft Ads", n_msft_conv * NON_CONVERTING_MULTIPLIER["Microsoft Ads"]))
        all_touches.extend(make_non_converting_touches(rng, year, month, "Meta", n_meta_conv * NON_CONVERTING_MULTIPLIER["Meta"]))
        all_touches.extend(make_non_converting_touches(rng, year, month, "Organic", n_organic_conv * NON_CONVERTING_MULTIPLIER["Organic"]))

        all_referrals.extend(gen_unlinked_referrals(rng, accounts_by_id, account_weights, linked_referrals_this_month))

    activities = gen_outreach_activities(rng, accounts, reps)

    all_episodes, all_claims, all_claim_events = [], [], []
    for opp in all_opportunities:
        if opp["admission_status"] == "Admitted":
            episodes = gen_episodes_for_admitted_opportunity(rng, opp)
            all_episodes.extend(episodes)
            for ep in episodes:
                claims, events = gen_claims_and_events_for_episode(rng, ep)
                all_claims.extend(claims)
                all_claim_events.extend(events)

    return {
        "reps": reps, "accounts": accounts, "contacts": all_contacts,
        "opportunities": all_opportunities, "inquiries": all_inquiries,
        "touches": all_touches, "referrals": all_referrals, "activities": activities,
        "episodes": all_episodes, "claims": all_claims, "claim_events": all_claim_events,
        "monthly_opp_counts": monthly_opp_counts,
    }


def generate_dataset_scenario1():
    """
    Scenario 1 orchestration (docs/harbor-ridge-scenario-1-specification.md).
    Parallels generate_dataset() -- same per-month structure (opportunity
    volume, orphan inquiries, non-converting touches, unlinked referrals,
    outreach activities, EHR/claims/claim-events generation, all via the
    exact same shared functions) -- but differs in two deliberate ways:

    1. Uses SCENARIO_1_SEED, never SEED, and builds opportunities via
       build_opportunity_scenario1() instead of build_opportunity(), so
       scenario eligibility and the scenario-specific payer-mix /
       financial-verification tables are applied BEFORE the funnel
       decision (Section 14).

    2. Deliberately SKIPS the healthy baseline's post-hoc admit-count
       (38-42/month) and payer-mix (55/35/10) rebalancing block. Section
       14 requires that "no patient ever needs to be 'un-admitted'" once
       the scenario-aware funnel decision is made, and the Scenario 1
       acceptance criteria (Section 16) are calibrated directly against
       the raw funnel-simulation math (Section 8's 22.8% / 18.5% / 11.0%
       figures) -- rebalancing the facility-wide total on top would both
       violate that "no un-admitting" requirement and distort the
       calibrated affected-campaign conversion rates the spec's math
       assumes are untouched after the funnel decision.

    generate_dataset() itself is never called here and is not modified by
    this function's existence.
    """
    ids.counters.clear()
    rng = random.Random(SCENARIO_1_SEED)

    reps = gen_outreach_reps()
    accounts, account_weights = gen_professional_accounts(rng, reps)
    accounts_by_id = {a["professional_account_id"]: a for a in accounts}

    all_contacts, all_opportunities, all_inquiries = [], [], []
    all_touches, all_referrals = [], []

    monthly_opp_counts = {}

    for year, month, label in MONTHS:
        n_opportunities = 175 + rng.randint(-15, 15)  # Section 3 baseline volume target, unaffected by Scenario 1
        monthly_opp_counts[label] = n_opportunities
        linked_referrals_this_month = 0

        month_opportunities = []
        for _ in range(n_opportunities):
            opp, contacts, inquiries, touch, referral = build_opportunity_scenario1(
                rng, year, month, accounts_by_id, account_weights
            )
            maybe_reopen_late_july(rng, opp)
            month_opportunities.append(opp)
            all_contacts.extend(contacts)
            all_inquiries.extend(inquiries)
            if touch is not None:
                all_touches.append(touch)
            if referral is not None:
                all_referrals.append(referral)
                linked_referrals_this_month += 1

        # No admit-count / payer-mix rebalancing here -- see docstring above.
        all_opportunities.extend(month_opportunities)

        # Non-patient / duplicate contacts that never resolve to a legitimate
        # Patient Opportunity (Section 3.1, 5.1 of the data dictionary) --
        # identical to the healthy baseline, unaffected by Scenario 1.
        n_orphans = max(round(n_opportunities * 0.03), 2)
        for _ in range(n_orphans):
            orphan_dt = random_datetime_in_month(rng, year, month)
            role = wchoice(rng, CONTACT_ROLES, CONTACT_ROLE_WEIGHTS)
            contact = fake_contact(rng, role, orphan_dt)
            all_contacts.append(contact)
            channel = wchoice(rng, ARRIVAL_CHANNELS, ARRIVAL_CHANNEL_WEIGHTS)
            platform = pick_source_platform(rng, channel)
            is_call = rng.random() < CHANNEL_CALL_PROB[channel]
            all_inquiries.append({
                "inquiry_id": ids.next("INQ"), "opportunity_id": None, "contact_id": contact["contact_id"],
                "inquiry_timestamp": iso_ts(orphan_dt), "contact_role": role,
                "inquiry_method": "Call" if is_call else "Web Form", "arrival_channel": channel,
                "source_platform": platform if channel != "Professional Referral" else None,
                "tracking_number": (f"555-{rng.randint(0,999):03d}-{rng.randint(0,9999):04d}" if is_call else None),
                "call_duration_seconds": (rng.randint(30, 300) if is_call else None),
                "landing_page": (None if is_call else "https://harborridge.example.test/contact"),
                "match_confidence": "Unmatched",
                "source_system": "Call Tracking" if is_call else "Web Form",
                "evidence_class": "System-Observed",
            })

        # Non-converting digital touches, for spend-benchmark realism (Section 6
        # of the V0.1 generation rules) -- identical mechanism to baseline.
        # Section 10 cost-multiplier is applied afterward, below, to every
        # affected-campaign touch (converting and non-converting alike).
        n_google_conv = sum(1 for t in all_touches if t["platform"] == "Google Ads"
                             and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        n_msft_conv = sum(1 for t in all_touches if t["platform"] == "Microsoft Ads"
                           and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        n_meta_conv = sum(1 for t in all_touches if t["platform"] == "Meta"
                           and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        n_organic_conv = sum(1 for t in all_touches if t["platform"] == "Google Organic"
                              and t["touch_timestamp"][:7] == f"{year}-{month:02d}")
        new_google_touches = make_non_converting_touches(rng, year, month, "Google Ads", n_google_conv * NON_CONVERTING_MULTIPLIER["Google Ads"])
        for t in new_google_touches:
            if t["campaign_id"] in SCENARIO1_AFFECTED_CAMPAIGNS:
                t["cost"] = round(t["cost"] * SCENARIO1_COST_MULTIPLIER[month], 2)
        all_touches.extend(new_google_touches)
        all_touches.extend(make_non_converting_touches(rng, year, month, "Microsoft Ads", n_msft_conv * NON_CONVERTING_MULTIPLIER["Microsoft Ads"]))
        all_touches.extend(make_non_converting_touches(rng, year, month, "Meta", n_meta_conv * NON_CONVERTING_MULTIPLIER["Meta"]))
        all_touches.extend(make_non_converting_touches(rng, year, month, "Organic", n_organic_conv * NON_CONVERTING_MULTIPLIER["Organic"]))

        all_referrals.extend(gen_unlinked_referrals(rng, accounts_by_id, account_weights, linked_referrals_this_month))

    activities = gen_outreach_activities(rng, accounts, reps)

    all_episodes, all_claims, all_claim_events = [], [], []
    for opp in all_opportunities:
        if opp["admission_status"] == "Admitted":
            episodes = gen_episodes_for_admitted_opportunity(rng, opp)
            all_episodes.extend(episodes)
            for ep in episodes:
                claims, events = gen_claims_and_events_for_episode(rng, ep)
                all_claims.extend(claims)
                all_claim_events.extend(events)

    return {
        "reps": reps, "accounts": accounts, "contacts": all_contacts,
        "opportunities": all_opportunities, "inquiries": all_inquiries,
        "touches": all_touches, "referrals": all_referrals, "activities": activities,
        "episodes": all_episodes, "claims": all_claims, "claim_events": all_claim_events,
        "monthly_opp_counts": monthly_opp_counts,
    }


# ===========================================================================
# Database insertion (Section 20: exact insertion order)
# ===========================================================================


def build_database(data, db_path=DB_PATH):
    if os.path.exists(db_path):
        os.remove(db_path)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(schema_sql)

    cur = conn.cursor()

    # 1. Contacts
    cur.executemany(
        "INSERT INTO contacts (contact_id, first_name, last_name, phone, email, date_of_birth, created_at) "
        "VALUES (:contact_id, :first_name, :last_name, :phone, :email, :date_of_birth, :created_at)",
        data["contacts"],
    )

    # 2. Outreach Reps
    cur.executemany(
        "INSERT INTO outreach_reps (outreach_rep_id, rep_name, active_flag) "
        "VALUES (:outreach_rep_id, :rep_name, :active_flag)",
        data["reps"],
    )

    # 3. Professional Accounts
    cur.executemany(
        "INSERT INTO professional_accounts (professional_account_id, professional_name, organization_name, "
        "professional_type, owner_rep_id, created_at) VALUES "
        "(:professional_account_id, :professional_name, :organization_name, :professional_type, "
        ":owner_rep_id, :created_at)",
        data["accounts"],
    )

    # 4. Patient Opportunities -- originating IDs NULL at insert time
    cur.executemany(
        "INSERT INTO patient_opportunities (opportunity_id, patient_contact_id, created_at, vob_submitted_flag, "
        "vob_outcome, payer, payer_relationship, admission_financial_status, admission_status, "
        "originating_influence_type, originating_touch_id, originating_referral_id, attribution_confidence) "
        "VALUES (:opportunity_id, :patient_contact_id, :created_at, :vob_submitted_flag, :vob_outcome, :payer, "
        ":payer_relationship, :admission_financial_status, :admission_status, :originating_influence_type, "
        "NULL, NULL, :attribution_confidence)",
        data["opportunities"],
    )

    # 5. Inquiries
    cur.executemany(
        "INSERT INTO inquiries (inquiry_id, opportunity_id, contact_id, inquiry_timestamp, contact_role, "
        "inquiry_method, arrival_channel, source_platform, tracking_number, call_duration_seconds, landing_page, "
        "match_confidence, source_system, evidence_class) VALUES "
        "(:inquiry_id, :opportunity_id, :contact_id, :inquiry_timestamp, :contact_role, :inquiry_method, "
        ":arrival_channel, :source_platform, :tracking_number, :call_duration_seconds, :landing_page, "
        ":match_confidence, :source_system, :evidence_class)",
        data["inquiries"],
    )

    # 6. Acquisition Touches / Professional Referrals
    cur.executemany(
        "INSERT INTO acquisition_touches (touch_id, inquiry_id, touch_timestamp, channel, platform, campaign_id, "
        "campaign_name, ad_group, keyword, search_term, match_type, landing_page, geography, cost, "
        "platform_conversion, source_system, evidence_class) VALUES "
        "(:touch_id, :inquiry_id, :touch_timestamp, :channel, :platform, :campaign_id, :campaign_name, :ad_group, "
        ":keyword, :search_term, :match_type, :landing_page, :geography, :cost, :platform_conversion, "
        ":source_system, :evidence_class)",
        data["touches"],
    )
    cur.executemany(
        "INSERT INTO professional_referrals (referral_id, professional_account_id, opportunity_id, "
        "referral_timestamp, referral_channel, source_system, evidence_class, attribution_confidence) VALUES "
        "(:referral_id, :professional_account_id, :opportunity_id, :referral_timestamp, :referral_channel, "
        ":source_system, :evidence_class, :attribution_confidence)",
        data["referrals"],
    )

    # 7. Update Patient Opportunities with originating_touch_id / originating_referral_id
    updates = [
        (opp["originating_touch_id"], opp["originating_referral_id"], opp["opportunity_id"])
        for opp in data["opportunities"]
        if opp["originating_touch_id"] is not None or opp["originating_referral_id"] is not None
    ]
    cur.executemany(
        "UPDATE patient_opportunities SET originating_touch_id = ?, originating_referral_id = ? "
        "WHERE opportunity_id = ?",
        updates,
    )

    # 8. Outreach Activities
    cur.executemany(
        "INSERT INTO outreach_activities (activity_id, professional_account_id, outreach_rep_id, "
        "activity_timestamp, activity_type, direction, reciprocated_flag, evidence_class) VALUES "
        "(:activity_id, :professional_account_id, :outreach_rep_id, :activity_timestamp, :activity_type, "
        ":direction, :reciprocated_flag, :evidence_class)",
        data["activities"],
    )

    # 9. EHR Episodes
    episode_rows = [{k: v for k, v in ep.items() if not k.startswith("_")} for ep in data["episodes"]]
    cur.executemany(
        "INSERT INTO ehr_episodes (episode_id, opportunity_id, prior_episode_id, episode_relationship, "
        "admission_datetime, discharge_datetime, level_of_care, payer, authorization_start, authorization_end, "
        "discharge_disposition, source_system, evidence_class) VALUES "
        "(:episode_id, :opportunity_id, :prior_episode_id, :episode_relationship, :admission_datetime, "
        ":discharge_datetime, :level_of_care, :payer, :authorization_start, :authorization_end, "
        ":discharge_disposition, :source_system, :evidence_class)",
        episode_rows,
    )

    # 10. Claims
    cur.executemany(
        "INSERT INTO claims (claim_id, episode_id, service_start_date, service_end_date, payer, billed_amount, "
        "allowed_amount, patient_responsibility, claim_status, source_system, evidence_class) VALUES "
        "(:claim_id, :episode_id, :service_start_date, :service_end_date, :payer, :billed_amount, "
        ":allowed_amount, :patient_responsibility, :claim_status, :source_system, :evidence_class)",
        data["claims"],
    )

    # 11. Claim Events
    cur.executemany(
        "INSERT INTO claim_events (claim_event_id, claim_id, event_date, event_type, amount, source_system, "
        "evidence_class) VALUES (:claim_event_id, :claim_id, :event_date, :event_type, :amount, :source_system, "
        ":evidence_class)",
        data["claim_events"],
    )

    conn.commit()
    return conn


# ===========================================================================
# CSV export
# ===========================================================================

TABLES = [
    "contacts", "outreach_reps", "professional_accounts", "patient_opportunities",
    "inquiries", "acquisition_touches", "professional_referrals", "outreach_activities",
    "ehr_episodes", "claims", "claim_events",
]


def export_csv(conn, out_dir=CSV_EXPORT_DIR):
    os.makedirs(out_dir, exist_ok=True)
    cur = conn.cursor()
    for table in TABLES:
        cur.execute(f"SELECT * FROM {table}")
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()
        path = os.path.join(out_dir, f"{table}.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(cols)
            writer.writerows(rows)
        print(f"  exported {table}: {len(rows)} rows -> {path}")


# ===========================================================================
# Summary / manifest
# ===========================================================================


def print_summary(data):
    print("\n=== Harbor Ridge V0.1 Baseline Generation Summary ===\n")
    print(f"SEED = {SEED}")
    print(f"Observation date = {OBSERVATION_DATE.isoformat()}\n")

    print("Row counts:")
    for name, key in [
        ("contacts", "contacts"), ("outreach_reps", "reps"), ("professional_accounts", "accounts"),
        ("patient_opportunities", "opportunities"), ("inquiries", "inquiries"),
        ("acquisition_touches", "touches"), ("professional_referrals", "referrals"),
        ("outreach_activities", "activities"), ("ehr_episodes", "episodes"),
        ("claims", "claims"), ("claim_events", "claim_events"),
    ]:
        print(f"  {name:26s} {len(data[key])}")

    print("\nOpportunities generated by month (Section 3 target ~175 +-5-10%):")
    for label, n in data["monthly_opp_counts"].items():
        print(f"  {label}: {n}")

    n_admitted = sum(1 for o in data["opportunities"] if o["admission_status"] == "Admitted")
    n_opps = len(data["opportunities"])
    n_inquiries = len(data["inquiries"])
    print(f"\nTotal opportunities: {n_opps}, Admitted: {n_admitted} "
          f"({n_admitted/n_opps:.1%} Opportunity->Admission)")
    print(f"Total inquiries: {n_inquiries} "
          f"({n_admitted/n_inquiries:.1%} Inquiry->Admission)")

    # Section 6 marketing-budget allocation: only the 45/20/15/10/5/5
    # PERCENTAGE split is an approved generation-rules figure. No absolute
    # monthly dollar amount is part of the approved rules, so none is
    # asserted here -- report the percentage allocation and the actual
    # digital spend captured in acquisition_touches.cost side by side,
    # without implying a target dollar figure either one should hit.
    #
    # NOTE: acquisition_touches.cost values are drawn from flat per-touch
    # random ranges (e.g. Google Ads ~$14-45/touch) with no calibration
    # logic tying their sum to the 45% (or any) share of an actual budget.
    # If a real monthly budget figure is proposed and approved, hitting it
    # will require calibration logic (e.g. scaling per-touch cost or touch
    # volume to a target sum), not just stating a target -- that does not
    # exist yet.
    allocation = {
        "Google Ads": 0.45, "Professional Outreach / BD": 0.20, "SEO / Organic Content": 0.15,
        "Events / Community / Referral Development": 0.10, "Microsoft Ads": 0.05, "Meta": 0.05,
    }
    google_spend = sum(t["cost"] or 0 for t in data["touches"] if t["platform"] == "Google Ads")
    msft_spend = sum(t["cost"] or 0 for t in data["touches"] if t["platform"] == "Microsoft Ads")
    meta_spend = sum(t["cost"] or 0 for t in data["touches"] if t["platform"] == "Meta")

    print("\nSection 6 marketing-budget allocation (approved generator validation config -- "
          "percentages only; no absolute dollar target is part of the approved rules):")
    for channel, pct in allocation.items():
        print(f"  {channel:42s} {pct:>4.0%}")
    print("\n  Actual digital spend recorded in acquisition_touches.cost (3-mo, uncalibrated to any target):")
    print(f"    Google Ads:     ${google_spend:>10,.2f}")
    print(f"    Microsoft Ads:  ${msft_spend:>10,.2f}")
    print(f"    Meta:           ${meta_spend:>10,.2f}")
    print("    (Professional Outreach/BD, SEO/Organic Content, and Events/Community spend "
          "are not stored relationally per Section 6 -- reported here as config only.)")


def print_summary_scenario1(data):
    print("\n=== Harbor Ridge Scenario 1 Generation Summary ===\n")
    print(f"SCENARIO_1_SEED = {SCENARIO_1_SEED}")
    print(f"Observation date = {OBSERVATION_DATE.isoformat()}\n")

    print("Row counts:")
    for name, key in [
        ("contacts", "contacts"), ("outreach_reps", "reps"), ("professional_accounts", "accounts"),
        ("patient_opportunities", "opportunities"), ("inquiries", "inquiries"),
        ("acquisition_touches", "touches"), ("professional_referrals", "referrals"),
        ("outreach_activities", "activities"), ("ehr_episodes", "episodes"),
        ("claims", "claims"), ("claim_events", "claim_events"),
    ]:
        print(f"  {name:26s} {len(data[key])}")

    print("\nOpportunities generated by month:")
    for label, n in data["monthly_opp_counts"].items():
        print(f"  {label}: {n}")

    opps = data["opportunities"]
    print("\nAffected attributable opportunities (Section 3 definition) by month:")
    for year, month, label in MONTHS:
        month_opps = [o for o in opps if o["_month"] == (year, month)]
        affected = [o for o in month_opps if o["_scenario1_affected"]]
        affected_admitted = [o for o in affected if o["admission_status"] == "Admitted"]
        affected_oon = [o for o in affected if o["payer_relationship"] == "OON"]
        conv = len(affected_admitted) / len(affected) if affected else 0
        oon_share = len(affected_oon) / len(affected) if affected else 0
        print(f"  {label}: {len(affected)} affected opportunities, "
              f"Opportunity->Admission {conv:.1%} ({len(affected_admitted)}/{len(affected)}), "
              f"OON share {oon_share:.1%}")

    total_admitted = sum(1 for o in opps if o["admission_status"] == "Admitted")
    print(f"\nTotal opportunities: {len(opps)}, Admitted: {total_admitted} "
          f"({total_admitted/len(opps):.1%} facility-wide Opportunity->Admission)")
    print("(No facility-wide admit-count/payer-mix rebalancing is applied in Scenario 1 mode --")
    print(" see generate_dataset_scenario1() docstring for why.)")


def main():
    parser = argparse.ArgumentParser(description="Harbor Ridge synthetic data generator")
    parser.add_argument(
        "--mode", choices=["baseline", "scenario1"], default="baseline",
        help="'baseline' (default): SEED, harbor_ridge.db, data/csv_export/. "
             "'scenario1': SCENARIO_1_SEED, harbor_ridge_scenario1.db, data/csv_export_scenario1/. "
             "Never both from the same run.",
    )
    args = parser.parse_args()

    if args.mode == "scenario1":
        data = generate_dataset_scenario1()
        conn = build_database(data, db_path=SCENARIO1_DB_PATH)
        print_summary_scenario1(data)
        print("\nExporting CSVs...")
        export_csv(conn, out_dir=SCENARIO1_CSV_EXPORT_DIR)
        conn.close()
        print("\nDone. Database written to", SCENARIO1_DB_PATH)
    else:
        data = generate_dataset()
        conn = build_database(data)
        print_summary(data)
        print("\nExporting CSVs...")
        export_csv(conn)
        conn.close()
        print("\nDone. Database written to", DB_PATH)


if __name__ == "__main__":
    main()
