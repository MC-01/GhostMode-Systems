# GhostMode: Intelligent Product Delivery Skill for IBM Bob 2.0

> **Empowering Product Managers to deliver, verify, and approve technical changes with absolute confidence.**
> Built for the **IBM TechXchange 2026 Pre-conference Dev Day Hackathon** (August 28–30, 2026).

---

## 🚀 The Hypothesis

**A Product Manager with basic Python and GitHub knowledge can autonomously deliver a high-integrity, compliant production release without a dedicated engineering team, using IBM Bob 2.0 and the Plan → Implement → Verify → Explore methodology.**

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
* `users` - Customer identity and KYC tier.
* `wallets` - Wallet balances and currency types (including digital fiat/CBDC).
* `transactions` - Transaction ledgers, timestamps, and routing info.
* `merchants` - Merchant classification and high-risk flags.
* `compliance_rules` - Dynamic limits and regulatory requirements.
* `currencies` - Supported currency configurations.

---

## 🛠️ Key IBM Bob 2.0 Features Utilised

To deliver maximum impact in a robust, stable, and highly professional manner, GhostMode leverages the advanced features of the Bob 2.0 architecture:

1. **Agent Mode**: For autonomous execution of the database schema updates and validation test scripts [5, 7].
2. **Subagents / Parallel Tasks**: Used to process release notes, compile schema documentation in HTML, and analyze git histories concurrently without overloading the main session's token context [5, 7].
3. **Document Understanding**: Bob analyzes our official regulatory PDF (`FINOVA_Regulatory_Standards_2026.pdf`) to match technical SQL alterations with strict financial compliance rules (e.g. flagging any transactions exceeding KYC threshold limits without proper verification steps) [5, 7].
4. **Custom Modes & Rules**: A restricted custom mode `product-delivery-pm` configured in `.bop/custom_modes.yaml` to give Bob the persona of a risk-aware PM while restricting write access during analytical phases.
5. **Lifecycle Hooks**: Configured in `.bop/hooks/settings.json` to execute deterministic backend validation tests (`verify_compliance.py`) automatically before any change is allowed to be packaged into a Pull Request.

---

## 📋 The Ghost Decision Card (End Deliverable)

The output of the GhostMode skill is a highly structured, automated Markdown (and rendered HTML) document that details the proposed change:

* **Business Objective**: The high-level intent of the change.
* **Database Impact**: Clear explanation of table additions, column drops, or modification risks.
* **Compliance / AML Impact**: Analysis of whether the change violates or alters any regulatory rules based on the compliance PDF.
* **Test Status**: Deterministic test outcomes (Passed / Failed) from the Hook validations.
* **Risk Level**: (Low / Medium / High) with business rationale.
* **Recommendation**: Actionable advice for the PM (e.g., "Safe to merge", "Needs compliance override").

---

## 🗂️ Project Directory Structure

```text
FINOVA-Repo/
├── .bop/
│   ├── custom_modes.yaml     # Persona and permission boundaries
│   ├── rules/
│   │   └── compliance.md     # Structural and compliance rules for Bob
│   ├── skills/
│   │   └── ghost_decision.md # Core execution prompt for GhostMode Skill
│   └── hooks/
│       └── settings.json     # Lifecycle Hooks mapping to python validations
├── database/
│   ├── finova.db             # SQLite database
│   └── data_dictionary.json  # Schema explanation mapping
├── docs/
│   └── FINOVA_Compliance_2026.pdf # Regulatory PDF for Document Understanding
├── verify_compliance.py      # Deterministic validation script (Verify phase)
└── README.md                 # Project manifesto and documentation
```

---

## ⏱️ How to Run and Demo

Detailed step-by-step instructions on triggering GhostMode, executing the validation hook, and viewing the generated **Ghost Decision Card** within IBM Bob 2.0. 
*(To be completed during the active Hackathon phase starting August 28, 10:00 AM ET).*
