# Write a program that appends a user-input line to an existing file without overwriting it.
filename = input("Enter filename to append to: ")
line = input("Enter line to append: ")
try:
    with open(filename, 'a') as file:
        file.write(line + '\n')
    print("Line appended successfully.")
except FileNotFoundError:
    print("File not found.")
