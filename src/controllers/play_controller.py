from src.serializers.turn_serializer import TurnSerializer
from src.serializers.board_serializer import BoardSerializer
from src.controllers.bet_controller import BetController
from src.controllers.controller import Controller
from src.controllers.rules import chain_move_rules
from src.models import Match, Menu, Move
from src.models.commands import (
    BetCommand,
    MovePieceCommand,
    RollDiceCommand,
)
from src.types import Position
from src.views.view_factory import ViewFactory


class PlayController(Controller):

    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        super().__init__(match, view_factory)
        self.game_view = view_factory.create_game_view()
        self.menu_view = view_factory.create_menu_view()
        self.board_view = view_factory.create_board_view()

        self.bet_controller = BetController(self.match, self.view_factory)

    def __call__(self) -> None:
        assert self.match.goal > 0

        while not self.match.is_goal():
            self.match.add_game()
            self.game_view.show_start()

            game = self.match.last_game
            while not game.is_endgame():
                menu = self.create_menu()
                active_commands = menu.active_commands()
                if active_commands:
                    self.board_view.show(game.turn.current_color, BoardSerializer(game.board).data)
                    option = self.menu_view.interact(active_commands)
                    active_commands[option]()
                else:
                    game.change_turn()

            game.give_score()
            self.match.give_score()
            self.game_view.show_score(TurnSerializer(game.turn).data)
            self.match.change_turn()

    def add_game(self) -> None:
        self.match.add_game()

    def create_menu(self) -> Menu:
        menu = Menu(title='', commands=[
            BetCommand(self),
            RollDiceCommand(self),
        ])
        menu.commands += [
            MovePieceCommand(self, move)
            for move in self.calculate_available_moves()
        ]
        return menu

    def calculate_available_moves(self) -> list[Move]:
        moves: list[Move] = []
        game = self.match.last_game

        for pos in reversed(Position):
            for dice_value in set(game.possible_moves):
                moves.append(Move(position_from=pos, dice_value=dice_value))

        return chain_move_rules.restrict(game, moves)

    def bet(self) -> None:
        self.bet_controller()

    def move_piece(self, move: Move) -> None:
        game = self.match.last_game
        game.move_piece(move)
        game.try_eat_piece(move.position_to)

    def roll_dice(self) -> None:
        self.match.last_game.roll_current_player()
