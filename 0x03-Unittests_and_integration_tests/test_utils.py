#!/usr/bin/env python3
"""TestAccessNestedMap class that inherits from unittest.TestCase.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Teat suite for AccessNestedMap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """method to test that the method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
