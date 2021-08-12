from src.controllers.bet_controller import BetController
from src.controllers.move_piece_controller import MovePieceController
from src.controllers.controller import Controller
from src.models import Game, Match, Menu, Move
from src.models.commands import (
    BetCommand,
    MovePieceCommand,
    RollDiceCommand,
)
from src.types import GameState, Position
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
                for move in self.calculate_available_moves()
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

        game = Game()

        if self.match.is_first_game():
            game.state = GameState.MOVING_PIECE
            game.last_roll = self.match.first_roll
        else:
            self.match.change_turn()

        game.turn.current_color = self.match.turn.current_color
        self.match.games.append(game)

    def calculate_available_moves(self) -> list[Move]:
        # TODO: check rules with chain of responsability pattern
        # Rules: force move bar
        # Rules: no move is more than one enemy pieces
        # Rules: no move to OFF_BOARD if not all piece in last_square
        moves: list[Move] = []
        game = self.match.last_game
        current_color = game.turn.current_color
        opponent_color = game.turn.opponent_player.color

        for pos in reversed(Position):
            is_piece = game.board.count_color_in_position(current_color, pos)
            if not is_piece:
                continue

            for dice_value in set(game.possible_moves):
                move = Move(position_from=pos, dice_value=dice_value)
                enemy_pieces = game.board.count_color_in_position(opponent_color, move.position_to)
                if enemy_pieces >= 2:
                    continue

                if (
                    move.position_to == Position.OFF_BOARD and
                    not game.board.is_all_pieces_first_square(current_color)
                ):
                    continue

                moves.append(move)

            if pos == Position.BAR:
                break

        return moves

    def is_goal(self) -> bool:
        return self.match.is_goal()

    def bet(self) -> None:
        self.bet_controller()

    def move_piece(self, move: Move) -> None:
        self.move_piece_controller(move)

    def roll_dice(self) -> None:
        self.match.last_game.roll_current_player()
