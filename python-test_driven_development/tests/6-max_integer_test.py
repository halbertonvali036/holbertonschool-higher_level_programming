#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for max_integer function testing."""

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with a list where max value is at the start."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test calling max_integer with no arguments."""
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -5, -3, -10]), -1)

    def test_mixed_numbers(self):
        """Test with a list containing positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, 0, -2, 12]), 12)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3, -4.1]), 2.7)

    def test_mixed_ints_and_floats(self):
        """Test with a list of mixed ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 0.8]), 3)

    def test_string(self):
        """Test passing a string as an argument."""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """Test passing a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")


if __name__ == '__main__':
    unittest.main()
