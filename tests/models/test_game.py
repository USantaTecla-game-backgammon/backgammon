import unittest
from unittest.mock import patch

from src.models import Board, Game
from src.types import Endgame


class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_initial_game_have_board(self) -> None:
        self.assertIsNotNone(self.game.board)

    @patch.object(Board, 'is_all_pieces_off_board', return_value=True)
    @patch.object(Board, 'is_any_piece_off_board', return_value=True)
    def test_type_endgame_simple(self, *_) -> None:
        self.assertEqual(self.game.type_endgame(), Endgame.SIMPLE)

    @patch.object(Board, 'is_all_pieces_off_board', return_value=True)
    @patch.object(Board, 'is_any_piece_off_board', return_value=False)
    @patch.object(Board, 'is_any_piece_at_first_square', return_value=False)
    @patch.object(Board, 'is_any_piece_in_bar', return_value=False)
    def test_type_endgame_gammon(self, *_) -> None:
        self.assertEqual(self.game.type_endgame(), Endgame.GAMMON)

    @patch.object(Board, 'is_all_pieces_off_board', return_value=True)
    @patch.object(Board, 'is_any_piece_off_board', return_value=False)
    @patch.object(Board, 'is_any_piece_at_first_square', return_value=True)
    @patch.object(Board, 'is_any_piece_in_bar', return_value=False)
    def test_type_endgame_backgammon_first_square(self, *_) -> None:
        self.assertEqual(self.game.type_endgame(), Endgame.BACKGAMMON)

    @patch.object(Board, 'is_all_pieces_off_board', return_value=True)
    @patch.object(Board, 'is_any_piece_off_board', return_value=False)
    @patch.object(Board, 'is_any_piece_at_first_square', return_value=False)
    @patch.object(Board, 'is_any_piece_in_bar', return_value=True)
    def test_type_endgame_backgammon_bar(self, *_) -> None:
        self.assertEqual(self.game.type_endgame(), Endgame.BACKGAMMON)
