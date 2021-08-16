from typing import Any
from src.models.player import Player


class PlayerSerializer:
    def __init__(self, player: Player) -> None:
        self.player: Player = player

    @property
    def data(self) -> Any:
        doubling_cube_int: int = 0
        if self.player.doubling_cube is not None:
            doubling_cube_int = self.player.doubling_cube.value

        player_dic = {
            "color": self.player.color.name,
            "score": self.player.score,
            "doubling_cube": doubling_cube_int,
            "is_winner": self.player.is_winner
        }
        return player_dic
