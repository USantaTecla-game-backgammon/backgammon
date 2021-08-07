import random
from typing import Optional


class Dice:
    def __init__(self, value: Optional[int] = None) -> None:
        if value:
            self._value = value
        else:
            self._value = random.randint(1, 6)

    @property
    def value(self) -> int:
        return self._value

    def __cmp__(self, other: 'Dice') -> int:
        return self.value - other.value

    def __lt__(self, other: 'Dice') -> int:
        return self.value < other.value

    def __str__(self) -> str:
        return str(self._value)
