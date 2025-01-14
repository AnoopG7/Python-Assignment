# Calculate the factorial of a number using a for loop.
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))