def odometer(oksana: list) -> int:
	distance = oksana[0] * oksana[1]
	for i in range(3, len(oksana), 2):
		distance += oksana[i-1] * (oksana[i] - oksana[i-2])
	return distance	