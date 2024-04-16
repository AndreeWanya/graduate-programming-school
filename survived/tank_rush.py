def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
	s_1 = S1.split(' ')
	s_2 = S2.split(' ')
	if len(s_2) == 1 and s_2[0] in S1:
		return True
	map_including = {}
	for i in range(len(s_1)):
		for j in range(len(s_2)):
			if s_2[j] in s_1[i]:
				map_including[s_2[j]] = [s_1[i].find(s_2[j]), i]
	if len(map_including.keys()) != len(s_2):
		return False
	values = list(map_including.values())
	s, r = values[0][0], values[0][1]
	for i in range(1, len(values)):
		if s != values[i][0] or abs(r) != abs(values[i][1]) - 1:
			return False
		r = values[i][1]
	return True
	
#print(TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'))
#print(TankRush(3, 4, '1234 2345 0987', 1, 2, '45'))