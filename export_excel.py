import pandas as pd
import os

def create_excel(results, leave_results, total):
    """
    Create Excel file with arrear calculations
    
    Args:
        results: List of salary arrear results
        leave_results: List of leave surrender results
        total: Total arrear amount
    
    Returns:
        str: Path to created Excel file
    """
    data = []

    # salary arrear rows
    for r in results:
        data.append({
            "Type": "Salary",
            "Month": r["month"],
            "Basic Pay": r["basic"],
            "Arrear %": r["percent"],
            "Arrear": r["arrear"],
            "Revised Basic": r["revised_basic"]
        })

    # leave surrender rows
    for r in leave_results:
        data.append({
            "Type": "Leave Surrender",
            "Month": r["year"],
            "Basic Pay": r["amount"],
            "Arrear %": 35,
            "Arrear": r["arrear"],
            "Revised Basic": ""
        })

    # Add total row
    if data:
        data.append({
            "Type": "TOTAL",
            "Month": "",
            "Basic Pay": "",
            "Arrear %": "",
            "Arrear": total,
            "Revised Basic": ""
        })

    # Create DataFrame
    df = pd.DataFrame(data)

    # Generate filename with timestamp to avoid caching
    file = "arrear_statement.xlsx"

    # Write to Excel
    with pd.ExcelWriter(file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Arrear Statement', index=False)

    return file