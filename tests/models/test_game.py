import unittest

from src.models.game import Game


class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_initial_game_have_two_player(self) -> None:
        self.assertIsNotNone(self.game.red_player)
        self.assertIsNotNone(self.game.black_player)

    def test_initial_game_have_turn_none(self) -> None:
        self.assertIsNone(self.game.turn)


if __name__ == '__main__':
    unittest.main()
