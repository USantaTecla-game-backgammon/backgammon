from typing import Optional

from src.factories.game import game_factory
from src.models.doubling_cube import doubling_cube
from src.models.game import Game
from src.models.dice import Dice
from src.models.turn import Turn
from src.models.player import Player
from src.types.color import Color


class Match:
    colors: list[Color] = [Color.BLACK, Color.RED]

    def __init__(self) -> None:
        self.games: list[Game] = []
        self.goal: int = 0
        self.turn: Turn = Turn()
        self.first_roll: list[Dice] = []

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

    def throw_first_dices(self) -> dict[Color, Dice]:
        return {color: Dice() for color in self.colors}

    def is_first_game(self) -> bool:
        return not bool(self.games)

    def reset(self) -> None:
        self.games = []
        self.goal = 0
        self.turn = Turn()

    def current_score(self) -> int:
        if self.turn.rejected_bet():
            score = doubling_cube.value
        else:
            score = self.last_game.get_type_endgame().value * doubling_cube.value

        return score

    def give_score(self) -> None:
        score = self.current_score()
        if self.last_game.board.is_all_pieces_off_board(Color.BLACK):
            self.turn.give_score(score, Color.BLACK)
            self.last_game.turn.give_score(score, Color.BLACK)

        if self.last_game.board.is_all_pieces_off_board(Color.RED):
            self.turn.give_score(score, Color.RED)
            self.last_game.turn.give_score(score, Color.RED)

    def add_game(self) -> None:
        self.games.append(game_factory(self.turn.current_color, self.first_roll))
        self.first_roll = []

    def roll_dice(self) -> list[dict[Color, Dice]]:
        dices: dict[Color, Dice] = {}
        winner_color: Optional[Color] = None
        list_dices: list[dict[Color, Dice]] = []

        while not winner_color:
            dices = self.throw_first_dices()

            if dices[Color.BLACK] > dices[Color.RED]:
                winner_color = Color.BLACK
            elif dices[Color.BLACK] < dices[Color.RED]:
                winner_color = Color.RED

            list_dices.append(dices)

        self.change_turn(winner_color)
        self.first_roll = list(dices.values())
        return list_dices
