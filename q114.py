# - Write a script that demonstrates the difference between a list comprehension and a generator expression for large data.

import time

# List comprehension
start_time = time.time()
list_comp = [x * 2 for x in range(1000000)]  # Creating a list
end_time = time.time()
print(f"List comprehension time: {end_time - start_time} seconds")

# Generator expression
start_time = time.time()
gen_exp = (x * 2 for x in range(1000000))  # Creating a generator
end_time = time.time()
print(f"Generator expression time: {end_time - start_time} seconds")

# Using list to consume generator
start_time = time.time()
gen_list = list(gen_exp)
end_time = time.time()
print(f"Converting generator to list time: {end_time - start_time} seconds")
