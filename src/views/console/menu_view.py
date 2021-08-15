from typing import Final

from src.models.command import Command
from src.views import MenuView as MenuViewBase
from src.views.console import console


class MenuView(MenuViewBase):
    START_OPTION: Final[int] = 1

    def interact(self, commands: list[Command]) -> int:
        self._show(commands)
        return self._read(commands)

    def _show(self, commands: list[Command]) -> None:
        menu = ''
        for number, command in enumerate(commands, start=self.START_OPTION):
            menu += f'{number}) {command.title}\n'

        console.show(menu)

    def _read(self, commands: list[Command]) -> int:
        valids = list(range(self.START_OPTION, self.START_OPTION + len(commands)))
        option = console.read_int_range(valids=valids, msg=self.SELECT_CHOICE)
        return option - self.START_OPTION
