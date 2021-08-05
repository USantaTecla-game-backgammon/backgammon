from src.models.dice import Dice
from src.types import Color


class Player:
    def __init__(self, color: Color):
        self.color = color
        self._dices: list[Dice] = []

    @property
    def dices(self) -> list[Dice]:
        return self._dices

    def roll(self, amount: int = 2) -> None:
        self._dices = [Dice() for _ in range(amount)]
