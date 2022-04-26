"""This module is for testing task 88b."""

import unittest

from tasks.task_88b import reverse_number


class Task88bTests(unittest.TestCase):
    """This class is for testing function is_3_in_sqiare_of_number."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(reverse_number(327123), 321723)


    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            reverse_number("!22")
        with self.assertRaises(AssertionError):
            reverse_number([])


    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            reverse_number(0)
        with self.assertRaises(AssertionError):
            reverse_number(-23)


    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(reverse_number(327123), 321123)


if __name__ == '__main__':
    unittest.main()
