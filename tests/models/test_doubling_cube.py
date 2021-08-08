import unittest
from src.models.doubling_cube import DoublingCube


class DoublingCubeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.doubling_cube = DoublingCube()

    def test_first_value(self) -> None:
        self.assertEqual(self.doubling_cube.value, 64)

    def test_double(self) -> None:
        self.doubling_cube.double()
        self.assertEqual(self.doubling_cube.value, 2)

    def test_when_double_7_times_rise_exception(self) -> None:
        for _ in range(6):
            self.doubling_cube.double()

        with self.assertRaises(AssertionError):
            self.doubling_cube.double()
