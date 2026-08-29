import os
import sys

def check_environment():
    print("=== [GhostMode Hook] SessionStart ===")
    
    # 1. Python version check
    python_version = sys.version_info
    print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro} ... OK")
    
    # 2. Database existence check
    db_exists = os.path.exists("finova.db")
    print(f"Database 'finova.db' existence: {'OK' if db_exists else 'MISSING'}")
    
    # 3. Compliance PDF existence check
    pdf_exists = os.path.exists("FINOVA_Compliance_2026.pdf")
    print(f"Compliance PDF 'FINOVA_Compliance_2026.pdf' existence: {'OK' if pdf_exists else 'MISSING'}")
    
    # 4. Data dictionary existence check
    dict_exists = os.path.exists("data_dictionary.json")
    print(f"Data Dictionary 'data_dictionary.json' existence: {'OK' if dict_exists else 'MISSING'}")
    
    print("=======================================")
    if not (db_exists and pdf_exists and dict_exists):
        print("⚠️ Warning: Some environment dependencies are missing. Run setup_ghostmode.py script.")
        
if __name__ == "__main__":
    check_environment()
