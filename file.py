import sys


def Cat(filename):
	f = open(filename, 'rU')
	text = f.read()
	print text,
	f.close()
def main():
	Cat(sys.argv[1])

if __name__ == '__main__':
	main()