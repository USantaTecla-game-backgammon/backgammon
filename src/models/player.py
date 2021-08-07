from src.models.dice import Dice
from src.types import Color


class Player:
    def __init__(self, color: Color):
        self.color = color
        self.score: int = 0

    def roll(self, amount: int = 2) -> list[Dice]:
        return [Dice() for _ in range(amount)]
