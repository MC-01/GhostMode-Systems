-- Scenario 1: SAFE TO MERGE
-- Add kyc_verified column to transactions table
ALTER TABLE transactions ADD COLUMN kyc_verified BOOLEAN DEFAULT FALSE;
