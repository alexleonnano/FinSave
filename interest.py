def calculate_compound_interest_with_contributions(principal, rate, years, compounds_per_year, monthly_contribution=0):
    """
    Calculate compound interest with recurring monthly contributions (assuming deposits are made at the beginning of the month).
    
    :param principal: Initial amount (P)
    :param rate: Annual interest rate in decimal (r)
    :param years: Number of years (t)
    :param compounds_per_year: Number of times interest compounds per year (n)
    :param monthly_contribution: Monthly recurring contribution (C)
    :return: Final amount (A)
    """
    # Calculate compound interest for initial principal
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)
    
    # Calculate compound interest for each monthly contribution
    if monthly_contribution > 0:
        total_contributions = 0
        months_total = years * 12  # Total number of months in the investment period
        
        for month in range(1, months_total + 1):
            # Each contribution is made at the beginning of the month and is compounded for the remaining time
            remaining_years = (months_total - month + 1) / 12  # Calculate the remaining years for the deposit
            contribution_amount = monthly_contribution * (1 + rate / compounds_per_year) ** (compounds_per_year * remaining_years)
            total_contributions += contribution_amount
        
        amount += total_contributions

    return amount
