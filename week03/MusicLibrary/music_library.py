def validate_sec_min_hour(time):

	if len(time) == 2 and time[0] == '0':
		return int(time[1])
		
	return int(time)


def validate_length(length):

	list_length = length.split(':')

	if len(list_length) == 2:

		mins = int(list_length[0])
		secs = int(list_length[1])
		assert mins < 60 and secs < 60, 'Invalid input.'

	else:
		mins = int(list_length[1])
		secs = int(list_length[2])
		assert mins < 60 and secs < 60, 'Invalid input.'



class Song:

	def __init__(self, title, artist, album, length):

		self.title = title
		self.artist = artist
		self.album = album

		n = length.count(':')
		assert (n == 1 or n == 2), 'Invalid input.'
		validate_length(length)

		self.length = length


	def __str__(self):

		return f'{self.title} - {self.artist} from {self.album} - {self.length}'


	def __key(self):

		return (self.title, self.artist, self.album, self.length)


	def __eq__(self, other):

		return self.__key() == other.__key()


	def __hash__(self):

		return hash(self.__key())


	def length1(self, seconds=False, minutes=False, hours=False):

		list_length = self.length.split(':')
		result = 0

		if seconds is True:

			if len(list_length) == 2:

				mins = validate_sec_min_hour(list_length[0])
				secs = validate_sec_min_hour(list_length[1])
				result = mins * 60 + secs
				return result

			else:

				hrs = validate_sec_min_hour(list_length[0])
				mins = validate_sec_min_hour(list_length[1])
				secs = validate_sec_min_hour(list_length[2])
				result = hrs * 360 + mins * 60 + secs
				return result

		if minutes is True:

			if len(list_length) == 2:

				return validate_sec_min_hour(list_length[0])

			else:

				hrs = validate_sec_min_hour(list_length[0])
				mins = validate_sec_min_hour(list_length[1])
				result = hrs * 60 + mins
				return result

		if hours is True:

			if len(list_length) == 2:
				return 0

			else:
				return validate_sec_min_hour(list_length[0])

		return self.length





