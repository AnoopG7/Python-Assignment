# Prompt the user for a string and write it to a new text file.
text = input("Enter the text to write to the file: ")
filename = input("Enter the filename to write to: ")
with open(filename, 'w') as file:
    file.write(text)
print("Text written to the file successfully.")