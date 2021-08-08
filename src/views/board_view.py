from typing import Dict
from src.models.board import Board
from src.types.color import Color
from src.types.position import Position
from src.views import console


class BoardView:

    BOARD_WRAPPER: str = '|{:->56}|'
    ROW_POINT: str = '|{:>4}{:>4}{:>4}{:>4}{:>4}{:>4} |    |{:>4}{:>4}{:>4}{:>4}{:>4}{:>4} |'
    BAR_VALUES: str = '|{:24} |{:>4}|{:24} |'

    def __init__(self, board: Board) -> None:
        self.board = board
        self.color: Color
        self.font_color: console.FontColors

    def show(self, color: Color) -> None:
        self.color = color
        if self.color == Color.RED:
            console.FontColors = console.FontColors.RED
        else:
            console.FontColors = console.FontColors.BLACK

        self.__print_wrapper()
        self.__print_top()
        self.__print_top_val()
        self.__print_bar()
        self.__print_down_val()
        self.__print_down()
        self.__print_wrapper()

    @staticmethod
    def __pice_of_position(position: Dict[str, int]) -> str:
        black = position[Color.BLACK.name]
        red = position[Color.RED.name]
        if black > 0:
            return str(black) + Color.BLACK.value
        if red > 0:
            return str(red) + Color.RED.value
        return Color.EMPY.value

    def __print_wrapper(self) -> None:
        console.show(self.BOARD_WRAPPER.format('-'))

    def __print_top(self) -> None:
        console.show_in_color(
            self.ROW_POINT.format(
                self.board.position_of_color(Position.THIRTEEN, self.color),
                self.board.position_of_color(Position.FOURTEEN, self.color),
                self.board.position_of_color(Position.FIFTEEN, self.color),
                self.board.position_of_color(Position.SIXTEEN, self.color),
                self.board.position_of_color(Position.SEVENTEEN, self.color),
                self.board.position_of_color(Position.EIGHTEEN, self.color),
                self.board.position_of_color(Position.NINETEEN, self.color),
                self.board.position_of_color(Position.TWENTY, self.color),
                self.board.position_of_color(Position.TWENTY_ONE, self.color),
                self.board.position_of_color(Position.TWENTY_TWO, self.color),
                self.board.position_of_color(Position.TWENTY_THREE, self.color),
                self.board.position_of_color(Position.TWENTY_FOUR, self.color)
            ),
            self.font_color)

    def __print_down(self) -> None:
        console.show_in_color(
            self.ROW_POINT.format(
                self.board.position_of_color(Position.TWELVE, self.color),
                self.board.position_of_color(Position.ELEVEN, self.color),
                self.board.position_of_color(Position.TEN, self.color),
                self.board.position_of_color(Position.NINE, self.color),
                self.board.position_of_color(Position.EIGHT, self.color),
                self.board.position_of_color(Position.SEVEN, self.color),
                self.board.position_of_color(Position.SIX, self.color),
                self.board.position_of_color(Position.FIVE, self.color),
                self.board.position_of_color(Position.FOUR, self.color),
                self.board.position_of_color(Position.THREE, self.color),
                self.board.position_of_color(Position.TWO, self.color),
                self.board.position_of_color(Position.ONE, self.color)
            ),
            self.font_color)

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
        num_red: str = str(
            self.board.positions[Position.BAR.value][Color.RED.name]) + Color.RED.value
        num_black: str = str(
            self.board.positions[Position.BAR.value][Color.BLACK.name]) + Color.BLACK.value
        console.show(self.BAR_VALUES.format(' ', num_red, ' '))
        console.show(self.BAR_VALUES.format(' ', 'BAR', ' '))
        console.show(self.BAR_VALUES.format(' ', num_black, ' '))
