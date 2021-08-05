from src.models import Match
from src.views import GameView


class GameController:

    def __init__(self, match: Match, view: GameView) -> None:
        self.match = match
        self.view = view

    def play(self) -> None:
        pass
