import os
import sys

def main():
    command = " ".join(sys.argv[1:]).lower()
    if not command:
        command = os.getenv("BOB_COMMAND", "").lower()
        
    override = os.getenv("COMPLIANCE_OVERRIDE", "0") == "1"
    
    critical_tables = ["users", "wallets", "transactions"]
    destructive_patterns = ["drop table", "rm -rf", "delete from"]
    
    violates = False
    violation_reason = ""
    
    if "rm -rf" in command:
        violates = True
        violation_reason = "Use of 'rm -rf' is prohibited as a destructive system command."
        
    for table in critical_tables:
        if table in command:
            if "drop table" in command:
                violates = True
                violation_reason = f"DROP TABLE operation on critical table '{table}' is prohibited."
            elif "delete from" in command:
                violates = True
                violation_reason = f"DELETE FROM operation on critical table '{table}' is prohibited."
            elif "alter table" in command and "drop column" in command:
                violates = True
                violation_reason = f"DROP COLUMN operation on critical table '{table}' is prohibited."
                
    if violates:
        if override:
            print(f"⚠️ [GhostMode PreToolUse Warning] Command '{command}' contains restricted actions, but COMPLIANCE_OVERRIDE=1 is set. Proceeding...")
            sys.exit(0)
        else:
            print("==================================================")
            print("🛑 GHOSTMODE SECURITY HOOK: COMMAND BLOCKED!")
            print("==================================================")
            print(f"Violation: {violation_reason}")
            print("Policy: No Destructive Operations Without Override (Rule 1).")
            print("To bypass this safeguard in development, set environment variable COMPLIANCE_OVERRIDE=1.")
            print("==================================================")
            sys.exit(2)
            
    sys.exit(0)

if __name__ == "__main__":
    main()
