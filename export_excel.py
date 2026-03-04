import pandas as pd

def create_excel(results):

    df=pd.DataFrame(results)

    file="arrear_statement.xlsx"

    df.to_excel(file,index=False)

    return file