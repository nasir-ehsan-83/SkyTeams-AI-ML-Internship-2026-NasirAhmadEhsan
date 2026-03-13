from src.python_fundamental.file_operations.io_file_handler.reader import read_lines

# Count the number of lines in a file
def line_count(file) -> int:
    lines = read_lines(file)
    return len(lines)