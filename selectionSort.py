def selection_sort(unsorted):
	"""Selection Sorting"""
	for index, value in enumerate(unsorted):
		if( index == len(unsorted)-1 ):
			break
		least = index
		for i in range( index, len(unsorted)):
			if(unsorted[least]>unsorted[i]):
				least = i
		temp = unsorted[index]
		unsorted[index] = unsorted[least]
		unsorted[least] = temp
	return unsorted

print(selection_sort([2,4,32,23,43,34,423,7,42,24,2,6,2,4,6,7,3,2]))
