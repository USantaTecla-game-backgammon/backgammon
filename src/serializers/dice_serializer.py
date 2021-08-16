from typing import Any
from src.models.dice import Dice


class DiceSerializer:
    def __init__(self, dice: Dice) -> None:
        self.value: int = dice.value
    
    def data(self) -> Any:
        return {'value': self.value}
