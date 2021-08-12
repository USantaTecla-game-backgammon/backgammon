from typing import Final

from src.types.color import Color
from src.types.position import Position


class Board:

    NUM_PICES_PER_COLOR: Final = 15
    FIRST_SQUARE: list[Position] = [
        Position.ONE,
        Position.TWO,
        Position.THREE,
        Position.FOUR,
        Position.FIVE,
        Position.SIX,
    ]
    LAST_SQUARE: list[Position] = [
        Position.NINETEEN,
        Position.TWENTY,
        Position.TWENTY_ONE,
        Position.TWENTY_TWO,
        Position.TWENTY_THREE,
        Position.TWENTY_FOUR,
    ]

    def __init__(self) -> None:
        self._sense: Color = Color.BLACK
        self.positions: list[list[Color]] = []
        self.reset()

    def count_color_in_position(self, color: Color, position: Position) -> int:
        return self.positions[position].count(color)

    def is_all_pieces_off_board(self, color: Color) -> bool:
        position = Position.OFF_BOARD if Color.BLACK else Position.BAR
        return self.positions[position].count(color) == self.NUM_PICES_PER_COLOR

    def is_any_piece_off_board(self, color: Color) -> bool:
        position = Position.OFF_BOARD if Color.BLACK else Position.BAR
        return self.positions[position].count(color) > 0

    def is_any_piece_at_last_square(self, color: Color) -> bool:
        positions = self.FIRST_SQUARE if Color.BLACK else self.LAST_SQUARE
        for position in positions:
            if self.positions[position].count(color) > 0:
                return True
        return False

    def is_all_pieces_first_square(self, color: Color) -> bool:
        pieces = 0
        positions = self.LAST_SQUARE if Color.BLACK else self.FIRST_SQUARE
        for position in positions:
            pieces += self.positions[position].count(color)
        return pieces == self.NUM_PICES_PER_COLOR

    def is_any_piece_in_bar(self, color: Color) -> bool:
        position = Position.BAR if Color.BLACK else Position.OFF_BOARD
        return self.positions[position].count(color) > 0

    def get_pieces(self, position: Position) -> list[Color]:
        if position == Position.BAR:
            in_bar = [col for col in self.positions[position] if col == self._sense]
            offboard = [col for col in self.positions[Position.OFF_BOARD] if col != self._sense]
            return in_bar + offboard

        if position == Position.OFF_BOARD:
            offboard = [col for col in self.positions[position] if col == self._sense]
            in_bar = [col for col in self.positions[Position.BAR] if col != self._sense]
            return in_bar + offboard

        return self.positions[position]

    @property
    def sense(self) -> Color:
        return self._sense

    @sense.setter
    def sense(self, color: Color) -> None:
        if self._sense != color:
            self._sense = color
            self.positions.reverse()

    def move_piece(self, position_from: Position, position_to: Position) -> None:
        piece = self.positions[position_from].pop()
        self.positions[position_to].append(piece)

    def eat_piece(self, position: Position) -> None:
        piece = self.positions[position].pop(0)
        self.positions[Position.OFF_BOARD].append(piece)

    def reset(self) -> None:
        self.positions = [
            [],  # OFF_BOARD (BLACK) / BAR (RED)
            [Color.RED] * 2, [], [], [], [], [Color.BLACK] * 5,  # 1 to 6
            [], [Color.BLACK] * 3, [], [], [], [Color.RED] * 5,  # 7 to 12
            [Color.BLACK] * 5, [], [], [], [Color.RED] * 3, [],  # 13 to 18
            [Color.RED] * 5, [], [], [], [], [Color.BLACK] * 2,  # 19 to 24
            [],  # BAR (BLACK) / OFF_BOARD (RED)
        ]
