from abc import abstractmethod
from typing import Final


class FirstRollView:
    FIRST_ROLL: Final[str] = '\nFirst roll: choosing first player ...'
    FIRST_PLAYER: Final[str] = 'First player is {}'

    @abstractmethod
    def show(self, dices: dict[str, int]) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_winner(self, color: str) -> None:
        raise NotImplementedError
