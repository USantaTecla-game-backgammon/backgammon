import random
import string
import unittest
from unittest.mock import patch

from src.views.console import console


class ConsoleTestSuite(unittest.TestCase):

    @classmethod
    def gen_random_text(cls, length: int = 10) -> str:
        return ''.join(random.choices(string.printable, k=length))

    def test_show(self) -> None:
        random_text = self.gen_random_text(20)
        with patch('builtins.print') as mock:
            console.show(random_text)
            mock.assert_called_once_with(random_text)

    def test_read_str(self) -> None:
        empty_text = ''
        random_text = self.gen_random_text(5)

        with patch('builtins.input') as mock:
            mock.side_effect = [empty_text, random_text]
            result = console.read_str()
            self.assertEqual(result, random_text)
            self.assertEqual(mock.call_count, 2)

    def test_read_int(self) -> None:
        bad_input = 'bad'
        good_input = '42'

        with (
            patch('builtins.input') as mock,
            patch.object(console, 'show') as mock_show
        ):
            mock.side_effect = [bad_input, good_input]
            result = console.read_int()
            self.assertEqual(result, 42)
            self.assertEqual(mock.call_count, 2)
            mock_show.assert_called_once_with(console.ONLY_NUMBERS_ARE_ALLOWED)

    def test_read_int_range(self) -> None:
        valids = [1, 2]
        bad_input = '4'
        good_input = '2'

        with (
            patch('builtins.input') as mock_input,
            patch('builtins.print') as mock_print
        ):

            mock_input.side_effect = [bad_input, good_input]
            result = console.read_int_range(valids=valids)
            self.assertEqual(result, 2)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_called_once_with(console.ALLOWED_VALUES, valids)
