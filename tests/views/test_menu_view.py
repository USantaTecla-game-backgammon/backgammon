import unittest
from unittest.mock import call, patch

from src.models import Command, Menu
from src.views import console
from src.views.menu_view import MenuView, MenuWithoutOption
from src.types import Color


class FakeCommand(Command):
    title = 'fake command'

    def __call__(self) -> None:
        pass

    def is_active(self) -> bool:
        return True


class MenuViewTest(unittest.TestCase):

    def setUp(self) -> None:
        self.menu = Menu('', [])
        self.menu_view = MenuView()
        self.command = FakeCommand()

    def test_call_no_active_commands(self) -> None:
        with self.assertRaises(MenuWithoutOption):
            self.menu_view(self.menu, Color.BLACK)

    def test_call_with_one_active_command(self) -> None:
        with (
            patch.object(Menu, 'active_commands', return_value=[self.command]),
            patch.object(console, 'show') as mock_show,
            patch.object(console, 'read_int_range') as mock_read,
        ):
            self.menu_view(self.menu, Color.BLACK)
            mock_show.assert_has_calls([
                call(MenuView.TURN_TEXT.format(Color.BLACK)),
                call(f'1) {self.command.title}\n'),
                call(MenuView.OPTION_SELECTED.format(1)),
            ])
            self.assertEqual(mock_read.call_count, 0)

    def test_call_with_two_active_command(self) -> None:
        with (
            patch.object(Menu, 'active_commands', return_value=[self.command, self.command]),
            patch.object(console, 'show') as mock_show,
            patch.object(console, 'read_int_range', return_value=1) as mock_read,
        ):
            self.menu_view(self.menu, Color.BLACK)
            mock_show.assert_has_calls([
                call(MenuView.TURN_TEXT.format(Color.BLACK)),
                call(f'1) {self.command.title}\n2) {self.command.title}\n'),
                call(MenuView.OPTION_SELECTED.format(1)),
            ])
            mock_read.assert_called_once_with(valids=[1, 2], msg=MenuView.SELECT_CHOICE)
