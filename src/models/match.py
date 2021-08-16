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

    def give_score(self) -> None:
        score = self.last_game.get_type_endgame().value * doubling_cube.value
        # print(score)
        if self.last_game.board.is_all_pieces_off_board(Color.BLACK):
            self.turn.give_score(score, Color.BLACK)

        if self.last_game.board.is_all_pieces_off_board(Color.RED):
            self.turn.give_score(score, Color.RED)
        # print("current > ", self.turn.current_player.score)
        # print("opponent > ", self.turn.opponent_player.score)
        # self.turn.give_score_to_winner(score)

        # for player in self.last_game.turn.players:
        #     if player.color == self.turn.current_player:
        #         self.turn.current_player.earn_score(score)
        #     else:
        #         self.turn.opponent_player.earn_score(score)

    def add_game(self) -> None:
        self.games.append(game_factory(self.turn.current_color, self.first_roll))
        self.first_roll = []
