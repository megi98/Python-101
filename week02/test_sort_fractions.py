import unittest
from sort_fractions import sort_fractions

class TestSortFractions(unittest.TestCase):

	def test_sorting_in_ascending_order(self):

		fractions1 = [(2, 3), (1, 2)]
		fractions2 = [(2, 3), (1, 2), (1, 3)]
		fractions3 = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]

		expected1 = [(1, 2), (2, 3)]
		expected2 = [(1, 3), (1, 2), (2, 3)]
		expected3 = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
		result1 = sort_fractions(fractions1)
		result2 = sort_fractions(fractions2)
		result3 = sort_fractions(fractions3)

		self.assertEqual(result1, expected1)
		self.assertEqual(result2, expected2)
		self.assertEqual(result3, expected3)


	def test_sorting_in_descending_order(self):

		fractions1 = [(1, 2), (1, 3), (2, 3)]
		fractions2 = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
		ascending = False

		expected1 = [(2, 3), (1, 2), (1, 3)]
		expected2 = [(22, 7), (9, 6), (7, 8), (5, 6), (15, 32), (22, 78)]
		result1 = sort_fractions(fractions1, ascending)
		result2 = sort_fractions(fractions2, ascending)

		self.assertEqual(result1, expected1)
		self.assertEqual(result2, expected2)



if __name__ == '__main__':
	unittest.main()
