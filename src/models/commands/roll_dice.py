from src.controllers import PlayController
from src.models.command import Command
from src.types import CommandState, GameState


class RollDiceCommand(Command):
    title = 'roll'

    def __init__(self, play_controller: PlayController) -> None:
        self.play_controller = play_controller

    def __call__(self) -> None:
        self.roll_dice_controller()

    def state(self) -> CommandState:
        game = self.play_controller.last_game()
        if game.state == GameState.IN_GAME:
            return CommandState.ACTIVE
        return CommandState.INACTIVE
