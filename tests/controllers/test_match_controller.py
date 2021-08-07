import unittest
from unittest.mock import patch

from src.controllers import MatchController
from src.models import Match
from src.views import MatchView, console


class MatchControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()
        self.match_controller = MatchController(self.match, MatchView)

    @patch.object(MatchView, 'show')
    @patch.object(MatchView, 'read_goal')
    def test_match_controller_configure(self, mock_read, mock_show):
        goal = 2
        mock_read.return_value = goal

        self.match_controller.configure()
        mock_show.assert_called_once()
        mock_read.assert_called_once()
        self.assertEqual(self.match.goal, goal)

    def test_match_controller_initialize_game_without_goal_defined(self):
        with self.assertRaises(AssertionError):
            self.match_controller.initialize_game()

    def test_match_controller_initialize_game(self):
        self.assertEqual(len(self.match.games), 0)

        self.match.goal = 2
        self.match_controller.initialize_game()

        self.assertEqual(len(self.match.games), 1)

    @patch.object(Match, 'is_goal')
    def test_match_controller_is_goal(self, mock):
        self.match_controller.is_goal()
        mock.assert_called_once()

    def test_match_controller_resume_yes(self):
        with patch.object(console, 'read_bool', return_value=True):
            self.assertTrue(self.match_controller.resume())

    def test_match_controller_resume_no(self):
        with patch.object(console, 'read_bool', return_value=False):
            self.assertFalse(self.match_controller.resume())
