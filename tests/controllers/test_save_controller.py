import unittest
from pathlib import Path

from src.models.match import Match
from src.models.move import Move
from src.controllers.save_controller import SaveController
from src.types.position import Position


class SaveControllerTest(unittest.TestCase):

    def test_save_complete_match(self) -> None:
        self.match = Match()
        self.save_controller = SaveController(self.match, 'save.pickle')
        self.save_controller()
        self.assertTrue(Path('saved/save.pickle').is_file())

    def test_save_complete_match_with_different_name(self) -> None:
        self.match = Match()
        self.save_controller = SaveController(self.match, 'save2.pickle')
        self.save_controller()
        self.assertTrue(Path('saved/save2.pickle').is_file())

    def test_save_with_different_state_are_different(self) -> None:
        self.match = Match()
        self.save_controller = SaveController(self.match, 'state1.pickle')
        self.save_controller()

        self.match = Match()
        self.match.last_game.possible_moves = [4]
        self.match.last_game.move_piece(Move(position_from=Position.TWENTY_FOUR, dice_value=4))
        self.save_controller = SaveController(self.match, 'state2.pickle')
        self.save_controller()

        with (
            open('saved/state1.pickle', 'rb') as file1,
            open('saved/state2.pickle', 'rb') as file2
        ):
            text1 = file1.read()
            text2 = file2.read()
        self.assertNotEqual(text1, text2)
