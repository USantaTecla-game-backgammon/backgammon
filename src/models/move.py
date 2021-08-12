from __future__ import annotations
from typing import Optional

from src.types import Position


class Move:
    def __init__(
        self,
        position_from: Position,
        position_to: Optional[Position] = None,
        dice_value: int = 0
    ) -> None:
        if position_to is None:
            tmp_position_to = position_from - dice_value
            if tmp_position_to < 0:
                tmp_position_to = 0
            position_to = Position(tmp_position_to)

        self.position_from = position_from
        self.position_to = position_to
        self.dice_value = dice_value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Move):
            return False

        return (
            self.position_from == other.position_from and
            self.position_to == other.position_to and
            self.dice_value == other.dice_value
        )

    def __str__(self) -> str:
        return f'from {self.position_from} to {self.position_to} (dice {self.dice_value})'
