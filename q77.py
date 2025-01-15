# Write a program that prompts the user for a line of text and writes that line to a file.
filename = input("Enter filename to write to: ")
line = input("Enter text: ")
with open(filename, 'w') as file:
    file.write(line)
