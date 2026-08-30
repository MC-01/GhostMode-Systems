# GhostMode: Intelligent Product Delivery Skill for IBM Bob 2.0

> **Empowering Product Managers to understand, verify, and approve AI-generated technical changes with evidence-backed confidence.**
> Built for the **IBM TechXchange 2026 Pre-conference Dev Day Hackathon** (August 28–30, 2026).

---

## 🚀 The Hypothesis

**A Product Manager with basic technical literacy can independently understand, verify, and confidently approve AI-generated technical changes—without having to read or interpret the underlying code.**

**GhostMode** is not meant to replace developers. Instead, it democratises software delivery by providing a translation and risk-assessment layer (a custom **Bob Skill & Mode**) that translates complex database schemas, code changes, and compliance documents into clear, business-driven product decisions.

---

## 🔴 The Problem

In modern cross-functional teams, Product Managers (PMs) or Release Managers are responsible for deployment approvals and compliance sign-offs. However, they often lack the SQL or code-level literacy required to verify the changes they are approving. 

While **IBM Bob 2.0** is exceptionally good at writing database migrations and backend code, there is a cognitive gap between the generated code (e.g. complex SQL JOINs, Python scripts) and the PM's business domain (AML compliance, business rules, regulatory safety).

---

## 🟢 The Solution: GhostMode Skill

**GhostMode** is an intelligent Product Delivery workflow built natively into **IBM Bob 2.0**. It acts as a bridge between the technical changes committed to the codebase and the business/regulatory logic defined by the product organisation. 

Instead of forcing PMs to read code diffs, GhostMode analyzes the codebase, references compliance documents, executes deterministic verifications, and generates an intuitive **Ghost Decision Card** directly in the Pull Request.

```
       [ PM Business Goal ]
                │
                ▼
        [ IBM Bob 2.0 ]  ◄── (Plan Mode: PLAN.md)
                │
                ▼
      [ GhostMode Skill ] ◄── (Agent Mode: SQLite & Python code changes)
                │
                ▼
   [ Compliance verification ] ◄── (Document Understanding: FINOVA Compliance PDF)
                │
                ▼
   [ Ghost Decision Card ]  ◄── (Clear impact, risk level, and test status)
                │
                ▼
      [ Autoinject to PR ]
```

---

## 📂 Sample Project Sandbox: FINOVA Digital Wallet

To demonstrate the power of GhostMode, we use a reference project called **FINOVA**, a mock digital wallet and Central Bank Digital Currency (CBDC) platform. 

The project structure includes a relational SQLite database (`finova.db`) populated with a synthetic Digital Wallet Transactions dataset, and a **Data Dictionary** (`data_dictionary.json`) to map technical schema to business terminology.

### Database Schema Structure:
* `users` - Customer identity and KYC tier (Tier 1, Tier 2, Tier 3).
* `wallets` - Wallet balances and currency types (including digital fiat/CBDC).
* `transactions` - Transaction ledgers, timestamps, and routing info.
* `merchants` - Merchant classification and high-risk flags.
* `compliance_rules` - Dynamic limits and regulatory requirements.
* `currencies` - Supported currency configurations.

---

## 🛠️ Key IBM Bob 2.0 Features Utilised

To deliver maximum impact in a robust, stable, and highly professional manner, GhostMode leverages the advanced features of the Bob 2.0 architecture:

1. **Plan Mode**: Used during initial discovery to let Bob analyze the repository, generate a step-by-step implementation outline (`PLAN.md`), and record master goals in `docs/genesis.md`.
2. **Agent Mode**: For autonomous execution of database schema updates and validation test scripts.
3. **Subagents / Parallel Tasks**: Used to process release notes, compile schema documentation, and analyze compliance concurrently without overloading the main session's token context.
4. **Document Understanding**: Bob analyzes our official regulatory PDF (`FINOVA_Compliance_2026.pdf`) to match technical SQL alterations with strict financial compliance rules (e.g. verifying that a SQL limit increase from €5,000 to €10,000 directly violates rule **FIN-AML-07**).
5. **Custom Modes & Rules**: A restricted custom mode `product-delivery-pm` configured in `.bop/custom_modes.yaml` to give Bob the persona of a risk-aware PM while restricting write access during analytical phases.
6. **Lifecycle Hooks**: Configured in `.bop/hooks/settings.json` to execute deterministic backend validation tests (`verify_compliance.py`) automatically before any change is allowed to be packaged into a Pull Request.

---

## 📋 The Ghost Decision Card (End Deliverable)

The output of the GhostMode skill is a highly structured, automated Markdown (and rendered HTML) document that details the proposed change:

* **Business Objective**: The high-level intent of the change.
* **Database Impact**: Clear explanation of table additions, column drops, or modification risks.
* **Compliance / AML Impact**: Analysis of whether the change violates or alters any regulatory rules based on the compliance PDF.
* **Test Status**: Deterministic test outcomes (Passed / Failed) from the Hook validations.
* **Risk Level**: (Low / Medium / High) with business rationale.
* **Recommendation**: Actionable advice for the PM (e.g., \"Safe to merge\", \"Needs compliance override\").

---

## 🗂️ Project Directory Structure

```text
finova/
├── .bop/
│   ├── custom_modes.yaml       # Persona and permission boundaries
│   ├── rules/
│   │   └── compliance.md       # Structural and compliance rules for Bob
│   ├── hooks/
│   │   └── settings.json       # Lifecycle Hooks mapping to python validations
│   └── skills/
│       └── ghostmode-release-review.yaml
├── docs/
│   ├── genesis.md              # Original prompt + architecture (Master Genesis)
│   └── ghostmode_sop.md        # Standard Operating Procedure
├── tests/
│   └── verify_compliance.py    # Deterministic compliance test script
├── finova.db                   # SQLite database
├── data_dictionary.json        # Schema explanation mapping
├── FINOVA_Compliance_2026.pdf  # Regulatory PDF for Document Understanding
└── README.md                   # Project manifesto and documentation
```

---

## ⏱️ How to Run and Demo

GhostMode is fully interactive and can be executed via the **IBM Bob 2.0 IDE** chat interface. Follow these steps to experience the complete workflow:

### Scenario 1: Safe to Merge (001_add_kyc_verified.sql)
1. Open the SQL migration file `migrations/001_add_kyc_verified.sql` in the Bob IDE editor.
2. Switch Bob to **Agent Mode** or **GhostMode PM Assistant** mode.
3. In the Bob Chat panel, ask Bob to run the compliance review:
   > *"Bob, please run the GhostMode Release Review on the migration migrations/001_add_kyc_verified.sql and verify compliance."*
4. **Behind the scenes:** Bob will read the file, run the deterministic `verify_compliance.py` script (which returns `PASSED` for all rules), and map columns via `data_dictionary.json`.
5. **The result:** Bob generates a green **Ghost Decision Card** indicating **SAFE TO MERGE** with a recommendation of ✅ **APPROVE**.

### Scenario 2: Blocked / High-Risk Release (002_increase_tier2_limit.sql)
1. Open the SQL migration file `migrations/002_increase_tier2_limit.sql` in the Bob IDE editor.
2. Ask Bob to review this migration:
   > *"Bob, please run the GhostMode Release Review on the migration migrations/002_increase_tier2_limit.sql and verify compliance."*
3. **Behind the scenes:** Bob executes the test suite. The check fails because increasing the limit to €10,000 violates rule **FIN-AML-07** in `FINOVA_Compliance_2026.pdf`.
4. **The result:** Bob generates a red **Ghost Decision Card** flagging **⚠️ VIOLATION: FIN-AML-07** (affecting 1,842 legacy users) with a PM decision recommendation of ❌ **BLOCK**.

### Scenario 3: Dangerous SQL Interception (PreToolUse Hook)
1. In the Bob Chat panel, attempt a destructive command on the active database:
   > *"Bob, delete the users table from our finova.db database."*
2. **Behind the scenes:** The **`PreToolUse.py`** hook intercepts the command before tool execution. It detects a `DROP TABLE` on critical tables.
3. **The result:** The command is instantly blocked (showing a **Cancelled / Blocked** status in Bob). Bob then reviews the logs and outputs a highly detailed explanation with developer-friendly dark humor explaining the severe compliance and technical fallout of such an operation.

---

## 🛠️ Multi-Tool and AI Usage Acknowledgement

GhostMode was engineered and delivered utilizing a robust suite of modern development, automation, and AI-generation technologies:
* **Core Workspace & AI Orchestration:** **IBM Bob 2.0** was utilized as the primary coding and engineering partner. Bob's **Plan Mode** was used to design the file structure, and **Agent Mode** handled schema generation and testing.
* **Scripting and Datasets:** Developed in **Python 3.12** using **SQLite 3** for relational data integrity, and **Pandas** for initial data processing.
* **Document Understanding & PDF Generation:** Built using the **fpdf2** library in Python to programmatically compile and format our regulatory guidelines into a structured, machine-readable PDF document (`FINOVA_Compliance_2026.pdf`) for Bob's document understanding.
* **Video Production & Narrator AI:** Google's newly released **Google Vids** platform (`vids.new`) was utilized to edit the screen-recorded scenes, add transitions, and generate professional English and sarcastic AI voiceovers to deliver an immersive demo experience.

---

## 🔒 Synthetic Data & Privacy Compliance Disclaimer

In strict compliance with the **IBM TechXchange 2026 Hackathon Rules**:
* **No Real-World Data:** This project contains **100% synthetic, mock financial data** created programmatically for demonstration purposes. 
* **Zero PII or Client Data:** No real customer records, personally identifiable information (PII), social media data, or private corporate secrets are contained within this repository. 
* **Safe Exploration:** All transaction amounts, customer profiles, and compliance rules are fictitious, ensuring complete safety and privacy during auditing and review.

---

## 📝 License

This project is open-source and released under the **MIT License**. It was developed strictly for demonstration, evaluation, and 
