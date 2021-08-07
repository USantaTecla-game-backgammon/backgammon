from typing import List

ONLY_NUMBERS_ARE_ALLOWED: str = 'Only numbers are allowed'
ALLOWED_VALUES: str = 'allowed values: '


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
