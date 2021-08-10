from abc import abstractmethod
from typing import Final


class StartView:
    TITLE: Final[str] = '### BACKGAMMON ###'
    MSG_CHOOSE_COLOR: Final[str] = 'Each player should choose a color.'

    @abstractmethod
    def show(self) -> None:
        raise NotImplementedError
