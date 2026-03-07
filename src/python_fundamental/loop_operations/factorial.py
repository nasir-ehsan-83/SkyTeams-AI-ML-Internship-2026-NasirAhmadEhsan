from typing import Optional

# add this function for input validation(is inputer greater or equal to 0)
def fact_loop(number: int) -> Optional[int]:
    # if number positive or 0
    if number >= 0:
        __fact_loop(number)
    else:
        return None

# compute factorial by loop
def __fact_loop(number: int) -> int:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    return factorial

# add this function for input validation(is input greater or equal to 0)
def fact_recursion(number: int) -> Optional[int]:
    # if number positive or 0
    if number >= 0:
        __fact_recursion(number)
    else:
        return None

# compute factorial by recursion
def __fact_recursion(number: int) -> int:
    if number == 0:
        return 1
    return number * __fact_recursion(number - 1)
    