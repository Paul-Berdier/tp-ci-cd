"""
Unit tests for SimpleMath class.
"""

import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    """Unit tests for SimpleMath class."""

    def test_addition(self):
        """Test addition method."""
        self.assertEqual(SimpleMath.addition(2, 3), 5)

    def test_soustraction(self):
        """Test soustraction method."""
        self.assertEqual(SimpleMath.soustraction(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
