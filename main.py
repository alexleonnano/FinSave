from breakdown import calculate_contributions_and_growth
from exchange import get_exchange_rate
from interest import calculate_compound_interest_with_contributions

def main():
    base_currency = "EUR"
    target_currency = "COP"
    
    try:
        # Step 1: Ask if user wants to convert to COP
        convert_to_cop = input("Do you want to convert your savings to COP? (yes/no): ").strip().lower()

        # Step 2: Get exchange rate if converting to COP
        if convert_to_cop == "yes":
            rate = get_exchange_rate(base_currency, target_currency)
            print(f"1 {base_currency} = {rate:,.2f} {target_currency}")
        else:
            rate = 1  # No conversion if not converting to COP

        # Step 3: Allow user to input principal amount
        principal_eur = float(input("Enter the principal amount (in EUR): "))
        initial_savings = principal_eur * rate
        if convert_to_cop == "yes":
            print(f"Initial savings after conversion: {initial_savings:,.2f} COP")
        else:
            print(f"Initial savings: {initial_savings:,.2f} EUR")

        # Step 4: Allow user to input the interest rate
        interest_rate_percentage = float(input("Enter the annual interest rate (in %): "))
        interest_rate_decimal = interest_rate_percentage / 100  # Convert to decimal
        
        # Step 5: Allow user to input investment period (in years)
        years = int(input("Enter the investment period (in years): "))

        # Step 6: Ask for the compounding frequency
        print("\nChoose the compounding frequency:")
        print("1. Yearly")
        print("2. Monthly")
        print("3. Daily")
        compounding_choice = input("Enter your choice (1/2/3): ")

        # Set compounding frequency
        if compounding_choice == "1":
            compounds_per_year = 1  # Yearly compounding
        elif compounding_choice == "2":
            compounds_per_year = 12  # Monthly compounding
        elif compounding_choice == "3":
            compounds_per_year = 365  # Daily compounding
        else:
            print("Invalid choice! Defaulting to yearly compounding.")
            compounds_per_year = 1
        
        # Step 7: Ask if the user has recurring monthly savings
        recurring_contribution = input("Do you want to add a recurring monthly saving? (yes/no): ").strip().lower()
        if recurring_contribution == "yes":
            monthly_saving = float(input("Enter the recurring monthly saving amount (in EUR): "))
            monthly_saving *= rate  # Convert monthly saving to COP if needed
        else:
            monthly_saving = 0

        # Step 8: Calculate compound interest with recurring contributions
        final_amount = calculate_compound_interest_with_contributions(
            initial_savings, rate=interest_rate_decimal, years=years, compounds_per_year=compounds_per_year, monthly_contribution=monthly_saving)
        
        # Calculate the contributions and interest growth separately
        total_contributions, interest_growth = calculate_contributions_and_growth(initial_savings, monthly_saving, years, interest_rate_decimal, compounds_per_year)
        
        # Display the final result
        if convert_to_cop == "yes":
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"Final savings after {years} years with {compounds_per_year} compounding periods per year: {final_amount:,.2f} COP")
            print(f"Total contributions: {total_contributions:,.2f} COP")
            print(f"Growth from interest: {interest_growth:,.2f} COP")
        else:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"Final savings after {years} years with {compounds_per_year} compounding periods per year: {final_amount:,.2f} EUR")
            print(f"Total contributions: {total_contributions:,.2f} EUR")
            print(f"Growth from interest: {interest_growth:,.2f} EUR")
    except ValueError:
        print("Invalid input. Please enter numerical values where required.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
