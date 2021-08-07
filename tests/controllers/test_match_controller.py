import unittest
from unittest.mock import MagicMock, patch

from src.controllers import MatchController
from src.models import Dice, Match, Turn
from src.types import Color
from src.views import MatchView, console


class MatchControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()
        self.match_controller = MatchController(self.match, MatchView())

    @patch.object(MatchView, 'show_title')
    @patch.object(MatchView, 'read_goal')
    def test_match_controller_configure(
        self,
        mock_read: MagicMock,
        mock_show: MagicMock,
    ) -> None:

        goal = 2
        mock_read.return_value = goal

        self.match_controller.configure()
        mock_show.assert_called_once()
        mock_read.assert_called_once()
        self.assertEqual(self.match.goal, goal)

    def test_match_controller_initialize_game_without_goal_defined(self) -> None:
        with self.assertRaises(AssertionError):
            self.match_controller.initialize_game()

    def test_match_controller_initialize_game(self) -> None:
        self.assertEqual(len(self.match.games), 0)

        self.match.goal = 2
        self.match_controller.initialize_game()

        self.assertEqual(len(self.match.games), 1)

    @patch.object(Turn, 'next')
    @patch.object(MatchView, 'show_dices')
    @patch.object(Match, 'first_roll')
    def test_match_controller_first_roll_one_tie_and_black_win(
        self,
        mock_roll: MagicMock,
        mock_show: MagicMock,
        mock_turn: MagicMock,
    ):
        mock_roll.side_effect = [
            {Color.BLACK: Dice(4), Color.RED: Dice(4)},
            {Color.BLACK: Dice(5), Color.RED: Dice(3)},
        ]
        self.match_controller.first_roll()
        mock_turn.assert_called_once_with(Color.BLACK)
        self.assertEqual(mock_show.call_count, 2)

    @patch.object(Turn, 'next')
    @patch.object(MatchView, 'show_dices')
    @patch.object(Match, 'first_roll')
    def test_match_controller_first_roll_red_win(
        self,
        mock_roll: MagicMock,
        mock_show: MagicMock,
        mock_turn: MagicMock,
    ):
        mock_roll.return_value = {Color.BLACK: Dice(1), Color.RED: Dice(6)}
        self.match_controller.first_roll()
        mock_turn.assert_called_once_with(Color.RED)
        self.assertEqual(mock_show.call_count, 1)

    @patch.object(Match, 'is_goal')
    def test_match_controller_is_goal(self, mock: MagicMock) -> None:
        self.match_controller.is_goal()
        mock.assert_called_once()

    def test_match_controller_resume_yes(self) -> None:
        with patch.object(console, 'read_bool', return_value=True):
            self.assertTrue(self.match_controller.resume())

    def test_match_controller_resume_no(self) -> None:
        with patch.object(console, 'read_bool', return_value=False):
            self.assertFalse(self.match_controller.resume())
