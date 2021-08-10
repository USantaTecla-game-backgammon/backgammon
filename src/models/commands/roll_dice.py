from src.controllers.roll_dice_controller import RollDiceController
from src.models.command import Command
from src.types import CommandState, GameState


class RollDiceCommand(Command):
    title = 'roll'

    def __init__(self, roll_dice_controller: RollDiceController) -> None:
        self.roll_dice_controller = roll_dice_controller

    def __call__(self) -> None:
        self.roll_dice_controller()

    def state(self) -> CommandState:
        game = self.roll_dice_controller.last_game()
        if game.state == GameState.IN_GAME:
            return CommandState.ACTIVE
        return CommandState.INACTIVE
