""" Test of task_108.py """

from unittest import TestCase
from unittest import main

from task.task_108 import task_108


class TestTask108(TestCase):
    """Test for function test_108"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_108(9), 16)
        self.assertEqual(task_108(2), 4)

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_108(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_108(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])


if __name__ == "__main__":
    main()
