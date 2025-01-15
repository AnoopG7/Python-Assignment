# Write a Python program to copy the contents of one file to another.
source = input("Enter source filename: ")
destination = input("Enter destination filename: ")
try:
    with open(source, 'r') as src_file:
        with open(destination, 'w') as dest_file:
            dest_file.write(src_file.read())
except FileNotFoundError:
    print("Source file not found.")
