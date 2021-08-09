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

    def filter_color_in_position(self, color: Color, position: Position) -> int:
        self.sense = color
        return len([col for col in self.positions[position] if col == color])

    def is_all_pieces_off_board(self, color: Color) -> bool:
        return self.filter_color_in_position(color, Position.OFF_BOARD) == self.NUM_PICES_PER_COLOR

    def is_any_piece_off_board(self, color: Color) -> bool:
        return self.filter_color_in_position(color, Position.OFF_BOARD) > 0

    def is_any_piece_at_first_square(self, color: Color) -> bool:
        for position in self.FIRST_SQUARE:
            if self.filter_color_in_position(color, position) > 0:
                return True
        return False

    def is_any_piece_in_bar(self, color: Color) -> bool:
        return self.filter_color_in_position(color, Position.BAR) > 0

    def is_all_pieces_last_square(self, color: Color) -> bool:
        for position in self.LAST_SQUARE:
            if self.filter_color_in_position(color, position) > 0:
                return True
        return False

    def get_pieces(self, color: Color, position: Position) -> list[Color]:
        self.sense = color
        if position == Position.BAR:
            in_bar = [col for col in self.positions[position] if col == color]
            offboard = [col for col in self.positions[Position.OFF_BOARD] if col != color]
            return in_bar + offboard

        if position == Position.OFF_BOARD:
            offboard = [col for col in self.positions[position] if col == color]
            in_bar = [col for col in self.positions[Position.BAR] if col != color]
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

    def move_piece(self, position_from: int, position_to: int, color: Color) -> None:
        self.sense = color
        piece = self.positions[position_from].pop()
        self.positions[position_to].append(piece)

    def reset(self) -> None:
        self.positions = [
            [],  # OFF_BOARD
            [Color.RED] * 2, [], [], [], [], [Color.BLACK] * 5,  # 1 to 6
            [], [Color.BLACK] * 3, [], [], [], [Color.RED] * 5,  # 7 to 12
            [Color.BLACK] * 5, [], [], [], [Color.RED] * 3, [],  # 13 to 18
            [Color.RED] * 5, [], [], [], [], [Color.BLACK] * 2,  # 19 to 24
            [],  # BAR
        ]
