from typing import List

from src.python_fundamental.file_operations.io_file_handler.reader import read_lines

# Count the number of words in a file
def word_count(file) -> int:
    lines = read_lines(file)
    words: List[str] = []
    
    for line in lines:
        words.extend(line.split())
    
    return len(words)