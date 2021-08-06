from src.types import Color


class Board:
    def is_all_pieces_off_board(self, color: Color) -> bool:
        raise NotImplementedError

    def is_any_piece_off_board(self, color: Color) -> bool:
        raise NotImplementedError

    def is_any_piece_at_first_square(self, color: Color) -> bool:
        raise NotImplementedError

    def is_any_piece_in_bar(self, color: Color) -> bool:
        raise NotImplementedError
