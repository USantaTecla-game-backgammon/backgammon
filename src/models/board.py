from src.types.position import Position
from src.types.color import Color


class Board:
    def __init__(self) -> None:
        self.positions = {}
        self.reset()

    def is_all_pieces_off_board(self, color: Color) -> bool:
        raise NotImplementedError

    def is_any_piece_off_board(self, color: Color) -> bool:
        raise NotImplementedError

    def is_any_piece_at_first_square(self, color: Color) -> bool:
        raise NotImplementedError

    def is_any_piece_in_bar(self, color: Color) -> bool:
        raise NotImplementedError

    def is_all_pieces_last_square(self, color: Color) -> bool:
        raise NotImplementedError

    def move_pice(self, position_from: Position, position_to: Position, color: Color) -> None:
        self.positions.update(position_from)

    def reset(self) -> None:
        self.positions.clear()
        self.__update_position(Position.TWENTY_FOUR, 0, 2)
        self.__update_position(Position.TWENTY_THREE, 0,0)
        self.__update_position(Position.TWENTY_TWO, 0,0)
        self.__update_position(Position.TWENTY_ONE, 0,0)
        self.__update_position(Position.TWENTY, 0,0)
        self.__update_position(Position.NINETEEN, 5, 0)
        self.__update_position(Position.EIGHTEEN, 0,0)
        self.__update_position(Position.SEVENTEEN, 3, 0)
        self.__update_position(Position.SIXTEEN, 0,0)
        self.__update_position(Position.FIFTEEN, 0,0)
        self.__update_position(Position.FOURTEEN, 0,0)
        self.__update_position(Position.THIRTEEN, 0, 5)
        self.__update_position(Position.TWELVE, 5, 0)
        self.__update_position(Position.ELEVEN, 0,0)
        self.__update_position(Position.TEN, 0,0)
        self.__update_position(Position.NINE, 0,0)
        self.__update_position(Position.EIGHT, 0, 3)
        self.__update_position(Position.SEVEN, 0,0)
        self.__update_position(Position.SIX, 0, 5)
        self.__update_position(Position.FIVE, 0,0)
        self.__update_position(Position.FOUR, 0,0)
        self.__update_position(Position.THREE, 0,0)
        self.__update_position(Position.TWO, 0,0)        
        self.__update_position(Position.ONE, 2, 0)

    def __update_position(self, position: Position, num_black: int, num_red: int) -> None:
        self.positions.update({position.value: {Color.BLACK.name: num_black, Color.RED.name: num_red}})

