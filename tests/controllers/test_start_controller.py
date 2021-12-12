import unittest
from unittest.mock import MagicMock, patch

from src.controllers import StartController
from src.models import Match
from src.views.console import MatchView
from src.views.console.console_view_factory import ConsoleViewFactory


class StartControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()
        self.start_controller = StartController(self.match, ConsoleViewFactory())

    @patch.object(MatchView, 'show_title')
    @patch.object(MatchView, 'read_goal')
    def test_match_controller_configure(
        self,
        mock_read: MagicMock,
        mock_show: MagicMock,
    ) -> None:

        goal = 2
        mock_read.return_value = goal

        self.start_controller.configure_goal()
        mock_show.assert_called_once()
        mock_read.assert_called_once()
        self.assertEqual(self.match.goal, goal)
