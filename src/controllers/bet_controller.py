from src.models.game import Game
from src.views.view_factory import ViewFactory
from src.types.game_state import GameState


class BetController:

    def __init__(self, game: Game, view_factory: ViewFactory) -> None:
        self.view = view_factory.create_bet_view()
        self.game = game

    def ask(self) -> None:
        self.game.turn.change()
        self.game.state = GameState.BETTING

    def answer(self) -> None:
        accept = self.view.read()
        if accept:
            self.view.show_accept()
            self.game.turn.accept_bet()
            self.game.state = GameState.IN_GAME
        else:
            self.view.show_reject()
            self.game.turn.reject_bet()
            self.game.state = GameState.END_GAME
