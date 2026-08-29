# Security and Compliance Rules

## Purpose
These rules enforce security policies and compliance requirements for the FINOVA Digital Wallet platform. All technical changes must adhere to these rules before being approved for deployment.

---

## Rule 1: No Destructive Operations Without Override
* **Policy:** DROP TABLE, DROP COLUMN, and DELETE FROM operations on critical tables (`users`, `wallets`, `transactions`) are prohibited unless the environment variable `COMPLIANCE_OVERRIDE=1` is explicitly set.
* **Rationale:** Prevents accidental data loss in production environments.
* **Enforcement:** PreToolUse hook will block any command matching these patterns unless override is confirmed.

---

## Rule 2: All Schema Changes Require Migration Files
* **Policy:** All database schema changes must be implemented as SQL migration files in the `migrations/` directory with sequential numbering (e.g., `001_add_kyc_verified.sql`, `002_increase_tier2_limit.sql`).
* **Rationale:** Ensures version control and rollback capability for all database changes.
* **Enforcement:** GhostMode Skill will verify that changes are accompanied by properly named migration files.

---

## Rule 3: Compliance Verification Mandatory
* **Policy:** All changes affecting `transactions`, `users`, `wallets`, or `compliance_rules` tables must pass automated compliance verification via `verify_compliance.py` before being approved.
* **Rationale:** Ensures adherence to FIN-AML regulatory standards (FIN-AML-01, 07, 12, 15).
* **Enforcement:** SessionStart hook will run compliance checks; any FAILED result blocks PR generation.

---

## Rule 4: No External Dependencies Without Approval
* **Policy:** No external Python libraries or npm packages may be added to the project without explicit PM approval and security review.
* **Rationale:** Prevents supply chain vulnerabilities and maintains audit trail.
* **Enforcement:** Code Review will flag any new import statements or package.json dependencies.

---

## Rule 5: Data Dictionary Must Be Updated
* **Policy:** Any new table or column added to the database must be documented in `data_dictionary.json` with business-level descriptions.
* **Rationale:** Ensures GhostMode can translate technical changes into business language for PM decision-making.
* **Enforcement:** GhostMode Skill will verify that `data_dictionary.json` is updated for all schema changes.
