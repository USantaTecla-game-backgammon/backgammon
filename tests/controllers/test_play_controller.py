import unittest
from unittest.mock import call, patch

from src.controllers import PlayController
from src.models import Board, Game, Match, Menu, Move
from src.models.doubling_cube import doubling_cube
from src.views.console import GameView
from src.views.console.console_view_factory import ConsoleViewFactory
from src.types import Color, Endgame, Position


# INITIAL STATE OF BOARD
#
# |--------------------------------------------------------|
# |  13  14  15  16  17  18 |    |  19  20  21  22  23  24 |
# |  5●              3○     |    |  5○                  2● |
# |                         |  0○|                         |
# |                         | BAR|                         |
# |                         |  0●|                         |
# |  5○              3●     |    |  5●                  2○ |
# |  12  11  10   9   8   7 |    |   6   5   4   3   2   1 |
# |--------------------------------------------------------|


class PlayControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.match = Match()
        self.play_controller = PlayController(self.match, ConsoleViewFactory())

    def test_play_when_not_is_endgame_create_menu(self) -> None:
        self.match.goal = 1
        with (
            patch.object(Match, 'is_goal', side_effect=[False, True]),
            patch.object(GameView, 'show_start') as mock_show,
            patch.object(Game, 'is_endgame', side_effect=[False, True]) as mock_game,
            patch.object(Menu, 'active_commands', return_value=[]) as mock_menu,
            patch.object(Game, 'get_type_endgame', return_value=Endgame.SIMPLE) as mock_endgame,
            patch.object(GameView, 'show_score') as mock_show_score,
        ):
            self.play_controller()
            mock_show.assert_called_once()
            self.assertEqual(mock_game.call_count, 2)
            mock_menu.assert_called_once()
            mock_endgame.assert_called_once()
            mock_show_score.assert_called_once()

    def test_end_game_save_score_in_match(self) -> None:
        self.match.goal = 1
        with (
            patch.object(Match, 'is_goal', side_effect=[False, True]),
            patch.object(GameView, 'show_start') as mock_show,
            patch.object(Game, 'is_endgame', return_value=True) as mock_game,
            patch.object(Game, 'get_type_endgame', return_value=Endgame.GAMMON) as mock_endgame,
            patch.object(GameView, 'show_score') as mock_show_score,
        ):
            self.play_controller()
            mock_show.assert_called_once()
            mock_game.assert_called_once()
            mock_endgame.assert_called_once()
            mock_show_score.assert_called_once()
            score = doubling_cube.value * Endgame.GAMMON
            self.assertEqual(self.match.last_game.turn.current_player.score, 0)
            self.assertEqual(self.match.last_game.turn.opponent_player.score, score)
            self.assertEqual(self.match.turn.current_player.score, 0)
            self.assertEqual(self.match.turn.opponent_player.score, score)

    def test_initialize_game_without_goal_defined(self) -> None:
        with self.assertRaises(AssertionError):
            self.play_controller()

    def test_initialize_game(self) -> None:
        self.match.goal = 1
        self.assertEqual(len(self.match.games), 0)

        self.match.goal = 2
        self.play_controller.add_game()

        self.assertEqual(len(self.match.games), 1)

    def test_move_eat_piece(self) -> None:
        self.match.add_game()
        game = self.match.last_game
        game.board.positions[1] = [Color.RED]
        game.possible_moves = [5]

        move = Move(position_from=Position(6), dice_value=5)

        with patch.object(Board, 'move_piece') as mock_move:
            self.play_controller.move_piece(move)
            mock_move.assert_has_calls([
                call(
                    sense=game.turn.current_color,
                    move=move,
                    color=game.turn.current_color
                ),
                call(
                    sense=game.turn.current_color,
                    move=Move(position_from=move.position_to, position_to=Position.OFF_BOARD),
                    color=game.turn.opponent_color
                ),
            ])


class PlayControllerAvailableMoveTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()
        self.match = Match()
        self.match.games = [self.game]
        self.play_controller = PlayController(self.match, ConsoleViewFactory())

    def test_move_normal_valid_black(self) -> None:
        self.game.possible_moves = [1]

        self.assertEqual(self.game.get_pieces(Position(24)), [Color.BLACK, Color.BLACK])
        self.assertEqual(self.game.get_pieces(Position(23)), [])

        move = Move(position_from=Position(24), dice_value=1)
        self.play_controller.move_piece(move)

        self.assertEqual(self.game.get_pieces(Position(24)), [Color.BLACK])
        self.assertEqual(self.game.get_pieces(Position(23)), [Color.BLACK])
        self.assertFalse(self.game.possible_moves)

    def test_move_normal_valid_red(self) -> None:
        self.game.change_turn()
        self.game.possible_moves = [2]
        self.assertEqual(self.game.get_pieces(Position(24)), [Color.RED, Color.RED])
        self.assertEqual(self.game.get_pieces(Position(22)), [])

        move = Move(position_from=Position(24), dice_value=2)
        self.play_controller.move_piece(move)

        self.assertEqual(self.game.get_pieces(Position(24)), [Color.RED])
        self.assertEqual(self.game.get_pieces(Position(22)), [Color.RED])
        self.assertFalse(self.game.possible_moves)

    def test_move_from_bar(self) -> None:
        self.game.board.positions[Position.BAR] = [Color.BLACK]
        self.game.possible_moves = [2]

        move = Move(position_from=Position.BAR, dice_value=2)
        self.play_controller.move_piece(move)

        self.assertEqual(self.game.get_pieces(Position.BAR), [])
        self.assertEqual(self.game.get_pieces(Position(23)), [Color.BLACK])
        self.assertFalse(self.game.possible_moves)

    def test_move_invalid_by_opponent_pieces(self) -> None:
        self.game.possible_moves = [5]
        move = Move(position_from=Position(24), dice_value=5)
        available_moves = self.play_controller.calculate_available_moves()
        self.assertFalse(move in available_moves)

    def test_move_invalid_by_piece_in_bar(self) -> None:
        self.game.board.positions[Position.BAR] = [Color.BLACK]
        self.game.possible_moves = [5]
        move = Move(position_from=Position(24), dice_value=5)
        available_moves = self.play_controller.calculate_available_moves()
        self.assertFalse(move in available_moves)

    def test_move_invalid_by_unexist_piece(self) -> None:
        self.game.possible_moves = [1]
        move = Move(position_from=Position(23), dice_value=1)
        available_moves = self.play_controller.calculate_available_moves()
        self.assertFalse(move in available_moves)

    def test_move_invalid_by_any_piece_not_in_first_square(self) -> None:
        self.game.possible_moves = [6]
        move = Move(position_from=Position(6), dice_value=6)
        available_moves = self.play_controller.calculate_available_moves()
        self.assertFalse(move in available_moves)
