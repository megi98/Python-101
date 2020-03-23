def validate_types(iterable, ascending, key):
	
	arg1 = type(iterable)
	arg2 = type(ascending)
	arg3 = type(key)
	
	if arg1 is not list and arg1 is not tuple:
		raise ValueError('Invalid input.')

	if arg2 is not bool:
		raise ValueError('Invalid input.')

	if arg3 is not str:
		raise ValueError('Invalid input.')


def sorting(iterable, ascending=True):

	n = len(iterable)

	for i in range(n):
		for j in range(0, n-i-1):
			if iterable[j] > iterable[j+1]:
				iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

	if ascending is False:
		iterable.reverse()
		return iterable

	return iterable


def sorting_dictionaries(iterable, ascending=True, key='age'):

	n = len(iterable)

	for i in range(n):
		for j in range(0, n-i-1):
			if iterable[j][key] > iterable[j+1][key]:
				iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

	if ascending is False:
		iterable.reverse()
		return iterable

	return iterable



def my_sort(iterable=[], ascending=True, key=''):
	
	validate_types(iterable, ascending, key)

	my_type = type(iterable[0])

	if my_type is not dict:
		return sorting(iterable, ascending)

	if my_type is dict:
		return sorting_dictionaries(iterable, ascending)

