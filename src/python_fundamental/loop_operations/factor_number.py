# compute all prime factor of a number
def factors_of_number(number: int):
    if number != 0:
        __factors_of_number(number)
    return None

def __factors_of_number(number: int) -> list[int]:
    # add 1 as first factor
    factors = [1]
    # store number in tem_number to performe some operation on it
    temp_number = number

    while True:
        # if temp_number is divisible by 2 means that 2 is a factor of number
        if temp_number % 2 == 0:
            temp_number //= 2
            factors.append(2)
        # if temp_number is divisibale by 3 means that 3 is a factor of number
        elif temp_number % 3 == 0:
            temp_number //= 3
            factors.append(3)
        # if temp_number is divisible by 5 means that 5 is a factor of number
        elif temp_number % 5 == 0:
            temp_number //= 5
            factors.append(5)
        else:
            break
    if -1 != temp_number != 1:
        factors.append(temp_number)
    factors.append(number)
    return factors
