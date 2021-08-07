from typing import Optional

from src.models.player import Player
from src.types.color import Color


class Turn:
    def __init__(self, players: list[Player]):
        self.players = players
        self.current_player: Optional[Player] = None

    def next(self, color: Optional[Color] = None) -> None:
        raise NotImplementedError
