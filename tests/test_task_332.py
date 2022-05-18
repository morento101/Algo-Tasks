"""Test of task_332.py."""

from unittest import TestCase
from unittest import main

from tasks.task_332 import task_332


class TestTask332(TestCase):
    """Test for function test_322"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertCountEqual(task_332(31), (5, 1, 2, 1))

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_332(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_332(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])


if __name__ == "__main__":
    main()
