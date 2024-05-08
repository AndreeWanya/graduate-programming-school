def sum_of_nums_digits(num: int) -> int:
	res = num % 10
	if num // 10 == 0:
		return res
	return res + sum_of_nums_digits(num // 10)
		
# nums = [1, 23, 456, 7890]
# for num in nums:
# 	print(sum_of_nums_digits(num))