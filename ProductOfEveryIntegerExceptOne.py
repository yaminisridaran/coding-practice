
def productofeveryint(intlist):
	product_except = [None] * len(intlist)
	product_so_far = 1

	for i in range(len(intlist)):
		product_except[i] = product_so_far
		product_so_far *= intlist[i]
	
	product_so_far = 1
	for i in range(len(intlist)-1, -1, -1):
		product_except[i] *= product_so_far
		product_so_far *= intlist[i]

	return product_except


if __name__ == "__main__":
	list = [1,2,3]
	print productofeveryint(list)