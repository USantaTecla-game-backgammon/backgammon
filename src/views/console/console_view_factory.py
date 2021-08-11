from src.views import (
    BetView as BetViewBase,
    BoardView as BoardViewBase,
    MenuView as MenuViewBase,
    GameView as GameViewBase,
    MatchView as MatchViewBase,
)
from src.views.console import (
    BetView,
    BoardView,
    MenuView,
    GameView,
    MatchView,
)
from src.views.view_factory import ViewFactory


class ConsoleViewFactory(ViewFactory):
    @staticmethod
    def create_match_view() -> MatchViewBase:
        return MatchView()

    @staticmethod
    def create_game_view() -> GameViewBase:
        return GameView()

    @staticmethod
    def create_board_view() -> BoardViewBase:
        return BoardView()

    @staticmethod
    def create_menu_view() -> MenuViewBase:
        return MenuView()

    @staticmethod
    def create_bet_view() -> BetViewBase:
        return BetView()
