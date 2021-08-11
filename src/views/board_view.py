from abc import abstractmethod

from src.models import Board
from src.types import Color


class BoardView:
    @abstractmethod
    def show(self, color: Color, board: Board) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_position(self) -> int:
        raise NotImplementedError
