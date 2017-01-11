a = [2,4,10,16]

def multiply(list, number):
	newlist = []
	for value in list:
		newlist.append(value * number)
	return newlist

b = multiply(a,5)
print b