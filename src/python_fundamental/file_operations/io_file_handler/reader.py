from typing import List


# Read all lines from a file
def read_lines(file) -> List[str]:
    file.seek(0)
    return file.readlines()

# Read the entire file as text
def read_text(file) -> str:
    file.seek(0)
    return file.read()
