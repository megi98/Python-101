import sys

def cat(arguments):

	f = open(arguments, "r")
	print(f.read())
	f.close()

	
def main():
	
	file = sys.argv[1]
	cat(file)

if __name__ == "__main__":
	main()