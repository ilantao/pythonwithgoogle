def second_element_tuple(tuplename):
	list_of_second_element = []
	for k in range(len(tuplename)):
		list_of_second_element.append(tuplename[k][1])
	return list_of_second_element

a = [('c', 1),('d',3),('e',4)]

print second_element_tuple(a)