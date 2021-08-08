import enum
from typing import List

ONLY_NUMBERS_ARE_ALLOWED: str = 'Only numbers are allowed'
ALLOWED_VALUES: str = 'allowed values: '


class FontColors(str, enum.Enum):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLACK = '\033[0m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def show_in_color(msg: str, font_color: FontColors) -> None:
    print(font_color.value, end='')
    print(msg)
    print(FontColors.ENDC.value, end='')


def show(msg: str) -> None:
    print(msg)


def read_str(msg: str = '') -> str:
    while True:
        user_input: str = input(msg + ': ')
        if user_input:
            break
    return user_input


def read_int(msg: str = '') -> int:
    user_str: str = read_str(msg)
    try:
        user_int: int = int(user_str)
        return user_int
    except ValueError:
        show(ONLY_NUMBERS_ARE_ALLOWED)
        return read_int(msg)


def read_int_range(valids: List[int], msg: str = '') -> int:
    user_int: int = read_int(msg)
    if user_int not in valids:
        print(ALLOWED_VALUES, valids)
        return read_int_range(valids, msg)
    return user_int


def read_bool(msg: str = '') -> bool:
    raise NotImplementedError
