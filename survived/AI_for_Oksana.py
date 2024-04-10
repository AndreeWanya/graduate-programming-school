def SumOfThe(N: int, data: list) -> int:
	for i in range(N):
		if data[i] == sum(data[:i]) + sum(data[i+1:]):
			return data[i]
			
#print(SumOfThe(7, [100, -50, 10, -25, 90, -35, 90]))
#print(SumOfThe(5, [5, -25, 10, -35, -45]))
#print(SumOfThe(5, [10, -25, -45, -35, 5]))
#print(SumOfThe(2, [3, 3]))