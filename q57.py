# Search for a specific word in a file and replace it with another word, then overwrite the file with the changes.
filename = input("Enter the filename to search and replace: ")
word_to_find = input("Enter the word to find: ")
word_to_replace = input("Enter the word to replace with: ")

try:
    with open(filename, 'r') as file:
        content = file.read()

    content = content.replace(word_to_find, word_to_replace)

    with open(filename, 'w') as file:
        file.write(content)

    print(f"Replaced '{word_to_find}' with '{word_to_replace}' in {filename}.")
except FileNotFoundError:
    print("File not found.")
