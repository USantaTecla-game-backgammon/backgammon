from __future__ import annotations
from typing import TYPE_CHECKING

from src.models import Move
from src.models.command import Command
from src.types import GameState

if TYPE_CHECKING:
    # pylint: disable=cyclic-import
    from src.controllers import PlayController


class MovePieceCommand(Command):
    title = 'Move from point {} to {} (dice {})'

    def __init__(self, play_controller: PlayController, move: Move) -> None:
        self.play_controller = play_controller
        self.move = move
        self.title = self.title.format(move.position_from, move.position_to, move.dice_value)

    def __call__(self) -> None:
        self.play_controller.move_piece(self.move)

    def is_active(self) -> bool:
        game = self.play_controller.match.last_game
        return game.state == GameState.MOVING_PIECE
