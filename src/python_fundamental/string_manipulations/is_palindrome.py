from reverse_string import reverse

def is_palindrome(text: str) -> bool:
    # if text and it's reversed case are equeal means that text is palindrome
    return text == reverse(text)
