# Prompt for principal, rate, and time to calculate simple interest.
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in %): "))
time = float(input("Enter time (in years): "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)