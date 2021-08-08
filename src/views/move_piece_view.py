from typing import Final

from src.views import console


class MovePieceView:
    POSITION: Final = 'Move from position'

    def read_position(self) -> int:
        return console.read_int(self.POSITION)
