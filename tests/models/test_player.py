import unittest
from src.models.player import Player
from src.types.color import Color


class PlayerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player(Color.RED)

    def test_player_default_values(self) -> None:
        self.assertFalse(self.player.score)
        self.assertFalse(self.player.doubling_cube)
