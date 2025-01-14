# Using the GCD function, write a function lcm(a, b) that returns the least common multiple.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("LCM:", lcm(a, b))

