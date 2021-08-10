from typing import Final

from src.views import console


class MovePieceView:
    POSITION: Final = 'Move from position'

    def read_position(self, valids: list[int]) -> int:
        return console.read_int_range(valids=valids, msg=self.POSITION)
