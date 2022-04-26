"""This module is for testing task 88a."""

from unittest import TestCase
from unittest import main

from tasks.task_88a import task_88a


class TestTask88a(TestCase):
    """This class is for testing function task_88a."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(task_88a(3211237), True)

    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            task_88a("!22")
        with self.assertRaises(AssertionError):
            task_88a([])

    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            task_88a(0)
        with self.assertRaises(AssertionError):
            task_88a(-23)

    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(task_88a(3211237), False)


if __name__ == '__main__':
    main()
