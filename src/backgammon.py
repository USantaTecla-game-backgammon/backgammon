from src.controllers.configure_controller import ConfigureController
from src.controllers.play_controller import PlayController
from src.controllers.resume_controller import ResumeController
from src.models.game import Game
from src.views.factory_view import FactoryView


class Backgammon:
    def __init__(self) -> None:
        self.game = Game()
        self.factory_view = FactoryView()

        self.configure_controller = ConfigureController(self.game, self.factory_view)
        self.play_controller = PlayController(self.game, self.factory_view)
        self.resume_controller = ResumeController(self.game, self.factory_view)

    def play(self) -> None:
        while 1:
            self.configure_controller.configure()
            self.play_controller.play()
            if not self.resume_controller.resume():
                break
