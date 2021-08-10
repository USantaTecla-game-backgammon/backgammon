from typing import Final


class MenuView:
    TURN_TEXT: Final = '\nPlayer {} turn:\n'
    SELECT_CHOICE: Final = 'Select your choice'
    OPTION_SELECTED: Final = 'Selected option {}'

    @classmethod
    def show(cls, commands: list[str]):
        raise NotImplementedError

    @classmethod
    def read(cls, commands: list[str]) -> int:
        raise NotImplementedError
