def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
	day = 1
	occupied_territory = []
	for i in range(0, len(battalion), 2):
		occupied_territory.append((battalion[i], battalion[i+1]))
	while len(occupied_territory) < N * M:
		battalion = occupied_territory.copy()
		for cell in battalion:
			if cell[0] - 1 > 0 and (cell[0] -1, cell[1]) not in occupied_territory:
				occupied_territory.append((cell[0] - 1, cell[1]))
			if cell[0] + 1 <= N and (cell[0] + 1, cell[1]) not in occupied_territory:
				occupied_territory.append((cell[0] + 1, cell[1]))
			if cell[1] - 1 > 0 and (cell[0], cell[1] - 1) not in occupied_territory:
				occupied_territory.append((cell[0], cell[1] - 1))
			if cell[1] + 1 <= M and (cell[0], cell[1] + 1) not in occupied_territory:
				occupied_territory.append((cell[0], cell[1] + 1))
		day += 1
	return day
	
#print(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]))