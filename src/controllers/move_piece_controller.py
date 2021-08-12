from src.controllers.controller import Controller
from src.models import Move


class MovePieceController(Controller):

    # It violates the Liskov Substitution Principle
    def __call__(self, move: Move) -> None:  # type: ignore
        game = self.match.last_game
        game.move_piece(move)
        game.try_eat_piece(move.position_to)
