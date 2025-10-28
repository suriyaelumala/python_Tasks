# JSON Handling in Python
# This shows encoding/decoding JSON data.

import json

# Python dict to JSON string
data = {"name": "Alice", "age": 25, "city": "New York"}
json_string = json.dumps(data)
print("JSON string:", json_string)

# JSON string to Python dict
parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)

# Writing to JSON file
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading from JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print("Loaded from file:", loaded_data)