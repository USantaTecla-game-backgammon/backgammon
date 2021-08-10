import unittest
from unittest.mock import MagicMock, patch

from src.controllers import PlayController
from src.models import Game, Match, Turn
from src.views import GameView
from src.views.menu_view import MenuView
from src.types import Endgame


class GameControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()
        turn = Turn(self.match.turn.players)
        self.game = Game(turn)
        self.match.games.append(self.game)
        self.play_controller = PlayController(self.match, GameView())

    @patch.object(Game, 'is_endgame', side_effect=[False, True])
    @patch.object(MenuView, '__call__')
    @patch.object(Game, 'type_endgame', return_value=Endgame.SIMPLE)
    def test_game_controller_play_when_not_is_endgame(
        self,
        mock_endgame: MagicMock,
        mock_view: MagicMock,
        mock_game: MagicMock,
    ) -> None:
        self.play_controller.play()
        self.assertEqual(mock_game.call_count, 2)
        self.assertEqual(mock_view.call_count, 1)
        self.assertEqual(mock_endgame.call_count, 1)
