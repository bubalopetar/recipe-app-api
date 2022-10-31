"""sample tests
"""

from app import calc
from django.test import SimpleTestCase


class CalcTests(SimpleTestCase):
    """
    Tests for calc module
    """

    def test_add_numbers(self):
        """
        test calc function
        """
        res = calc.add(2, 4)
        self.assertEqual(res, 6)

    def test_subtract_numbers(self):
        """
        test subtracting numbers
        """
        res = calc.subtract(4, 3)
        self.assertEqual(res, 1)
