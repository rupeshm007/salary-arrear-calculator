def calculate_arrear(data, leave_data):

    results = []
    leave_results = []
    total = 0

    for month, basic in sorted(data.items()):

        # arrear percentage
        if month <= "2023-05":
            percent = 0.35
        else:
            percent = 0.15

        # arrear calculation
        arrear = round(basic * percent)

        # revised basic (always +35%)
        revised_basic = round(basic + (basic * 0.35))

        results.append({
            "month": month,
            "basic": basic,
            "percent": percent * 100,
            "arrear": arrear,
            "revised_basic": revised_basic
        })

        total += arrear


    # Leave surrender calculation
    for key, amount in leave_data.items():

        year = key.replace("leave_", "")

        arrear = round(amount * 0.35)

        leave_results.append({
            "year": year,
            "amount": amount,
            "arrear": arrear
        })

        total += arrear


    total = round(total)

    return results, leave_results, total