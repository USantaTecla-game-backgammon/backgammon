from src.models.game import Game
from src.views.factory_view import FactoryView


class Controller:
    def __init__(self, game: Game, factory_view: FactoryView):
        self.game = game
        self.factory_view = factory_view
