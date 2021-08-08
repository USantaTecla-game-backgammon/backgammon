from typing import Optional
from src.models.dice import Dice
from src.models.doubling_cube import DoublingCube
from src.models.move import Move
from src.types import Color


class Player:
    def __init__(self, color: Color) -> None:
        self.color = color
        self.score: int = 0
        self.doubling_cube: Optional[DoublingCube] = None
        self.movements: list[Move] = []
        self.rolls: list[Dice] = []

    @classmethod
    def roll(cls, amount: int = 2) -> list[Dice]:
        return [Dice() for _ in range(amount)]
