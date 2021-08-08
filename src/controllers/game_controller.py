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
from src.views.board_view import BoardView
from src.views.menu_view import MenuView


class GameController:

    def __init__(self, match: Match, view: GameView) -> None:
        self.match = match
        self.view = view
        self.menu: Menu = Menu(title='', commands=[])
        self.menu_view = MenuView()

    def play(self) -> None:
        self.view.show_start()

        game = self.match.games[-1]
        board_view = BoardView(game.board)

        while not game.is_endgame():
            self.menu.commands = [
                RollDiceCommand(RollDiceController(game, self.view))
            ]

            self.menu.commands += [
                MovePieceCommand(MovePieceController(game, self.view), move)
                for move in game.possible_moves
            ]

            if game.turn.can_bet_current_player():
                self.menu.commands.append(
                    BetCommand(BetController(game, self.view)),
                )

            if self.menu.active_commands():
                board_view.show(game.current_player.color)
                self.menu_view(self.menu, game.current_player.color)
            else:
                game.change_turn()

        game.give_score()
        self.view.show_score(game.turn)
