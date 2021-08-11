from typing import Final

from src.models.command import Command
from src.models.menu import Menu
from src.types import Color
from src.views import MenuView as MenuViewBase
from src.views.console import console


class MenuWithoutOption(Exception):
    pass


class MenuView(MenuViewBase):
    TURN_TEXT: Final = '\nPlayer {} turn:\n'
    SELECT_CHOICE: Final = 'Select your choice'
    START_OPTION: Final = 1
    OPTION_SELECTED: Final = 'Selected option {}'

    def __call__(self, menu: Menu, color: Color) -> None:
        active_commands = menu.active_commands()

        if len(active_commands) == 0:
            raise MenuWithoutOption()

        self._show_menu(active_commands, color)
        option = self._select_option(active_commands)
        console.show(self.OPTION_SELECTED.format(option))
        active_commands[option - self.START_OPTION]()

    def _show_menu(self, commands: list[Command], color: Color) -> None:
        console.show(self.TURN_TEXT.format(color))
        menu = ''
        for number, command in enumerate(commands, start=self.START_OPTION):
            menu += f'{number}) {command.title}\n'

        console.show(menu)

    def _select_option(self, commands: list[Command]) -> int:
        if len(commands) == 1:
            return self.START_OPTION

        valids = list(range(self.START_OPTION, self.START_OPTION + len(commands)))
        return console.read_int_range(valids=valids, msg=self.SELECT_CHOICE)
