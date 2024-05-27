def ECC_help(arr1: list, arr2: list) -> bool:
	arr_dict = {}
	if len(arr1) != len(arr2):
		return False
	for i in range(len(arr1)):
		if arr1[i] == arr2[i]:
			continue
		else:
			if arr1[i] in arr_dict:
				arr_dict[arr1[i]] += 1
			else:
				arr_dict[arr1[i]] = 1
			if arr2[i] in arr_dict:
				arr_dict[arr2[i]] -= 1
			else:
				arr_dict[arr2[i]] = -1
			if arr_dict[arr2[i]] == 0:
				arr_dict.pop(arr2[i])
			if arr_dict[arr1[i]] == 0:
				arr_dict.pop(arr1[i])
	if len(arr_dict) == 0:
		return True
	return False
	
#arrs = [([1, 2, 3], [1, 2, 3, 4]), ([1, 2, 3], [1, 2, 3]), ([1, 3, 2], [1, 2, 3]), ([1, 3, 2, 3], [1, 2, 3, 2]), ([1, 1], [1, 1])]
#for arr in arrs:
#	print(ECC_help(arr[0], arr[1]))