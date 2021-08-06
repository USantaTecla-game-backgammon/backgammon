from __future__ import annotations

from src.models.game import Game
from src.models.turn import Turn


class Match:
    def __init__(self) -> None:
        self.games: list[Game] = []
        self.goal: int = 0
        self.turn: Turn = Turn()

    def is_goal(self) -> bool:
        raise NotImplementedError
