# Prompt for a string and replace all occurrences of a specific character with another.
s = input("Enter the string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
replaced_string = s.replace(old_char, new_char)
print("Updated string:", replaced_string)