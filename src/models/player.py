from typing import Optional
from src.models.dice import Dice
from src.models.doubling_cube import DoublingCube
from src.types import Color


class Player:
    def __init__(self, color: Color) -> None:
        self.color = color
        self.score: int = 0
        self.doubling_cube: Optional[DoublingCube] = None
        self.is_winner: bool = False

    @classmethod
    def roll(cls, amount: int = 2) -> list[Dice]:
        return [Dice() for _ in range(amount)]

    def earn_score(self, score: int) -> None:
        assert score > 0
        self.score += score
