from typing import Optional

from src.models.game import Game
from src.models.dice import Dice
from src.models.turn import Turn
from src.models.player import Player
from src.types.color import Color


class Match:
    def __init__(self) -> None:
        self.games: list[Game] = []
        self.goal: int = 0
        self.turn: Turn = Turn(players=(Player(Color.BLACK), Player(Color.RED)))

    @property
    def current_player(self) -> Player:
        return self.turn.current_player

    def change_turn(self, color: Optional[Color] = None) -> None:
        self.turn.change(color)

    def is_goal(self) -> bool:
        return any([player.score >= self.goal for player in self.turn.players])

    @property
    def last_game(self) -> Game:
        return self.games[-1]

    def first_roll(self) -> dict[Color, Dice]:
        return {player.color: player.roll(1)[0] for player in self.turn.players}

    def is_first_game(self) -> bool:
        return not bool(self.games)

    def reset(self) -> None:
        self.games = []
        self.goal = 0
        self.turn = Turn(players=(Player(Color.BLACK), Player(Color.RED)))
