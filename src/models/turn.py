from typing import Optional

from src.models.player import Player
from src.types.color import Color
from src.models.doubling_cube import doubling_cube


class Turn:
    def __init__(self, players: tuple[Player, Player]):
        assert len(players) == 2
        self.players = players
        self.current_player: Player = players[0]

    @property
    def opponent_player(self) -> Player:
        return self.players[0] if self.current_player == self.players[1] else self.players[1]

    def change(self, color: Optional[Color] = None) -> None:
        if color is not None:
            for player in self.players:
                if player.color == color:
                    self.current_player = player
        elif self.current_player == self.players[0]:
            self.current_player = self.players[1]
        elif self.current_player == self.players[1]:
            self.current_player = self.players[0]
        else:
            raise AssertionError

    def accept_bet(self) -> None:
        doubling_cube.double()
        self.current_player.doubling_cube = doubling_cube
        self.opponent_player.doubling_cube = None

    def reject_bet(self) -> None:
        self.opponent_player.is_winner = True

    def give_score_to_winner(self, score: int) -> None:
        if self.current_player.is_winner:
            self.current_player.earn_score(score)

        if self.opponent_player.is_winner:
            self.opponent_player.earn_score(score)

    def winner_by_color(self, color: Color) -> None:
        if self.current_player.color == color:
            self.current_player.is_winner = True
        else:
            self.opponent_player.is_winner = True
