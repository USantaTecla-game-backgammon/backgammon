from abc import abstractmethod

from src.views import (
    BetView,
    BoardView,
    MenuView,
    MatchView,
    GameView,
)


class ViewFactory:
    @staticmethod
    @abstractmethod
    def create_match_view() -> MatchView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_game_view() -> GameView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_board_view() -> BoardView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_menu_view() -> MenuView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_bet_view() -> BetView:
        raise NotImplementedError
