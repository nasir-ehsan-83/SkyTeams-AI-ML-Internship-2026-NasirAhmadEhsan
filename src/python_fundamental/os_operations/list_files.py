import os

# list of all files in a specific directory
def list_files(path: str):
    # if the path exists return list of all files
    if os.path.exists(path):
        return os.listdir(path)
    
    # if the path does not exist return None
    return None