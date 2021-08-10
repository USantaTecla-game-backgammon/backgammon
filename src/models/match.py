from typing import Optional

from src.models.dice import Dice
from src.models.game import Game
from src.models.turn import Turn
from src.models.player import Player
from src.types.color import Color
from src.types.game_state import GameState


class Match:
    def __init__(self) -> None:
        self.games: list[Game] = []
        self.goal: int = 0
        self.turn: Turn = Turn()
        self._first_roll: list[Dice] = []

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
        return {color: Dice() for color in [Color.BLACK, Color.RED]}

    def is_first_game(self) -> bool:
        return not bool(self.games)

    def reset(self) -> None:
        self.games = []
        self.goal = 0
        self.turn = Turn()

    def create_game(self) -> None:
        game = Game()
        if self.is_first_game():
            game.state = GameState.MOVING_PIECE
            game.last_roll = self._first_roll
        else:
            self.change_turn()

        game.change_turn(self.turn.current_color)  # TAKE CARE: select color instead player
        self.games.append(game)
