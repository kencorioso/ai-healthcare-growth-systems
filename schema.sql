-- Harbor Ridge V1 SQLite Schema
-- Generated from docs/minimum-viable-data-dictionary.md (Version 1.0)
-- Every table, column, type, constraint, and FK here traces directly to that document.

PRAGMA foreign_keys = ON;

-- ===========================================================================
-- 3. contacts
-- ===========================================================================
CREATE TABLE contacts (
    contact_id      TEXT NOT NULL PRIMARY KEY,
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,
    phone           TEXT NULL,
    email           TEXT NULL,
    date_of_birth   TEXT NULL,
    created_at      TEXT NOT NULL
);

-- ===========================================================================
-- 7. outreach_reps
-- ===========================================================================
CREATE TABLE outreach_reps (
    outreach_rep_id TEXT NOT NULL PRIMARY KEY,
    rep_name        TEXT NOT NULL,
    active_flag     INTEGER NOT NULL,
    CHECK (active_flag IN (0, 1))
);

-- ===========================================================================
-- 8. professional_accounts
-- ===========================================================================
CREATE TABLE professional_accounts (
    professional_account_id TEXT NOT NULL PRIMARY KEY,
    professional_name       TEXT NOT NULL,
    organization_name       TEXT NULL,
    professional_type       TEXT NOT NULL,
    owner_rep_id             TEXT NULL,
    created_at               TEXT NOT NULL,
    FOREIGN KEY (owner_rep_id) REFERENCES outreach_reps (outreach_rep_id)
);

-- ===========================================================================
-- 4. patient_opportunities
-- ===========================================================================
CREATE TABLE patient_opportunities (
    opportunity_id              TEXT NOT NULL PRIMARY KEY,
    patient_contact_id          TEXT NULL,
    created_at                  TEXT NOT NULL,
    vob_submitted_flag          INTEGER NOT NULL,
    vob_outcome                 TEXT NULL,
    payer                       TEXT NULL,
    payer_relationship          TEXT NOT NULL,
    admission_financial_status  TEXT NOT NULL,
    admission_status            TEXT NOT NULL,
    originating_influence_type  TEXT NOT NULL,
    originating_touch_id        TEXT NULL,
    originating_referral_id     TEXT NULL,
    attribution_confidence      TEXT NOT NULL,

    FOREIGN KEY (patient_contact_id) REFERENCES contacts (contact_id),
    FOREIGN KEY (originating_touch_id) REFERENCES acquisition_touches (touch_id),
    FOREIGN KEY (originating_referral_id) REFERENCES professional_referrals (referral_id),

    CHECK (vob_submitted_flag IN (0, 1)),
    CHECK (payer_relationship IN ('INN', 'OON', 'Private Pay')),
    CHECK (admission_financial_status IN ('Financially Cleared', 'At-Risk Admission', 'Not Financially Cleared')),
    CHECK (admission_status IN ('Open', 'Admitted', 'Not Admitted')),
    CHECK (originating_influence_type IN ('Paid', 'Organic', 'Professional Referral', 'Direct', 'Unknown')),
    CHECK (attribution_confidence IN ('Confirmed', 'Probable', 'Possible', 'Unmatched')),

    -- 15.1 VOB Conditional Integrity Rule
    -- (vob_outcome IS NOT NULL is explicit here, not just implied by IN(), because
    -- SQLite's `x IN (...)` evaluates to NULL rather than 0 when x IS NULL, and a
    -- CHECK expression that evaluates to NULL is treated as satisfied, not violated.)
    CHECK (
        (vob_submitted_flag = 0 AND vob_outcome IS NULL)
        OR
        (vob_submitted_flag = 1 AND vob_outcome IS NOT NULL
            AND vob_outcome IN ('Pending', 'Viable', 'Non-Viable', 'Unable to Verify'))
    )
);

-- ===========================================================================
-- 5. inquiries
-- ===========================================================================
CREATE TABLE inquiries (
    inquiry_id            TEXT NOT NULL PRIMARY KEY,
    opportunity_id        TEXT NULL,
    contact_id            TEXT NOT NULL,
    inquiry_timestamp     TEXT NOT NULL,
    contact_role          TEXT NOT NULL,
    inquiry_method        TEXT NOT NULL,
    arrival_channel       TEXT NOT NULL,
    source_platform       TEXT NULL,
    tracking_number       TEXT NULL,
    call_duration_seconds INTEGER NULL,
    landing_page          TEXT NULL,
    match_confidence      TEXT NOT NULL,
    source_system         TEXT NOT NULL,
    evidence_class        TEXT NOT NULL,

    FOREIGN KEY (opportunity_id) REFERENCES patient_opportunities (opportunity_id),
    FOREIGN KEY (contact_id) REFERENCES contacts (contact_id),

    CHECK (contact_role IN ('Patient', 'Loved One', 'Professional Referral Source')),
    CHECK (inquiry_method IN ('Call', 'Web Form')),
    CHECK (arrival_channel IN ('Paid Search', 'Organic', 'Local', 'Professional Referral', 'Direct', 'Other', 'Unknown')),
    CHECK (match_confidence IN ('Confirmed', 'Probable', 'Possible', 'Unmatched')),
    CHECK (evidence_class IN ('System-Observed', 'Human-Entered', 'Derived / Analytical'))
);

-- ===========================================================================
-- 6. acquisition_touches
-- ===========================================================================
CREATE TABLE acquisition_touches (
    touch_id             TEXT NOT NULL PRIMARY KEY,
    inquiry_id           TEXT NULL,
    touch_timestamp      TEXT NOT NULL,
    channel              TEXT NOT NULL,
    platform             TEXT NULL,
    campaign_id          TEXT NULL,
    campaign_name        TEXT NULL,
    ad_group             TEXT NULL,
    keyword              TEXT NULL,
    search_term          TEXT NULL,
    match_type           TEXT NULL,
    landing_page         TEXT NULL,
    geography            TEXT NULL,
    cost                 REAL NULL,
    platform_conversion  INTEGER NOT NULL,
    source_system        TEXT NOT NULL,
    evidence_class       TEXT NOT NULL,

    FOREIGN KEY (inquiry_id) REFERENCES inquiries (inquiry_id),

    CHECK (channel IN ('Paid Search', 'Paid Social', 'Organic', 'Local', 'Direct')),
    CHECK (match_type IS NULL OR match_type IN ('Exact', 'Phrase', 'Broad')),
    CHECK (platform_conversion IN (0, 1)),
    CHECK (evidence_class IN ('System-Observed', 'Human-Entered', 'Derived / Analytical'))
);

-- ===========================================================================
-- 9. professional_referrals
-- ===========================================================================
CREATE TABLE professional_referrals (
    referral_id              TEXT NOT NULL PRIMARY KEY,
    professional_account_id  TEXT NOT NULL,
    opportunity_id           TEXT NULL,
    referral_timestamp       TEXT NOT NULL,
    referral_channel         TEXT NOT NULL,
    source_system            TEXT NOT NULL,
    evidence_class           TEXT NOT NULL,
    attribution_confidence   TEXT NOT NULL,

    FOREIGN KEY (professional_account_id) REFERENCES professional_accounts (professional_account_id),
    FOREIGN KEY (opportunity_id) REFERENCES patient_opportunities (opportunity_id),

    CHECK (referral_channel IN ('Call', 'Email/Text Coordination', 'Patient Told to Call', 'Other')),
    CHECK (evidence_class IN ('System-Observed', 'Human-Entered', 'Derived / Analytical')),
    CHECK (attribution_confidence IN ('Confirmed', 'Probable', 'Possible', 'Unmatched'))
);

-- ===========================================================================
-- 10. outreach_activities
-- ===========================================================================
CREATE TABLE outreach_activities (
    activity_id              TEXT NOT NULL PRIMARY KEY,
    professional_account_id  TEXT NOT NULL,
    outreach_rep_id          TEXT NOT NULL,
    activity_timestamp       TEXT NOT NULL,
    activity_type            TEXT NOT NULL,
    direction                TEXT NOT NULL,
    reciprocated_flag        INTEGER NOT NULL,
    evidence_class           TEXT NOT NULL,

    FOREIGN KEY (professional_account_id) REFERENCES professional_accounts (professional_account_id),
    FOREIGN KEY (outreach_rep_id) REFERENCES outreach_reps (outreach_rep_id),

    CHECK (activity_type IN ('Call', 'Email', 'Meeting', 'Lunch', 'Presentation', 'Tour')),
    CHECK (direction IN ('Outbound', 'Inbound')),
    CHECK (reciprocated_flag IN (0, 1)),
    CHECK (evidence_class IN ('System-Observed', 'Human-Entered', 'Derived / Analytical'))
);

-- ===========================================================================
-- 11. ehr_episodes
-- ===========================================================================
CREATE TABLE ehr_episodes (
    episode_id           TEXT NOT NULL PRIMARY KEY,
    opportunity_id       TEXT NULL,
    prior_episode_id     TEXT NULL,
    episode_relationship TEXT NOT NULL,
    admission_datetime   TEXT NOT NULL,
    discharge_datetime   TEXT NULL,
    level_of_care        TEXT NOT NULL,
    payer                TEXT NULL,
    authorization_start  TEXT NULL,
    authorization_end    TEXT NULL,
    discharge_disposition TEXT NULL,
    source_system        TEXT NOT NULL,
    evidence_class        TEXT NOT NULL,

    FOREIGN KEY (opportunity_id) REFERENCES patient_opportunities (opportunity_id),
    FOREIGN KEY (prior_episode_id) REFERENCES ehr_episodes (episode_id),

    CHECK (episode_relationship IN ('Initial', 'LOC Transition', 'Administrative Re-Admit')),
    CHECK (level_of_care IN ('Detox', 'Residential')),
    CHECK (evidence_class IN ('System-Observed', 'Human-Entered', 'Derived / Analytical')),

    -- 15.2 Episode Conditional Integrity Rule
    CHECK (
        (episode_relationship = 'Initial' AND prior_episode_id IS NULL)
        OR
        (episode_relationship IN ('LOC Transition', 'Administrative Re-Admit') AND prior_episode_id IS NOT NULL)
    )
);

-- ===========================================================================
-- 12. claims
-- ===========================================================================
CREATE TABLE claims (
    claim_id               TEXT NOT NULL PRIMARY KEY,
    episode_id             TEXT NULL,
    service_start_date     TEXT NOT NULL,
    service_end_date       TEXT NOT NULL,
    payer                  TEXT NOT NULL,
    billed_amount          REAL NOT NULL,
    allowed_amount         REAL NULL,
    patient_responsibility REAL NULL,
    claim_status            TEXT NOT NULL,
    source_system           TEXT NOT NULL,
    evidence_class           TEXT NOT NULL,

    FOREIGN KEY (episode_id) REFERENCES ehr_episodes (episode_id),

    CHECK (claim_status IN ('Submitted', 'Pending', 'Paid', 'Denied', 'Appealed', 'Closed')),
    CHECK (evidence_class IN ('System-Observed', 'Human-Entered', 'Derived / Analytical'))
);

-- ===========================================================================
-- 13. claim_events
-- ===========================================================================
CREATE TABLE claim_events (
    claim_event_id TEXT NOT NULL PRIMARY KEY,
    claim_id       TEXT NULL,
    event_date     TEXT NOT NULL,
    event_type     TEXT NOT NULL,
    amount         REAL NULL,
    source_system  TEXT NOT NULL,
    evidence_class TEXT NOT NULL,

    FOREIGN KEY (claim_id) REFERENCES claims (claim_id),

    CHECK (event_type IN ('Insurance Payment', 'Patient Payment', 'Adjustment', 'Write-Off', 'Denial', 'Appeal')),
    CHECK (evidence_class IN ('System-Observed', 'Human-Entered', 'Derived / Analytical'))
);
