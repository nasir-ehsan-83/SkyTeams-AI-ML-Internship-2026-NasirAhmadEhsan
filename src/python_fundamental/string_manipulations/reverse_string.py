def reverse(text: str) -> str:
    new_text = ""

    # reverse text
    i = len(text) - 1
    while i >= 0:
        new_text += text[i]
        i -= 1

    return new_text