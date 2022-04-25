"""Module with tests for task 178d"""
from tasks.task_178d import task_178d
from unittest import TestCase


class Task178dTests(TestCase):
    """
    Tests for task 178d
    """
    def test_task_178d_positive(self):
        """
        Test with positive numbers in sequence
        """
        sequence = (23, 4, 6, 11, 6, 93, 56, 43, 12, 88, 55, 3, 100)
        actual = task_178d(len(sequence), sequence)
        self.assertEqual("task 178(d): 1", actual)

    def test_task_178d_zeros(self):
        """
        Test with zeros in sequence
        """
        sequence = (23, 4, 6, 0, 6, 93, 56, 43, 12, 88, 55, 3, 0)
        actual = task_178d(len(sequence), sequence)
        self.assertEqual("task 178(d): 1", actual)

    def test_task_178d_empty(self):
        """
        Test with empty sequence
        """
        sequence = ()
        actual = task_178d(len(sequence), sequence)
        self.assertEqual("task 178(d): 0", actual)

    def test_task_178d_negative(self):
        """
        Test with negative numbers
        """
        sequence = (-2, -9, -17, 100, -46, -90, -55, -40, -98, 1)
        actual = task_178d(len(sequence), sequence)
        self.assertNotEqual("task 178(d): 2", actual)

    def test_task_178d_index_error(self):
        """
        Test with too big first argument
        """
        sequence = (2, 9, 17, 100, 46, 90, 55, 40, 98, 1)
        with self.assertRaises(IndexError):
            task_178d(100, sequence)
