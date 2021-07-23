from typing import Optional

from src.models.player import Player
from src.types.color import Color


class Game:
    def __init__(self) -> None:
        self.red_player = Player(Color.RED)
        self.black_player = Player(Color.BLACK)

        self.__turn: Optional[Player] = None  # pylint: disable=unsubscriptable-object

    @property
    def turn(self) -> Optional[Player]:  # pylint: disable=unsubscriptable-object
        return self.__turn

    def first_roll(self) -> None:
        self.red_player.roll(1)
        self.black_player.roll(1)

    def roll(self) -> None:
        assert self.__turn is not None

        self.__turn.roll()
