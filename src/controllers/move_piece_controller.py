from src.models.game import Game
from src.views.game_view import GameView


class IllegalMove(Exception):
    pass


class MovePieceController:

    def __init__(self, game: Game, view: GameView) -> None:
        self.view = view.move_piece_view
        self.game = game

    def _check_rules(self, amount: int, position: int) -> None:
        color = self.game.current_player.color
        print(color, amount, position)
        # TODO: check rules

    def move(self, amount: int) -> None:
        position = self.view.read_position()
        self._check_rules(amount, position)
        self.game.move_piece(amount, position)
