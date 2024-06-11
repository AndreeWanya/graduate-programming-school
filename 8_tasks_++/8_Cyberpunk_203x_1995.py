def army_communication_matrix(n: int, matrix: list) -> str:
	max_count = 0
	min_mtrx = 2
	for i in range(n - 2):
		for j in range((n - i - 1) ** 2):
			aver_result = [j // (n - i - 1), j % (n - i - 1), 0]
			for k in range(min_mtrx ** 2):
				aver_result[2] += matrix[aver_result[0] + k // min_mtrx][aver_result[1] + k % min_mtrx]
			if aver_result[2] > max_count:
				max_count = aver_result[2]
				result = [aver_result[0], aver_result[1], min_mtrx]
		min_mtrx += 1
	return str(result[1]) + ' ' + str(result[0]) + ' ' + str(result[2])
						
	
# mtrx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(army_communication_matrix(3, mtrx))
# mtrx = [[1, 9, 2, 3], [4, 8, 5, 6], [0, 7, 1, 2], [0, 0, 0, 0]]
# print(army_communication_matrix(4, mtrx))
