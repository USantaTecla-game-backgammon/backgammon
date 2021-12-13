from src.controllers.controller import Controller
from src.models import Match
from src.views.view_factory import ViewFactory


class RollDiceController(Controller):

    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        super().__init__(match, view_factory)
        self.view = view_factory.create_match_view()

    def __call__(self) -> None:
        self.match.roll_dice()
        game_serialized = self.match.serialize_last_game()
        self.view.show_dices(game_serialized)
