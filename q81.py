# Modify the file-reading program to handle exceptions (e.g., file not found) gracefully.
filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{filename}'.")