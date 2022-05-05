"""Module with tests for task 178d."""

from tasks.task_178d import task_178d
from unittest import TestCase


class Task178dTests(TestCase):
    """Tests for task 178d"""

    def test_task_178d_positive(self):
        """Test with positive numbers in sequence"""
        sequence = (23, 4, 6, 11, 6, 93, 56, 43, 12, 88, 55, 3, 100)
        actual = task_178d(*sequence)
        self.assertEqual(1, actual)

    def test_task_178d_zeros(self):
        """Test with zeros in sequence"""
        sequence = (23, 4, 6, 0, 6, 93, 56, 43, 12, 88, 55, 3, 0)
        actual = task_178d(*sequence)
        self.assertEqual(1, actual)

    def test_task_178d_empty(self):
        """Test with empty sequence"""
        sequence = ()
        print(task_178d(*sequence))

    def test_task_178d_negative(self):
        """Test with negative numbers"""
        sequence = (-2, -9, -17, 100, -46, -90, -55, -40, -98, 1)
        actual = task_178d(*sequence)
        self.assertNotEqual(2, actual)
