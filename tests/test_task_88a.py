"""This module is for testing task 88a."""

import unittest

from tasks.task_88a import is_3_in_square_of_number


class Task88aTests(unittest.TestCase):
    """This class is for testing function is_3_in_square_of_number."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(is_3_in_square_of_number(3211237), True)


    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            is_3_in_square_of_number("!22")
        with self.assertRaises(AssertionError):
            is_3_in_square_of_number([])


    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            is_3_in_square_of_number(0)
        with self.assertRaises(AssertionError):
            is_3_in_square_of_number(-23)


    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(is_3_in_square_of_number(3211237), False)


if __name__ == '__main__':
    unittest.main()
