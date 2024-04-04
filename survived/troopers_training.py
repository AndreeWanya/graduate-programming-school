def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
	day = 1
	occupied_territory = battalion.copy()
	while len(battalion)/2 < N * M:
		for i in range(0, len(battalion), 2):
			if battalion[i] - 1 >= 0:
				print('ok')
				occupied_territory.append(battalion[i] - 1)
				occupied_territory.append(battalion[i + 1])
		battalion = occupied_territory.copy()
		print(battalion)
		
print(ConquestCampaign(3, 4, 2, [2, 2, 3, 4]))