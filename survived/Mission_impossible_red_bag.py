import math

def TheRabbitsFoot(s: str, encode: bool) -> str:
	result = ''
	if encode:
	    s = s.replace(' ', '')
	    N = len(s)
	    n = int(math.sqrt(N))
	    m = math.ceil(math.sqrt(N))
	    if n * m < N:
	    	n += 1
	    if len(s) < n * m:
	    	s += (n * m - len(s)) * ' '
	    for i in range(m):
	    	line = ''
	    	for j in range(i, len(s), m):
	    		line += s[j]
	    	result += line.strip() + ' '
	else:
		s = s.split(' ')
		for i in range(1, len(s)):
			if len(s[i]) < len(s[0]):
				s[i] = s[i] + (len(s[0]) - len(s[i])) * ' '
		n = len(s)
		m = len(s[0])
		for i in range(m):
			for j in range(n):
				result += s[j][i]	
	return result.rstrip()
		
#print(TheRabbitsFoot('отдай мою кроличью лапку', True))
#print(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False))
#print(TheRabbitsFoot('мама мыла раму', True))
#print(TheRabbitsFoot('ммр аыа млм аау', False))