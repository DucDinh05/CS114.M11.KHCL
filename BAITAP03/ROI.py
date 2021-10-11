h, w = map(int, input().split())
matrix = []
arr = []
matrix_0 = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    arr = list(map(int,input().strip().split()))[:w]
    matrix.append(arr)

top, left, bottom, right = map(int, input().split())

for i in range(top, bottom + 1):
	for j in range(left, right + 1):
		matrix_0[i][j] = matrix[i][j]

for i in range(h):
	print(' '.join(map(str,matrix_0[i])))