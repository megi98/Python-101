from simplify_fractions import simplify_fraction
from collect_fractions import lcm


def sort_fractions(fractions, ascending = True):
	
	n = len(fractions)

	for i in range(n):
		for j in range(0, n-i-1):

			denominator = lcm(fractions[j][1], fractions[j+1][1])

			multiplier1 = denominator // fractions[j][1]
			multiplier2 = denominator // fractions[j+1][1]

			nominator1 = fractions[j][0] * multiplier1
			nominator2 = fractions[j+1][0] * multiplier2

			if nominator1 > nominator2:
				fractions[j], fractions[j+1] = fractions[j+1], fractions[j]

	if ascending is False:
		fractions.reverse()
		return fractions

	return fractions