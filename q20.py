# Given a list of numbers, calculate and print the sum of the elements.
numbers = []
for i in range(5):
    numbers.append(int(input(f"Enter number {i+1}: ")))
print("Sum of list:", sum(numbers))
