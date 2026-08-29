-- Scenario 2: BLOCKED (HIGH RISK)
-- Increase Tier 2 transaction limit from €5,000 to €10,000
UPDATE compliance_rules SET max_transaction_limit = 10000 WHERE kyc_tier_required = 'Tier 2';
