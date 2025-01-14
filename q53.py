# Copy the contents of one text file to another.
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

try:
    with open(source_file, 'r') as source:
        content = source.read()

    with open(destination_file, 'w') as destination:
        destination.write(content)

    print(f"Contents copied from {source_file} to {destination_file}")
except FileNotFoundError:
    print("Source file not found.")
