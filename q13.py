# Demonstrate various string slicing operations (e.g., reverse a string, skip letters).
s = input("Enter a string ")
print("Reversed string:", s[::-1])  # Reverse the string
print("Skipping every second letter:", s[::2])  # Skip every second letter
print("Substring (index 2 to 5):", s[2:6])  # Slice from index 2 to 5