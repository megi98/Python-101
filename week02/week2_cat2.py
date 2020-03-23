import sys

def cat2(arguments):

	i = 1
	while i < len(arguments):
		f = open(arguments[i], "r")
		print(f.read())
		f.close()
		i += 1


def main():

	files = sys.argv
	cat2(files)


if __name__ == '__main__':
	main()