from src.controllers.bet_controller import BetController
from src.controllers.move_piece_controller import MovePieceController
from src.controllers.roll_dice_controller import RollDiceController
from src.models import Match, Menu
from src.models.commands import (
    BetCommand,
    MovePieceCommand,
    RollDiceCommand,
)
from src.views import GameView
from src.views.menu_view import MenuView


class GameController:

    def __init__(self, match: Match, view: GameView) -> None:
        self.match = match
        self.view = view
        self.menu: Menu = Menu(title='', commands=[])
        self.menu_view = MenuView()

    def play(self) -> None:
        game = self.match.games[-1]

        self.menu.commands += [
            BetCommand(BetController(game, self.view)),
            MovePieceCommand(MovePieceController(game, self.view)),
            RollDiceCommand(RollDiceController(game, self.view)),
        ]

        while not game.is_endgame():
            self.menu_view(self.menu)
