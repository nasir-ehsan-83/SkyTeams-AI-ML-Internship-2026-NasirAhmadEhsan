def is_prtime(number: int) -> bool:
    # if the number is not divisible by 2, 3, 5 is a prime number
    return number % 2 != 0 and number % 3 != 0 and number % 5 != 0