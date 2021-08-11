from __future__ import annotations
from typing import TYPE_CHECKING

from src.models.command import Command
from src.types import GameState

if TYPE_CHECKING:
    # pylint: disable=cyclic-import
    from src.controllers import PlayController


class BetCommand(Command):
    title = 'bet'

    def __init__(self, play_controller: PlayController) -> None:
        self.play_controller = play_controller

    def __call__(self) -> None:
        self.play_controller.bet()

    def is_active(self) -> bool:
        game = self.play_controller.match.last_game
        return (
            game.state in [GameState.IN_GAME, GameState.BETTING] and
            game.turn.can_bet_current_player()
        )
