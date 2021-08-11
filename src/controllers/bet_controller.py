from src.types.game_state import GameState
from src.controllers.controller import Controller


class BetController(Controller):

    def __call__(self) -> None:
        self.ask()
        self.answer()

    def ask(self) -> None:
        game = self.match.last_game
        game.turn.change()
        game.state = GameState.BETTING

    def answer(self) -> None:
        game = self.match.last_game
        accept = self.view_factory.create_bet_view().read()
        if accept:
            self.view_factory.create_bet_view().show_accept()
            game.turn.accept_bet()
            game.state = GameState.IN_GAME
        else:
            self.view_factory.create_bet_view().show_reject()
            game.turn.reject_bet()
            game.state = GameState.END_GAME
