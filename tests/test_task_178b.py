""" Test of task_178b.py """

from unittest import TestCase
from unittest import main

from tasks.task_178b import task_178b


class TestTask178b(TestCase):
    """Test for function test_107"""
    def test_task178b_valid(self):
        entry_sequence = (711, 3, 5, 1, 15, 10, 8, 9, 0)
        expected_answer = 3
        answer = task_178b(entry_sequence)
        self.assertEqual(expected_answer, answer)
 

    def test_task178b_valid_empty(self):
        entry_sequence = []
        expected_answer = 0
        answer = task_178b(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task178b_valid_str(self):
        entry_sequence = "(1, 2, 3, 4, 5, 6)"
        with self.assertRaises(AssertionError):
            task_178b(entry_sequence)

if __name__ == "__main__":
    main()
