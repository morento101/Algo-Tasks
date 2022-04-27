"""This module is for testing task 330."""

import unittest

from tasks.task_330 import task_330


class TestTask330(unittest.TestCase):
    """This class is for testing function task_86b."""
    
    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(task_330(9000), [6, 28, 496, 8128])

    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            task_330("!22")
        with self.assertRaises(AssertionError):
            task_330([])

    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            task_330(0)
        with self.assertRaises(AssertionError):
            task_330(-23)

    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(task_330(9000), [6, 28, 496, 8128, 33550336])


if __name__ == '__main__':
    unittest.main()
