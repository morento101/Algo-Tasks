""" Test of task_331a.py """

from unittest import TestCase
from unittest import main

from task.task_331a import task_331a


class TestTask331a(TestCase):
    """Test for function test_331a"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_331a(21), [(1, 2, 4)])
        self.assertEqual(task_331a(67), [(3, 3, 7)])

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_331a(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_331a(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_empty_results(self):
        """Test with empty results"""
        self.assertEqual(task_331a(1), None)


if __name__ == "__main__":
    main()
