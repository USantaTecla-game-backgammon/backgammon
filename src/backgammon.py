from src.controllers import MatchController, GameController
from src.models import Match
from src.views.view_factory import ViewFactory


class Backgammon:
    def __init__(self, view_factory: ViewFactory) -> None:
        self.match = Match()
        self.view_factory = view_factory

        self.match_controller = MatchController(self.match, self.view_factory)
        self.game_controller = GameController(self.match, self.view_factory)

    def play(self) -> None:
        self.match_controller.configure()
        self.match_controller.first_roll()
        while not self.match_controller.is_goal():
            self.match_controller.initialize_game()
            self.game_controller.play()

        if self.match_controller.resume():
            self.match.reset()
            self.play()
