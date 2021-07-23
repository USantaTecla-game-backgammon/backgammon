from src.models.dice import Dice
from src.types.color import Color


class Player:
    def __init__(self, color: Color):
        self.color = color
        self.__rolled: list[Dice] = []

    @property
    def rolled(self) -> list[Dice]:
        return self.__rolled

    def roll(self, amount: int = 2) -> None:
        self.__rolled = [Dice() for _ in range(amount)]
