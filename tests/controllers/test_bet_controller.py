import unittest
from unittest.mock import patch

from src.controllers import BetController
from src.models import Game, Player, Turn
from src.models.doubling_cube import doubling_cube
from src.views import GameView
from src.views.bet_view import BetView
from src.types import Color, GameState


class BetControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.turn = Turn((Player(Color.BLACK), Player(Color.RED)))
        self.game = Game(self.turn)
        self.bet_controller = BetController(self.game, GameView())

    def test_ask_change_turn_and_game_state(self) -> None:
        self.assertEqual(self.game.current_player.color, Color.BLACK)
        self.assertEqual(self.game.state, GameState.IN_GAME)

        self.bet_controller.ask()

        self.assertEqual(self.game.current_player.color, Color.RED)
        self.assertEqual(self.game.state, GameState.BETTING)

    def test_answer_accept(self) -> None:
        self.game.state = GameState.BETTING
        self.assertEqual(self.game.current_player.color, Color.BLACK)
        self.assertEqual(doubling_cube.value, 1)

        with patch.object(BetView, 'read', return_value=True):
            self.bet_controller.answer()

        self.assertEqual(self.game.current_player.color, Color.RED)
        self.assertEqual(self.game.state, GameState.IN_GAME)
        self.assertEqual(doubling_cube.value, 2)

    def test_answer_reject(self) -> None:
        self.game.state = GameState.BETTING
        self.assertEqual(self.game.current_player.color, Color.BLACK)

        with patch.object(BetView, 'read', return_value=False):
            self.bet_controller.answer()

        self.assertEqual(self.game.state, GameState.END_GAME)
        self.assertEqual(self.game.current_player.is_winner, False)
