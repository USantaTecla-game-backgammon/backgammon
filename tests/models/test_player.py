import unittest
from src.models.player import Player
from src.types.color import Color


class PlayerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player(Color.RED)

    def test_player_default_values(self) -> None:
        self.assertFalse(self.player.score)
        self.assertFalse(self.player.doubling_cube)

    def test_player_earn_score(self) -> None:
        score = 3
        self.player.earn_score(score)
        self.assertTrue(self.player.score, score)
