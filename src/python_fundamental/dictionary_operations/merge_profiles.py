def merge_dictionary(profile_a: dict[str : str], profile_b: dict[str : str]) -> dict[str : str]:
    merged_dict: dict[str : str] = {}

    # Copy first profile(profile_a)
    for key in profile_a:
        merged_dict[key] = profile_a[key]

    # Copy/overwrite with second profile(profile_b)
    for key in profile_b:
        merged_dict[key] = profile_b[key]

    return merged_dict
