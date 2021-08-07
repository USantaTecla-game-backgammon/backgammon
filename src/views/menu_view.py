from typing import Final

from src.models.command import Command
from src.models.menu import Menu
from src.views import console


class MenuWithoutOption(Exception):
    pass


class MenuView:
    SELECT_CHOICE: Final = 'Select your choice'
    START_OPTION: Final = 1

    def __call__(self, menu: Menu) -> None:
        active_commands = menu.active_commands()

        if len(active_commands) == 0:
            raise MenuWithoutOption()

        self._show_menu(active_commands)
        option = self._select_option(active_commands)
        active_commands[option - self.START_OPTION]()

    def _show_menu(self, commands: list[Command]) -> None:
        menu = ''
        for number, command in enumerate(commands, start=self.START_OPTION):
            menu += f'{number}) {command.title}\n'

        console.show(menu)

    def _select_option(self, commands: list[Command]) -> int:
        if len(commands) == 1:
            return self.START_OPTION

        return console.read_int(self.SELECT_CHOICE)
