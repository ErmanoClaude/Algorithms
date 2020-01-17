def bubble_sort(unsorted):
	"""Simple Bubble Sorting Algorithm"""
	switched = True
	while switched:
		switched = False
		for index, num in enumerate(unsorted):
			if(index== len(unsorted)-1):
				break
			if(num > unsorted[index + 1]):
				temp = num;
				unsorted[index] = unsorted[index + 1];
				unsorted[index + 1] = temp
				switched = True
	return unsorted


print(bubble_sort([1,2,43,5,6,31,5,67,7,3,2,6,3,2]))
