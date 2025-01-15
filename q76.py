# Write a Python script that reads a text file and prints its contents.
filename = input("Enter filename to read: ")
try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
