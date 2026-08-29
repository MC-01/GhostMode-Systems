### GhostMode Standard Operating Procedure (SOP)
#### Purpose
This document describes the standard workflow for Product Managers using GhostMode to verify and approve technical changes without reading code.

---

#### Workflow Overview
```
PM Request → Bob Plan → Implementation → GhostMode → Compliance Check → Ghost Decision Card → PM Decision
```

---

#### Step-by-Step Instructions

##### Step 1: PM Request (Business Change)
* **Action:** Product Manager identifies a business requirement or change.
* **Example:** "Increase the transaction limit for Tier 2 users from €5,000 to €10,000."
* **Output:** Business requirement documented in plain language.

##### Step 2: Bob Plan Mode (Analysis)
* **Action:** Launch Bob in Plan Mode to analyze the repository and detect the required change.
* **What Bob Does:**
    * Reads the current state of the codebase
    * Identifies which tables/columns need to be modified
    * Generates a detailed implementation plan (PLAN.md)
    * Captures the original prompt in docs/genesis.md
* **Output:** Implementation plan with task IDs and SQL migration draft.

##### Step 3: GhostMode Skill (Verification)
* **Action:** Switch to Agent Mode and execute the GhostMode Release Review Skill.
* **What GhostMode Does:**
    * Reads the SQL migration file
    * Translates technical changes to business language using data_dictionary.json
    * Loads FINOVA_Compliance_2026.pdf and extracts regulatory rules
    * Runs verify_compliance.py to check for compliance violations
* **Output:** Compliance analysis and test results.

##### Step 4: Ghost Decision Card (Decision Support)
* **Action:** GhostMode generates a 6-block decision card.
* **Output:** Markdown-formatted card ready for PR injection.

##### Step 5: PM Decision (Approve/Reject)
* **Action:** Product Manager reviews the Ghost Decision Card and makes a decision.
* **Options:**
    * **APPROVE:** Change is safe to merge (all tests passed, low/medium risk)
    * **REVIEW:** Change requires additional compliance review (medium/high risk)
    * **BLOCK:** Change violates compliance rules (high risk, do not merge)

##### Step 6: Auto-Generate Pull Request
* **Action:** If PM approves, Bob automatically generates a formatted Pull Request on GitHub.
* **Output:** Pull Request ready for merge (pending final approval).
