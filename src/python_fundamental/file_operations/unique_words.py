# Find all unique words
from typing import List

from src.python_fundamental.file_operations.io_file_handler.reader import read_lines
from src.python_fundamental.file_operations.frequency_counter import frequency_count

# Find unique words
def unique_words(file) -> List[str]:
    lines = read_lines(file)

    words: List[str] = []

    for line in lines:
        words.extend(line.split())

    words_frequency = frequency_count(words)

    unique_words = [word for word, count in words_frequency.items() if count == 1]

    return unique_words
