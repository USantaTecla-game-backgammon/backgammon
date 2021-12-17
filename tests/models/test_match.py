import unittest
from unittest.mock import patch

from src.models import Board, Dice, Match, Game
from src.models.doubling_cube import doubling_cube
from src.types import Color, Endgame


class MatchTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()

    def test_initial_match(self) -> None:
        self.assertEqual(len(self.match.games), 1)
        self.assertFalse(self.match.goal)
        self.assertEqual(len(self.match.turn.players), 2)

    def test_is_goal_false(self) -> None:
        self.match.goal = 3
        self.assertFalse(self.match.is_goal())

    def test_is_goal_true(self) -> None:
        goal = 3
        self.match.goal = goal
        self.match.turn.players[0].score = goal
        self.assertTrue(self.match.is_goal())

    def test_first_roll(self) -> None:
        first_roll = self.match.throw_first_dices()

        self.assertTrue(Color.BLACK in first_roll.keys())
        self.assertTrue(Color.RED in first_roll.keys())
        for value in first_roll.values():
            self.assertIsInstance(value, Dice)

    def test_give_same_score_game_and_match(self) -> None:
        def side_effect_board(color: Color) -> bool:
            return color == Color.BLACK

        # Given a empty match and game, the start score in match and game are 0
        self.match.add_game()

        # When
        with (
                patch.object(Game, 'get_type_endgame', return_value=Endgame.SIMPLE),
                patch.object(Board, 'is_all_pieces_off_board', side_effect=side_effect_board),
        ):
            self.match.give_score()

        # Then
        score = doubling_cube.value * Endgame.SIMPLE
        self.assertEqual(self.match.turn.current_player.score, score)
        self.assertEqual(self.match.last_game.turn.current_player.score, score)

        self.assertEqual(self.match.turn.opponent_player.score, 0)
        self.assertEqual(self.match.last_game.turn.opponent_player.score, 0)

    def test_give_score_match_during_match(self) -> None:
        def side_effect_board(color: Color) -> bool:
            return color == Color.BLACK

        # Given a empty match and game, the start score in match and game are 0
        initial_score = 5
        self.match.turn.current_player.score = initial_score
        self.match.add_game()

        # When
        with (
                patch.object(Game, 'get_type_endgame', return_value=Endgame.SIMPLE),
                patch.object(Board, 'is_all_pieces_off_board', side_effect=side_effect_board),
        ):
            self.match.give_score()

        # Then
        score = doubling_cube.value * Endgame.SIMPLE
        self.assertEqual(self.match.turn.current_player.score, initial_score + score)
        self.assertEqual(self.match.last_game.turn.current_player.score, score)

        self.assertEqual(self.match.turn.opponent_player.score, 0)
        self.assertEqual(self.match.last_game.turn.opponent_player.score, 0)
