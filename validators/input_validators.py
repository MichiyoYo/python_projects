from typing import List


def is_num(input_str: str) -> int:
    """checks if the input string is a number

    Args:
        input_str (str): the input string to be validated
    """
    if not input_str.isdigit():
        raise ValueError("Invalid value, pick a number")
    else:
        return int(input_str)


def is_valid_char(input_str: str, valid_options: List[str]) -> str:
    """Checks if the input string is a valid option

    Args:
        input_str (str): the input string to be validated
        valid_options (List[str]): a list of valid options
    """
    if not input_str in valid_options:
        raise ValueError(f"Invalid option, please pick one of {valid_options}")
    else:
        return input_str
