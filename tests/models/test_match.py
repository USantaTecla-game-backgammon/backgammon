import unittest
from unittest.mock import patch

from src.models import Dice, Match, Game
from src.types import Color, Endgame
from src.models.doubling_cube import doubling_cube

class MatchTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()

    def test_initial_match(self) -> None:
        self.assertFalse(self.match.games)
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
        score_match: int = 0
        score_game: int = 0
        self.match.add_game()
        self.assertEqual(self.match.turn.current_player.score, score_match)
        self.assertEqual(self.match.last_game.turn.current_player.score, score_game)

        with patch.object(Game, "get_type_endgame", return_value=Endgame.SIMPLE):
            self.match.give_score()

        score = doubling_cube.value * Endgame.SIMPLE
        self.assertEqual(self.match.turn.current_player.score, score)
        # self.assertEqual(self.match.last_game.turn.current_player.score, score)










