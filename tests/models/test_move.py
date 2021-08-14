import unittest
from src.models.move import Move
from src.types.position import Position


class MoveTestCase(unittest.TestCase):

    def test_position_from_with_dice_value(self) -> None:
        move = Move(position_from=Position.BAR, dice_value=4)
        self.assertEqual(move.position_to, Position(21))

    def test_position_from_with_dice_value_overflow(self) -> None:
        move = Move(position_from=Position(1), dice_value=6)
        self.assertEqual(move.position_to, Position.OFF_BOARD)

    def test_position_equals(self) -> None:
        move1 = Move(position_from=Position(1), dice_value=6)
        move2 = Move(position_from=Position(2), dice_value=6)
        self.assertNotEqual(move1, move2)
