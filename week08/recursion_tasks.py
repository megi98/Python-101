#1.

def deep_find(data, key):

	if key in data:
		return data[key]

	for k, v in data.items():
		if isinstance(v, dict):
			value = deep_find(v, key)
			if value is not None:
				return value

	
#2.

def deep_find_all(data, key, some_list=None):

	if some_list == None:
		values_array = []
	else:
		values_array = some_list

	for k, v in data.items():
		if isinstance(v, dict):
			deep_find_all(v, key, values_array)
		else:
			if k == key:
				values_array.append(v)

	return values_array


#3.

def deep_update(data, key, val):

	for k, v in data.items():

		if k == key:
				data[k] = val
		else:
			if isinstance(v, dict):
				deep_update(v, key, val)

	return data




		


