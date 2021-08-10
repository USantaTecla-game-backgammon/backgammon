from abc import abstractmethod

from src.views import (
    BetView,
    BoardView,
    ConfigureGoalView,
    FirstRollView,
    MenuView,
    PlayView,
    ResumeView,
    StartView,
)


class ViewFactory:
    @staticmethod
    @abstractmethod
    def create_start_view() -> StartView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_play_view() -> PlayView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_resume_view() -> ResumeView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_configure_goal_view() -> ConfigureGoalView:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def create_first_roll_view() -> FirstRollView:
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
