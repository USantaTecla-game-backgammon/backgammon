from src.models.game import Game
from src.views.view_factory import ViewFactory


class IllegalMove(Exception):
    pass


class MovePieceController:

    def __init__(self, game: Game, view_factory: ViewFactory) -> None:
        self.view = view_factory.create_board_view()
        self.game = game

    def _check_rules(self, amount: int, position: int) -> None:
        color = self.game.current_player.color
        print(color, amount, position)
        # TODO: check rules

    def move(self, amount: int) -> None:
        position = self.view.read_position()
        self._check_rules(amount, position)
        self.game.move_piece(amount, position)
