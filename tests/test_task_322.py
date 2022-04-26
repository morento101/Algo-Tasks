"""This module is for testing task 322."""

import unittest

from tasks.task_322 import (get_number_with_largest_sum_of_divisors,\
                            get_divisors_list)


class Task322Tests(unittest.TestCase):
    """This class is for testing function is_3_in_sqiare_of_number."""

    def test_valid(self):
        """This method is for testing the correct result."""
        self.assertEqual(get_number_with_largest_sum_of_divisors(1, 50), 48)
        self.assertCountEqual(get_divisors_list(12), [1, 2, 3, 4, 6, 12])


    def test_type(self):
        """This method is for testing the TypeError."""
        with self.assertRaises(AssertionError):
            get_number_with_largest_sum_of_divisors("!22", 2)
        with self.assertRaises(AssertionError):
            get_number_with_largest_sum_of_divisors([], 2)

        with self.assertRaises(AssertionError):
            get_divisors_list("!22")
        with self.assertRaises(AssertionError):
            get_divisors_list([])


    def test_value(self):
        """This method is for testing the ValueError."""
        with self.assertRaises(AssertionError):
            get_number_with_largest_sum_of_divisors(0, 10)
        with self.assertRaises(AssertionError):
            get_number_with_largest_sum_of_divisors(-23, 0)

        with self.assertRaises(AssertionError):
            get_divisors_list(0)
        with self.assertRaises(AssertionError):
            get_divisors_list(-23)


    def test_negative(self):
        """This method is for testing the incorrect result."""
        self.assertEqual(get_number_with_largest_sum_of_divisors(1, 50), 48)
        self.assertCountEqual(get_divisors_list(12), [1, 2, 3, 5, 6, 12])


if __name__ == '__main__':
    unittest.main()
