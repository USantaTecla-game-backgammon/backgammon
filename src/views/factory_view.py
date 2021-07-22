from src.views.bet_view import BetView
from src.views.board_view import BoardView
from src.views.configuration_view import ConfigurationView
from src.views.dice_view import DiceView
from src.views.endgame_view import EndgameView
from src.views.menu_view import MenuView


class FactoryView:

    @classmethod
    def create_bet_view(cls) -> BetView:
        return BetView()

    @classmethod
    def create_board_view(cls) -> BoardView:
        return BoardView()

    @classmethod
    def create_configuration_view(cls) -> ConfigurationView:
        return ConfigurationView()

    @classmethod
    def create_dice_view(cls) -> DiceView:
        return DiceView()

    @classmethod
    def create_endgame_view(cls) -> EndgameView:
        return EndgameView()

    @classmethod
    def create_menu_view(cls) -> MenuView:
        return MenuView()
