# Write a program to search for a specific substring in a file and print the lines where it appears.
filename = input("Enter filename: ")
search_string = input("Enter substring to search for: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, start=1):
            if search_string in line:
                print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print("File not found.")
