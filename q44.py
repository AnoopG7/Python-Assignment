# Prompt for n and create a dictionary where each key is from 1 to n and each value is the square of the key.
n = int(input("Enter a number n: "))
squares_dict = {x: x**2 for x in range(1, n + 1)}
print("Dictionary of squares:", squares_dict)