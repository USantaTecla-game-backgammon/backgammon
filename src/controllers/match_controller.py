from src.models import Match
from src.views import MatchView


class MatchController:
    def __init__(self, match: Match, view: MatchView) -> None:
        self.match = match
        self.view = view

    def configure(self) -> None:
        pass

    def initialize_game(self) -> None:
        pass

    def is_goal(self) -> bool:
        return self.match.is_goal()

    def resume(self) -> bool:
        raise NotImplementedError
