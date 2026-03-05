def reverse(list: list[int])-> list[int]:
    # storing reversed arr in another list
    reversed_list: list[int] = []

    i = len(list) - 1
    while i >= 0:
        reversed_list.append(list[i])
        i -= 1

    return reversed_list
