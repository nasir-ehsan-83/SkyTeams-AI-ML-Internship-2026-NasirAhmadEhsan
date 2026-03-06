def find_common_elements(list1: list[int], list2: list[int]) -> list[int]:
    common: list[int] = []

    for item in list1:
        # Check if item exists in list2 and not already in common
        if item in list2:
            exists: bool = False
            
            for x in common:
                if x ==  item:
                    exists = True

                    break
            if not exists:
                common.append(item)

    return common

