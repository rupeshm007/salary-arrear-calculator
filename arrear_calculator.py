def calculate_arrear(data):

    results=[]
    total=0

    for month,basic in sorted(data.items()):

        if month <= "2023-05":
            percent=0.35
        else:
            percent=0.15

        arrear=basic*percent

        results.append({
            "month":month,
            "basic":basic,
            "percent":percent*100,
            "arrear":round(arrear,2)
        })

        total+=arrear

    return results,round(total,2)