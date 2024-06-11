def matrix(n: int, m: int, matrix: list) -> list:
	lst_of_mtrx = []
	dir = 0
	for i in range(min(n, m)):
		for j in range(n + m - 1):
			if dir == 0:
				if j < n:
					lst_of_mtrx.append(matrix[0][j])
				elif len(matrix) > 1:
					lst_of_mtrx.append(matrix[j - n + 1][n - 1])
					matrix[j - n + 1].pop(n - 1)
			else:
				if j < n:
					lst_of_mtrx.append(matrix[-1][-j - 1])
				elif len(matrix) > 1:
					lst_of_mtrx.append(matrix[-j + n + 1][0])
					matrix[-j + n + 1].pop(0)
		if len(matrix) != 0:
			matrix.pop([0, -1][dir])
			n = n - 1
			m = m - 1
			dir = not dir
	return lst_of_mtrx
	
# mtrx = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(matrix(len(mtrx[0]), len(mtrx), mtrx))
# mtrx = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
# print(matrix(len(mtrx[0]), len(mtrx), mtrx))
