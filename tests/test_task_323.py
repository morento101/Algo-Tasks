"""Module with tests for task 323"""

from unittest import TestCase

from tasks.tasks_323 import task_323

class TestTask323(TestCase):
    """Tests for task 323"""
    def test_assert_equal(self):
        """ Test with positive number """
        test_n = 6
        test_res = ['5 & 4', '5 & 3', '5 & 2', '5 & 1', '4 & 3', '4 & 1', '3 & 2', '3 & 1', '2 & 1', '1 & 1']
        self.assertEqual(task_323(test_n), test_res)

    def test_assert_raises(self):
        """ Test with string """
        test_n = "9"
        self.assertRaises(AssertionError, task_323, test_n)

    def test_negative(self):
        """Test with negative numbers
        in sequence
        """
        test_n = -1
        self.assertRaises(AssertionError, task_323, test_n)

