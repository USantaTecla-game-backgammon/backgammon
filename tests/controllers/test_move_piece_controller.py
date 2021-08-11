import unittest
from unittest.mock import patch

from src.controllers import MovePieceController
from src.controllers.move_piece_controller import IllegalMove
from src.models import Game, Player, Turn
from src.views.console import BoardView
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
        self.turn = Turn((Player(Color.BLACK), Player(Color.RED)))
        self.game = Game(self.turn)
        self.move_piece_controller = MovePieceController(self.game, ConsoleViewFactory())

    def test_move_normal_valid_black(self) -> None:
        self.game.possible_moves = [1]
        self.assertEqual(self.game.get_pieces(Position(24)), [Color.BLACK, Color.BLACK])
        self.assertEqual(self.game.get_pieces(Position(23)), [])

        with patch.object(BoardView, 'read_position', return_value=24):
            self.move_piece_controller.move(1)

        self.assertEqual(self.game.get_pieces(Position(24)), [Color.BLACK])
        self.assertEqual(self.game.get_pieces(Position(23)), [Color.BLACK])

    def test_move_normal_valid_red(self) -> None:
        self.game.change_turn()
        self.game.possible_moves = [2]
        self.assertEqual(self.game.get_pieces(Position(24)), [Color.RED, Color.RED])
        self.assertEqual(self.game.get_pieces(Position(22)), [])

        with patch.object(BoardView, 'read_position', return_value=24):
            self.move_piece_controller.move(2)

        self.assertEqual(self.game.get_pieces(Position(24)), [Color.RED])
        self.assertEqual(self.game.get_pieces(Position(22)), [Color.RED])

    def test_move_from_bar(self) -> None:
        self.game.board.positions[Position.BAR] = [Color.BLACK]
        self.game.possible_moves = [2]

        with patch.object(BoardView, 'read_position', return_value=Position.BAR):
            self.move_piece_controller.move(2)

        self.assertEqual(self.game.get_pieces(Position.BAR), [])
        self.assertEqual(self.game.get_pieces(Position(23)), [Color.BLACK])

    def _test_move_eat_piece(self) -> None:
        self.game.board.positions[1] = [Color.RED]
        self.game.possible_moves = [5]

        self.assertEqual(self.game.get_pieces(Position(6)), [Color.BLACK] * 5)
        self.assertEqual(self.game.get_pieces(Position(1)), [Color.RED])
        self.assertEqual(self.game.get_pieces(Position.BAR), [])

        with patch.object(BoardView, 'read_position', return_value=6):
            self.move_piece_controller.move(5)

        self.assertEqual(self.game.get_pieces(Position(6)), [Color.BLACK] * 4)
        self.assertEqual(self.game.get_pieces(Position(1)), [Color.BLACK])
        self.assertEqual(self.game.get_pieces(Position.BAR), [Color.RED])

    def _test_move_invalid_by_opponent_pieces(self) -> None:
        self.game.possible_moves = [5]

        with patch.object(BoardView, 'read_position', return_value=24):
            with self.assertRaises(IllegalMove):
                self.move_piece_controller.move(5)

    def _test_move_invalid_by_piece_in_bar(self) -> None:
        self.game.board.positions[Position.BAR] = [Color.BLACK]
        self.game.possible_moves = [5]

        with patch.object(BoardView, 'read_position', return_value=24):
            with self.assertRaises(IllegalMove):
                self.move_piece_controller.move(5)

    def _test_move_invalid_by_unexist_piece(self) -> None:
        self.game.possible_moves = [1]

        with patch.object(BoardView, 'read_position', return_value=23):
            with self.assertRaises(IllegalMove):
                self.move_piece_controller.move(1)

    def _test_move_invalid_by_any_piece_not_in_last_square(self) -> None:
        self.game.possible_moves = [6]

        with patch.object(BoardView, 'read_position', return_value=6):
            with self.assertRaises(IllegalMove):
                self.move_piece_controller.move(6)
