from src.models.board import Board
from src.types import Color, Endgame


class Game:
    def __init__(self) -> None:
        self.board: Board = Board()

    def is_endgame(self) -> bool:
        return (
            self.board.is_all_pieces_off_board(Color.BLACK) or
            self.board.is_all_pieces_off_board(Color.RED)
        )

    def type_endgame(self) -> Endgame:
        assert self.is_endgame()

        looser_color: Color = Color.RED
        if self.board.is_all_pieces_off_board(Color.RED):
            looser_color = Color.BLACK

        if self.board.is_any_piece_off_board(looser_color):
            return Endgame.SIMPLE

        if (
            not self.board.is_any_piece_at_first_square(looser_color) and
            not self.board.is_any_piece_in_bar(looser_color)
        ):
            return Endgame.GAMMON

        return Endgame.BACKGAMMON
