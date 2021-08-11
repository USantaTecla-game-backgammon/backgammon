from src.controllers.controller import Controller


class IllegalMove(Exception):
    pass


class MovePieceController(Controller):

    # It violates the Liskov Substitution Principle
    def __call__(self, spaces: int) -> None:  # type: ignore
        game = self.match.last_game
        position = self.view_factory.create_board_view().read_position()
        # TODO: check rules with chain of responsability pattern
        game.move_piece(spaces, position)
