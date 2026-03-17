import os

# create a diretory in specific path
def create_dir(path: str):
    # if the path does not exist
    if not os.path.exists(path):
        os.mkdir(path)
        