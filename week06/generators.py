#Implement a function that takes two iterables and returns another one that concatenate the two iterables.

def chain(iterable_one, iterable_two):

	def concat_generator():

		for i in iterable_one:
			yield i

		for j in iterable_two:
			yield j

	result = []

	for item in concat_generator():
		result.append(item)

	return result



#Implement a function that takes one iterables and one iterable mask. The mask is an collection that contains only True or False
#This function returns only this objects from the first collection that have True on their position in the mask.

def compress(iterable, mask):

	def true_objects_generator():

		n = len(iterable)

		for i in range(n):
			if mask[i] is True:
				yield iterable[i]
			
	result = []

	for item in true_objects_generator():
		result.append(item)

	return result


print(tuple(compress(["Ivo", "Rado", "Panda"], [True, False, True])))