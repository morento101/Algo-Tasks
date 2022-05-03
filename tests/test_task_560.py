"""Module with tests for task 560"""

from unittest import TestCase

from tasks.task_560 import task_560


class TestTask560(TestCase):
    """Tests for task 560"""
    
    def test_valid(self):
        """ Test with valid result """
        test_res = ['220 284']
        self.assertEqual(task_560(), test_res)

    def test_not_valid(self):
        """ Test with not valid result """
        test_res = ['221 284']
        self.assertNotEqual(task_560(), test_res)
