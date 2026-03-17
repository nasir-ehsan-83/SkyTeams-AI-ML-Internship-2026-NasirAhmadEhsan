import json

# load json
def load_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)