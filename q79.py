# Write a Python program that reads a file and counts the number of words in it.
filename = input("Enter filename to count words: ")
try:
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        print("Number of words:", len(words))
except FileNotFoundError:
    print("File not found.")
