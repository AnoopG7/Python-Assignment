# Prompt for principal, rate, and time to calculate compound interest.
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in %): "))
time = float(input("Enter time (in years): "))
compound_interest = principal * (1 + rate / 100) ** time - principal
print("The compound interest is:", compound_interest)