# Implement a function factorial(n) that calculates n! using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

x=int(input("Enter the number to find factorial"))
print("Factorial of", x, "is",  factorial(x))
