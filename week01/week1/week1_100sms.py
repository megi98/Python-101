def numbers_to_message(pressed_sequence):

	dict1 = {
		'2': 'a',
		'22': 'b',
		'222': 'c',
		'3': 'd',
		'33': 'e',
		'333': 'f',
		'4': 'g',
		'44': 'h',
		'444': 'i',
		'5': 'j',
		'55': 'k',
		'555': 'l',
		'6': 'm',
		'66': 'n',
		'666': 'o',
		'7': 'p',
		'77': 'q',
		'777': 'r',
		'7777': 's',
		'8': 't',
		'88': 'u',
		'888': 'v',
		'9': 'w',
		'99': 'x',
		'999': 'y',
		'9999': 'z',
		'0': ' '
	}

	result = ''
	i = 0

	while i < len(pressed_sequence):

		if pressed_sequence[i] == -1:
			i += 1

		elif pressed_sequence[i] == 1:

			i += 1
			current = ''
			current += str(pressed_sequence[i])

			while i < len(pressed_sequence) - 1 and pressed_sequence[i] == pressed_sequence[i+1]:

				current += str(pressed_sequence[i+1])
				i += 1

			result += dict1[current].upper()
			i += 1

		else:

			current = ''
			current += str(pressed_sequence[i])

			while i < len(pressed_sequence) - 1 and pressed_sequence[i] == pressed_sequence[i+1]:

				current += str(pressed_sequence[i+1])
				i += 1

			result += dict1[current]
			i += 1

	return result



def message_to_numbers(message):

	dict2 = {
		'a': [2],
		'b': [2, 2],
		'c': [2, 2, 2],
		'd': [3],
		'e': [3, 3],
		'f': [3, 3, 3],
		'g': [4],
		'h': [4, 4],
		'i': [4, 4, 4],
		'j': [5],
		'k': [5, 5],
		'l': [5, 5, 5],
		'm': [6],
		'n': [6, 6],
		'o': [6, 6, 6],
		'p': [7],
		'q': [7, 7],
		'r': [7, 7, 7],
		's': [7, 7, 7, 7],
		't': [8],
		'u': [8, 8],
		'v': [8, 8, 8],
		'w': [9],
		'x': [9, 9],
		'y': [9, 9, 9],
		'z': [9, 9, 9, 9],
		' ': [0]
	}

	result = []
	i = 0

	while i < len(message):

		if message[i].isupper():
			result.append(1)
		
		current = message[i].lower()

		if i < len(message) - 1:
			current2 = message[i+1].lower()

		for j in dict2[current]:
			result.append(j)

		if i < len(message) - 1 and dict2[current][0] == dict2[current2][0]:
			result.append(-1)

		i += 1

	return result







