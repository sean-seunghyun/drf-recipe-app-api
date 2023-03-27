from django.test import SimpleTestCase
from app import calc
class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(3,8)
        return self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 2)
        return self.assertEqual(res, 8)
