from typing import List, Dict

# Count frequency of each word
def frequency_count(words: List[str]) -> Dict[str, int]:
    frequency: Dict[str, int] = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency