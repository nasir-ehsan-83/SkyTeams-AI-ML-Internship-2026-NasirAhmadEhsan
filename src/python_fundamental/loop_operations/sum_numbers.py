from typing import Optional

# some of all natural numbers from 1 to n
def sum_of_natural_number(number: int) -> Optional[int]:
    if number > 0:
        sum = 0
        for i in range(number):
            sum += i

        return sum

    return None

# sum of all odd numbers from 0 to n
def sum_of_odd_number(number: int) -> Optional[int]:
    if number >= 0:
        sum_of_odd = 0

        for i in range(number):
            if i % 2 != 0:
                sum_of_odd += i
        
        return sum_of_odd
    
    return None

# sum of all even numbers from 0 to n
def sum_of_even_number(number: int) -> Optional[int]:
    if number >= 0:
        sum_of_even = 0

        for i in range(number):
            if i % 2 == 0:
                sum_of_even += i

        return sum_of_even
    
    return None