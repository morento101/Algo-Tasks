""" Test of task_331b.py """

from unittest import TestCase
from unittest import main

from tasks.task_331b import task_331b


class TestTask331b(TestCase):
    """Test for function test_331b"""

    def test_valid(self):
        """This method is for testing the correct result"""
        self.assertEqual(task_331b(21),
                         [(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1),
                          (4, 1, 2), (4, 2, 1)])
        self.assertTrue((3, 3, 7) in task_331b(67))
        self.assertNotEqual(task_331b(1097),
                            [(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1),
                             (4, 1, 2), (4, 2, 1)])
        self.assertTrue((13, 28, 12) in task_331b(1097))

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            task_331b(-1)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_invalid_argument_type(self):
        """Test with wrong argument type"""
        with self.assertRaises(AssertionError) as test_exception:
            task_331b(None)
        self.assertEqual("Wrong argument, must be natural integer",
                         test_exception.exception.args[0])

    def test_with_empty_results(self):
        """Test with empty results"""
        self.assertEqual(task_331b(1), [])


if __name__ == "__main__":
    main()