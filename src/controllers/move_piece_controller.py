from src.controllers.controller import Controller


class IllegalMove(Exception):
    pass


class MovePieceController(Controller):

    def _check_rules(self, spaces: int) -> None:
        pass
        #color = self.game.current_player.color
        # print(color, amount, position)
        # TODO: check rules: chain of responsability

    def __call__(self, spaces: int) -> None:
        self.game = self.match.last_game
        valids = self._check_rules(spaces)
        position = self.view_factory.create_board_view().read_position(valids)

        self.game.move_piece(spaces, position)
        if self.game.is_captured_piece():
            self.game.move_piece_captured()
