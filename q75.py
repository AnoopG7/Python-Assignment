# Write a recursive function to compute the Greatest Common Divisor (GCD) of two numbers.
def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)

# Example usage
num1, num2 = 48, 18
print("GCD:", gcd_recursive(num1, num2))
