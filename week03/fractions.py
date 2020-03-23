from math import gcd

class Fraction:

	def __init__(self, nominator, denominator):

		assert denominator >= 1, "Invalid denominator."

		self.nominator = nominator
		self.denominator = denominator


	def __str__(self):

		return f'{self.nominator}/{self.denominator}'


	def __repr__(self):

		return f'Fraction {self}'



	def __add__(self, other):

		nominator = self.nominator * other.denominator + other.nominator * self.denominator
		denominator = self.denominator * other.denominator

		return Fraction(nominator, denominator).simplify()


	def __eq__(self, other):

		return self.nominator/self.denominator == other.nominator/other.denominator


	def __lt__(self, other):

		return self.nominator/self.denominator < other.nominator/other.denominator


	def simplify(self):

		g_c_d = gcd(self.nominator, self.denominator)
		return Fraction(self.nominator//g_c_d, self.denominator//g_c_d)