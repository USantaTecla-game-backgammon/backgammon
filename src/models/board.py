from typing import Final

from src.models.move import Move
from src.types.color import Color
from src.types.position import Position


class Board:
    COLORS: tuple[Color, Color] = (Color.BLACK, Color.RED)
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
        self.positions: list[list[Color]] = []
        self.reset()

    def count_color_in_position(self, color: Color, position: Position) -> int:
        return self.positions[position].count(color)

    def is_all_pieces_off_board(self, color: Color) -> bool:
        pieces = self.get_pieces(sense=color, position=Position.OFF_BOARD)
        return pieces.count(color) == self.NUM_PICES_PER_COLOR

    def is_any_piece_off_board(self, color: Color) -> bool:
        pieces = self.get_pieces(sense=color, position=Position.OFF_BOARD)
        return pieces.count(color) > 0

    def is_any_piece_at_last_square(self, sense: Color) -> bool:
        for position in self.LAST_SQUARE:
            if self.get_pieces(sense, position).count(sense) > 0:
                return True
        return False

    def is_all_pieces_first_square(self, sense: Color) -> bool:
        pieces = 0
        for position in self.FIRST_SQUARE:
            pieces += self.get_pieces(sense, position).count(sense)
        return pieces == self.NUM_PICES_PER_COLOR

    def is_any_piece_in_bar(self, color: Color) -> bool:
        pieces = self.get_pieces(sense=color, position=Position.BAR)
        return pieces.count(color) > 0

    def get_pieces(self, sense: Color, position: Position) -> list[Color]:
        positions = self.positions[:]
        if sense == Color.RED:
            positions = positions[::-1]

        if position == Position.BAR:
            in_bar = [color for color in positions[position] if color == sense]
            offboard = [color for color in positions[Position.OFF_BOARD] if color != sense]
            return in_bar + offboard

        if position == Position.OFF_BOARD:
            offboard = [color for color in positions[position] if color == sense]
            in_bar = [color for color in positions[Position.BAR] if color != sense]
            return in_bar + offboard

        return positions[position]

    def move_piece(self, sense: Color, move: Move, color: Color) -> None:
        assert sense in self.COLORS and color in self.COLORS
        if sense == Color.RED:
            self.positions.reverse()

        self.positions[move.position_from].remove(color)
        self.positions[move.position_to].append(color)

        if sense == Color.RED:
            self.positions.reverse()

    def reset(self) -> None:
        self.positions = [
            [],  # OFF_BOARD (BLACK) / BAR (RED)
            [Color.RED] * 2, [], [], [], [], [Color.BLACK] * 5,  # 1 to 6
            [], [Color.BLACK] * 3, [], [], [], [Color.RED] * 5,  # 7 to 12
            [Color.BLACK] * 5, [], [], [], [Color.RED] * 3, [],  # 13 to 18
            [Color.RED] * 5, [], [], [], [], [Color.BLACK] * 2,  # 19 to 24
            [],  # BAR (BLACK) / OFF_BOARD (RED)
        ]
