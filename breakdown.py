def calculate_contributions_and_growth(principal, monthly_contribution, years, rate, compounds_per_year):
    """
    Calculate the total contributions and growth from interest.
    
    :param principal: Initial amount (P)
    :param monthly_contribution: Monthly recurring contribution (C)
    :param years: Number of years (t)
    :param rate: Annual interest rate (decimal form)
    :param compounds_per_year: Number of times interest compounds per year (n)
    :return: Total Contributions, Interest Growth
    """
    # Calculate total contributions
    total_contributions = monthly_contribution * 12 * years
    
    # Calculate growth from interest for the initial principal
    interest_growth = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years) - principal
    
    return total_contributions, interest_growth

