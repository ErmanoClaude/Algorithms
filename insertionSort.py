def insertion_sort(unsorted):
	""" Insertion Sort Implementation """
	for index, value in enumerate(unsorted):
		j = index
		while j > 0 and unsorted[j-1] > unsorted[j]:
			temp = unsorted[j-1]
			unsorted[j-1] = unsorted[j]
			unsorted[j] = temp
			j = j-1

	print(unsorted)
	return unsorted


unsorted = [5,9,4,3,63,7,234,6,387,9,4,11,73,567,3,345]

insertion_sort(unsorted)
