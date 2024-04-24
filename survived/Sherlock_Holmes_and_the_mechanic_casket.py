def SherlockValidString(s: str) -> bool:
	counter_dict = {}
	for ch in s:
		counter_dict[ch] = s.count(ch)
	values = list(counter_dict.values())
	flag = 0
	for value in values:
		if value == sum(values)/len(values) or value == (sum(values) - 1)/len(values) or (value - 1) == (sum(values) - 1)/len(values) or value == (sum(values) - 1)/(len(values) - 1):
			continue
		elif value == 1:
			flag += 1
		else:
			return False
		if flag > 1:
			return False
	return True
	
s_list = ['xyz', 'xyzaa', 'xxyyz', 'xyzzz', 'xxyyza', 'xxyyzabc']
for s in s_list:
	print(SherlockValidString(s))