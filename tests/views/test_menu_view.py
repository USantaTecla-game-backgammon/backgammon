import unittest
from unittest.mock import patch

from src.models import Command, Menu
from src.views.console import console
from src.views.console.menu_view import MenuView


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

    def test_call_with_one_active_command(self) -> None:
        with (
            patch.object(Menu, 'active_commands', return_value=[self.command]),
            patch.object(console, 'show') as mock_show,
            patch.object(console, 'read_int_range') as mock_read,
        ):
            self.menu_view.interact(self.menu.active_commands())
            mock_show.assert_called_once_with(f'1) {self.command.title}\n')
            mock_read.assert_called_once_with(valids=[1], msg=MenuView.SELECT_CHOICE)

    def test_call_with_two_active_command(self) -> None:
        with (
            patch.object(Menu, 'active_commands', return_value=[self.command, self.command]),
            patch.object(console, 'show') as mock_show,
            patch.object(console, 'read_int_range', return_value=1) as mock_read,
        ):
            self.menu_view.interact(self.menu.active_commands())
            mock_show.assert_called_once_with(
                f'1) {self.command.title}\n2) {self.command.title}\n'
            )
            mock_read.assert_called_once_with(valids=[1, 2], msg=MenuView.SELECT_CHOICE)
