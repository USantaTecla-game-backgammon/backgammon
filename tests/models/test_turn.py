import unittest
from src.models.turn import Turn
from src.types.color import Color
from src.models.player import Player


class TurnTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.turn = Turn((Player(Color.BLACK), Player(Color.RED)))

    def test_not_two_players_tuple_then_assertion_error(self):
        with self.assertRaises(AssertionError):
            Turn(tuple())
            Turn(tuple(Player(Color.RED)))
            Turn((Player(Color.BLACK), Player(Color.BLACK), Player(Color.BLACK)))

    def test_current_player_is_none(self):
        self.assertIsNone(self.turn.current_player)

    def test_change_player_with_color_black(self):
        self.turn.change(color=Color.BLACK)
        self.assertEqual(self.turn.current_player.color, Color.BLACK)

    def test_change_player_with_color_red(self):
        self.turn.change(color=Color.RED)
        self.assertEqual(self.turn.current_player.color, Color.RED)

    def test_change_player_turn(self):
        self.turn.current_player = self.turn.players[0]
        self.turn.change()
        self.assertEqual(self.turn.current_player, self.turn.players[1])

    def test_change_player_turn_reverse(self):
        self.turn.current_player = self.turn.players[1]
        self.turn.change()
        self.assertEqual(self.turn.current_player, self.turn.players[0])
