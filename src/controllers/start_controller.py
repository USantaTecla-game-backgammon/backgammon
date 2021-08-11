from typing import Optional

from src.controllers.controller import Controller
from src.models import Dice, Match
from src.views.view_factory import ViewFactory
from src.types import Color


class StartController(Controller):

    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        super().__init__(match, view_factory)
        self.view = view_factory.create_match_view()

    def __call__(self) -> None:
        self.configure()
        self.first_roll()

    def configure(self) -> None:
        self.view.show_title()
        self.match.goal = self.view.read_goal()

    def first_roll(self) -> None:
        dices: dict[Color, Dice] = {}
        winner_color: Optional[Color] = None

        while not winner_color:
            dices = self.match.throw_first_dices()

            if dices[Color.BLACK] > dices[Color.RED]:
                winner_color = Color.BLACK
            elif dices[Color.BLACK] < dices[Color.RED]:
                winner_color = Color.RED

            self.view.show_dices(dices)

        self.match.change_turn(winner_color)
        self.match.first_roll = list(dices.values())
