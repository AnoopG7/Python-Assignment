# Prompt the user for 5 integers and store them in a list. Print the list and its length.
numbers = []
for i in range(5):
    numbers.append(int(input(f"Enter number {i+1}: ")))
print("List of numbers:", numbers)
print("Length of list:", len(numbers))