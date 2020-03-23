import sys
from random import randint

def generate_numbers(filename, numbers):

	f = open(filename, "w")
	for i in range(numbers):
		f.write(f'{randint(1,100)} ')
	f.close()


def main():
	file = sys.argv[1]
	n = int(sys.argv[2])
	generate_numbers(file, n)


if __name__ == "__main__":
	main()