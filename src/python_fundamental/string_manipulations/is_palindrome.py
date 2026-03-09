from typing import List

from reverse_string import reverse

def is_palindrome(text: str) -> bool:
    if text.__contains__(" "):
        word_list: List[int] = text.split(" ")
    
        i: int = 0
        j: int = len(word_list) - 1
        n: int = len(word_list) // 2

        while i <= n <= j:
            key: str = word_list[i]
            word_list[i] = word_list[j]
            word_list[j] = key

            i += 1
            j -= 1
        
        return text.split(" ") == word_list
    
    # if text is a word and it's reversed case are equal means that the text is palindrome
    return text == reverse(text)
