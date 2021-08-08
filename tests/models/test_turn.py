import unittest
from src.models.turn import Turn
from src.types.color import Color
from src.models.player import Player


class TurnTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.turn = Turn((Player(Color.BLACK), Player(Color.RED)))

    def test_change_player_with_color_black(self) -> None:
        self.turn.change(color=Color.BLACK)
        self.assertIsNotNone(self.turn.current_player)
        self.assertEqual(self.turn.current_player.color, Color.BLACK)

    def test_change_player_with_color_red(self) -> None:
        self.turn.change(color=Color.RED)
        self.assertIsNotNone(self.turn.current_player)
        self.assertEqual(self.turn.current_player.color, Color.RED)

    def test_change_player_turn(self) -> None:
        self.turn.current_player = self.turn.players[0]
        self.turn.change()
        self.assertEqual(self.turn.current_player, self.turn.players[1])

    def test_change_player_turn_reverse(self) -> None:
        self.turn.current_player = self.turn.players[1]
        self.turn.change()
        self.assertEqual(self.turn.current_player, self.turn.players[0])
