from src.controllers.controller import Controller


class RollDiceController(Controller):

    def __call__(self) -> None:
        self.match.last_game.roll_current_player()
