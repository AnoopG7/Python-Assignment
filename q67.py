# Implement a function fib(n) to return the nth Fibonacci number using recursion.
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

x=int(input("Enter the number to find Fibonacci"))
print("Fibonacci number at position", x, "is",  fib(6))