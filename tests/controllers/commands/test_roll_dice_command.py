import unittest
from unittest.mock import patch

from src.controllers import PlayController
from src.models import Match, Game
from src.models.commands.roll_dice import RollDiceCommand
from src.types import GameState
from src.views.console.console_view_factory import ConsoleViewFactory


class RollDiceCommandTest(unittest.TestCase):

    def setUp(self) -> None:
        self.play_controller = PlayController(Match(), ConsoleViewFactory())
        self.roll_dice_command = RollDiceCommand(self.play_controller)

    def test_is_called_once(self) -> None:
        with patch.object(PlayController, 'roll_dice') as mock_roll_dice:
            self.roll_dice_command()
            mock_roll_dice.assert_called_once()
            self.assertEqual(self.roll_dice_command.title, 'roll')

    def test_is_active_in_game_then_true(self) -> None:
        game = Game()
        game.state = GameState.IN_GAME
        self.play_controller.match.games.append(game)
        is_active = self.roll_dice_command.is_active()
        self.assertTrue(is_active)

    def test_is_active_betting_then_false(self) -> None:
        game = Game()
        game.state = GameState.BETTING
        self.play_controller.match.games.append(game)
        is_active = self.roll_dice_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_end_game_then_false(self) -> None:
        game = Game()
        game.state = GameState.END_GAME
        self.play_controller.match.games.append(game)
        is_active = self.roll_dice_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_moving_piece_then_false(self) -> None:
        game = Game()
        game.state = GameState.MOVING_PIECE
        self.play_controller.match.games.append(game)
        is_active = self.roll_dice_command.is_active()
        self.assertFalse(is_active)
