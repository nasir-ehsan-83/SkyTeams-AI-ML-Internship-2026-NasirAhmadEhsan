def validate_keys(data, required_keys):
    return all(k in data for k in required_keys)