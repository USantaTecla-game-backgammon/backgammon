from abc import abstractmethod

from src.models import Dice
from src.types import Color


class MatchView:

    @abstractmethod
    def show_title(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_dices(self, dices: dict[Color, Dice]) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_first_player(self, color: Color) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_goal(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def read_resume(self) -> bool:
        raise NotImplementedError
