"""This module is for testing task 86b."""

import unittest

from tasks.task_86b import task_86b


class TestTask86b(unittest.TestCase):
    """This class is for testing function task_86b."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(task_86b(928322), 26)

    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            task_86b("!22")
        with self.assertRaises(AssertionError):
            task_86b([])

    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            task_86b(0)
        with self.assertRaises(AssertionError):
            task_86b(-23)

    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(task_86b(928), 6)


if __name__ == '__main__':
    unittest.main()
