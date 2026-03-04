import pandas as pd

def create_excel(results, leave_results, total):

    data=[]

    # salary arrear rows
    for r in results:

        data.append({
            "Type":"Salary",
            "Month":r["month"],
            "Basic Pay":r["basic"],
            "Arrear %":r["percent"],
            "Arrear":r["arrear"],
            "Revised Basic":r["revised_basic"]
        })


    # leave surrender rows
    for r in leave_results:

        data.append({
            "Type":"Leave Surrender",
            "Month":r["year"],
            "Basic Pay":r["amount"],
            "Arrear %":35,
            "Arrear":r["arrear"],
            "Revised Basic":""
        })


    df=pd.DataFrame(data)

    file="arrear_statement.xlsx"

    df.to_excel(file,index=False)

    return file