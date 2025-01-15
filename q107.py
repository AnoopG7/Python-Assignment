# Read a JSON file, modify a value, and write updated data back to the file.
import json

filename = 'data.json'
try:
    with open(filename, 'r') as file:
        data = json.load(file)
    data['key'] = 'new value'
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Updated data: {data}")
except FileNotFoundError:
    print("JSON file not found.")