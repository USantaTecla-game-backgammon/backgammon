from src.models import Game, Match
from src.views import MatchView


class MatchController:
    def __init__(self, match: Match, view: MatchView) -> None:
        self.match = match
        self.view = view

    def configure(self) -> None:
        self.view.show()
        self.match.goal = self.view.read_goal()

    def initialize_game(self) -> None:
        assert self.match.goal > 0
        self.match.games.append(Game())

    def is_goal(self) -> bool:
        return self.match.is_goal()

    def resume(self) -> bool:
        return self.view.read_resume()
