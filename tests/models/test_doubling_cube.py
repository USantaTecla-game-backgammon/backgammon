import unittest

from src.models.doubling_cube import DoublingCube


class DoublingCubeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.doubling_cube = DoublingCube()

    def test_first_value(self) -> None:
        self.assertEqual(self.doubling_cube.value, 1)

    def test_double(self) -> None:
        self.doubling_cube.double()
        self.assertEqual(self.doubling_cube.value, 2)

    def test_when_double_6_times(self) -> None:
        for _ in range(6):
            self.doubling_cube.double()

        self.assertEqual(self.doubling_cube.value, 64)

    def test_reset(self) -> None:
        self.doubling_cube.double()
        self.assertTrue(self.doubling_cube.value > 1)
        self.doubling_cube.reset()
        self.assertEqual(self.doubling_cube.value, 1)
