from math import gcd

def simplify_fraction(fraction):
	
	nominator = fraction[0]
	denominator = fraction[1]

	if denominator == 0:
		raise ValueError('Denominator cannot be zero!')

	g_c_d = gcd(nominator, denominator)

	return nominator//g_c_d, denominator//g_c_d
