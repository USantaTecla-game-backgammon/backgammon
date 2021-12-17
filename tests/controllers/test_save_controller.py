import unittest
from pathlib import Path

from src.models.match import Match
from src.controllers.save_controller import SaveController


class SaveControllerTest(unittest.TestCase):

    def test_save_complete_match(self) -> None:
        self.match = Match()
        self.save_controller = SaveController(self.match, 'save.pickle')
        self.save_controller()
        self.assertTrue(Path('saved/save.pickle').is_file())
