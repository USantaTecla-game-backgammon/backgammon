from src.models import Match
from src.views.view_factory import ViewFactory


class Controller:
    def __init__(self, match: Match, view_factory: ViewFactory):
        self.match = match
        self.view_factory = view_factory

    def __call__(self) -> None:
        raise NotImplementedError
