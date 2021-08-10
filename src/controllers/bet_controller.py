from src.controllers.controller import Controller
from src.types.game_state import GameState


class BetController(Controller):

    def __call__(self) -> None:
        self.game = self.match.last_game
        self.ask()
        self.answer()

    def ask(self) -> None:
        self.view_factory.create_bet_view().show_ask()
        self.game.change_turn()
        self.game.state = GameState.BETTING

    def answer(self) -> None:
        accept = self.view_factory.create_bet_view().read_answer()
        if accept:
            self.game.turn.accept_bet()
            self.game.state = GameState.IN_GAME
        else:
            self.view.show_reject()
            self.game.turn.reject_bet()
            self.game.state = GameState.END_GAME

        self.view_factory.create_bet_view().show_answer(accept)
