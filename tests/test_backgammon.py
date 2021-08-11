import unittest
from unittest.mock import patch

from src.backgammon import Backgammon
from src.controllers import (
    PlayController,
    StartController,
    ResumeController,
)
from src.views.console.console_view_factory import ConsoleViewFactory


class BackgammonTest(unittest.TestCase):

    def setUp(self) -> None:
        self.backgammon = Backgammon(ConsoleViewFactory())

    def test_backgammon_flow(self) -> None:
        with (
            patch.object(StartController, '__call__') as mock_start,
            patch.object(PlayController, '__call__') as mock_play,
            patch.object(ResumeController, '__call__', side_effect=[True, False]) as mock_resume,
        ):
            self.backgammon.play()
            self.assertEqual(mock_start.call_count, 2)
            self.assertEqual(mock_play.call_count, 2)
            self.assertEqual(mock_resume.call_count, 2)
