import unittest

from src.models import Dice, Match
from src.types import Color


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
