#1.
#Implement deep_find(data, key) which finds the given key in the data and returns it's value.

def deep_find(data, key):

	if key in data:
		return data[key]

	for k, v in data.items():
		if isinstance(v, dict):
			value = deep_find(v, key)
			if value is not None:
				return value

	
#2.
#Implement deep_find_all(data, key) which finds the given key in the data and returns array of the found values.

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
#Implement deep_update(data, key, val) which updates every occurance of the given key in the data with val.

def deep_update(data, key, val):

	for k, v in data.items():

		if k == key:
				data[k] = val
		else:
			if isinstance(v, dict):
				deep_update(v, key, val)

	return data
