import unittest
from src.models.turn import Turn
from src.types.color import Color


class TurnTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.turn = Turn()

    def test_change_player_with_color_black(self) -> None:
        self.turn.change(color=Color.BLACK)
        self.assertIsNotNone(self.turn.current_player)
        self.assertEqual(self.turn.current_player.color, Color.BLACK)

    def test_change_player_with_color_red(self) -> None:
        self.turn.change(color=Color.RED)
        self.assertIsNotNone(self.turn.current_player)
        self.assertEqual(self.turn.current_player.color, Color.RED)

    def test_change_player_turn(self) -> None:
        self.assertEqual(self.turn.current_player.color, Color.BLACK)
        self.turn.change()
        self.assertEqual(self.turn.current_player.color, Color.RED)
        self.turn.change()
        self.assertEqual(self.turn.current_player.color, Color.BLACK)
