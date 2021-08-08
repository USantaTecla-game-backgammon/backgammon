from src.models.game import Game
from src.views.game_view import GameView


class BetController:

    def __init__(self, game: Game, view: GameView) -> None:
        self.view = view.bet_view
        self.game = game

    def ask(self) -> None:
        raise NotImplementedError

    def answer(self) -> None:
        raise NotImplementedError
