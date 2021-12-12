import unittest
from unittest.mock import MagicMock, patch

from src.controllers import StartController
from src.models import Dice, Match, Turn
from src.types import Color
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

    @patch.object(Turn, 'change')
    @patch.object(MatchView, 'show_dices')
    @patch.object(Match, 'throw_first_dices')
    def test_match_controller_first_roll_one_tie_and_black_win(
        self,
        mock_roll: MagicMock,
        mock_show: MagicMock,
        mock_turn: MagicMock,
    ) -> None:
        mock_roll.side_effect = [
            {Color.BLACK: Dice(4), Color.RED: Dice(4)},
            {Color.BLACK: Dice(5), Color.RED: Dice(3)},
        ]
        self.start_controller.roll_dice_controller.first_roll()
        mock_turn.assert_called_once_with(Color.BLACK)
        self.assertEqual(mock_show.call_count, 2)

    @patch.object(Turn, 'change')
    @patch.object(MatchView, 'show_dices')
    @patch.object(Match, 'throw_first_dices')
    def test_match_controller_first_roll_red_win(
        self,
        mock_roll: MagicMock,
        mock_show: MagicMock,
        mock_turn: MagicMock,
    ) -> None:
        mock_roll.return_value = {Color.BLACK: Dice(1), Color.RED: Dice(6)}
        self.start_controller.roll_dice_controller.first_roll()
        mock_turn.assert_called_once_with(Color.RED)
        self.assertEqual(mock_show.call_count, 1)
