from typing import Optional

from src.models.dice import Dice
from src.models.doubling_cube import doubling_cube
from src.models.player import Player
from src.types.color import Color


class Turn:
    def __init__(self) -> None:
        self.players = [Player(Color.BLACK), Player(Color.RED)]
        self._current_color: Color = Color.BLACK
        self._current_player: Player = self.players[0]
        self._opponent_player: Player = self.players[1]

    @property
    def current_color(self) -> Color:
        return self._current_color

    @current_color.setter
    def current_color(self, color: Color) -> None:
        assert color in [Color.BLACK, Color.RED]
        if color != self._current_color:
            self._current_color = color
            self._current_player, self._opponent_player = (
                self._opponent_player, self._current_player
            )

    @property
    def opponent_color(self) -> Color:
        return Color.BLACK if self._current_color == Color.RED else Color.RED

    @property
    def opponent_player(self) -> Player:
        return self._opponent_player

    @property
    def current_player(self) -> Player:
        return self._current_player

    def change(self, color: Optional[Color] = None) -> None:
        assert color in [Color.BLACK, Color.RED, None]
        if color is None:
            color = self.opponent_color
        self.current_color = color

    def can_bet_current_player(self) -> bool:
        return self.opponent_player.doubling_cube is None

    def accept_bet(self) -> None:
        doubling_cube.double()
        self.current_player.doubling_cube = doubling_cube
        self.opponent_player.doubling_cube = None
        self.change()

    def reject_bet(self) -> None:
        self.opponent_player.is_winner = True

    def give_score_to_winner(self, score: int) -> None:
        if self.current_player.is_winner:
            self.current_player.earn_score(score)

        if self.opponent_player.is_winner:
            self.opponent_player.earn_score(score)

    def give_score(self, score: int, color: Color) -> None:
        print("color >", self.current_color, color)
        if self.current_color == color:
            self.current_player.earn_score(score)
        else:
            self.opponent_player.earn_score(score)

    def winner_by_color(self, color: Color) -> None:
        assert color in [Color.BLACK, Color.RED]
        if self.current_player.color == color:
            self.current_player.is_winner = True
        else:
            self.opponent_player.is_winner = True

    def roll_current_player(self) -> list[Dice]:
        return self.current_player.roll()
