"""Test of task_88a.py."""

from unittest import TestCase
from unittest import main

from tasks.task_88a import task_88a


class TestTask88a(TestCase):
    """Tests for function: is_3_in_square_of_number."""

    def test_with_zero_argument(self):
        """Test with 0 as function argument."""
        with self.assertRaises(AssertionError):
            task_88a(0)

    def test_with_negative_argument(self):
        """Test with negative number as function argument."""
        with self.assertRaises(AssertionError):
            task_88a(-1)

    def test_negative_result(self):
        """Test with negative result expectation."""
        self.assertEqual(task_88a(1), False)
        self.assertEqual(task_88a(7), False)

    def test_positive_result(self):
        """Test with positive result expectation."""
        self.assertEqual(task_88a(6), True)
        self.assertEqual(task_88a(19), True)


if __name__ == "__main__":
    main()
