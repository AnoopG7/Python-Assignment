# Write a simple decorator timer that measures the execution time of a function.

import time

# Timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # End time
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

# Example function to decorate
@timer
def example_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

example_function()
