import os

# delete a file in a specific path
def delete_file(path: str):
    # if the path exists
    if os.path.exists(path):
        os.remove(str(path))