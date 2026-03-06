def invert_dictionary(orginal_dict: dict[str : str]) -> dict[str : str]:
    inverted_dict: dict[str : str] = {}

    # Manual iteration over keys
    for key in orginal_dict:
        # swap key and value
        value: str = orginal_dict[key]
        inverted_dict[value] = key

    return inverted_dict
