#1.
def sum_of_digits(n):
	sum = 0
	if n < 0:
		n = abs(n)
	while n >= 10:
		sum += n % 10
		n //= 10
	sum += n
	return sum
		

#2.
def to_digits(n):
	result = []
	while n >= 10:
		x = n % 10
		result.insert(0, x)
		n //= 10
	result.insert(0, n)
	return result


#3.
def to_number(digits):
	result = ''
	for number in digits:
		result += str(number)
	return int(result)


#4.
import math
def fact_digits(n):
	sum = 0
	while n >= 10:
		x = n % 10
		sum += math.factorial(x)
		n //= 10
	sum += math.factorial(n)
	return sum


#5.
def palindrome(obj):
	string = str(obj)
	if string == string[::-1]:
		return True
	else:
		return False


#6.
def count_vowels(str):
	count = 0
	str = str.lower()
	for letter in str:
		if letter in 'aeiouy':
			count += 1
	return count



#7.
def count_consonants(str):
	count = 0
	str = str.lower()
	for letter in str:
		if letter in 'bcdfghgklmnpqrstvwxz':
			count += 1
	return count


#8.
import ast
def char_histogram(string):
	symbols = ''
	sym_count = ''
	for symbol in string:
		if symbol not in symbols:
			symbols += symbol
	for letter in symbols:
		count = 0
		count = string.count(letter)
		sym_count += str(count)
	i = 0
	result_str = '{'
	j = -1
	for s in symbols:
		j += 1
	while i < j:
		result_str += f'"{symbols[i]}"  : {sym_count[i]}, '
		i += 1
	result_str += f'"{symbols[i]}" : {sym_count[i]}'
	result_str += '}'
	result = ast.literal_eval(result_str) 
	return result


#9.
def sum_matrix(m):
	result_sum = 0
	for i in m:
		row_sum = 0
		for j in i:
			row_sum += j
		result_sum += row_sum
	return result_sum


#10.
def nan_expand(times):
	result = '""'
	if times == 0:
		return result
	else:
		result = '"'
		while times > 1:
			result += 'Not a '
			times -= 1
		result += 'Not a NaN"'
		return result


#11.
def prime_factorization(n):

	prime_factors = []

	while n % 2 == 0:
		prime_factors.append(2)
		n //= 2

	for i in range(3, int(math.sqrt(n)) + 1, 2):
		while n % i == 0:
			prime_factors.append(i)
			n //= i

	if n > 2:
		prime_factors.append(n)

	no_duplicates = list(dict.fromkeys(prime_factors))
	power_arr = []
	
	for j in no_duplicates:
		power_arr.append(prime_factors.count(j))

	result = []

	k = 0
	while k < len(power_arr):
		tuples = no_duplicates[k], power_arr[k]
		result.append(tuples)
		tuples = ()
		k += 1

	return result



#12.
def group(inp):

	n = len(inp)
	result = []
	i = 0

	while i < n - 1:

		current = []
		current.append(inp[i])

		if inp[i] != inp[i+1]:
			result.append(current)
			i += 1

		else:
			while i < n - 1 and inp[i] == inp[i+1]:
				current.append(inp[i+1])
				i += 1
			i += 1
			result.append(current)

	if inp[n-1] != inp[n-2]:

		current = []
		current.append(inp[n-1])
		result.append(current)
	
	return result


#13.
def max_consecutive(items):

	result_arr = []
	i = 0
	n = len(items)

	while i < n - 1:

		count = 1

		if items[i] != items[i+1]:
			result_arr.append(count)
			i += 1

		else:
			while i < n - 1 and items[i] == items[i+1]:
				count += 1
				i += 1
			i += 1
			result_arr.append(count)

	return max(result_arr)







