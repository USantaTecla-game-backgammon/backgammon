from src.controllers.bet_controller import BetController
from src.controllers.move_piece_controller import MovePieceController
from src.controllers.roll_dice_controller import RollDiceController
from src.models import Match, Menu
from src.models.commands import (
    BetCommand,
    MovePieceCommand,
    RollDiceCommand,
)
from src.views.view_factory import ViewFactory


class GameController:

    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        self.match = match
        self.view_factory = view_factory
        self.view = view_factory.create_game_view()
        self.menu: Menu = Menu(title='', commands=[])
        self.menu_view = self.view_factory.create_menu_view()

    def play(self) -> None:
        self.view.show_start()

        game = self.match.games[-1]
        board_view = self.view_factory.create_board_view()

        while not game.is_endgame():
            self.menu.commands = [
                RollDiceCommand(RollDiceController(game, self.view_factory))
            ]

            self.menu.commands += [
                MovePieceCommand(MovePieceController(game, self.view_factory), move)
                for move in game.possible_moves
            ]

            if game.turn.can_bet_current_player():
                self.menu.commands.append(
                    BetCommand(BetController(game, self.view_factory)),
                )

            if self.menu.active_commands():
                board_view.show(game.current_player.color, game.board)
                self.menu_view(self.menu, game.current_player.color)
            else:
                game.change_turn()

        game.give_score()
        self.view.show_score(game.turn)
