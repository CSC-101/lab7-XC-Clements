from typing import Optional


def str_to_float(input_string:str) -> Optional[float]:
    try:
        return float(input_string)
    except ValueError:
        return None
