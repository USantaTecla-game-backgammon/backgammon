from typing import Optional

from src.models.player import Player
from src.types.color import Color


class Turn:
    def __init__(self, players: tuple[Player, Player]):
        assert len(players) == 2
        self.players = players
        self.current_player: Optional[Player] = None

    def change(self, color: Optional[Color] = None) -> None:
        if self.current_player is None and color is None:
            raise AssertionError

        if color is None:
            if self.current_player == self.players[0]:
                self.current_player = self.players[1]
            else:
                self.current_player = self.players[0]
            return

        for player in self.players:
            if player.color == color:
                self.current_player = player
