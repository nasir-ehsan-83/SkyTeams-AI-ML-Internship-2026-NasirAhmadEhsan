# some of all natural numbers from 1 to n
def sum_of_natural_number(n: int) -> int:
    sum = 0
    for i in range(n):
        sum += i

    return sum

# sum of all odd numbers from 0 to n
def sum_of_odd_number(n: int) -> int:
    sum_of_odd = 0

    for i in range(n):
        if i % 2 != 0:
            sum_of_odd += i
    
    return sum_of_odd

# sum of all even numbers from 0 to n
def sum_of_even_number(n: int) -> int:
    sum_of_even = 0

    for i in range(n):
        if i % 2 == 0:
            sum_of_even += i

    return sum_of_even