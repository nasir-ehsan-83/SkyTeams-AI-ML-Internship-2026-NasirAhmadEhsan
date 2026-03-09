def count_of_vowel(text: str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0

    for i in text:
        if i in vowels:
            count += 1

    return count