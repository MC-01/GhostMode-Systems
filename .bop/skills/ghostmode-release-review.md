### GhostMode Release Review Skill
#### Purpose
This skill translates AI-generated technical changes into evidence-backed product decisions, so Product Managers can understand risk, verify compliance, and confidently approve releases without having to interpret the underlying code.

---

#### Input Requirements
* **Branch/PR** : The Git branch or Pull Request to analyze
* **Migration SQL** : Path to SQL migration file(s) in `migrations/` directory
* **Compliance PDF** : `FINOVA_Compliance_2026.pdf` (source of truth for regulatory rules)
* **Data Dictionary** : `data_dictionary.json` (maps technical schema to business terminology)

---

#### Execution Steps
##### Step 1: Analyze Technical Changes
* Read the SQL migration file or git diff
* Identify which tables and columns are affected
* Classify the change type: ADD COLUMN, DROP COLUMN, UPDATE, ALTER TABLE, etc.

##### Step 2: Translate to Business Language
* Use `data_dictionary.json` to map technical names to business terms
* Example: `transactions.kyc_verified` → "KYC verification status for transactions"
* Generate a plain-English description of what changed

##### Step 3: Verify Compliance
* Load `FINOVA_Compliance_2026.pdf` and extract regulatory rules
* Check if the change violates any of the 4 FIN-AML rules:
    * FIN-AML-01: Negative Balance Prohibition
    * FIN-AML-07: Tier 2 Transaction Limit (€5,000)
    * FIN-AML-12: High-Value Transaction KYC (>$10,000 requires Tier 3)
    * FIN-AML-15: High-Risk Merchant Review
* Run `verify_compliance.py` to get deterministic test results

##### Step 4: Assess Risk
* **LOW** : No compliance impact, no data migration required
* **MEDIUM** : Minor compliance impact or legacy data handling required
* **HIGH** : Compliance violation detected or significant business impact

##### Step 5: Generate Ghost Decision Card
Create a 6-block decision card:
1. 🎯 **Business Intent** – What are we trying to achieve?
2. 🗄️ **Technical Impact** – What actually changed?
3. ⚖️ **Compliance Impact** – What rules could be affected?
4. 🧪 **Verification** – What evidence do we have? (test results)
5. 🚦 **Risk** – Low / Medium / High
6. 👤 **PM Decision** – Merge / Review / Block

##### Step 6: Inject into Pull Request
* Add the Ghost Decision Card as a comment or description in the PR
* Include a summary recommendation: "Safe to merge", "Needs compliance override", or "Do not merge"
* Link to detailed test results and compliance analysis

---

#### Output Format
The skill outputs a Markdown-formatted Ghost Decision Card ready for PR injection.
Example:
```markdown
| Block | Content |
|-------|---------|
| 🎯 **Business Intent** | Enable explicit tracking of KYC verification status per transaction. |
| 🗄️ **Technical Impact** | New column `kyc_verified BOOLEAN DEFAULT FALSE` in `transactions`. |
| ⚖️ **Compliance Impact** | No direct conflict with FIN-AML rules. Existing transactions default to FALSE. |
| 🧪 **Verification** | ✓ 14/14 compliance checks passed. |
| 🚦 **Risk** | MEDIUM – Legacy transactions may need migration script. |
| 👤 **PM Decision** | ✅ APPROVE (with note: confirm legacy handling before merge). |
```

---

#### Success Criteria
* PM can understand the change without reading SQL
* Compliance violations are detected and flagged before merge
* Test results are deterministic and reproducible
* Decision is evidence-backed (code + data + rules + tests → decision)
