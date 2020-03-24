import unittest
from music_library import Song



class TestSong(unittest.TestCase):

	def test_if_length_has_seconds_minutes_and_or_hours_only(self):

		length = '1:05:21:33'
		exc = None

		try:
			Song('title', 'artist', 'album', length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input.')


	def test_if_seconds_are_valid(self):

		length = '5:32:111'
		exc = None

		try:
			Song('title', 'artist', 'album', length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input.')


	def test_if_minutes_are_valid(self):

		length = '88:02'
		exc = None

		try:
			Song('title', 'artist', 'album', length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input.')


	def test_string_representation(self):

		song = Song('title', 'artist', 'album', '02:55')
		
		result = str(song)
		expected = 'title - artist from album - 02:55'

		self.assertEqual(result, expected)


	def test_equality(self):

		song1 = Song('title', 'artist', 'album', '02:55')
		song2 = Song('title', 'artist', 'album', '02:55')

		self.assertEqual(song1, song2)


	# def test_validate_sec_min_hour(self):

	# 	time1 = '05'
	# 	time2 = '23'
	# 	time3 = '8'

	# 	result1 = validate_sec_min_hour(time1)
	# 	result2 = validate_sec_min_hour(time2)
	# 	result3 = validate_sec_min_hour(time3)

	# 	self.assertEqual(result1, 5)
	# 	self.assertEqual(result2, 23)
	# 	self.assertEqual(result3, 8)


	def test_length_in_seconds(self):

		song1 = Song('title', 'artist', 'album', '02:55')
		song2 = Song('title2', 'artist2', 'album2', '02:03:55')
		song3 = Song('title3', 'artist3', 'album3', '00:58')

		secs1 = song1.length1(seconds=True)
		secs2 = song2.length1(seconds=True)
		secs3 = song3.length1(seconds=True)

		self.assertEqual(secs1, 175)
		self.assertEqual(secs2, 955)
		self.assertEqual(secs3, 58)


	def test_length_in_minutes(self):

		song1 = Song('title', 'artist', 'album', '2:55')
		song2 = Song('title2', 'artist2', 'album2', '02:03:55')
		song3 = Song('title3', 'artist3', 'album3', '00:58')

		mins1 = song1.length1(minutes=True)
		mins2 = song2.length1(minutes=True)
		mins3 = song3.length1(minutes=True)

		self.assertEqual(mins1, 2)
		self.assertEqual(mins2, 123)
		self.assertEqual(mins3, 0)


	def test_length_in_hours(self):

		song1 = Song('title', 'artist', 'album', '02:55')
		song2 = Song('title2', 'artist2', 'album2', '02:03:55')
		song3 = Song('title3', 'artist3', 'album3', '00:58')

		hours1 = song1.length1(hours=True)
		hours2 = song2.length1(hours=True)
		hours3 = song3.length1(hours=True)

		self.assertEqual(hours1, 0)
		self.assertEqual(hours2, 2)
		self.assertEqual(hours3, 0)


	def test_string_representation_of_length(self):

		song = Song('title', 'artist', 'album', '02:55')

		result = song.length1()
		expected = '02:55'

		self.assertEqual(result, expected)





if __name__ == '__main__':
	unittest.main()