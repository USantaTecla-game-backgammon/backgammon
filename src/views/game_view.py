from typing import Final

from src.models.turn import Turn
from src.views.bet_view import BetView
from src.views.dice_view import DiceView
from src.views.move_piece_view import MovePieceView
from src.views import console


class GameView:
    START: Final = '\n-- Starting new game --\n'
    SCORE: Final = 'Player {} has {} points'

    def __init__(self) -> None:
        self.bet_view = BetView()
        self.move_piece_view = MovePieceView()
        self.dice_view = DiceView()

    def show_start(self) -> None:
        console.show(self.START)

    def show_score(self, turn: Turn) -> None:
        for player in turn.players:
            console.show(self.SCORE.format(player.color, player.score))
