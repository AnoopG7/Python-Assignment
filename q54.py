# Read a file and count how many lines it contains.
filename = input("Enter the filename to count lines: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    print("Total number of lines:", len(lines))
except FileNotFoundError:
    print("File not found.")
