from typing import Optional

def is_prime(number: int) -> Optional[bool]:
    # if the number is not divisible by 2, 3, 5 is a prime number
    if number != 0:
        return number % 2 != 0 and number % 3 != 0 and number % 5 != 0
    else:
        return None