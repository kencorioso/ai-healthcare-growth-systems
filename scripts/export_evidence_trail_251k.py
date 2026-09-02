"""
Exports the $251K evidence trail (Harbor Ridge V1 Workstream B, Section 2 contract).

Reads only from harbor_ridge_scenario1.db, per docs/harbor-ridge-workstream-b-implementation-spec.md.
Output is deterministic: same frozen database + this script = byte-identical JSON.
"""

import json
import os
import sqlite3
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DB_PATH = os.path.join(REPO_ROOT, "harbor_ridge_scenario1.db")
DEFAULT_OUTPUT_PATH = os.path.join(REPO_ROOT, "src", "data", "evidence-trail-251k.json")

QUERY = """
SELECT
  po.opportunity_id,
  po.payer_relationship,
  e.episode_id,
  c.claim_id,
  c.billed_amount,
  c.allowed_amount,
  c.claim_status,
  COALESCE(SUM(CASE WHEN ce.event_type IN ('Insurance Payment', 'Patient Payment') THEN ce.amount ELSE 0 END), 0) AS collected_amount
FROM patient_opportunities po
JOIN ehr_episodes e ON e.opportunity_id = po.opportunity_id
JOIN claims c ON c.episode_id = e.episode_id
LEFT JOIN claim_events ce ON ce.claim_id = c.claim_id
WHERE po.payer_relationship IN ('INN', 'OON')
GROUP BY po.opportunity_id, po.payer_relationship, e.episode_id, c.claim_id, c.billed_amount, c.allowed_amount, c.claim_status
"""


def fetch_claims(db_path):
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute(QUERY)
        rows = cur.fetchall()
    finally:
        conn.close()

    claims = []
    for (opportunity_id, payer_relationship, episode_id, claim_id,
         billed_amount, allowed_amount, claim_status, collected_amount) in rows:
        claims.append({
            "opportunity_id": opportunity_id,
            "payer_relationship": payer_relationship,
            "episode_id": episode_id,
            "claim_id": claim_id,
            "billed_amount": billed_amount,
            "allowed_amount": allowed_amount,
            "collected_amount": collected_amount,
            "claim_status": claim_status,
        })

    # SQL row order is not guaranteed without an explicit ORDER BY; sort here
    # so byte-identical output does not depend on incidental SQLite return order.
    claims.sort(key=lambda c: (c["payer_relationship"], c["claim_id"]))
    return claims


def compute_summary(claims):
    inn_billed_total = sum(c["billed_amount"] for c in claims if c["payer_relationship"] == "INN")
    inn_collected_total = sum(c["collected_amount"] for c in claims if c["payer_relationship"] == "INN")
    oon_billed_total = sum(c["billed_amount"] for c in claims if c["payer_relationship"] == "OON")
    oon_collected_total = sum(c["collected_amount"] for c in claims if c["payer_relationship"] == "OON")

    inn_collection_realization_rate = inn_collected_total / inn_billed_total
    oon_collection_realization_rate = oon_collected_total / oon_billed_total
    expected_oon_collections_at_inn_rate = oon_billed_total * inn_collection_realization_rate
    estimated_gap = expected_oon_collections_at_inn_rate - oon_collected_total

    return {
        "inn_billed_total": inn_billed_total,
        "inn_collected_total": inn_collected_total,
        "inn_collection_realization_rate": inn_collection_realization_rate,
        "oon_billed_total": oon_billed_total,
        "oon_collected_total": oon_collected_total,
        "oon_collection_realization_rate": oon_collection_realization_rate,
        "expected_oon_collections_at_inn_rate": expected_oon_collections_at_inn_rate,
        "estimated_gap": estimated_gap,
    }


def export(db_path, output_path):
    claims = fetch_claims(db_path)
    summary = compute_summary(claims)

    payload = {
        "generated_from": "harbor_ridge_scenario1.db",
        "summary": summary,
        "claims": claims,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="\n", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=False)
        f.write("\n")

    return output_path


if __name__ == "__main__":
    db_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DB_PATH
    output_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUTPUT_PATH
    export(db_path, output_path)
    print(f"Wrote {output_path}")
