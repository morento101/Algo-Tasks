""" Test of task_243b.py """

from unittest import TestCase
from unittest import main

from tasks.task_243b import task_243b


class TestTask243a(TestCase):
    """Test for function test_243b"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_243b(13), [(3, 2)])
        self.assertEqual(task_243b(17), [(4, 1)])
        self.assertEqual(task_243b(29), [(5, 2)])

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_243b(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_243b(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])


if __name__ == "__main__":
    main()
