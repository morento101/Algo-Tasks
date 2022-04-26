""" Test of task_243a.py """

from unittest import TestCase
from unittest import main

from tasks.task_243a import task_243a


class TestTask243a(TestCase):
    """Test for function test_107"""
    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_243a(13), {2: 3})
        self.assertEqual(task_243a(89), {5: 8})

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_243a(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_243a(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_empty_results(self):
        """Test with empty results"""
        self.assertEqual(task_243a(45), {})
        self.assertEqual(task_243a(23), {})


if __name__ == "__main__":
    main()
