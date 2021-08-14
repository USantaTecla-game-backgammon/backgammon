from abc import abstractmethod
from typing import Final


from src.models import Command


class MenuView:
    SELECT_CHOICE: Final[str] = 'Select your choice'
    OPTION_SELECTED: Final[str] = 'Selected option {}'

    @abstractmethod
    def interact(self, commands: list[Command]) -> int:
        raise NotImplementedError
