""" Test of task_107.py """

from unittest import TestCase
from unittest import main

from tasks.task_107 import task_107


class TestTask107(TestCase):
    """Test for function test_107"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_107(32), 2)
        self.assertEqual(task_107(64), 2)

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_107(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_107(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])


if __name__ == "__main__":
    main()
