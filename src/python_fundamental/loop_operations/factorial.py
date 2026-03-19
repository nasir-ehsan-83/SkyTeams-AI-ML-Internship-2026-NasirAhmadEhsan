from typing import Optional

# compute factorial by loop
def fact_loop(number: int) -> int:
    if number == 0:
        return 1
    elif number > 0:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i

        return factorial

    return None

# compute factorial by recursion
def fact_recursion(number: int) -> int:
    if number >= 0:
        if number == 0:
            return 1
        return number * fact_recursion(number - 1)
    
    return None