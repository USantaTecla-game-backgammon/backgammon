from __future__ import annotations
from typing import TYPE_CHECKING

from src.models.command import Command

if TYPE_CHECKING:
    # pylint: disable=cyclic-import
    from src.controllers import PlayController  # pragma: no cover


class SaveCommand(Command):
    def __init__(self, play_controller: PlayController) -> None:
        self.play_controller = play_controller

    def __call__(self) -> None:
        pass

    def is_active(self) -> bool:
        return True
