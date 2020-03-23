from simplify_fractions import simplify_fraction


def lcm(x, y):

	if x > y:
		greater = x
	else:
		greater = y

	while True:
		if greater % x == 0 and greater % y == 0:
			lcm = greater
			break
		greater += 1

	return lcm


def collect_fractions(fractions):
	
	if fractions[0][1] == fractions[1][1]:

		nominator = fractions[0][0] + fractions[1][0]
		result = nominator, fractions[0][1]
		return simplify_fraction(result)
		
	denominator = lcm(fractions[0][1], fractions[1][1])
	multiplier1 = denominator // fractions[0][1]
	multiplier2 = denominator // fractions[1][1]

	nominator1 = fractions[0][0] * multiplier1
	nominator2 = fractions[1][0] * multiplier2
	nominator = nominator1 + nominator2

	result = nominator, denominator
	return simplify_fraction(result)