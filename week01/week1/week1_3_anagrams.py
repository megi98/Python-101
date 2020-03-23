word1 = input('Enter the first word: ')
word2 = input('Enter the second word: ')

if len(word1) != len(word2):
	print('NOT ANAGRAMS')

else:
	word1 = word1.lower()
	word2 = word2.lower()
	j = 0

	for i in range(len(word1)):

		if word1.count(word1[i]) == word2.count(word1[i]):
			j += 1


	if j == len(word1):
		print('ANAGRAMS')
	else:
		print('NOT ANAGRAMS')



