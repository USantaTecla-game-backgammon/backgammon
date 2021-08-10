from src.views.console import (
    BetView,
    BoardView,
    ConfigureGoalView,
    FirstRollView,
    MenuView,
    PlayView,
    ResumeView,
    StartView,
)
from src.views.view_factory import ViewFactory


class ConsoleViewFactory(ViewFactory):
    @staticmethod
    def create_start_view() -> StartView:
        return StartView()

    @staticmethod
    def create_play_view() -> PlayView:
        return PlayView()

    @staticmethod
    def create_resume_view() -> ResumeView:
        return ResumeView()

    @staticmethod
    def create_configure_goal_view() -> ConfigureGoalView:
        return ConfigureGoalView()

    @staticmethod
    def create_first_roll_view() -> FirstRollView:
        return FirstRollView()

    @staticmethod
    def create_board_view() -> BoardView:
        return BoardView()

    @staticmethod
    def create_menu_view() -> MenuView:
        return MenuView()

    @staticmethod
    def create_bet_view() -> BetView:
        return BetView()
