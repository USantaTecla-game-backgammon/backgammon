from src.models.game import Game
from src.views.view_factory import ViewFactory


class RollDiceController:

    def __init__(self, game: Game, view_factory: ViewFactory) -> None:
        self.view_factory = view_factory
        self.game = game

    def roll(self) -> None:
        self.game.roll_current_player()
