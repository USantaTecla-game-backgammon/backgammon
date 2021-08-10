from src.views import MenuView as MenuViewBase
from src.views.console import console


class MenuWithoutOption(Exception):
    pass


class MenuView(MenuViewBase):

    @classmethod
    def show(cls, commands: list[str]) -> None:
        console.show(f'TODO {commands}')
        #console.show(cls.TURN_TEXT.format(color))
        #menu = ''
        #for number, command in enumerate(commands, start=1):
        #    if command.is_locked:
        #        tachar
        #    else:
        #        menu += f'{number}) {command.title}\n'

        #console.show(menu)

    @classmethod
    def read(cls, commands: list[str]) -> int:
        valids = list(range(1, len(commands) + 1))
        return console.read_int_range(valids=valids, msg=cls.SELECT_CHOICE)
