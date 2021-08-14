from src.controllers import PlayController, ResumeController, StartController
from src.models import Match
from src.views.view_factory import ViewFactory
from src.views.console.console_view_factory import ConsoleViewFactory
from src.views.gui.gui_view_factory import GUIViewFactory


class Backgammon:
    VIEW_FACTORIES: dict[str, ViewFactory] = {
        'console': ConsoleViewFactory(),
        'gui': GUIViewFactory(),
    }

    def __init__(self, settings: str) -> None:
        self.match = Match()
        self.view_factory = self.create_factory(settings)

        self.start_controller = StartController(self.match, self.view_factory)
        self.play_controller = PlayController(self.match, self.view_factory)
        self.resume_controller = ResumeController(self.match, self.view_factory)

    def create_factory(self, settings: str) -> ViewFactory:
        return self.VIEW_FACTORIES.get(settings, ConsoleViewFactory())

    def play(self) -> None:
        while True:
            self.start_controller()
            self.play_controller()
            if not self.resume_controller():
                break
