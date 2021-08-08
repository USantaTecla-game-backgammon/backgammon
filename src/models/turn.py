from typing import Optional

from src.models.player import Player
from src.types.color import Color


class Turn:
    def __init__(self, players: tuple[Player, Player]):
        assert len(players) == 2
        self.players = players
        self.current_player: Player = players[0]

    def change(self, color: Optional[Color] = None) -> None:
        if color is not None:
            for player in self.players:
                if player.color == color:
                    self.current_player = player
        elif self.current_player == self.players[0]:
            self.current_player = self.players[1]
        elif self.current_player == self.players[1]:
            self.current_player = self.players[0]
        else:
            raise AssertionError
