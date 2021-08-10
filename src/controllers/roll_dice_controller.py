from src.controllers.controller import Controller
from src.models import Game


class RollDiceController(Controller):

    def __call__(self) -> None:
        self.match.last_game.roll_current_player()

    def last_game(self) -> Game:
        return self.match.last_game
