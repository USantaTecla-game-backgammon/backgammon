from src.models.game import Game
from src.views.game_view import GameView


class MovePieceController:

    def __init__(self, game: Game, view: GameView) -> None:
        self.view = view.move_piece_view
        self.game = game

    def move(self) -> None:
        raise NotImplementedError
