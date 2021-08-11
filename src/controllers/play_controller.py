from src.controllers.bet_controller import BetController
from src.controllers.move_piece_controller import MovePieceController
from src.controllers.controller import Controller
from src.models import Match, Menu
from src.models.turn import Turn
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
        self.view = view_factory.create_game_view()
        self.menu_view = self.view_factory.create_menu_view()

        self.bet_controller = BetController(self.match, self.view_factory)
        self.move_piece_controller = MovePieceController(self.match, self.view_factory)

    def __call__(self) -> None:
        assert self.match.goal > 0

        self.initialize_game()
        game = self.match.games[-1]
        self.view.show_start()

        board_view = self.view_factory.create_board_view()

        while not game.is_endgame():
            menu = Menu(title='', commands=[
                BetCommand(self),
                RollDiceCommand(self),
            ])
            menu.commands += [
                MovePieceCommand(self, move)
                for move in game.possible_moves
            ]

            if menu.active_commands():
                board_view.show(game.current_player.color, game.board)
                self.menu_view(menu, game.current_player.color)
            else:
                game.change_turn()

        game.give_score()
        self.view.show_score(game.turn)

    def initialize_game(self) -> None:
        assert self.match.goal > 0

        turn = Turn()
        game = Game(turn)

        if self.match.is_first_game():
            game.state = GameState.MOVING_PIECE
            game.last_roll = self.match.first_roll
        else:
            self.match.change_turn()

        turn.current_color = self.match.turn.current_color
        self.match.games.append(game)

    def is_goal(self) -> bool:
        return self.match.is_goal()

    def bet(self) -> None:
        self.bet_controller()

    def move_piece(self, move: int) -> None:
        self.move_piece_controller(move)

    def roll_dice(self) -> None:
        self.match.last_game.roll_current_player()
