#Make a decorator @accepts that takes as many arguments as the function takes. 
#That decorator specify the types of the arguments that your function takes. If any of the arguments does not match the type in the decorator raise a TypeError

def accept(*args1):

	def wrapper_func(original_func):

		def check_args(*args2):

			n = len(args2)

			for i in range(n):
				if type(args2[i]) is not args1[i]:
					raise TypeError(f'Argument {args2[i]} of {original_func.__name__} is not {args1[i]}!')

			return original_func(*args2)

		return check_args
		
	return wrapper_func




#Make a decorator @performance that takes a file_name and writes in to this file a log. 
#New line for every call of the decorated function. This decorator should log the time needed for the decorated function to execute.

import datetime


def performance(file_name):

	def wrapper_func(original_func):

		def write_log():

			start = datetime.datetime.now()
			original_func()
			end = datetime.datetime.now()
			needed_time = end - start
			needed_time = str(needed_time)[5:10]

			f = open(file_name, 'w')
			f.write(f'{original_func.__name__} was called and took {needed_time} seconds to complete\n')
			f.close()

			return original_func()

		return write_log

	return wrapper_func



#Make a decorator @silence that accepts a file_name as an argument. 
#All functions that are decorated with it should always run successfully. If an error is raised, it should be logged in the given file.

def silence(file_name):

	def wrapper_func(original_func):

		def check_for_errors(*args):

			try:
				original_func(*args)
			except Exception as err:
				arguments = [arg for arg in args]
				arguments = tuple(arguments)
				f = open(file_name, 'w')
				f.write(f"Calling {original_func.__name__} raised an error - {type(err).__name__}: '{str(err)}'. Provided arguments: {arguments}.\n")
				f.close()

		return check_for_errors

	return wrapper_func









		