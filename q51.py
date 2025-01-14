# Write a program that reads a text file and prints its contents to the screen.
filename = input("Enter the filename to read from: ")
try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found. Please check the filename and path.")
