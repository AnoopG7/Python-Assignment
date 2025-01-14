# Reverse a list in-place (without using reversed() or slicing).
def reverse_list(numbers):
    start = 0
    end = len(numbers) - 1
    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1

numbers = []
for i in range(5):
    numbers.append(int(input(f"Enter number {i+1}: ")))
reverse_list(numbers)
print("Reversed list:", numbers)