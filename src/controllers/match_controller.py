from src.models import Dice, Game, Match, Turn
from src.views import MatchView
from src.types import Color


class MatchController:
    def __init__(self, match: Match, view: MatchView) -> None:
        self.match = match
        self.view = view

    def configure(self) -> None:
        self.view.show_title()
        self.match.goal = self.view.read_goal()

    def first_roll(self) -> None:
        dices: dict[Color, Dice] = self.match.first_roll()
        self.view.show_dices(dices)

        if dices[Color.BLACK] > dices[Color.RED]:
            self.match.change_turn(Color.BLACK)
        elif dices[Color.BLACK] < dices[Color.RED]:
            self.match.change_turn(Color.RED)
        else:
            self.first_roll()

    def initialize_game(self) -> None:
        assert self.match.goal > 0
        turn = Turn(players=self.match.turn.players)
        turn.current_player = self.match.turn.current_player
        self.match.games.append(Game(turn))

    def is_goal(self) -> bool:
        return self.match.is_goal()

    def resume(self) -> bool:
        return self.view.read_resume()
