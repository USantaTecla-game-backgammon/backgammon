import unittest
import random
import string
from unittest.mock import patch

from src.models.match import Match
from src.models.move import Move
from src.controllers.save_controller import SaveController
from src.types.position import Position
from src.views.console.match_view import MatchView
from src.views.console.console_view_factory import ConsoleViewFactory


def random_filename(size=10, endfile='.pickle'):
    res = ''.join(random.choice(string.ascii_letters) for x in range(size))
    return f'test_{res}{endfile}'


class SaveControllerTest(unittest.TestCase):
    def setUp(self):
        match = Match()
        self.save_controller = SaveController(match, ConsoleViewFactory())

    def tearDown(self):
        self.save_controller.filepath.unlink()


    def test_save_complete_match(self) -> None:
        filename = random_filename()
        with patch.object(MatchView, 'read_filename', return_value=filename):
            self.save_controller()
        self.assertTrue(self.save_controller.filepath.is_file())

    def test_save_with_different_state_are_different(self) -> None:
        filename = random_filename(endfile='1.pickle')
        with patch.object(MatchView, 'read_filename', return_value=filename):
            self.save_controller()

        match = Match()
        match.last_game.possible_moves = [4]
        match.last_game.move_piece(Move(position_from=Position.TWENTY_FOUR, dice_value=4))
        filename2 = random_filename(endfile='2.pickle')
        save_controller2 = SaveController(match, ConsoleViewFactory())
        with patch.object(MatchView, 'read_filename', return_value=filename2):
            save_controller2()

        with (
            self.save_controller.filepath.open(mode='rb') as file1,
            save_controller2.filepath.open(mode='rb') as file2,
        ):
            text1 = file1.read()
            text2 = file2.read()
        self.assertNotEqual(text1, text2)
        save_controller2.filepath.unlink()

    def test_save_match_with_name_given_by_player(self) -> None:
        filename = random_filename()
        with patch.object(MatchView, 'read_filename', return_value=filename) as mock:
            self.save_controller()

        self.assertEqual(mock.call_count, 1)
        self.assertEqual(filename, self.save_controller.filename)
