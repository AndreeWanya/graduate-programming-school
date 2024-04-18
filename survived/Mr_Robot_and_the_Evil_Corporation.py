def MisterRobot(N: int, data: list) -> bool:
	while True:
		for i in range(2, N):
			if data[i] < data[i-1]:
				data[i], data[i-1], data[i-2] = data[i-1], data[i-2], data[i]
			if data == sorted(data):
				return True

print(MisterRobot(7, [1, 3, 4, 5, 6, 2, 7]))