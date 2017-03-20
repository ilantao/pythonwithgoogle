import sys


def Cat(filename):
	f = open(filename, 'rU')
	text = f.read()
	list_of_text = text.split()
	#print list_of_text
	dict_of_text = {}
	for key_word in list_of_text:
		if dict_of_text.get(key_word):
			dict_of_text[key_word] = dict_of_text[key_word] + 1
		else:
			dict_of_text[key_word] = 1


	for k in sorted(dict_of_text.keys()):
		print "The word:", "'{0}'".format(k), "appears", dict_of_text[k], 'times'
	f.close()

def second_element_tuple(tuplename):
	return tuplename[1]

def print_top(filename):
	f = open(filename, 'rU')
	text = f.read()
	list_of_text = text.split()
	#print list_of_text
	dict_of_text = {}
	for key_word in list_of_text:
		if dict_of_text.get(key_word):
			dict_of_text[key_word] = dict_of_text[key_word] + 1
		else:
			dict_of_text[key_word] = 1
	tuple_of_text = dict_of_text.items()
	#print tuple_of_text
	#outputs
	sorted_tuple = sorted(tuple_of_text, key = second_element_tuple, reverse=True)
	for item in sorted_tuple[:20]:
		print item[0],item[1]


def main():
	Cat(sys.argv[1])
	print_top(sys.argv[1])

if __name__ == '__main__':
	main()