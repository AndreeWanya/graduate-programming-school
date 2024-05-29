def artificial_muscle_fibers(arr: list) -> int:
    arr = [len(arr)] + arr
    for i in range(1, arr[0] + 1):
    	if arr[i] in arr[1: i] and arr[i] not in arr[arr[0] + 1:]:
    		arr.append(arr[i])
    return len(arr[arr[0] + 1:])

#arrs = [[1, 2, 3, 4, 5], [1, 2, 3, 2, 1], [1, 2, 3, 2, 1, 2, 4, 2, 1], [32000, 22, 546]]
#for arr in arrs:
#    print(artificial_muscle_fibers(arr))
