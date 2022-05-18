"""
sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substracts_numbers(self):
        """Test substracting numbers."""

        res = calc.substract(11, 6)

        self.assertEqual(res, 5)
