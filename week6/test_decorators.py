import unittest
from decorators import (accept, performance, silence)
from time import sleep


class TestAccept(unittest.TestCase):

	def test_accept_with_correct_input(self):

		@accept(str)
		def say_hello(name):
			return f"Hello, I am {name}"

		result = say_hello('Megi')
		expected = 'Hello, I am Megi'

		self.assertEqual(result, expected)


	def test_accept_with_incorrect_input(self):

		@accept(str)
		def say_hello(name):
			return f"Hello, I am {name}"

		exc = None

		try:
			say_hello(4)
		except TypeError as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Argument 4 of say_hello is not <class 'str'>!")


#log.txt and errors.txt are empty files

class TestPerformance(unittest.TestCase):

	def test_writing_in_file(self):

		@performance('log.txt')
		def something_heavy():
			sleep(2.10)
			return "I am done!"

		something_heavy()

		f = open('log.txt', 'r')
		result = f.readline()
		f.close()

		self.assertEqual(result, 'something_heavy was called and took 02.10 seconds to complete\n')



class TestSilence(unittest.TestCase):

	def test_silence(self):

		@silence('errors.txt')
		def foo(x):
			if x > 50:
				raise ValueError('Omg.')

		foo(10)
		foo(100)

		f = open('errors.txt', 'r')
		result = f.readline()
		f.close()

		self.assertEqual(result, "Calling foo raised an error - ValueError: 'Omg.'. Provided arguments: (100,).\n")



if __name__ == '__main__':
	unittest.main()