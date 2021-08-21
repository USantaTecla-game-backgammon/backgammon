import unittest
from unittest.mock import patch

from src.controllers import PlayController
from src.models import Match, Move, Game
from src.models.commands.move_piece import MovePieceCommand
from src.types import GameState, Position
from src.views.console.console_view_factory import ConsoleViewFactory


class MovePieceCommandTest(unittest.TestCase):

    def setUp(self) -> None:
        self.position_from = Position.ONE
        self.position_to = Position.FIVE
        self.dice_value = 4
        move = Move(
            position_from=self.position_from,
            position_to=self.position_to,
            dice_value=self.dice_value
        )
        self.play_controller = PlayController(Match(), ConsoleViewFactory())
        self.move_piece_command = MovePieceCommand(self.play_controller, move)

    def test_is_called_once(self) -> None:
        with patch.object(PlayController, 'move_piece') as mock_bet:
            self.move_piece_command()
            mock_bet.assert_called_once()
            self.assertEqual(self.move_piece_command.title,
                             f'Move from point {self.position_from} to {self.position_to} '
                             f'(dice {self.dice_value})')

    def test_is_active_in_game_then_false(self) -> None:
        game = Game()
        game.state = GameState.IN_GAME
        self.play_controller.match.games.append(game)
        is_active = self.move_piece_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_betting_then_false(self) -> None:
        game = Game()
        game.state = GameState.BETTING
        self.play_controller.match.games.append(game)
        is_active = self.move_piece_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_end_game_then_false(self) -> None:
        game = Game()
        game.state = GameState.END_GAME
        self.play_controller.match.games.append(game)
        is_active = self.move_piece_command.is_active()
        self.assertFalse(is_active)

    def test_is_active_moving_piece_then_true(self) -> None:
        game = Game()
        game.state = GameState.MOVING_PIECE
        self.play_controller.match.games.append(game)
        is_active = self.move_piece_command.is_active()
        self.assertTrue(is_active)
