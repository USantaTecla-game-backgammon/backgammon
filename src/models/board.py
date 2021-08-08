from typing import Dict
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
        self.positions: Dict[int, Dict[str, int]] = {}
        self.reset()

    def is_all_pieces_off_board(self, color: Color) -> bool:
        return self.position_of_color(Position.OFF_BOARD, color) == self.NUM_PICES_PER_COLOR

    def is_any_piece_off_board(self, color: Color) -> bool:
        return self.position_of_color(Position.OFF_BOARD, color) == 0

    def is_any_piece_at_first_square(self, color: Color) -> bool:
        for position in self.FIRST_SQUARE:
            if self.position_of_color(position, color) > 0:
                return True
        return False

    def is_any_piece_in_bar(self, color: Color) -> bool:
        return self.position_of_color(Position.BAR, color) > 0

    def is_all_pieces_last_square(self, color: Color) -> bool:
        for position in self.LAST_SQUARE:
            if self.position_of_color(position, color) > 0:
                return True
        return False

    def move_piece_int(self, position_from: int, position_to: int, color: Color) -> None:
        pos_from = position_from if color == Color.BLACK else abs(position_from - 25)
        pos_to = position_to if color == Color.BLACK else abs(position_to - 25)
        self.positions[pos_from][color.name] -= 1
        self.positions[pos_to][color.name] += 1

    def move_piece(self, position_from: Position, position_to: Position, color: Color) -> None:
        pos_from_absolute = self.position_of_color(position_from, color)
        pos_to_absolute = self.position_of_color(position_to, color)
        self.positions[pos_from_absolute][color.name] -= 1
        self.positions[pos_to_absolute][color.name] += 1

    def reset(self) -> None:
        self.positions.clear()
        self.__update_position(Position.TWENTY_FOUR, 2, 0)
        self.__update_position(Position.TWENTY_THREE, 0, 0)
        self.__update_position(Position.TWENTY_TWO, 0, 0)
        self.__update_position(Position.TWENTY_ONE, 0, 0)
        self.__update_position(Position.TWENTY, 0, 0)
        self.__update_position(Position.NINETEEN, 0, 5)
        self.__update_position(Position.EIGHTEEN, 0, 0)
        self.__update_position(Position.SEVENTEEN, 0, 3)
        self.__update_position(Position.SIXTEEN, 0, 0)
        self.__update_position(Position.FIFTEEN, 0, 0)
        self.__update_position(Position.FOURTEEN, 0, 0)
        self.__update_position(Position.THIRTEEN, 5, 0)
        self.__update_position(Position.TWELVE, 0, 5)
        self.__update_position(Position.ELEVEN, 0, 0)
        self.__update_position(Position.TEN, 0, 0)
        self.__update_position(Position.NINE, 0, 0)
        self.__update_position(Position.EIGHT, 3, 0)
        self.__update_position(Position.SEVEN, 0, 0)
        self.__update_position(Position.SIX, 5, 0)
        self.__update_position(Position.FIVE, 0, 0)
        self.__update_position(Position.FOUR, 0, 0)
        self.__update_position(Position.THREE, 0, 0)
        self.__update_position(Position.TWO, 0, 0)
        self.__update_position(Position.ONE, 0, 2)

        self.__update_position(Position.BAR, 0, 0)
        self.__update_position(Position.OFF_BOARD, 0, 0)

    def __update_position(self, position: Position, num_black: int, num_red: int) -> None:
        self.positions.update(
            {position.value: {Color.BLACK.name: num_black, Color.RED.name: num_red}})

    @staticmethod
    def position_of_color(position: Position, color: Color) -> int:
        if color == Color.BLACK:
            return position.color_black
        return position.color_red
