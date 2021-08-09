from src.controllers import MatchController, GameController
from src.models import Match
from src.views import GameView, MatchView


class Backgammon:
    def __init__(self) -> None:
        self.match = Match()

        self.match_view = MatchView()
        self.game_view = GameView()

        self.match_controller = MatchController(self.match, self.match_view)
        self.game_controller = GameController(self.match, self.game_view)

    def play(self) -> None:
        self.match_controller.configure()
        self.match_controller.first_roll()
        while not self.match_controller.is_goal():
            self.match_controller.initialize_game()
            self.game_controller.play()

        if self.match_controller.resume():
            self.match.reset()
            self.play()
