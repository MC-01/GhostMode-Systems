# GHOSTMODE – MASTER GENESIS & TECHNICAL SPECIFICATION v1.1

## IBM TechXchange 2026 Hackathon

---

### 1. OCENA ARCHITEKTONICZNA I PRODUKTOWA (Krytyczna Analiza)

1. **Dyscyplina zakresu (Scope Discipline):** Całkowite odrzucenie pomysłu budowania pełnej aplikacji fintechowej FINOVA na rzecz jednego, ultra-dopracowanego workflowu "Product Delivery". To właśnie wygrywa hackathony IBM – sędziowie wolą zobaczyć perfekcyjnie działający, innowacyjny proces AI niż niedokończoną, dziurawą aplikację.
2. **Koncepcja "Evidence-Backed Confidence":** Słuszna zmiana pozycjonowania. Słowo "evidence-backed" (poparte dowodami) natychmiast kieruje uwagę jury na proces weryfikacji (testy deterministyczne, dopasowanie do PDF).
3. **Konkretne Reguły Compliance:** Wybór 4 twardych, mierzalnych reguł w FINOVA Compliance PDF jest genialny, ponieważ pozwala łatwo napisać testy automatyczne i skrypty weryfikacyjne dla Boba.

---

## 2. GHOSTMODE CUSTOM MODE CONFIGURATION

### Plik: `.bop/custom_modes.yaml`
```yaml
modes:
  - id: product-delivery-pm
    name: GhostMode PM Assistant
    instructions: |
      You are GhostMode – an intelligent product delivery and deployment assistant for the Product Manager (PM) of the FINOVA Digital Wallet platform.
      Your primary objective is to translate technical codebase changes (such as git diffs and SQL schemas) into clear, business-driven product decisions and risk assessments.

      Always operate based on deterministic evidence (evidence-backed confidence). When the PM requests a release review, your job is to generate a "Ghost Decision Card".

      During your analysis:
      1. Retrieve the git diff or SQL migration schema.
      2. Analyze the changes using the database schema mappings from data_dictionary.json.
      3. Verify that the changes do not violate any regulatory compliance rules defined in the FINOVA_Compliance_2026.pdf document and the .bop/rules/compliance.md rulebook.
      4. Check the status of automated verification tests by executing the verify script (verify_compliance.py).
      5. Do not present raw SQL queries or code blocks to the PM unless explicitly requested. Focus entirely on the business implications, regulatory compliance, and risk.
    permissions:
      - read
      - execute
      - activate_skills
```
