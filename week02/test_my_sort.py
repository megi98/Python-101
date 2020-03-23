import unittest
from my_sort import (validate_types, sorting, sorting_dictionaries, my_sort)


class TestValidateTypes(unittest.TestCase):

	def test_raises_exception_if_iterable_is_not_tuple_or_list(self):

		iterable = 'a string'
		exc = None

		try:
			validate_types(iterable, True, '')
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input.')


	def test_raises_exception_if_ascending_is_not_boolean(self):

		ascending = 'a string'
		exc = None

		try:
			validate_types([], ascending, '')
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input.')


	def test_raises_exception_if_key_is_not_string(self):

		key = 5, 6
		exc = None

		try:
			validate_types([2,3,4], True, key)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input.')


class TestSorting(unittest.TestCase):

	def test_if_sorting_is_correct_in_ascending_order(self):

		iterable = [6, 3, 12, 26, 9, 10, 5]

		result = sorting(iterable)
		expected = [3, 5, 6, 9, 10, 12, 26]

		self.assertEqual(result, expected)


	def test_if_sorting_is_correct_in_descending_order(self):

		iterable = [6, 3, 12, 26, 9, 10, 5]

		result = sorting(iterable, False)
		expected = [26, 12, 10, 9, 6, 5, 3]

		self.assertEqual(result, expected)


class TestSortingDictionaries(unittest.TestCase):

	def test_sorting_in_ascending_order(self):

		iterable = [{'name': 'megi', 'age': 22}, {'name': 'ivo', 'age': 20}, {'name': 'gosho', 'age': 21}]
		key = 'age'

		result = sorting_dictionaries(iterable, True, key)
		expected = [{'name': 'ivo', 'age': 20}, {'name': 'gosho', 'age': 21}, {'name': 'megi', 'age': 22}]

		self.assertEqual(result, expected)


	def test_sorting_in_descending_order(self):

		iterable = [{'name': 'megi', 'age': 22}, {'name': 'ivo', 'age': 20}, {'name': 'gosho', 'age': 21}]
		key = 'age'

		result = sorting_dictionaries(iterable, False, key)
		expected = [{'name': 'megi', 'age': 22}, {'name': 'gosho', 'age': 21}, {'name': 'ivo', 'age': 20}]

		self.assertEqual(result, expected)


class TestMySort(unittest.TestCase):

	def test_my_sort_with_no_dictionaries_in_ascending_order(self):

		iterable = [6, 3, 12, 26, 9, 10, 5]

		result = my_sort(iterable, True)
		expected = [3, 5, 6, 9, 10, 12, 26]

		self.assertEqual(result, expected)


	def test_my_sort_with_no_dictionaries_in_descending_order(self):

		iterable = [6, 3, 12, 26, 9, 10, 5]

		result = my_sort(iterable, False)
		expected = [26, 12, 10, 9, 6, 5, 3]

		self.assertEqual(result, expected)


	def test_my_sort_with_dictionaries_in_ascending_order(self):

		iterable = [{'name': 'megi', 'age': 22}, {'name': 'ivo', 'age': 20}, {'name': 'gosho', 'age': 21}]
		key = 'age'

		result = my_sort(iterable, True, key)
		expected = [{'name': 'ivo', 'age': 20}, {'name': 'gosho', 'age': 21}, {'name': 'megi', 'age': 22}]

		self.assertEqual(result, expected)


	def test_my_sort_with_dictionaries_in_descending_order(self):

		iterable = [{'name': 'megi', 'age': 22}, {'name': 'ivo', 'age': 20}, {'name': 'gosho', 'age': 21}]
		key = 'age'

		result = my_sort(iterable, False, key)
		expected = [{'name': 'megi', 'age': 22}, {'name': 'gosho', 'age': 21}, {'name': 'ivo', 'age': 20}]

		self.assertEqual(result, expected)


if __name__ == "__main__":
	unittest.main()