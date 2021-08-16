from typing import Any, Final

from src.types import Color, Position
from src.views import BoardView as BoardViewBase
from src.views.console import console


class BoardView(BoardViewBase):

    BOARD_WRAPPER: str = '|{:->56}|'.format('')
    ROW_POINT: str = '|{:>4}{:>4}{:>4}{:>4}{:>4}{:>4} |    |{:>4}{:>4}{:>4}{:>4}{:>4}{:>4} |'
    BAR_VALUES: str = '|{:24} |{:>4}|{:24} |'
    POSITION: Final[str] = 'Move from position'

    def show(self, color: Color, board: Any) -> None:
        if color == Color.RED:
            font_color = console.FontColors.RED
        else:
            font_color = console.FontColors.BLACK

        console.show(self.BOARD_WRAPPER)
        console.show_in_color(self._top_position(color), font_color)
        console.show(self._top_pieces(color, board))
        console.show(self._bar(board))
        console.show(self._down_pieces(color, board))
        console.show_in_color(self._down_position(color), font_color)
        console.show(self.BOARD_WRAPPER)

    def _top_position(self, color: Color) -> str:
        if color == Color.BLACK:
            return self.ROW_POINT.format(*Position.pos_13_to_24())

        return self.ROW_POINT.format(*Position.pos_12_to_1())

    def _top_pieces(self, color: Color, board: Any) -> str:
        pos_12_to_24 = []
        for pos in Position.pos_13_to_24():
            pieces = board[color.name][pos.name]
            value = ''
            if pieces[Color.RED.name] > 0:
                value = f'{pieces[Color.RED.name]}{Color.RED.value}'
            if pieces[Color.BLACK.name] > 0:
                value = f'{pieces[Color.BLACK.name]}{Color.BLACK.value}'
            pos_12_to_24.append(value)

        return self.ROW_POINT.format(*pos_12_to_24)

    def _bar(self, board: Any) -> str:
        num_black = board[Color.BLACK.name][Position.BAR.name][Color.BLACK.name]
        num_red = board[Color.RED.name][Position.BAR.name][Color.RED.name]   
        return (
            self.BAR_VALUES.format(' ', str(num_red) + Color.RED.value, ' ') + '\n' +
            self.BAR_VALUES.format(' ', 'BAR', ' ') + '\n' +
            self.BAR_VALUES.format(' ', str(num_black) + Color.BLACK.value, ' ')
        )

    def _down_pieces(self, color: Color, board: Any) -> str:
        pos_11_to_1 = []
        for pos in Position.pos_12_to_1():
            pieces = board[color.name][pos.name]
            value = ''
            if pieces[Color.RED.name] > 0:
                value = f'{pieces[Color.RED.name]}{Color.RED.value}'
            if pieces[Color.BLACK.name] > 0:
                value = f'{pieces[Color.BLACK.name]}{Color.BLACK.value}'
            pos_11_to_1.append(value)

        return self.ROW_POINT.format(*pos_11_to_1)

    def _down_position(self, color: Color) -> str:
        if color == Color.BLACK:
            return self.ROW_POINT.format(*Position.pos_12_to_1())

        return self.ROW_POINT.format(*Position.pos_13_to_24())
