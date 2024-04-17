def MaximumDiscount(N: int, price: list) -> int:
	price = sorted(price, reverse=True)
	counter = 0
	for i in range(2, N, 3):
		counter += price[i]
	return counter
		
#print(MaximumDiscount(7, [400, 350, 300, 250, 150, 200, 100]))