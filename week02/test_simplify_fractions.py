import unittest
from simplify_fractions import simplify_fraction


class TestSimplifyFraction(unittest.TestCase):

	def test_raises_exception_if_denominator_is_zero(self):

		fraction = (3, 0)
		exc = None

		try:
			simplify_fraction(fraction)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Denominator cannot be zero!')


	def test_simplify_fractions(self):

		fraction1 = (3, 6)
		fraction2 = (1, 7)
		fraction3 = (462, 63)

		result1 = simplify_fraction(fraction1)
		result2 = simplify_fraction(fraction2)
		result3 = simplify_fraction(fraction3)

		self.assertEqual(result1, (1, 2))
		self.assertEqual(result2, (1, 7))
		self.assertEqual(result3, (22, 3))



if __name__ == '__main__':
	unittest.main()