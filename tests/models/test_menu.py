import unittest

from src.models import Game, Menu, Player, Turn
from src.models.commands import MovePieceCommand
from src.views import GameView
from src.types import Color, GameState, Position
from src.controllers.move_piece_controller import MovePieceController


class MenuTest(unittest.TestCase):

    def setUp(self) -> None:
        self.menu = Menu('', [])

    def _test_disable_move_if_not_possible_exit_bar(self):
        turn = Turn((Player(Color.BLACK), Player(Color.RED)))
        game = Game(turn)
        game.state = GameState.MOVING_PIECE
        game.board.positions[Position.BAR] = [Color.BLACK]

        move = 6
        self.menu.commands = [
            MovePieceCommand(MovePieceController(game, GameView()), move)
        ]

        self.assertFalse(self.menu.active_commands())

    def _test_disable_move_if_not_possible_move(self):
        turn = Turn((Player(Color.BLACK), Player(Color.RED)))
        game = Game(turn)
        game.state = GameState.MOVING_PIECE
        game.board.positions[Position.BAR] = [Color.BLACK]

        move = 6
        self.menu.commands = [
            MovePieceCommand(MovePieceController(game, GameView()), move)
        ]

        self.assertFalse(self.menu.active_commands())
