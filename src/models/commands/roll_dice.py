from src.controllers.roll_dice_controller import RollDiceController
from src.models.command import Command
from src.types import GameState


class RollDiceCommand(Command):
    title = 'roll'

    def __init__(self, roll_dice_controller: RollDiceController) -> None:
        self.roll_dice_controller = roll_dice_controller
        self.game = self.roll_dice_controller.game

    def __call__(self) -> None:
        self.roll_dice_controller.roll()

    def is_active(self) -> bool:
        return self.game.state in [GameState.CHOOSING_PLAYER, GameState.IN_GAME]
