""" Test of task_178c.py """

from unittest import TestCase
from unittest import main

from tasks.task_178c import task_178c


class TestTask178b(TestCase):
    """Test for function test_107"""

    def test_task178v_valid(self):
        entry_sequence = (16, 9, 1, 14, 7, 22, 25, 121, 1, 0, 100)
        expected_answer = 3
        answer = task_178c(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task178v_negative(self):
        entry_sequence = (16, 9, -1, 14, 7, 22, 25, -121, 1, 0, 100)
        with self.assertRaises(AssertionError):
            task_178c(entry_sequence)


    def test_task178v_valid_empty(self):
        entry_sequence = []
        expected_answer = 0
        answer = task_178c(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task178v_valid_str(self):
        entry_sequence = "(1, 2, 3, 4, 5, 6)"
        with self.assertRaises(AssertionError):
            task_178c(entry_sequence)

if __name__ == "__main__":
    main()
