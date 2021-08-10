from src.controllers import PlayController, ResumeController, StartController
from src.models import Match
from src.views.view_factory import ViewFactory


class Backgammon:
    def __init__(self, view_factory: ViewFactory) -> None:
        self.match = Match()
        self.view_factory = view_factory

        self.start_controller = StartController(self.match, self.view_factory)
        self.play_controller = PlayController(self.match, self.view_factory)
        self.resume_controller = ResumeController(self.match, self.view_factory)

    def play(self) -> None:
        while True:
            self.start_controller()
            self.play_controller()
            if not self.resume_controller():
                break
