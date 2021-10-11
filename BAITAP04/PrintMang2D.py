r , c = map(int, input().split())

arr2 = []
length = []

for i in range(r):
	a = [int(i) for i in input().split()]
	arr2.append(a)

for i in range(c):
	max = 0
	for j in range(r):
		if len(str(arr2[j][i])) > max:
			max = len(str(arr2[j][i]))
	length.append(max)

for i in range(r):
	for j in range(c):
		space = length[j] - len(str(arr2[i][j]))
		print(space * ' ' + str(arr2[i][j]), end = ' ')
	print()