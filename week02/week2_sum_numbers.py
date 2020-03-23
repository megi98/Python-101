import sys

def sum_numbers(filename):

	f = open(filename, "r")
	numbers_list = f.read().split()
	f.close()

	result = 0
	for i in numbers_list:
		result += int(i)

	return result
	


def main():
	file = sys.argv[1]
	print(sum_numbers(file))


if __name__ == "__main__":
	main()	