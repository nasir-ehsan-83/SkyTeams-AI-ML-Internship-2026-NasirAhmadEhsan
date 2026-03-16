from typing import Optional

def validate_int_convert(value: float | str) -> Optional[int]:
    try:
        return int(value)
    except ValueError:
        return None