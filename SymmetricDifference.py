"""  A function that takes two or more arrays and returns an array of the symmetric difference (△ or ⊕). """

def sym(*args):
	"""Return Unique Values between Arrays into one array """
	sym = [];
	value = args[0][0]
	
	for array in args:
		#iterate over tuple of arrays
		for value in array:
			#iterate over values in each arrays in tuple
			count = 0
			for array2 in args:
				#iterate each array in tuple
				#check if value is in other arrays
				try:
					index = array2.index(value)
				except ValueError:
					count = count + 1
			if(count == len(args) - 1):
				#count one less then number of arrays means
				#Value is unique add it to sym
				sym.append(value)
	
	return list(dict.fromkeys(sym))


SymDif = sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])
print(SymDif)
