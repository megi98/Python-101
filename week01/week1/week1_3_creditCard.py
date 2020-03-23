def is_credit_card_valid(number):
	
	str_number = str(number)
	transformed = ''
	n = len(str_number)

	if n % 2 == 0:
		return False

	sum_transform = 0
	i = 0
	
	while i < n:

		if i % 2 == 0:
			transformed += str_number[i]

		else:
			transformed += str(int(str_number[i]) * 2)

		i += 1

	for digit in transformed:
		sum_transform += int(digit)

	if sum_transform % 10 == 0:
		return True

	else:
		return False

print(is_credit_card_valid(79927398715))

	

