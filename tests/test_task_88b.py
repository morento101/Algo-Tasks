"""This module is for testing task 88b."""

from unittest import TestCase
from unittest import main

from tasks.task_88b import task_88b


class TestTask88b(TestCase):
    """This class is for testing function task_88b."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(task_88b(327123), 321723)

    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            task_88b("!22")
        with self.assertRaises(AssertionError):
            task_88b([])

    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            task_88b(0)
        with self.assertRaises(AssertionError):
            task_88b(-23)

    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(task_88b(327123), 321123)


if __name__ == '__main__':
    main()
