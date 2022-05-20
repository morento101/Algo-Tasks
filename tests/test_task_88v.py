"""Test of task_88v.py."""

from unittest import TestCase
from unittest import main

from tasks.task_88v import task_88v


class TestTask88v(TestCase):
    """Test for function test_88v"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_88v(371239), 971233)

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_88v(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_zero(self):
        """Test with zero as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_88v(0)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_88v(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])


if __name__ == "__main__":
    main()
