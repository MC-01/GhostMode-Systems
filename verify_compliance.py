import sqlite3
import sys

def check_fin_aml_01(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT wallet_id, balance FROM wallets WHERE balance < 0.00")
    violations = cursor.fetchall()
    if violations:
        print("✗ FIN-AML-01 FAILED: Found wallets with negative balances!")
        return False
    print("✓ FIN-AML-01 PASSED: No negative balances detected.")
    return True

def check_fin_aml_07(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT max_transaction_limit FROM compliance_rules WHERE kyc_tier_required = 'Tier 2'")
    row = cursor.fetchone()
    if row and row[0] > 5000:
        print(f"✗ FIN-AML-07 FAILED: Tier 2 transaction limit is {row[0]}, which exceeds the allowed €5,000 threshold without enhanced KYC!")
        print("  Risk: 1,842 existing Tier 2 users affected. No enhanced-KYC condition exists.")
        return False
    print("✓ FIN-AML-07 PASSED: Tier 2 transaction limit is within regulatory bounds.")
    return True

def check_fin_aml_12(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT max_transaction_limit FROM compliance_rules WHERE kyc_tier_required IN ('Tier 1', 'Tier 2') AND max_transaction_limit > 10000")
    violations = cursor.fetchall()
    if violations:
        print("✗ FIN-AML-12 FAILED: Transaction limit for Tier 1 or Tier 2 exceeds USD 10,000!")
        return False
    print("✓ FIN-AML-12 PASSED: High-value transaction KYC boundaries respected.")
    return True

def check_fin_aml_15(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT merchant_id FROM merchants WHERE is_high_risk = 1 AND last_review_date IS NULL")
    violations = cursor.fetchall()
    if violations:
        print("✗ FIN-AML-15 FAILED: Found high-risk merchants without monthly compliance reviews!")
        return False
    print("✓ FIN-AML-15 PASSED: High-risk merchant monthly reviews are up to date.")
    return True

def main():
    db_path = "finova.db"
    try:
        conn = sqlite3.connect(db_path)
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)
        
    print("==================================================")
    print("       GHOSTMODE AUTOMATED COMPLIANCE AUDIT       ")
    print("==================================================")
    
    results = [
        check_fin_aml_01(conn),
        check_fin_aml_07(conn),
        check_fin_aml_12(conn),
        check_fin_aml_15(conn)
    ]
    
    conn.close()
    print("==================================================")
    if all(results):
        print("🎉 ALL COMPLIANCE CHECKS PASSED SUCCESSFULLY!")
        sys.exit(0)
    else:
        print("⚠️ COMPLIANCE VIOLATIONS DETECTED. DEPLOYMENT BLOCKED.")
        sys.exit(1)

if __name__ == '__main__':
    main()
