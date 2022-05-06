""" Test of task_178b.py """

from unittest import TestCase
from unittest import main

from tasks.task_178b import task_178b


class TestTask178b(TestCase):
    """Test for function test_178b"""

    def test_task178b_valid(self):
        """Test that task_178 function returns correct result."""
        entry_sequence = (711, 3, 5, 1, 15, 10, 8, 9, 0)
        expected_answer = 3
        answer = task_178b(*entry_sequence)
        self.assertEqual(expected_answer, answer)
 
    def test_task178b_valid_empty(self):
        """Test when one of args is zero result is zero."""
        entry_sequence = []
        expected_answer = 0
        with self.assertRaises(AssertionError):
            task_178b(entry_sequence)

    def test_task178b_valid_str(self):
        """Test when one of args is incorrect data type an 
        AssertionError exception is called.
        """
        entry_sequence = "(1, 2, 3, 4, 5, 6)"
        with self.assertRaises(AssertionError):
            task_178b(entry_sequence)

if __name__ == "__main__":
    main()
