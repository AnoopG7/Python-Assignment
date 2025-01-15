# Write a program that counts how many lines are in a file.
filename = input("Enter filename to count lines: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))
except FileNotFoundError:
    print("File not found.")
