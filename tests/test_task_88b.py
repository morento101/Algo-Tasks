"""Test of task_88b.py."""

from unittest import TestCase
from unittest import main

from tasks.task_88b import task_88b


class TestReverseNumber(TestCase):
    """Tests for function: reverse_number."""

    def test_with_zero_argument(self):
        """Test with 0 as function argument."""
        with self.assertRaises(AssertionError) as test_exception:
            task_88b(0)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_with_negative_argument(self):
        """Test with negative number as function argument."""
        with self.assertRaises(AssertionError) as test_exception:
            task_88b(-1)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_negative_result(self):
        """Test with negative result expectation."""
        self.assertNotEqual(task_88b(7), 0)
        self.assertNotEqual(task_88b(123456789), 987654320)

    def test_positive_result(self):
        """Test with positive result expectation."""
        self.assertEqual(task_88b(1), 1)
        self.assertEqual(task_88b(123456789), 987654321)
        self.assertEqual(task_88b(123454321), 123454321)


if __name__ == "__main__":
    main()
