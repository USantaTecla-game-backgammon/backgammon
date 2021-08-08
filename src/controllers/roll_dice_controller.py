from src.models.game import Game
from src.views.game_view import GameView


class RollDiceController:

    def __init__(self, game: Game, view: GameView) -> None:
        self.view = view.dice_view
        self.game = game

    def roll(self) -> None:
        raise NotImplementedError
