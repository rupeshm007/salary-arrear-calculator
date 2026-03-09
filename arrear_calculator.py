def calculate_arrear(data, leave_data):
    """
    Calculate arrear amounts based on monthly salary data and leave surrender data
    
    Args:
        data: Dictionary of month -> salary amount
        leave_data: Dictionary of leave year -> amount
    
    Returns:
        tuple: (results list, leave_results list, total amount)
    """
    results = []
    leave_results = []
    total = 0

    # Process monthly salary data
    for month, basic in sorted(data.items()):
        
        # Ensure basic is a number
        try:
            basic = float(basic)
        except (TypeError, ValueError):
            continue  # Skip invalid entries
        
        # arrear percentage based on date
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
            "percent": int(percent * 100),  # Convert to integer percentage
            "arrear": arrear,
            "revised_basic": revised_basic
        })

        total += arrear

    # Process leave surrender data
    for key, amount in leave_data.items():
        
        # Ensure amount is a number
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            continue  # Skip invalid entries
        
        year = key.replace("leave_", "")
        
        # Calculate 35% arrear on leave amount
        arrear = round(amount * 0.35)

        leave_results.append({
            "year": year,
            "amount": amount,
            "arrear": arrear
        })

        total += arrear

    total = round(total)

    return results, leave_results, total