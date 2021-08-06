import unittest

from src.models import Game


class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_initial_game_have_board(self) -> None:
        self.assertIsNotNone(self.game.board)


if __name__ == '__main__':
    unittest.main()
