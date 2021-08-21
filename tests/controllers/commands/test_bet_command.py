import unittest
from unittest.mock import patch

from src.controllers import PlayController
from src.models import Match, Turn, Game
from src.models.commands.bet import BetCommand
from src.types import GameState
from src.views.console.console_view_factory import ConsoleViewFactory


class BetCommandTest(unittest.TestCase):

    def setUp(self) -> None:
        self.play_controller = PlayController(Match(), ConsoleViewFactory())
        self.bet_command = BetCommand(self.play_controller)

    def test_is_called_once(self) -> None:
        with patch.object(PlayController, 'bet') as mock_bet:
            self.bet_command()
            mock_bet.assert_called_once()
            self.assertEqual(self.bet_command.title, 'bet')

    def test_is_active_in_game_can_bet_then_true(self) -> None:
        game = Game()
        game.state = GameState.IN_GAME
        self.play_controller.match.games.append(game)
        with patch.object(Turn, 'can_bet_current_player', return_value=True):
            is_active = self.bet_command.is_active()
        self.assertTrue(is_active)

    def test_is_active_in_game_cannot_bet_then_false(self) -> None:
        game = Game()
        game.state = GameState.IN_GAME
        self.play_controller.match.games.append(game)
        with patch.object(Turn, 'can_bet_current_player', return_value=False):
            is_active = self.bet_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_betting_can_bet_then_true(self) -> None:
        game = Game()
        game.state = GameState.BETTING
        self.play_controller.match.games.append(game)
        with patch.object(Turn, 'can_bet_current_player', return_value=True):
            is_active = self.bet_command.is_active()
        self.assertTrue(is_active)

    def test_is_active_betting_cannot_bet_then_false(self) -> None:
        game = Game()
        game.state = GameState.BETTING
        self.play_controller.match.games.append(game)
        with patch.object(Turn, 'can_bet_current_player', return_value=False):
            is_active = self.bet_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_moving_piece_can_bet_then_false(self) -> None:
        game = Game()
        game.state = GameState.MOVING_PIECE
        self.play_controller.match.games.append(game)
        with patch.object(Turn, 'can_bet_current_player', return_value=True):
            is_active = self.bet_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_end_game_can_bet_then_false(self) -> None:
        game = Game()
        game.state = GameState.END_GAME
        self.play_controller.match.games.append(game)
        with patch.object(Turn, 'can_bet_current_player', return_value=True):
            is_active = self.bet_command.is_active()
        self.assertFalse(is_active)
