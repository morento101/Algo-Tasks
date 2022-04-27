"""This module is for testing task 86a."""

import unittest

from tasks.task_86a import task_86a


class TestTask86a(unittest.TestCase):
    """This class is for testing function task_86a."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(task_86a(928322), 6)

    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            task_86a("!22")
        with self.assertRaises(AssertionError):
            task_86a([])

    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            task_86a(0)
        with self.assertRaises(AssertionError):
            task_86a(-23)

    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(task_86a(928), 6)


if __name__ == '__main__':
    unittest.main()
