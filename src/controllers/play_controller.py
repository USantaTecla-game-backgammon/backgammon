from src.controllers.bet_controller import BetController
from src.controllers.move_piece_controller import MovePieceController
from src.controllers.roll_dice_controller import RollDiceController
from src.controllers.controller import Controller
from src.models import Match, Menu
from src.models.game import Game
from src.models.commands import (
    BetCommand,
    MovePieceCommand,
    RollDiceCommand,
)
from src.types.game_state import GameState
from src.views.view_factory import ViewFactory


class PlayController(Controller):

    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        super().__init__(match, view_factory)

        self.bet_controller = BetController(self.match, self.view_factory)
        self.move_piece_controller = MovePieceController(self.match, self.view_factory)
        self.roll_dice_controller = RollDiceController(self.match, self.view_factory)

    def __call__(self) -> None:
        assert self.match.goal > 0

        self.initialize_game()
        game = self.match.last_game

        while not game.is_endgame():
            self.view_factory.create_board_view().show(game.board, game.turn.current_color)

            menu = Menu(title='', commands=[
                BetCommand(self.bet_controller),
                RollDiceCommand(self.roll_dice_controller),
            ])
            menu.commands += [
                MovePieceCommand(self.move_piece_controller, move)
                for move in game.possible_moves
            ]

            valid_commands = menu.valid_commands()

            if valid_commands:
                self.view_factory.create_menu_view().show(valid_commands)
                option = self.view_factory.create_menu_view().read(valid_commands)
                valid_commands[option - 1]()
            else:
                game.change_turn()
                print('Cambiar turno, no quedan comandos disponibles')
                print(game.state)

        game.give_score()
        self.view.show_score(game.turn)

    def initialize_game(self) -> None:
        self.match.create_game()
        self.view_factory.create_play_view().show()
        assert self.match.games

    def is_goal(self) -> bool:
        return self.match.is_goal()

    def resume(self) -> bool:
        return self.view.read_resume()
    def bet(self) -> None:
        self.bet_controller()

    def move_piece(self) -> None:
        self.move_piece_controller()

    def roll_dice(self) -> None:
        self.roll_dice_controller()
