import unittest
from unittest.mock import MagicMock, patch

from src.controllers import GameController
from src.models import Game, Match
from src.models.commands import (
    BetCommand,
    MovePieceCommand,
    RollDiceCommand,
)
from src.views import GameView
from src.views.menu_view import MenuView
from src.types.game_state import GameState


class GameControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()
        self.match = Match()
        self.match.games.append(self.game)
        self.game_controller = GameController(self.match, GameView())

    @patch.object(BetCommand, '__init__', return_value=None)
    @patch.object(MovePieceCommand, '__init__', return_value=None)
    @patch.object(RollDiceCommand, '__init__', return_value=None)
    @patch.object(Game, 'is_endgame', return_value=True)
    def test_game_controller_play_when_is_endgame(
        self,
        mock_game: MagicMock,
        mock_roll_dice_cmd: MagicMock,
        mock_move_piece_cmd: MagicMock,
        mock_bet_cmd: MagicMock,
    ) -> None:
        self.game_controller.play()
        mock_game.assert_called_once()
        mock_roll_dice_cmd.assert_called_once()
        mock_move_piece_cmd.assert_called_once()
        mock_bet_cmd.assert_called_once()

    def check_active_commands_depend_on_game_state(
        self,
        game_state: GameState,
        expected_commands: list[str],
    ) -> None:
        self.game.state = game_state
        with patch.object(Game, 'is_endgame', return_value=True):
            self.game_controller.play()
            active_commands = self.game_controller.menu.active_commands()
            self.assertEqual([cmd.title for cmd in active_commands], expected_commands)
            self.assertEqual(len(active_commands), len(expected_commands))

    def test_active_commands_with_in_game(self) -> None:
        self.check_active_commands_depend_on_game_state(
            game_state=GameState.IN_GAME,
            expected_commands=[BetCommand.title, RollDiceCommand.title],
        )

    def test_active_commands_with_moving_piece(self) -> None:
        self.check_active_commands_depend_on_game_state(
            game_state=GameState.MOVING_PIECE,
            expected_commands=[MovePieceCommand.title],
        )

    def test_active_commands_with_betting(self) -> None:
        self.check_active_commands_depend_on_game_state(
            game_state=GameState.BETTING,
            expected_commands=[BetCommand.title],
        )

    def test_active_commands_with_end_game(self) -> None:
        self.check_active_commands_depend_on_game_state(
            game_state=GameState.END_GAME,
            expected_commands=[],
        )

    @patch.object(Game, 'is_endgame', side_effect=[False, True])
    @patch.object(MenuView, '__call__')
    def test_game_controller_play_when_not_is_endgame(
        self,
        mock_view: MagicMock,
        mock_game: MagicMock,
    ) -> None:
        self.game_controller.play()
        self.assertEqual(mock_game.call_count, 2)
        self.assertEqual(mock_view.call_count, 1)
