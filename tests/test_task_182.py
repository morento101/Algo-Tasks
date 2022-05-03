"""Module with tests for task 182"""

from unittest import TestCase

from tasks.task_182 import task_182


class TestTask182(TestCase):
    """ Tests for task 182 """
    
    def test_assert_equal(self):
        """ Test with positive numbers in sequence """
        test_n = 5
        test_list = [6, 35, 40, 97, 21]
        self.assertEqual(task_182(test_n, test_list), (1, 40))

    def test_assert_raises(self):
        """ Test with string in sequence """
        self.assertRaises(AssertionError, task_182, "3", "[2, 3, 4]")

    def test_with_negative_arr(self):
        """ Test with negative numbers in sequence """
        test_n = 1
        test_list = [-6]
        self.assertEqual(task_182(test_n, test_list), (0, 0))

    def test_with_zero(self):
        """ Test with zero """
        test_n = 0
        test_list = []
        self.assertRaises(AssertionError, task_182, test_n, test_list)
