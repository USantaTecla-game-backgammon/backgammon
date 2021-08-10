from src.controllers.bet_controller import BetController
from src.models.command import Command
from src.types import CommandState, GameState


class BetCommand(Command):
    title = 'bet'

    def __init__(self, bet_controller: BetController) -> None:
        self.bet_controller = bet_controller

    def __call__(self) -> None:
        self.bet_controller()

    def state(self) -> CommandState:
        game = self.bet_controller.last_game()
        if (
            game.state in [GameState.IN_GAME, GameState.BETTING] and
            game.turn.can_bet_current_player()
        ):
            return CommandState.ACTIVE

        return CommandState.INACTIVE
