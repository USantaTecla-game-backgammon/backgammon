from abc import abstractmethod
from typing import Any

from src.types import Color


class BoardView:
    @abstractmethod
    def show(self, color: Color, board: Any) -> None:
        raise NotImplementedError
