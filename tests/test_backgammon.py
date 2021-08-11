import unittest
from unittest.mock import patch

from src.backgammon import Backgammon
from src.models import Dice, Match
from src.views.console import MatchView
from src.types import Color
from src.controllers.game_controller import GameController
from src.views.console.console_view_factory import ConsoleViewFactory


class BackgammonTest(unittest.TestCase):

    def setUp(self) -> None:
        self.backgammon = Backgammon(ConsoleViewFactory())

    def test_backgammon_flow_resume(self) -> None:
        first_roll = {Color.BLACK: Dice(1), Color.RED: Dice(6)}

        with (
            patch.object(MatchView, 'show_title'),
            patch.object(MatchView, 'read_goal', return_value=1),

            patch.object(Match, 'first_roll', return_value=first_roll),
            patch.object(Match, 'is_goal', return_value=True),

            patch.object(MatchView, 'read_resume', side_effect=[True, False])
        ):
            self.backgammon.play()
            self.assertEqual(self.backgammon.match.goal, 1)

    def test_backgammon_flow_game(self) -> None:
        first_roll = {Color.BLACK: Dice(1), Color.RED: Dice(6)}

        with (
            patch.object(MatchView, 'show_title'),
            patch.object(MatchView, 'read_goal', return_value=1),

            patch.object(Match, 'first_roll', return_value=first_roll),
            patch.object(Match, 'is_goal', side_effect=[False, True]),
            patch.object(GameController, 'play') as mock_play,

            patch.object(MatchView, 'read_resume', return_value=False)
        ):
            self.backgammon.play()
            self.assertEqual(self.backgammon.match.goal, 1)
            mock_play.assert_called_once()
