from src.models.board import Board
from src.types import Color, Position
from src.views import console


class BoardView:

    BOARD_WRAPPER: str = '|{:->56}|'.format('')
    ROW_POINT: str = '|{:>4}{:>4}{:>4}{:>4}{:>4}{:>4} |    |{:>4}{:>4}{:>4}{:>4}{:>4}{:>4} |'
    BAR_VALUES: str = '|{:24} |{:>4}|{:24} |'

    def __init__(self, board: Board) -> None:
        self.board = board
        self.color = Color.BLACK
        self.font_color: console.FontColors

    def show(self, color: Color) -> None:
        self.color = color
        if self.color == Color.RED:
            font_color = console.FontColors.RED
        else:
            font_color = console.FontColors.BLACK

        console.show(self.BOARD_WRAPPER)
        console.show_in_color(self._top_position(color), font_color)
        console.show(self._top_pieces())
        console.show(self._bar())
        console.show(self._down_pieces())
        console.show_in_color(self._down_position(color), font_color)
        console.show(self.BOARD_WRAPPER)

    def _top_position(self, color: Color) -> str:
        if color == Color.BLACK:
            return self.ROW_POINT.format(*Position.pos_13_to_24())

        return self.ROW_POINT.format(*Position.pos_12_to_1())

    def _top_pieces(self) -> str:
        pos_12_to_24 = []
        for pos in Position.pos_13_to_24():
            pieces = self.board.get_pieces(self.color, pos)
            value = ''
            if pieces:
                value = f'{len(pieces)}{pieces[0].value}'
            pos_12_to_24.append(value)

        return self.ROW_POINT.format(*pos_12_to_24)

    def _bar(self) -> str:
        num_black: int = self.board.filter_color_in_position(Color.BLACK, Position.BAR)
        num_red: int = self.board.filter_color_in_position(Color.RED, Position.BAR)

        return (
            self.BAR_VALUES.format(' ', str(num_red) + Color.RED.value, ' ') + '\n' +
            self.BAR_VALUES.format(' ', 'BAR', ' ') + '\n' +
            self.BAR_VALUES.format(' ', str(num_black) + Color.BLACK.value, ' ')
        )

    def _down_pieces(self) -> str:
        pos_11_to_1 = []
        for pos in Position.pos_12_to_1():
            pieces = self.board.get_pieces(self.color, pos)
            value = ''
            if pieces:
                value = f'{len(pieces)}{pieces[0].value}'
            pos_11_to_1.append(value)

        return self.ROW_POINT.format(*pos_11_to_1)

    def _down_position(self, color: Color) -> str:
        if color == Color.BLACK:
            return self.ROW_POINT.format(*Position.pos_12_to_1())

        return self.ROW_POINT.format(*Position.pos_13_to_24())
