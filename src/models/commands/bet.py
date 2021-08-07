from src.controllers.bet_controller import BetController
from src.models.command import Command
from src.types import GameState


class BetCommand(Command):
    title = 'bet'

    def __init__(self, bet_controller: BetController) -> None:
        self.bet_controller = bet_controller
        self.game = self.bet_controller.game

    def __call__(self) -> None:
        self.bet_controller.ask()
        self.bet_controller.answer()

    def is_active(self) -> bool:
        return self.game.state == GameState.IN_GAME
