import unittest

from src.models.match import Match
from src.models.move import Move
from src.controllers.save_controller import SaveController
from src.types.position import Position


class SaveControllerTest(unittest.TestCase):

    def test_save_complete_match(self) -> None:
        match = Match()
        filename = 'save.pickle'
        save_controller = SaveController(match, filename)
        save_controller()
        self.assertTrue(save_controller.filepath.is_file())

    def test_save_complete_match_with_different_name(self) -> None:
        match = Match()
        filename = 'save2.pickle'
        save_controller = SaveController(match, filename)
        save_controller()
        self.assertTrue(save_controller.filepath.is_file())

    def test_save_with_different_state_are_different(self) -> None:
        match = Match()
        filename = 'state1.pickle'
        save_controller = SaveController(match, filename)
        save_controller()

        match = Match()
        match.last_game.possible_moves = [4]
        match.last_game.move_piece(Move(position_from=Position.TWENTY_FOUR, dice_value=4))
        filename2 = 'state2.pickle'
        save_controller2 = SaveController(match, filename2)
        save_controller2()

        with (
            save_controller.filepath.open(mode='rb') as file1,
            save_controller2.filepath.open(mode='rb') as file2,
        ):
            text1 = file1.read()
            text2 = file2.read()
        self.assertNotEqual(text1, text2)
