# Write a program that finds the longest word in a text file and prints it.
filename = input("Enter filename: ")
try:
    with open(filename, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        print("Longest word:", longest_word)
except FileNotFoundError:
    print("File not found.")