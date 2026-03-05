from typing import Optional

def max_value(list: list[int]) -> int:
    # store nothing if list is empty
    max: Optional[int] = None

    if len(list) != 0:
        # store the first element of list as maximum value
        max = list[0]
        for i in list:
            # if i is greater than max, swap the max by i
            if i > max:
                max = i

    return max

def min_value(list: list[int]):
    # store nothing if list is empty
    min: Optional[int] = None

    if len(list) != 0:
        # store the first element of list as minimum value
        min = list[0]
        for j in list:
            # if j is less than min, swap the min by j
            if j < min:
                min = j

    return min
