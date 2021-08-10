from typing import Optional

from src.models import Dice, Match
from src.views.view_factory import ViewFactory
from src.types import Color
from src.controllers.controller import Controller


class StartController(Controller):
    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        super().__init__(match, view_factory)
        self._first_roll: list[Dice] = []

    def __call__(self) -> None:
        self.view_factory.create_start_view().show()
        self.configure_goal()
        self.first_roll()

    def configure_goal(self) -> None:
        self.match.goal = self.view_factory.create_configure_goal_view().read()

    def first_roll(self) -> None:
        dices: dict[Color, Dice] = {}
        winner_color: Optional[Color] = None

        while not winner_color:
            dices = self.match.first_roll()

            if dices[Color.BLACK] > dices[Color.RED]:
                winner_color = Color.BLACK
            elif dices[Color.BLACK] < dices[Color.RED]:
                winner_color = Color.RED

            self.view_factory.create_first_roll_view().show(dices)

        self.match.change_turn(winner_color)
        self.match.first_roll = list(dices.values())
        self.view_factory.create_first_roll_view().show_winner(winner_color)
