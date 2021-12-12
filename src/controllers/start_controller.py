from src.controllers.controller import Controller
from src.controllers.roll_dice_controller import RollDiceController
from src.models import Match
from src.views.view_factory import ViewFactory


class StartController(Controller):

    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        super().__init__(match, view_factory)
        self.view = view_factory.create_match_view()
        self.roll_dice_controller = RollDiceController(match, view_factory)

    def __call__(self) -> None:
        self.configure_goal()
        self.roll_dice_controller()

    def configure_goal(self) -> None:
        self.view.show_title()
        self.match.goal = self.view.read_goal()
