from abc import abstractmethod

from src.models import Menu
from src.types import Color


class MenuView:
    @abstractmethod
    def __call__(self, menu: Menu, color: Color) -> None:
        raise NotImplementedError
