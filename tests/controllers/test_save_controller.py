import unittest
from unittest.mock import patch

from src.models.match import Match
from src.models.move import Move
from src.controllers.save_controller import SaveController
from src.types.position import Position
from src.views.console.match_view import MatchView
from src.views.console.console_view_factory import ConsoleViewFactory


class SaveControllerTest(unittest.TestCase):

    def test_save_complete_match(self) -> None:
        match = Match()
        filename = 'save.pickle'
        save_controller = SaveController(match, ConsoleViewFactory())
        with patch.object(MatchView, 'read_filename', return_value=filename):
            save_controller()
        self.assertTrue(save_controller.filepath.is_file())

    def test_save_complete_match_with_different_name(self) -> None:
        match = Match()
        filename = 'save2.pickle'
        save_controller = SaveController(match, ConsoleViewFactory())
        with patch.object(MatchView, 'read_filename', return_value=filename):
            save_controller()
        self.assertTrue(save_controller.filepath.is_file())

    def test_save_with_different_state_are_different(self) -> None:
        match = Match()
        filename = 'state1.pickle'
        save_controller = SaveController(match, ConsoleViewFactory())
        with patch.object(MatchView, 'read_filename', return_value=filename):
            save_controller()

        match = Match()
        match.last_game.possible_moves = [4]
        match.last_game.move_piece(Move(position_from=Position.TWENTY_FOUR, dice_value=4))
        filename2 = 'state2.pickle'
        save_controller2 = SaveController(match, ConsoleViewFactory())
        with patch.object(MatchView, 'read_filename', return_value=filename2):
            save_controller2()

        with (
            save_controller.filepath.open(mode='rb') as file1,
            save_controller2.filepath.open(mode='rb') as file2,
        ):
            text1 = file1.read()
            text2 = file2.read()
        self.assertNotEqual(text1, text2)

    def test_save_match_with_name_given_by_player(self) -> None:
        match = Match()
        filename = 'save.pickle'
        save_controller = SaveController(match, ConsoleViewFactory())
        with patch.object(MatchView, 'read_filename', return_value=filename) as mock:
            save_controller()

        self.assertEqual(mock.call_count, 1)
        self.assertEqual(filename, save_controller.filename)
