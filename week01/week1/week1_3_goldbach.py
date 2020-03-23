def is_prime(number):

	if number <= 1: 
		return False

	if number <= 3: 
		return True
  
	if number % 2 == 0 or number % 3 == 0: 
		return False
  
	i = 5
	while i * i <= number: 

		if number % i == 0 or number % (i + 2) == 0: 
			return False

		i += 6
  
	return True


def goldbach(n):

	result = []

	for i in range(2, (n//2 + 1)):

		tuples = ()

		if is_prime(i) and is_prime(n - i):

			tuples = i, n - i
			result.append(tuples)

	return result



	
