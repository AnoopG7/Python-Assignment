# Given a list of integers, prompt for a specific integer and count how many times it appears.
numbers = [10, 20, 30, 10, 40, 10]
target = int(input("Enter a number to count its occurrences: "))
count = numbers.count(target)
print(f"The number {target} appears {count} times.")