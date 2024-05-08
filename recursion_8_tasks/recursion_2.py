def sum_of_nums_digits(num: int) -> int:
	num = str(num)
	res = int(num[0])
	if len(num) == 1:
		return res
	num = num[1:]
	return res + sum_of_nums_digits(num)
		
# nums = [1, 23, 456, 7890]
# for num in nums:
#	print(sum_of_nums_digits(num))