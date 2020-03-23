import unittest
from fractions import Fraction


class TestFraction(unittest.TestCase):

	def test_raises_exception_if_denominator_is_less_than_1(self):

		exc = None

		try:
			Fraction(2, 0)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Invalid denominator.")


	def test_simplifying(self):

		fraction1 = Fraction(3, 6)
		fraction2 = Fraction(1, 7)
		fraction3 = Fraction(462, 63)

		result1 = fraction1.simplify()
		result2 = fraction2.simplify()
		result3 = fraction3.simplify()

		self.assertEqual(str(result1), '1/2')
		self.assertEqual(str(result2), '1/7')
		self.assertEqual(str(result3), '22/3')


	def test_if_collecting_is_correct(self):

		fraction1 = Fraction(1, 7)
		fraction2 = Fraction(2, 6)

		result = fraction1 + fraction2

		self.assertEqual(str(result), '10/21')


	def test_equality(self):

		fraction1 = Fraction(1, 7)
		fraction2 = Fraction(1, 7)
		fraction3 = Fraction(3, 21)

		self.assertEqual(fraction1, fraction2)
		self.assertEqual(fraction1, fraction3)
		


if __name__ == "__main__":
	unittest.main()

