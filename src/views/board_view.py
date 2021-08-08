from typing import Dict
from src.types.position import Position
from typing import Final
from src.types.color import Color
from src.views import console
from src.models.board import Board


class BoardView:
    BOARD_WRAPPER: Final = '|{:->44}|'
    ROW_POINT: Final = '|{:>3}{:>3}{:>3}{:>3}{:>3}{:>3} |   | {:>3}{:>3}{:>3}{:>3}{:>3}{:>3} |'
    BAR_VALUES: Final = '|{:18} |{:>3}| {:18} |'


    def __init__(self, board: Board) -> None:
        self.board = board


    def show(self, color: Color) -> None:
        self.__print_wrapper()
        self.__print_top(color)
        self.__print_top_val()
        self.__print_bar()
        self.__print_down_val()
        self.__print_down(color)
        self.__print_wrapper()


    def __pice_of_position(self, position: Dict[str, int]) -> str:
        black = position[Color.BLACK.name]
        red = position[Color.RED.name]
        if black > 0:
            return str(black) + Color.BLACK.value
        if red > 0:
            return str(red) + Color.RED.value
        return ' '


    def __print_wrapper(self) -> None:
        console.show(self.BOARD_WRAPPER.format('-'))


    def __print_top(self, color: Color) -> None:
        console.show(self.ROW_POINT.format(
            self.board.position_of_color(Position.THIRTEEN, color),
            self.board.position_of_color(Position.FOURTEEN, color),
            self.board.position_of_color(Position.FIFTEEN, color),
            self.board.position_of_color(Position.SIXTEEN, color),
            self.board.position_of_color(Position.SEVENTEEN, color),
            self.board.position_of_color(Position.EIGHTEEN, color),
            self.board.position_of_color(Position.NINETEEN, color),
            self.board.position_of_color(Position.TWENTY, color),
            self.board.position_of_color(Position.TWENTY_ONE, color),
            self.board.position_of_color(Position.TWENTY_TWO, color),
            self.board.position_of_color(Position.TWENTY_THREE, color),
            self.board.position_of_color(Position.TWENTY_FOUR, color)
        ))


    def __print_down(self, color: Color) -> None:
        console.show(self.ROW_POINT.format(
            self.board.position_of_color(Position.TWELVE, color),
            self.board.position_of_color(Position.ELEVEN, color),
            self.board.position_of_color(Position.TEN, color),
            self.board.position_of_color(Position.NINE, color),
            self.board.position_of_color(Position.EIGHT, color),
            self.board.position_of_color(Position.SEVEN, color),
            self.board.position_of_color(Position.SIX, color),
            self.board.position_of_color(Position.FIVE, color),
            self.board.position_of_color(Position.FOUR, color),
            self.board.position_of_color(Position.THREE, color),
            self.board.position_of_color(Position.TWO, color),
            self.board.position_of_color(Position.ONE, color)
        ))


    def __print_top_val(self) -> None:
        console.show(self.ROW_POINT.format(
            self.__pice_of_position(self.board.positions[Position.THIRTEEN.value]),
            self.__pice_of_position(self.board.positions[Position.FOURTEEN.value]),
            self.__pice_of_position(self.board.positions[Position.FIFTEEN.value]),
            self.__pice_of_position(self.board.positions[Position.SIXTEEN.value]),
            self.__pice_of_position(self.board.positions[Position.SEVENTEEN.value]),
            self.__pice_of_position(self.board.positions[Position.EIGHTEEN.value]),
            self.__pice_of_position(self.board.positions[Position.NINETEEN.value]),
            self.__pice_of_position(self.board.positions[Position.TWENTY.value]),
            self.__pice_of_position(self.board.positions[Position.TWENTY_ONE.value]),
            self.__pice_of_position(self.board.positions[Position.TWENTY_TWO.value]),
            self.__pice_of_position(self.board.positions[Position.TWENTY_THREE.value]),
            self.__pice_of_position(self.board.positions[Position.TWENTY_FOUR.value])
        ))


    def __print_down_val(self) -> None:
        console.show(self.ROW_POINT.format(
            self.__pice_of_position(self.board.positions[Position.TWELVE.value]),
            self.__pice_of_position(self.board.positions[Position.ELEVEN.value]),
            self.__pice_of_position(self.board.positions[Position.TEN.value]),
            self.__pice_of_position(self.board.positions[Position.NINE.value]),
            self.__pice_of_position(self.board.positions[Position.EIGHT.value]),
            self.__pice_of_position(self.board.positions[Position.SEVEN.value]),
            self.__pice_of_position(self.board.positions[Position.SIX.value]),
            self.__pice_of_position(self.board.positions[Position.FIVE.value]),
            self.__pice_of_position(self.board.positions[Position.FOUR.value]),
            self.__pice_of_position(self.board.positions[Position.THREE.value]),
            self.__pice_of_position(self.board.positions[Position.TWO.value]),
            self.__pice_of_position(self.board.positions[Position.ONE.value])
        ))


    def __print_bar(self) -> None:
        num_red: str = str(self.board.positions[Position.BAR.value][Color.RED.name])
        num_black: str = str(self.board.positions[Position.BAR.value][Color.BLACK.name])
        console.show(self.BAR_VALUES.format(' ', num_red + 'r', ' '))
        console.show(self.BAR_VALUES.format(' ', 'BAR', ' '))
        console.show(self.BAR_VALUES.format(' ', num_black + 'b', ' '))

