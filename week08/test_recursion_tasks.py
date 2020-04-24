import unittest
from recursion_tasks import (deep_find, deep_find_all, deep_update, deep_apply)


class TestDeepFind(unittest.TestCase):

	def test_deep_find_when_key_is_not_nested(self):

		data = {
	    'key1': 'val1',
	    'key2': 'val2',
	    'key3': {
	        'inner_key1': 'val1',
	        'inner_key2': 'val2'
	    },
	    'key4': 'not expected'
		}
		key = 'key2'

		result = deep_find(data, key)
		expected = 'val2'

		self.assertEqual(result, expected)


	def test_deep_find_when_key_is_nested(self):

		data = {
	    'key1': 'val1',
	    'key2': 'val2',
	    'key3': {
	        'inner_key1': 'val1',
	        'inner_key2': 'val2'
	    },
	    'key4': 'not expected'
		}
		key = 'inner_key2'

		result = deep_find(data, key)
		expected = 'val2'

		self.assertEqual(result, expected)


	def test_deep_find_when_key_value_is_dict(self):

		data = {
	    'key1': 'val1',
	    'key2': 'val2',
	    'key3': {
	        'inner_key1': 'val1',
	        'inner_key2': 'val2'
	    },
	    'key4': 'not expected'
		}
		key = 'key3'

		result = deep_find(data, key)
		expected = {
			'inner_key1': 'val1',
	        'inner_key2': 'val2'
		}

		self.assertEqual(result, expected)


	def test_deep_find_when_there_is_no_such_key(self):

		data = {
	    'key1': 'val1',
	    'key2': 'val2',
	    'key3': {
	        'inner_key1': 'val1',
	        'inner_key2': 'val2'
	    },
	    'key4': 'not expected'
		}
		key = 'key6'

		result = deep_find(data, key)
		expected = None

		self.assertEqual(result, expected)



class TestDeepFindAll(unittest.TestCase):

	def test_deep_find_all_when_the_key_is_found_only_once(self):

		data = {
		'key1': 'val1',
		'key2': 'val2',
		'key3': {
		'key6': 'val6',
		'key2': 'val5',
		'key7': 'val7'
		},
		'key4': 'val5',
		'key5': 'some value'
		}
		key = 'key4'

		result = deep_find_all(data, key)
		expected = ['val5']

		self.assertEqual(result, expected)


	def test_deep_find_all_when_the_key_is_found_more_than_once(self):

		data = {
		'key1': 'val1',
		'key2': 'val2',
		'key3': {
		'key6': 'val6',
		'key2': 'val5',
		'key7': 'val7'
		},
		'key4': 'val5',
		'key5': 'some value'
		}
		key = 'key2'

		result = deep_find_all(data, key)
		expected = ['val2', 'val5']

		self.assertEqual(result, expected)


	def test_deep_find_all_when_there_is_no_such_key(self):

		data = {
		'key1': 'val1',
		'key2': 'val2',
		'key3': {
		'key6': 'val6',
		'key2': 'val5',
		'key7': 'val7'
		},
		'key4': 'val5',
		'key5': 'some value'
		}
		key = 'key'

		result = deep_find_all(data, key)
		expected = []

		self.assertEqual(result, expected)



class TestDeepUpdate(unittest.TestCase):

	def test_deep_update_when_the_key_is_found_once(self):

		data = {
		'key1': 'val1',
		'key2': 'val2',
		'key3': {
		'key6': 'val6',
		'key2': 'val5'
		},
		'key4': 'val5',
		'key5': 'some value'
		}	
		key = 'key4'
		val = 'new value'

		result = deep_update(data, key, val)
		expected = {
		'key1': 'val1',
		'key2': 'val2',
		'key3': {
		'key6': 'val6',
		'key2': 'val5'
		},
		'key4': 'new value',
		'key5': 'some value'
		}	

		self.assertEqual(result, expected)


	def test_deep_update_when_the_key_is_found_more_than_once(self):

		data = {
		'key1': 'val1',
		'key2': 'val2',
		'key3': {
		'key6': 'val6',
		'key2': 'val5'
		},
		'key4': 'val5',
		'key5': 'some value'
		}	
		key = 'key2'
		val = 'new value'

		result = deep_update(data, key, val)
		expected = {
		'key1': 'val1',
		'key2': 'new value',
		'key3': {
		'key6': 'val6',
		'key2': 'new value'
		},
		'key4': 'val5',
		'key5': 'some value'
		}	

		self.assertEqual(result, expected)




if __name__ == '__main__':
	unittest.main()
