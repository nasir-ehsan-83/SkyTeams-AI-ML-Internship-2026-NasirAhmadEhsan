# compute factorial by loop
def fact_loop(number: int) -> int:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    return factorial

# compute factorial by recursion
def fact_recursion(number: int) -> int:
    if number == 0:
        return 1
    return number * fact_recursion(number - 1)
    