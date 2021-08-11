from src.views import (
    BetView as BetViewBase,
    BoardView as BoardViewBase,
    MenuView as MenuViewBase,
    GameView as GameViewBase,
    MatchView as MatchViewBase,
)
from src.views.view_factory import ViewFactory


class GUIViewFactory(ViewFactory):
    @staticmethod
    def create_match_view() -> MatchViewBase:
        raise NotImplementedError

    @staticmethod
    def create_game_view() -> GameViewBase:
        raise NotImplementedError

    @staticmethod
    def create_board_view() -> BoardViewBase:
        raise NotImplementedError

    @staticmethod
    def create_menu_view() -> MenuViewBase:
        raise NotImplementedError

    @staticmethod
    def create_bet_view() -> BetViewBase:
        raise NotImplementedError
