def safe_divide(number1: int | float, number2: int | float) -> int | str:
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "can not divide by zero"