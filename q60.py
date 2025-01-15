import json

# Read data from a JSON file, modify a value, and write the updated data back to the file.
filename = input("Enter the JSON filename: ")

try:
    with open(filename, 'r') as file:
        data = json.load(file)

    # Modify data
    key = input("Enter the key to modify: ")
    new_value = input("Enter the new value: ")
    data[key] = new_value

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Updated {key} in {filename} to {new_value}.")
except FileNotFoundError:
    print("JSON file not found.")
except json.JSONDecodeError:
    print("Error: The file is not properly formatted as JSON.")
