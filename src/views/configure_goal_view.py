from abc import abstractmethod
from typing import Final


class ConfigureGoalView:
    DEFINE_GOAL: Final[str] = 'Define your goal? (1-64)'
    GOAL_RANGE: list[int] = list(range(1, 65))

    @abstractmethod
    def show(self, title: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def read(self) -> int:
        raise NotImplementedError

