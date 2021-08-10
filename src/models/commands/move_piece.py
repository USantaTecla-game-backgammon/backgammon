from src.controllers import PlayController
from src.models.command import Command
from src.types import CommandState, GameState


class MovePieceCommand(Command):
    title = 'move {} spaces'

    def __init__(self, play_controller: PlayController, move: int) -> None:
        self.play_controller = play_controller
        self.move = move
        self.title = self.title.format(move)

    def __call__(self) -> None:
        self.move_piece_controller(self.move)

    def state(self) -> CommandState:
        game = self.play_controller.last_game()
        if self.game.state == GameState.MOVING_PIECE:
            return CommandState.ACTIVE

        return CommandState.INACTIVE
