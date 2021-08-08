from src.views.bet_view import BetView
from src.views.dice_view import DiceView
from src.views.move_piece_view import MovePieceView


class GameView:
    def __init__(self) -> None:
        self.bet_view = BetView()
        self.move_piece_view = MovePieceView()
        self.dice_view = DiceView()
