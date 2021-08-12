import unittest
from unittest.mock import patch

from src.controllers.move_piece_controller import MovePieceController
from src.models import Board, Game, Match, Move
from src.views.console.console_view_factory import ConsoleViewFactory
from src.types import Color, Position


# INITIAL STATE OF BOARD
#
# |--------------------------------------------------------|
# |  13  14  15  16  17  18 |    |  19  20  21  22  23  24 |
# |  5●              3○     |    |  5○                  2● |
# |                         |  0○|                         |
# |                         | BAR|                         |
# |                         |  0●|                         |
# |  5○              3●     |    |  5●                  2○ |
# |  12  11  10   9   8   7 |    |   6   5   4   3   2   1 |
# |--------------------------------------------------------|


class MovePieceControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()
        self.match = Match()
        self.match.games = [self.game]
        self.move_piece_controller = MovePieceController(self.match, ConsoleViewFactory())

    def test_move_eat_piece(self) -> None:
        self.game.board.positions[1] = [Color.RED]
        self.game.possible_moves = [5]

        move = Move(position_from=Position(6), dice_value=5)

        with (
            patch.object(Game, 'move_piece') as mock_move,
            patch.object(Board, 'eat_piece') as mock_eat,
        ):
            self.move_piece_controller(move)
            mock_move.assert_called_once_with(move)
            mock_eat.assert_called_once_with(move.position_to)
