import json
# import load_json to load json files
from src.python_fundamental.json_operations.load_json import load_json

# update a specific json file
def update_json(file_path, key, value):
    # load json file and store in data
    data = load_json(file_path)
    data[key] = value

    # write in json file to update
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)