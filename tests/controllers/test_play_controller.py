import unittest
from unittest.mock import MagicMock, patch

from src.controllers import PlayController
from src.models import Game, Match
from src.views.console.console_view_factory import ConsoleViewFactory
from src.types import Endgame


class PlayControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()
        self.play_controller = PlayController(self.match, ConsoleViewFactory())

    @patch.object(Game, 'is_endgame', side_effect=[False, True])
    @patch.object(Game, 'type_endgame', return_value=Endgame.SIMPLE)
    def test_play_when_not_is_endgame(
        self,
        mock_endgame: MagicMock,
        mock_game: MagicMock,
    ) -> None:
        self.match.goal = 1
        self.play_controller.__call__()
        self.assertEqual(mock_game.call_count, 2)
        self.assertEqual(mock_endgame.call_count, 1)

    @patch.object(Match, 'is_goal')
    def test_is_goal(self, mock: MagicMock) -> None:
        self.match.goal = 1
        self.play_controller.is_goal()
        mock.assert_called_once()

    def test_initialize_game_without_goal_defined(self) -> None:
        with self.assertRaises(AssertionError):
            self.play_controller.initialize_game()

    def test_initialize_game(self) -> None:
        self.match.goal = 1
        self.assertEqual(len(self.match.games), 0)

        self.match.goal = 2
        self.play_controller.initialize_game()

        self.assertEqual(len(self.match.games), 1)
