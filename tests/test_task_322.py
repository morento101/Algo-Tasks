""" Test of task_322.py """

from unittest import TestCase
from unittest import main

from tasks.task_322 import task_322


class TestTask322(TestCase):
    """This class is for testing function is_3_in_sqiare_of_number."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(task_322(), 9240)

    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertNotEqual(task_322(), 48)


if __name__ == '__main__':
    main()
