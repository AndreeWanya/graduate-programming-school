import sys

def artificial_muscle_fibers(arr: list) -> int:
    nums_arr = []
    for i in range(len(arr)):
    	if arr[i] in arr[:i] and arr[i] not in nums_arr:
    		nums_arr.append(arr[i])
    return len(nums_arr), sys.getsizeof(nums_arr)

arrs = [[1, 2, 3, 4, 5], [1, 2, 3, 2, 1], [1, 2, 3, 2, 1, 2, 4, 2, 1], [32000, 22, 546]]
for arr in arrs:
    print(artificial_muscle_fibers(arr))
