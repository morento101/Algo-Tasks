""" Test of task_554.py """

from unittest import TestCase
from unittest import main

from tasks.task_554 import task_554


class TestTask554(TestCase):
    """Test for function task_554"""

    def test_task554_valid(self):
        """Test that task_554 function returns correct result."""
        entry_sequence = 10
        expected_answer = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
        answer = task_554(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task554_valid_zero(self):
        """Test when one of args is zero result is an empty list."""
        entry_sequence = 0
        expected_answer = []
        answer = task_554(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task554_valid_negative(self):
        """Test when one of args is zero result is an empty list."""
        entry_sequence = -8
        expected_answer = []
        answer = task_554(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task554_valid_str(self):
        """Test when one of args is incorrect data type an 
        AssertionError exception is called.
        """
        entry_sequence = ""
        with self.assertRaises(AssertionError):
            task_554(entry_sequence)

    def test_task554_valid_str(self):
        """Test when one of args is incorrect data type an 
        AssertionError exception is called.
        """
        entry_sequence = []
        with self.assertRaises(AssertionError):
            task_554(entry_sequence)


if __name__ == '__main__':
    main()
