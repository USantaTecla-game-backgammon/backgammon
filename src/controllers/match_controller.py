from src.models import Dice, Game, Match, Turn
from src.views import MatchView
from src.types import Color, GameState


class MatchController:
    def __init__(self, match: Match, view: MatchView) -> None:
        self.match = match
        self.view = view
        self._first_roll: list[Dice] = []

    def configure(self) -> None:
        self.view.show_title()
        self.match.goal = self.view.read_goal()

    def first_roll(self) -> None:
        dices: dict[Color, Dice] = self.match.first_roll()
        self.view.show_dices(dices)

        if dices[Color.BLACK] > dices[Color.RED]:
            self.match.change_turn(Color.BLACK)
            self.view.show_first_player(Color.BLACK)
            self._first_roll = list(dices.values())
        elif dices[Color.BLACK] < dices[Color.RED]:
            self.match.change_turn(Color.RED)
            self.view.show_first_player(Color.RED)
            self._first_roll = list(dices.values())
        else:
            self.first_roll()

    def initialize_game(self) -> None:
        assert self.match.goal > 0

        turn = Turn(players=self.match.turn.players)
        game = Game(turn)

        if self.match.is_first_game():
            game.state = GameState.MOVING_PIECE
            game.last_roll = self._first_roll
        else:
            self.match.change_turn()

        turn.current_player = self.match.turn.current_player
        self.match.games.append(game)

    def is_goal(self) -> bool:
        return self.match.is_goal()

    def resume(self) -> bool:
        return self.view.read_resume()
