#1.
def gas_stations(distance, tank_size, stations):

	current = 0
	result = []

	while current + tank_size < distance:

		i = len(stations) - 1

		while current + tank_size < stations[i]:

			i -= 1

		current = stations[i]
		result.append(stations[i])

	return result


#2.
def is_number_balanced(number):

	inp = number

	if number < 10:
		return True

	num_digits = 0

	while inp >= 10:
		num_digits += 1
		inp //= 10
	num_digits += 1

	sum1 = 0
	sum2 = 0
	to_str = str(number)
	half = num_digits // 2
	i = 0

	while i < half:
		sum1 += int(to_str[i])
		i += 1

	if num_digits % 2 != 0:
		half += 1

	while half < num_digits:
		sum2 += int(to_str[half])
		half += 1

	if sum1 == sum2:
		return True

	return False


#3.
def increasing_or_decreasing(seq):

	n = len(seq)
	count1 = 0
	count2 = 0

	for i in range(n-1):

		if seq[i] < seq[i+1]:
			count1 += 1

		if seq[i] > seq[i+1]:
			count2 += 1

	if count1 == n - 1:
		return 'Up!'
	elif count2 == n - 1:
		return 'Down!'
	else:
		return False


#4.
def get_largest_palindrome(n):


	while str(n-1) != str(n-1)[::-1]:
		n -= 1

	return n - 1


	# palindromes = []

	# for i in range(n):

	# 	current = str(i)
	# 	if current == current[::-1]:
	# 		palindromes.append(int(current))

	# return max(palindromes)


#5.
def sum_of_numbers(input_string):

	result = 0
	i = 0

	while i < len(input_string):

		number = ''

		while i < len(input_string) and ord(input_string[i]) >= 48 and ord(input_string[i]) <= 57:

			number += input_string[i]
			i += 1

		i += 1
		if number != '':
			result += int(number)

	return result


#6.
def bithday_ranges(birthdays, ranges):

	result = []

	for tuples in ranges:

		count = 0

		for bday in birthdays:

			if bday >= tuples[0] and bday <= tuples[1]:
				count += 1

		result.append(count)

	return result


