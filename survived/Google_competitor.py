def WordSearch(len_sub: int, s: str, subs: str) -> list:
    if len(s) < len_sub:
        if subs in s:
            return [1]
        else:
            return [0]
    query_lines = []
    new_line = ''
    s = s.split(' ')
    for i in range(len(s)):
    	new_line += ' ' + s[i]
    	new_line = new_line.lstrip(' ')
    	if len(new_line) < len_sub - 1:
    		if i == len(s) - 1:
    			query_lines.append(new_line)
    			new_line = ''
    			break
    		else:
    			continue
    	elif len(new_line) in [len_sub - 1, len_sub]:
    		query_lines.append(new_line)
    		new_line = ''
    		continue
    	while len(new_line) > len_sub:
    		if ' ' in new_line:
    			query_lines.append(new_line[:-new_line[::-1].find(' ')-1])
    			new_line = new_line[-new_line[::-1].find(' '):]
    		else:
    			query_lines.append(new_line[0: len_sub])
    			new_line = new_line[len_sub:]
    if len(new_line) > 0:
    	query_lines.append(new_line)
    result = []
    for sub in query_lines:
    	if subs in sub.split(' '):
    		result.append(1)
    	else:
    		result.append(0)
    return result
        
#print(WordSearch(12, '1) stroka razbivaetsya na nabor strok cherez vyravnivanie po zadannoj shirine.', 'strok'))
#print(WordSearch(10, '12345', 'subs'))
#print(WordSearch(3, '12345', '123'))