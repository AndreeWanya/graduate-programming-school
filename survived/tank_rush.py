def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
	s_1 = S1.split(' ')
	s_2 = S2.split(' ')
	counter = 0
	for i in range(len(s_1)):
		for j in range(len(s_1[i])):
			if s_1[i][j] == s_2[0][0] and len(s_1[i:]) >= len(s_2) and len(s_1[i][j:]) >= len(s_2[0]):
				for x in range(len(s_2)):
					for y in range(len(s_2[x])):
						if s_1[i+x][j+y] == s_2[x][y]:
							counter += 1
							if counter == len(S2.replace(' ', '')):
								return True
						else:
							counter = 0
	return False
	
#print(TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'))
#print(TankRush(3, 4, '1234 2345 0987', 1, 2, '45'))
#print(TankRush(4, 6, '029402 560202 029694 780288', 2, 2, '02 94'))