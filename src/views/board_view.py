from abc import abstractmethod

from src.models import Board
from src.types import Color


class BoardView:
    @abstractmethod
    def show(self, color: Color, board: str) -> None:
        raise NotImplementedError
