from typing import Any
from src.models.board import Board
from src.types.color import Color
from src.types.position import Position


class BoardSerializer(Board):
    board: Board

    def __init__(self, board: Board) -> None:
        self.board = board

    @property
    def data(self) -> Any:
        available_colors: list[Color] = [Color.BLACK, Color.RED]
        board_dic: dict[str, dict[str, dict[str, int]]] = {}
        for sense_color in available_colors:
            board_dic[sense_color.name] = {}
            for position in Position:
                board_dic[sense_color.name][position.name] = {}
                pices_in_position: list[Color] = self.board.get_pieces(sense_color, position)
                num_of_color_dic = {}
                for pice_color in available_colors:
                    num_of_color_dic[pice_color.name] = pices_in_position.count(pice_color)
                board_dic[sense_color.name][position.name].update(num_of_color_dic)

        return board_dic
