import time
def three_nums_sorting(sub_data):
	for i in range(2):
		sub_data[2], sub_data[1], sub_data[0] = sub_data[0], sub_data[2], sub_data[1]
		if sub_data[2] > sub_data[1] > sub_data[0]:
			return sub_data
	return sub_data

def MisterRobot(N: int, data: list) -> bool:
	while (time.time() - start_time) < 1:
		for i in range(2, N):
			if data[i] < data[i - 1]:
				print(data)
				data = data[:i - 2] + three_nums_sorting(data[i - 2: i + 1]) + data[i + 1:]
				print(data)
				print()
			if data == sorted(data):
				return True
	return False

start_time = time.time()

#print(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]))
#print(MisterRobot(10, [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]))