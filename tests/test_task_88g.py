"""Test of task_88g.py."""

from unittest import TestCase
from unittest import main

from tasks.task_88g import task_88g


class TestTask88g(TestCase):
    """Test for function test_88g"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_88g(371239), 13712391)

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_88g(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_88g(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])


if __name__ == "__main__":
    main()
