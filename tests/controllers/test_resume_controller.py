import unittest
from unittest.mock import patch

from src.controllers import ResumeController
from src.models import Match
from src.views.console.console_view_factory import ConsoleViewFactory
from src.views.console import console


class ResumeControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()
        self.resume_controller = ResumeController(self.match, ConsoleViewFactory())

    def test_match_controller_resume_yes(self) -> None:
        with patch.object(console, 'read_bool', return_value=True):
            self.assertTrue(self.resume_controller())

    def test_match_controller_resume_no(self) -> None:
        with patch.object(console, 'read_bool', return_value=False):
            self.assertFalse(self.resume_controller())
