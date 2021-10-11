""" 
len(a) = na
len(b) = nb
a = [1,2,3,4,5]
b = [2,3,5,6,7.9]
a[0] <> b[0]
"""
na,nb = map(int,input().split())
a = list(map(int, input().strip().split()))[:na]
b = list(map(int, input().strip().split()))[:nb]


def mergeArrays(arr1, arr2, n1, n2):
	arr3 = [None] * (n1 + n2)
	i = 0
	j = 0
	k = 0

	# Traverse both array
	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
			arr3[k] = arr1[i]
			k = k + 1
			i = i + 1
		else:
			arr3[k] = arr2[j]
			k = k + 1
			j = j + 1
	
	while i < n1:
		arr3[k] = arr1[i]
		k = k + 1
		i = i + 1

	while j < n2:
		arr3[k] = arr2[j]
		k = k + 1
		j = j + 1
	for i in range(n1 + n2):
		print(str(arr3[i]), end = " ")
mergeArrays(a, b, na, nb)
