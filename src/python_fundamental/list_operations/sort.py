def insertion_sort(arr: list[int]):
    length: int = len(arr)
    
    for i in range(0, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr: list[int]):
    __merge_sort(arr, 0, len(arr) - 1)

def __merge_sort(arr: list[int], start_index: int, end_index: int):
    if start_index >= end_index:
        return 
    else:
        middle_index = start_index + (end_index - start_index) // 2

        __merge_sort(arr, start_index, middle_index)
        __merge_sort(arr, middle_index + 1, end_index)
        __merge(arr, start_index, middle_index, end_index)

def __merge(arr: list[int], start_index: int, middle_index: int, end_index: int):
    
    left_arr_length = middle_index - start_index + 1
    rigth_arr_length = end_index - middle_index

    left_arr = [0 for n in range(left_arr_length)]
    rigth_arr = [0 for n in range(rigth_arr_length)]

    for i in range(left_arr_length):
        left_arr[i] = arr[start_index + i]

    for j in range(rigth_arr_length):
        rigth_arr[j] = arr[middle_index + j + 1]

    i = 0
    j = 0 
    k = start_index

    while i < left_arr_length and j < rigth_arr_length:
        if left_arr[i] <= rigth_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = rigth_arr[j]
            j += 1
        k += 1

    while i < left_arr_length:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < rigth_arr_length:
        arr[k] = rigth_arr[j]
        j += 1
        k += 1