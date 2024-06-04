def TRC_sort(trc: list) -> list:
    sorted_trc = []
    for i in range(len(trc)):
    	if trc[i] == 0:
    		sorted_trc = [0] + sorted_trc
    	elif trc[i] == 1:
    		sorted_trc.append(1)
    return sorted_trc + [2] * (len(trc) - len(sorted_trc))

#arrs = [[2, 1, 0], [0, 1, 2, 1, 0, 2], [1, 0, 1, 0, 2]]
#for arr in arrs:
#    print(TRC_sort(arr))
