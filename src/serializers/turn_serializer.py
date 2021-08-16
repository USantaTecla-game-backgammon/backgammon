from src.models.turn import Turn
from typing import Any

from src.serializers.player_serializer import PlayerSerializer


class TurnSerializer:
    def __init__(self, turn: Turn) -> None:
        self.players = turn.players

    @property
    def data(self) -> Any:
        turn_dict: dict[str, list[Any]] = {}
        player_list: list[Any] = []
        for player in self.players:
            player_list.append(PlayerSerializer(player).data)
        turn_dict["players"] = player_list
        return turn_dict
