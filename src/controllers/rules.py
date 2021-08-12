from __future__ import annotations
from typing import Optional

from src.models.game import Game
from src.models.move import Move
from src.types import Position


class Rule:

    def __init__(self, next_rule: Optional[Rule] = None) -> None:
        self.next_rule = next_rule

    def restrict(self, game: Game, moves: list[Move]) -> list[Move]:
        if self.can_restrict(moves):
            moves = self._restrict(game, moves)

        if moves and self.next_rule is not None:
            return self.next_rule.restrict(game, moves)

        return moves

    def _restrict(self, game: Game, moves: list[Move]) -> list[Move]:
        raise NotImplementedError

    @classmethod
    def can_restrict(cls, moves: list[Move]) -> bool:
        return bool(moves)


class RuleNoPiece(Rule):
    def _restrict(self, game: Game, moves: list[Move]) -> list[Move]:
        for move in moves[:]:
            if not game.get_my_pieces(move.position_from):
                moves.remove(move)
        return moves


class RuleBarMoveFirst(Rule):
    def _restrict(self, game: Game, moves: list[Move]) -> list[Move]:
        for move in moves[:]:
            if move.position_from != Position.BAR:
                moves.remove(move)
        return moves

    @classmethod
    def can_restrict(cls, moves: list[Move]) -> bool:
        return any([move.position_from == Position.BAR for move in moves])


class RulePointOccupied(Rule):
    def _restrict(self, game: Game, moves: list[Move]) -> list[Move]:
        for move in moves[:]:
            if game.get_opponent_pieces(move.position_to) >= 2:
                moves.remove(move)
        return moves


class RuleOffBoardWhenPieceInFirstSquare(Rule):
    def _restrict(self, game: Game, moves: list[Move]) -> list[Move]:
        for move in moves[:]:
            if (
                move.position_to == Position.OFF_BOARD and
                not game.board.is_all_pieces_first_square(game.current_player.color)
            ):
                moves.remove(move)
        return moves

    @classmethod
    def can_restrict(cls, moves: list[Move]) -> bool:
        return any([move.position_to == Position.OFF_BOARD for move in moves])


chain_move_rules = RuleNoPiece(
    RuleBarMoveFirst(
        RulePointOccupied(
            RuleOffBoardWhenPieceInFirstSquare()
        )
    )
)
