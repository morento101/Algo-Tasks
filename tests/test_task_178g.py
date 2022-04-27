"""Module with tests for task 178g."""

from tasks.task_178g import task_178g
from unittest import TestCase


class Task178gTests(TestCase):
    """Tests for task 178g"""

    def test_task_178g_positive(self):
        """Test with positive numbers"""
        sequence = (23, 4, 6, 11, 6, 93, 56, 43, 12, 88, 55, 3, 100)
        actual = task_178g(len(sequence), sequence)
        self.assertEqual("task 178(g): 6", actual)

    def test_task_178g_zero(self):
        """Test with one zero in sequence"""
        sequence = (0,)
        actual = task_178g(len(sequence), sequence)
        self.assertEqual("task 178(g): 0", actual)

    def test_task_178g_empty(self):
        """Test with empty sequence"""
        sequence = ()
        actual = task_178g(len(sequence), sequence)
        self.assertEqual("task 178(g): 0", actual)

    def test_task_178g_index_error(self):
        """Test with too big index"""
        sequence = (2, 9, 17, 100, 46, 90, 55, 40, 98, 1)
        with self.assertRaises(IndexError):
            task_178g(100, sequence)
