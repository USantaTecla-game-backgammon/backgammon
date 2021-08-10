import unittest
from unittest.mock import patch

from src.models import Board, Game, Player, Turn
from src.types import Color, Endgame


class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        turn = Turn((Player(Color.BLACK), Player(Color.RED)))
        self.game = Game(turn)

    def test_initial_game_have_board(self) -> None:
        self.assertIsNotNone(self.game.board)

    def test_type_endgame_simple(self) -> None:
        with (
            patch.object(Board, 'is_all_pieces_off_board', return_value=True),
            patch.object(Board, 'is_any_piece_off_board', return_value=True),
        ):
            self.assertEqual(self.game.get_endgame(), Endgame.SIMPLE)

    def test_type_endgame_gammon(self) -> None:
        with (
            patch.object(Board, 'is_all_pieces_off_board', return_value=True),
            patch.object(Board, 'is_any_piece_off_board', return_value=False),
            patch.object(Board, 'is_any_piece_at_first_square', return_value=False),
            patch.object(Board, 'is_any_piece_in_bar', return_value=False),
        ):
            self.assertEqual(self.game.get_endgame(), Endgame.GAMMON)

    def test_type_endgame_backgammon_first_square(self) -> None:
        with (
            patch.object(Board, 'is_all_pieces_off_board', return_value=True),
            patch.object(Board, 'is_any_piece_off_board', return_value=False),
            patch.object(Board, 'is_any_piece_at_first_square', return_value=True),
            patch.object(Board, 'is_any_piece_in_bar', return_value=False),
        ):
            self.assertEqual(self.game.get_endgame(), Endgame.BACKGAMMON)

    def test_type_endgame_backgammon_bar(self) -> None:
        with (
            patch.object(Board, 'is_all_pieces_off_board', return_value=True),
            patch.object(Board, 'is_any_piece_off_board', return_value=False),
            patch.object(Board, 'is_any_piece_at_first_square', return_value=False),
            patch.object(Board, 'is_any_piece_in_bar', return_value=True),
        ):
            self.assertEqual(self.game.get_endgame(), Endgame.BACKGAMMON)
