from abc import abstractmethod
from typing import Final


class BoardView:
    POSITION: Final[str] = 'Move from position'

    @abstractmethod
    def show(self, board: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def read_position(self, positions: list[int]) -> int:
        raise NotImplementedError
