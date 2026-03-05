from sort import insertion_sort

def count_of_frequency(list: list[int]) -> dict[int]:
    # sort the list for better formatting
    insertion_sort(list)
    
    # store element and it's count as a dictionary
    element_frequency: dict[int:int] = {}

    for i in list:
        count = 0
        if i in element_frequency.keys():
            continue
        else:
            for j in list:
                if j == i: 
                    count += 1
        # add element and it's count
        element_frequency.update({i: count})

    return element_frequency
