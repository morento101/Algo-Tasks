"""Module with tests for task 555."""

from tasks.task_555 import task_555
from unittest import TestCase


class Task555Tests(TestCase):
    """Tests for task 555"""
    
    def test_task_555_valid_3(self):
        """Test with argument 3"""
        expected = [
            [1], 
            [1, 1], 
            [1, 2, 1]
        ]
        actual = task_555(3)
        self.assertEqual(expected, actual)

    def test_task_555_valid_5(self):
        """Test with argument 5"""
        expected = [
            [1], 
            [1, 1], 
            [1, 2, 1], 
            [1, 3, 3, 1], 
            [1, 4, 6, 4, 1]
        ]
        actual = task_555(5)
        self.assertEqual(expected, actual)

    def test_task_555_valid_8(self):
        """Test with argument 8"""
        expected = [
            [1], 
            [1, 1], 
            [1, 2, 1], 
            [1, 3, 3, 1], 
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1]
        ]
        actual = task_555(8)
        self.assertEqual(expected, actual)

    def test_task_555_valid_zero(self):
        """Test for argument 0"""
        actual = task_555(0)
        self.assertEqual([], actual)

    def test_pascal_negative(self):
        """Test for negative argument"""
        actual = task_555(-1)
        self.assertEqual([], actual)
