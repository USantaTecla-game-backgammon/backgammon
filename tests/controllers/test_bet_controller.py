import unittest
from unittest.mock import patch

from src.controllers.bet_controller import BetController
from src.models import Game, Match
from src.models.doubling_cube import doubling_cube
from src.views.console.console_view_factory import ConsoleViewFactory
from src.views.console import BetView
from src.types import Color, GameState


class BetControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()
        match = Match()
        match.games = [self.game]
        self.bet_controller = BetController(match, ConsoleViewFactory())

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

        with (
            patch.object(BetView, 'read', return_value=True) as mock_read,
            patch.object(BetView, 'show_accept') as mock_show
        ):
            self.bet_controller.answer()
            mock_read.assert_called_once()
            mock_show.assert_called_once()

        self.assertEqual(self.game.current_player.color, Color.RED)
        self.assertEqual(self.game.state, GameState.IN_GAME)
        self.assertEqual(doubling_cube.value, 2)

    def test_answer_reject(self) -> None:
        self.game.state = GameState.BETTING
        self.assertEqual(self.game.current_player.color, Color.BLACK)

        with (
            patch.object(BetView, 'read', return_value=False) as mock_read,
            patch.object(BetView, 'show_reject') as mock_show
        ):
            self.bet_controller.answer()
            mock_read.assert_called_once()
            mock_show.assert_called_once()

        self.assertEqual(self.game.state, GameState.END_GAME)
        self.assertEqual(self.game.current_player.is_winner, False)
