import json

# write in to json file
def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)