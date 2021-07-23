import random


class Dice:
    def __init__(self) -> None:
        self.__value = random.randint(1, 6)

    @property
    def value(self) -> int:
        return self.__value

    def __cmp__(self, other: 'Dice') -> int:
        return self.value - other.value
