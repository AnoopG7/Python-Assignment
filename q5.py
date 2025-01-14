# Write a program that swaps the values of two variables without using a temporary variable.
a = input("Enter first value: ")
b = input("Enter second value: ")
a, b = b, a
print("After swapping, first value:", a, "second value:", b)
