from src.python_fundamental.file_operations.io_file_handler.reader import read_text
# Count all characters in the file
def character_count(file) -> int:

    text = read_text(file)
    return len(text)

# Count characters excluding whitespaces
def character_count_without_spaces(file) -> int:
    
    text = read_text(file)
    characters = [char for char in text if not char.isspace()]

    return len(characters)