# Find the minimum and maximum values in a list without using built-in min() or max().
def find_min_max(numbers):
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

numbers = []
for i in range(5):
    numbers.append(int(input(f"Enter number {i+1}: ")))
min_val, max_val = find_min_max(numbers)
print("Minimum value:", min_val)
print("Maximum value:", max_val)