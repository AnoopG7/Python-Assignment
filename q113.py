# Use filter to filter out even numbers from a list, then use functools.reduce to sum the filtered numbers.

from functools import reduce

# Sample list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Sum the filtered numbers using reduce
sum_even = reduce(lambda x, y: x + y, even_numbers)

print("Sum of even numbers:", sum_even)