from typing import Optional

from src.controllers.controller import Controller
from src.models import Dice, Match
from src.views.view_factory import ViewFactory
from src.types import Color


class RollDiceController(Controller):

    def __init__(self, match: Match, view_factory: ViewFactory) -> None:
        super().__init__(match, view_factory)
        self.view = view_factory.create_match_view()

    def __call__(self) -> None:
        list_dices = self.roll_dice()
        self.show_dices(list_dices)

    def roll_dice(self) -> list[dict[Color, Dice]]:
        dices: dict[Color, Dice] = {}
        winner_color: Optional[Color] = None
        list_dices: list[dict[Color, Dice]] = []

        while not winner_color:
            dices = self.match.throw_first_dices()

            if dices[Color.BLACK] > dices[Color.RED]:
                winner_color = Color.BLACK
            elif dices[Color.BLACK] < dices[Color.RED]:
                winner_color = Color.RED

            list_dices.append(dices)

        self.match.change_turn(winner_color)
        self.match.first_roll = list(dices.values())
        return list_dices

    def show_dices(self, list_dices):
        for dices in list_dices:
            self.view.show_dices(dices)
