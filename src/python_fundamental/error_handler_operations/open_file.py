# create this class to handle custom exceptions
class FileNotFound(Exception):
    pass

def open_file_safe(file_path: str):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFound(f"File '{file_path}' does not exist.")