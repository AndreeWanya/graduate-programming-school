def x_power_of_num(num: float, x: int) -> float:
	if x == 0:
		return 1
	elif x == 1:
		return num
	x -= 1
	return num * x_power_of_num(num, x)
	
# print(x_power_of_num(2, 4))